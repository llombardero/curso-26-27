"""Renderer H1 editable; no modifica el plan ni las fuentes canónicas.

Las vistas conservan la identidad de unidad y las fronteras explícitas de código,
campos, secciones README e instrucciones independientes. El número de pantallas
puede superar el de SlideSpec: no se reduce tipografía para forzar el plan visual.
El tiempo orientativo se guarda solo en notas y metadata, para no distraer al
alumnado; cada reparto conserva el presupuesto del reloj fuente.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
import hashlib
import json
import math
import re
import sys
import textwrap

from lxml import etree
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_AUTO_SIZE
from pptx.util import Inches, Pt

from tiempos_presentaciones_semanticas import allocate_slide_timings
import componer_presentaciones_semanticas as composition
import enriquecer_soportes_semanticos as source_supports


INK = RGBColor(28, 35, 48)
PAPER = RGBColor(249, 247, 242)
DARK = RGBColor(18, 24, 36)
WHITE = RGBColor(255, 255, 255)
ACCENT = RGBColor(47, 91, 168)
META_NS = "urn:minijarvis:semantic-render:v1"


def rendered_height(text, width=11.9, size=28):
    """Point-based line boxes shared by measurement and DrawingML rendering.

    Keep this separate from the planner's capacity heuristic: changing physical
    containment must not redistribute units, notes or their source clock.
    """
    columns = max(1, math.floor((width - 0.24) * 72 / (size * 0.6)))
    lines = sum(max(1, len(textwrap.wrap(line, columns, replace_whitespace=False,
                                       drop_whitespace=False))) for line in text.split("\n"))
    # Code keeps its full 22 pt face; slightly tighter leading preserves complete
    # source blocks inside the safe area without shrinking or truncating text.
    return lines * size * (1.05 if size == 22 else 1.10) / 72 + 0.18


def text_box(slide, name, text, x, y, width, height, *, size=28, color=INK, bold=False, code=False):
    compact = name == "Propuesta editable"
    height = max(height, size * 1.15 / 72 + 0.04 if compact else rendered_height(text, width, size))
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(height))
    box.name = name
    box._element.xpath(".//p:cNvPr")[0].set("descr", name)
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.auto_size = MSO_AUTO_SIZE.NONE
    frame.margin_left = frame.margin_right = Inches(0.03 if compact else 0.12)
    frame.margin_top = frame.margin_bottom = Inches(0.02 if compact else 0.08)
    for index, line in enumerate(text.split("\n")):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = line
        paragraph.font.name = "Liberation Mono" if code else "Liberation Sans"
        paragraph.font.size = Pt(size)
        paragraph.font.bold = bold
        paragraph.font.color.rgb = color
        paragraph.space_after = Pt(0)
        # A relative multiplier uses Office's font metrics, not size * multiplier.
        paragraph.line_spacing = Pt(size * (1.05 if code else 1.10))
        if code:
            # Hanging indent affects only visual wraps; editable source stays exact.
            indent = Pt(size * 0.6 * 2)
            paragraph._p.get_or_add_pPr().set("marL", str(indent))
            paragraph._p.get_or_add_pPr().set("indent", str(-indent))
    return box


def write_metadata(slide, metadata):
    extension_list = etree.SubElement(slide._element, "{http://schemas.openxmlformats.org/presentationml/2006/main}extLst")
    extension = etree.SubElement(extension_list, "{http://schemas.openxmlformats.org/presentationml/2006/main}ext", uri=META_NS)
    node = etree.SubElement(extension, f"{{{META_NS}}}renderMetadata")
    node.text = json.dumps(metadata, ensure_ascii=False)


def render_semantic_title(prs, session, spec):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = DARK
    text_box(slide, "Código de sesión", f"S{session.number} · {session.hito}", 0.7, 0.6, 11.9, 0.5,
             size=26, color=WHITE, bold=True)
    text_box(slide, "Título", spec.title, 0.7, 1.65, 11.9, 1.8, size=40, color=WHITE, bold=True)
    if session.moment:
        text_box(slide, "Fase HEXA", f"Fase HEXA: {session.moment}", 0.7, 4.0, 11.9, 0.8, color=WHITE)
    text_box(slide, "Modalidad del alumnado", f"Modalidad publicada: {session.student_mode}",
             0.7, 5.05, 11.9, 0.55, size=22, color=WHITE, bold=True)
    text_box(slide, "Organización docente", f"Organización docente: {session.grouping}",
             0.7, 5.72, 11.9, 0.95, size=20, color=WHITE)
    return slide


@dataclass
class RenderAtom:
    text: str
    source_indices: tuple[int, ...]
    kind: str = "prose"
    language: str = ""
    alternative: str = ""
    labels: tuple[str, str] = ("Versión A", "Versión B")
    reference: bool = False


@dataclass
class RenderFrame:
    """Vista derivada: una unidad mantiene su identidad en todas sus vistas."""
    plan_index: int
    title: str
    kind: str
    units: list
    atoms: list[RenderAtom] = field(default_factory=list)
    timeline_refs: list[int] = field(default_factory=list)
    relations: dict = field(default_factory=dict)
    notes: list[tuple[str, str, str]] = field(default_factory=list)
    recognition: bool = False
    modality: str = ""
    origin_slides: tuple[int, ...] = ()


class RepresentationError(ValueError):
    """La unidad necesita revisión explícita; nunca reducir la letra o recortar."""


def prose_text(text):
    text = text.replace("**", "").replace("`", "")
    return re.sub(r"(?m)^\s*(?:>\s*|[-*]\s+|\d+\.\s+)", "", text).strip()


def fenced_body(text):
    match = re.fullmatch(r"(`{3,}|~{3,})([^\n]*)\n([\s\S]*?)\n\1", text.strip())
    return (match[2].strip(), match[3]) if match else None


def text_height(text, width=11.9, size=28, code=False):
    # Salvaguarda conservadora; no es una aprobación visual de Office.
    columns = max(1, math.floor((width - 0.12) * 72 / (size * 0.6)))
    lines = sum(max(1, len(textwrap.wrap(line, columns, replace_whitespace=False,
                                       drop_whitespace=False))) for line in text.split("\n"))
    return lines * size * 1.05 / 72 + 0.10


def atom_height(atom, recognition=False):
    size = 24 if recognition else 28
    if atom.kind == "cards":
        return cards_geometry(atom.text.splitlines())[1]
    if atom.kind == "pair":
        font = 22 if atom.language else size
        side = max(text_height(atom.text, 5.65, font), text_height(atom.alternative, 5.65, font))
        stacked = text_height(atom.text, 11.9, font) + text_height(atom.alternative, 11.9, font) + 0.3
        return min(side, stacked) + 0.45
    if atom.kind == "code":
        return text_height(atom.text, 11.9, 22, True)
    return text_height(atom.text, 11.9, size)


def cards_geometry(items, *, rendered=False):
    candidates = []
    for columns in (2, 3):
        width = 11.9 / columns - 0.2
        measure = rendered_height if rendered else text_height
        chars = max(1, math.floor((width - (0.24 if rendered else 0.12)) * 72 / (24 * 0.6)))
        max_lines = max(sum(max(1, len(textwrap.wrap(line, chars, replace_whitespace=False,
                                                     drop_whitespace=False)))
                            for line in text.split("\n")) for text in items)
        row_heights = [max(measure(text, width, 24) for text in items[i:i + columns])
                       for i in range(0, len(items), columns)]
        gap = 0.10 if rendered else 0.18
        candidates.append((columns, sum(row_heights) + gap * (len(row_heights) - 1), row_heights, max_lines))
    legible = [candidate for candidate in candidates if candidate[3] <= 3]
    columns, height, row_heights, _ = min(legible or candidates, key=lambda candidate: candidate[1])
    return columns, height, row_heights


def visible_owner(spec, index):
    text = spec.visible_content[index]
    samples = spec.relations.get("question_samples", {})
    for unit in spec.pedagogical_units:
        if isinstance(samples, dict) and samples.get(unit.unit_id) == text:
            return unit
        if text in [*unit.visible_content, *unit.presenter_content]:
            return unit
    for unit in spec.pedagogical_units:
        if spec.unit_dispositions[unit.unit_id].channels and "visible" in spec.unit_dispositions[unit.unit_id].channels:
            if unit.source_refs[0].heading in text:
                return unit
    return next(unit for unit in spec.pedagogical_units if "visible" in spec.unit_dispositions[unit.unit_id].channels)


def project_item(text, index, unit):
    """Solo desde visible_content; detalle y facilitación vuelven a notas."""
    fenced = fenced_body(text)
    if fenced:
        language, body = fenced
        if language == "markdown":
            # Frontera del propio README, no corte por longitud ni líneas.
            sections = re.split(r"(?m)(?=^## )", body)
            return [RenderAtom(section.rstrip(), (index,), "code", language) for section in sections if section.strip()]
        if language == "text":
            # Plantillas de campos: el espacio en blanco no es una línea de código.
            # Conservar todos los campos y valores, sin compactar nunca Java.
            body = re.sub(r"\n{2,}", "\n", body)
        return [RenderAtom(body, (index,), "code", language)]
    plain = prose_text(text)
    if re.match(r"^(?:Di:|Pregunta:|Proyecta\b|Muestra\b|Presenta\b|Introduce\b|Aclara\b|"
                r"Amplía oralmente\b|No aceptes\b|Cierra (?:en voz alta|con)\b|"
                r"Antes de .*\b(?:pregunta|pide):|Pide .*:|Explica oralmente:)", plain):
        return []
    if plain.endswith(":") and "\n" not in plain:
        return []
    if plain.startswith("Explica que "):
        plain = plain.removeprefix("Explica que ")
    lines = plain.splitlines()
    if unit.function == "scaffolding":
        # La fuente comparte la recuperación, no el lenguaje interno de petición
        # del docente. Conservar este en notas y proyectar la misma acción al alumno.
        actions = []
        for line in lines:
            if not line or line == unit.source_refs[0].heading or line.endswith(":"):
                continue
            line = line.replace("pide señalar", "señala").replace("pide volver a explicar", "vuelve a explicar")
            line = line.replace("aísla los valores y solicita una predicción", "predice con los valores indicados")
            actions.append(line[0].upper() + line[1:])
        return [RenderAtom("\n".join(actions), (index,), "cards")] if actions else []
    if len(lines) >= 3 and re.match(r"(?:[-*]\s|\d+\.\s)", text):
        if re.match(r"\d+\.\s", text) and any("defensa práctica" in ref.heading.lower() for ref in unit.source_refs):
            lines = [f"{index + 1} · {line}" for index, line in enumerate(lines)]
        # Cada instrucción/criterio de la lista es una frontera explícita.
        pending = [lines]
        cards = []
        while pending:
            items = pending.pop(0)
            if cards_geometry(items)[1] > 4.1 and len(items) > 1:
                middle = len(items) // 2
                pending[:0] = [items[:middle], items[middle:]]
            else:
                cards.append(RenderAtom("\n".join(items), (index,), "cards"))
        return cards
    result = []
    for line in lines:
        # Extractivo por oración completa, sin recorte de caracteres.
        summary = line if "¿" in line else re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ])", line)[0]
        if text_height(summary) > 4.6:
            summary = unit.source_refs[0].heading
        if summary.strip():
            result.append(RenderAtom(summary, (index,)))
    return result


def frame_kind(spec, unit, atoms):
    if spec.kind == "closure":
        return "closure"
    if unit.role == "recognition":
        return "recognition"
    if any(atom.kind == "pair" for atom in atoms):
        return "contrast"
    if "prediction_cycle" in unit.relations or unit.function == "predictions":
        if any(re.search(r"(?:Salida|Resultado)\s+(?:esperad|obtenid)|Demuestra:", atom.text, re.I) for atom in atoms):
            # Un modelo resuelto sirve para comprobar/contrastar, no para
            # presentar la respuesta dentro del estímulo de predicción.
            return "check"
        return "prediction"
    if any(atom.kind == "code" for atom in atoms):
        return "code"
    if unit.function in {"individual_check", "scaffolding"}:
        return "check"
    if spec.kind in {"activity", "closure"}:
        return spec.kind
    return "concept"


def expand_semantic_frames(session, plan):
    frames = []
    for plan_index, spec in enumerate(plan):
        first = len(frames)
        if spec.kind == "title":
            frames.append(RenderFrame(plan_index, spec.title, "title", list(spec.pedagogical_units), timeline_refs=[0]))
            if "concurrency" in spec.relations:
                lane_ids = {unit_id for lane in spec.relations["concurrency"]["lanes"].values() for unit_id in lane}
                lane_units = [unit for member in plan for unit in member.pedagogical_units if unit.unit_id in lane_ids]
                frames.append(RenderFrame(plan_index, "Trabajo simultáneo", "parallel", lane_units,
                                          timeline_refs=[0], relations=dict(spec.relations)))
        groups = {}
        for index in range(len(spec.visible_content)):
            unit = visible_owner(spec, index)
            # Las muestras del banco son una sola vista, no seis obligaciones.
            key = "question_bank" if unit.function == "question_bank" else unit.unit_id
            groups.setdefault(key, []).append((index, unit))
        for entries in groups.values():
            units = list({unit.unit_id: unit for _, unit in entries}.values())
            unit = units[0]
            modality = re.findall(r"\b(?:INDIVIDUAL|PAREJAS|EQUIPO)\b", " ".join(u.source_refs[0].heading for u in units), re.I)
            if not modality:
                supports = {key for u in units for key in u.relations.get("supports", ())}
                context = " ".join(u.source_refs[0].heading for u in spec.pedagogical_units if u.unit_id in supports)
                modality = re.findall(r"\b(?:INDIVIDUAL|PAREJAS|EQUIPO)\b", context, re.I)
            local_modality = " · ".join(dict.fromkeys(m.upper() for m in modality))
            source_entries = list(entries)
            targets = None
            for index, _ in entries:
                fenced = fenced_body(spec.visible_content[index])
                if fenced is not None and "|" in fenced[1]:
                    targets = (index, fenced[1])
                    break
            if unit.function == "activity" and targets and "clasific" in unit.source_refs[0].heading.lower():
                proposals = next((index for index, _ in entries if spec.visible_content[index].startswith("- ")), None)
                if proposals is not None:
                    proposal_atoms = [RenderAtom(prose_text(line).rstrip(";."), (proposals,))
                                      for line in spec.visible_content[proposals].splitlines()]
                    frames.append(RenderFrame(plan_index, unit.source_refs[0].heading, "classification", units,
                        [*proposal_atoms, RenderAtom(targets[1], (targets[0],), "code", "text")],
                        list(spec.timeline_refs), {"classification": {"targets": [t.strip() for t in targets[1].split("|")],
                                                                     "proposals": [atom.text for atom in proposal_atoms]},
                                                  "schedule": spec.relations.get("schedule")}, modality=local_modality))
                    source_entries = [(index, owner) for index, owner in entries if index not in (proposals, targets[0])]
            atoms = [atom for index, owner in source_entries for atom in project_item(spec.visible_content[index], index, owner)]
            if unit.function == "counterexamples" or "contrast" in unit.relations:
                code_positions = [i for i, atom in enumerate(atoms) if atom.kind == "code"]
                if len(code_positions) >= 2:
                    a, b = code_positions[:2]
                    left, right = atoms[a], atoms[b]
                    pair = RenderAtom(left.text, (*left.source_indices, *right.source_indices), "pair",
                                      left.language, right.text)
                    if unit.function == "counterexamples":
                        pair.labels = ("Versión problemática", "Alternativa")
                    elif re.search(r"leer no .*utilizar", unit.source_refs[0].heading, re.I):
                        pair.labels = ("Lee y utiliza", "Lee sin utilizar")
                    atoms[a] = pair
                    del atoms[b]
            local = []
            chunk = []
            height = 0
            for atom in atoms:
                needed = atom_height(atom, unit.role == "recognition") + 0.18
                limit = (4.35 if "prediction_cycle" in unit.relations or unit.function == "predictions"
                         else 4.75 if spec.kind == "activity" or unit.function in {"individual_check", "scaffolding"} else 5.25)
                if needed > limit:
                    raise RepresentationError(f"{unit.unit_id} ({unit.source_refs[0].heading}): representación especial pendiente; "
                                              "bloque íntegro no cabe a tamaño legible, no se recorta")
                if chunk and (height + needed > limit or len(chunk) == 3):
                    local.append(chunk)
                    chunk, height = [], 0
                chunk.append(atom)
                height += needed
            if chunk:
                local.append(chunk)
            for chunk in local:
                heading = "Muestra del banco de preguntas" if unit.function == "question_bank" else unit.source_refs[0].heading
                frames.append(RenderFrame(plan_index, heading, frame_kind(spec, unit, chunk), units, chunk,
                    [0] if spec.kind == "title" else list(spec.timeline_refs),
                    {"unit_relations": {u.unit_id: u.relations for u in units}, "schedule": spec.relations.get("schedule")},
                    recognition=unit.role == "recognition", modality=local_modality))
        owned_frames = frames[first:]
        if not owned_frames:
            raise RepresentationError(f"SlideSpec {plan_index} sin representación")
        for unit in spec.pedagogical_units:
            target = next((frame for frame in owned_frames if frame.kind != "title" and unit in frame.units), owned_frames[0])
            if not any(unit in frame.units for frame in owned_frames):
                # También las unidades exclusivamente docentes deben tener destino
                # trazable, no solo texto sin identidad dentro de las notas.
                target.units.append(unit)
            for text in spec.presenter_content:
                if text in [*unit.presenter_content, *unit.visible_content] and not any(text == entry[2] for f in owned_frames for entry in f.notes):
                    target.notes.append((unit.function, unit.source_refs[0].heading, text))
        for text in spec.presenter_content:
            if not any(text == entry[2] for f in owned_frames for entry in f.notes):
                owned_frames[0].notes.append(("facilitation", spec.title, text))
        for index, text in enumerate(spec.visible_content):
            unit = visible_owner(spec, index)
            candidates = [f for f in owned_frames if any(index in atom.source_indices for atom in f.atoms)]
            target = candidates[0] if candidates else next((f for f in owned_frames if unit in f.units), owned_frames[0])
            displayed = "\n".join(atom.text + ("\n" + atom.alternative if atom.alternative else "")
                                  for f in candidates for atom in f.atoms if index in atom.source_indices)
            body = fenced_body(text)
            equivalent = prose_text(body[1] if body else text)
            if re.sub(r"\s+", " ", equivalent) not in re.sub(r"\s+", " ", prose_text(displayed)):
                already_in_notes = "\n".join(heading + "\n" + detail for _, heading, detail in target.notes)
                if not all(line.strip() in already_in_notes for line in text.splitlines() if line.strip()):
                    target.notes.append(("visible_detail" if candidates else "facilitation", unit.source_refs[0].heading, text))
    composed = composition.compose(sys.modules[__name__], session, frames)
    return source_supports.enrich(sys.modules[__name__], session, composed)


def semantic_base(prs, session, frame):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = PAPER
    label = "Para reconocer · leer, no ampliar la práctica" if frame.recognition else frame.modality or ""
    if frame.kind == "linked_prediction":
        label = "Proceso: PREDICE → EJECUTA → CONTRASTA"
    if any(atom.kind == "mixed_question" for atom in frame.atoms):
        label = "NÚCLEO · excepción: PARA RECONOCER"
    text_box(slide, "Contexto", label, 0.7, 0.28, 11.9, 0.38, size=20, color=ACCENT, bold=True)
    text_box(slide, "Idea principal", frame.title, 0.7, 0.76, 11.9, 0.65, size=30, bold=True)
    text_box(slide, "Sesión y procedencia", f"S{session.number} · {session.hito}", 0.7, 7.03, 11.9, 0.3, size=16)
    return slide


def frame_content_top(frame, minimum=1.55, gap=0.14):
    """Keep content below the physical line box of a wrapped semantic title."""
    title_bottom = 0.76 + rendered_height(frame.title, 11.9, 30)
    return max(minimum, title_bottom + gap)


def validate_semantic_slide_geometry(slide):
    """Reject a rendered semantic slide outside its title/footer safe area."""
    chrome = {
        "Código de sesión", "Título", "Fase HEXA", "Modalidad", "Contexto",
        "Idea principal", "Sesión y procedencia",
    }
    content = [
        shape for shape in slide.shapes
        if shape.has_text_frame and shape.text.strip() and shape.name not in chrome
    ]
    failures = [shape for shape in content if shape.top + shape.height > Inches(6.84)]
    if failures:
        details = ", ".join(
            f"{shape.name}={(shape.top + shape.height) / Inches(1):.3f}\"" for shape in failures
        )
        raise RepresentationError(f"Contenido fuera del límite 6.84\": {details}")
    titles = [shape for shape in slide.shapes if shape.name == "Idea principal"]
    if titles and content and titles[0].top + titles[0].height > min(shape.top for shape in content):
        raise RepresentationError("El título invade la primera caja de contenido")


def render_atom(slide, atom, y, recognition=False):
    size = 24 if recognition else 28
    if atom.kind == "cards":
        items = atom.text.splitlines()
        columns, height, row_heights = cards_geometry(items, rendered=True)
        # Compress only inter-row whitespace when a grid approaches the footer.
        # Glyph line boxes and font sizes never shrink.
        rows = len(row_heights)
        gap = min(0.10, (6.84 - y - sum(row_heights)) / max(1, rows - 1))
        if gap < 0.03:
            raise RepresentationError("Tarjetas sin espacio antes del pie; no reducir tipografía ni ocultar acciones")
        height = sum(row_heights) + gap * (rows - 1)
        top = y
        for row, row_height in enumerate(row_heights):
            for col, text in enumerate(items[row * columns:(row + 1) * columns]):
                box = text_box(slide, f"Acción o criterio {row * columns + col}", text,
                               0.7 + col * 11.9 / columns, top, 11.9 / columns - 0.2, row_height, size=24)
                box.fill.solid()
                box.fill.fore_color.rgb = WHITE
                box.line.color.rgb = ACCENT
            top += row_height + gap
        return height
    if atom.kind == "pair":
        font = 22 if atom.language else size
        side = max(rendered_height(atom.text, 5.65, font), rendered_height(atom.alternative, 5.65, font))
        stacked = rendered_height(atom.text, 11.9, font) + rendered_height(atom.alternative, 11.9, font) + 0.45
        h = min(side, stacked) + 0.55
        for i, text in enumerate((atom.text, atom.alternative)):
            x = 0.7 + 6.15 * i if side <= stacked else 0.7
            top = y if side <= stacked or i == 0 else y + rendered_height(atom.text, 11.9, font) + 0.55
            width = 5.65 if side <= stacked else 11.9
            text_box(slide, f"Etiqueta alternativa {i}", atom.labels[i], x, top, width, 0.35,
                     size=20, color=ACCENT, bold=True)
            text_box(slide, f"Contraste {i}", text, x, top + 0.55, width, rendered_height(text, width, font),
                     size=font, code=bool(atom.language))
        return h
    code = atom.kind == "code"
    h = rendered_height(atom.text, 11.9, 22 if code else size)
    box = text_box(slide, "Código editable" if code else "Contenido", atom.text, 0.7, y, 11.9, h,
                   size=22 if code else size, code=code)
    if atom.kind == "mixed_question":
        for paragraph in box.text_frame.paragraphs:
            prefix, marker, suffix = paragraph.text.partition("y por qué Integer.parseInt")
            if marker:
                paragraph.clear()
                paragraph.add_run().text = prefix
                recognition = paragraph.add_run()
                recognition.text = marker + suffix
                recognition.font.size = Pt(24)
                recognition.font.color.rgb = ACCENT
    if code:
        box.fill.solid()
        box.fill.fore_color.rgb = WHITE
    return h


def render_content(prs, session, frame):
    slide = semantic_base(prs, session, frame)
    y = frame_content_top(frame)
    for atom in frame.atoms:
        y += render_atom(slide, atom, y, frame.recognition) + 0.10
    if frame.kind == "concept":
        boxes = [shape for shape in slide.shapes if shape.name == "Contenido"]
        if boxes:
            boxes[0].fill.solid()
            boxes[0].fill.fore_color.rgb = ACCENT
            for paragraph in boxes[0].text_frame.paragraphs:
                paragraph.font.bold = True
                paragraph.font.color.rgb = WHITE
    if frame.kind == "closure":
        for shape in slide.shapes:
            if shape.has_text_frame and shape.name == "Contenido" and "¿" in shape.text:
                shape.fill.solid()
                shape.fill.fore_color.rgb = ACCENT
                for paragraph in shape.text_frame.paragraphs:
                    paragraph.font.bold = True
                    paragraph.font.color.rgb = WHITE
                    for run in paragraph.runs:
                        run.font.color.rgb = WHITE
    return slide


def render_classification(prs, session, frame):
    slide = semantic_base(prs, session, frame)
    info = frame.relations["classification"]
    top = frame_content_top(frame, 1.6)
    shift = top - 1.6
    text_box(slide, "Acción de clasificación", "PROPUESTAS · sin asignar", 0.7, top, 6.1, 0.5, size=24, bold=True)
    for i, proposal in enumerate(info["proposals"]):
        text_box(slide, "Propuesta editable", proposal, 0.7, 2.3 + shift + i * 0.44, 6.1, 0.43, size=24)
    for i, destination in enumerate(info["targets"]):
        x = 7.05 + i * 1.85
        box = text_box(slide, "Destino de clasificación", destination, x, 2.2 + shift, 1.65, 4.3, size=24, bold=True)
        box.line.color.rgb = ACCENT
    return slide


def render_prediction(prs, session, frame):
    slide = semantic_base(prs, session, frame)
    protocol = next((a.text for a in frame.atoms if a.kind == "code" and a.text.startswith("señalo →")), None)
    process = "Protocolo: " + protocol if protocol else "Proceso: PREDICE → EJECUTA → CONTRASTA"
    top = frame_content_top(frame, 1.5)
    header_height = max(0.5, rendered_height(process, 11.9, 24))
    text_box(slide, "Proceso de predicción", process,
             0.7, top, 11.9, header_height, size=24, bold=True, color=ACCENT)
    y = top + header_height + 0.30
    for atom in frame.atoms:
        y += render_atom(slide, atom, y) + 0.10
    return slide


def render_activity(prs, session, frame):
    slide = semantic_base(prs, session, frame)
    top = frame_content_top(frame, 1.5)
    label = "QUÉ COMPROBAR" if frame.kind == "check" else "QUÉ HACER"
    header_height = max(0.4, rendered_height(label, 11.9, 20))
    text_box(slide, "Acción", label, 0.7, top, 11.9, header_height,
             size=20, color=ACCENT, bold=True)
    y = top + header_height + 0.15
    for atom in frame.atoms:
        y += render_atom(slide, atom, y, frame.recognition) + 0.10
    return slide


def render_parallel(prs, session, frame):
    slide = semantic_base(prs, session, frame)
    top = frame_content_top(frame, 1.5)
    shift = top - 1.5
    text_box(slide, "Concurrencia", "AL MISMO TIEMPO · un reloj compartido", 0.7, top, 11.9, 0.5, size=26, color=ACCENT, bold=True)
    concurrency = frame.relations["concurrency"]
    for i, lane in enumerate(("DOCENTE", "PAREJAS", "EQUIPO")):
        x = 0.7 + i * 4.1
        text_box(slide, "Carril " + lane, lane, x, 2.15 + shift, 3.95, 0.5, size=26, bold=True)
        lane_units = [unit for unit in frame.units if unit.unit_id in concurrency["lanes"][lane] and unit.function != "timeline"]
        # El carril ya declara EQUIPO: no repetir ese sufijo en cada acción.
        labels = list(dict.fromkeys(re.sub(r"\s*[—–-]\s*EQUIPO$", "", unit.source_refs[0].heading)
                                    for unit in lane_units))
        top = 2.85 + shift
        for label in labels:
            height = rendered_height(label, 4.07, 24)
            if top + height > 6.84:
                raise RepresentationError("Carril concurrente necesita otra vista; no reducir tipografía ni ocultar acciones")
            text_box(slide, "Actividad concurrente " + lane, label, x, top, 4.07, height, size=24)
            top += height + 0.09
    return slide


def render_study(prs, session, frame):
    return composition.render_study(sys.modules[__name__], prs, session, frame)


def render_criteria(prs, session, frame):
    return composition.render_criteria(sys.modules[__name__], prs, session, frame)


def render_comparison(prs, session, frame):
    return composition.render_comparison(sys.modules[__name__], prs, session, frame)


SEMANTIC_LAYOUTS = {
    "title": render_semantic_title,
    "concept": render_content,
    "focus": render_content,
    "code": render_content,
    "prediction": render_prediction,
    "linked_prediction": render_content,
    "contrast": render_content,
    "activity": render_activity,
    "check": render_activity,
    "closure": render_content,
    "parallel": render_parallel,
    "recognition": render_content,
    "classification": render_classification,
    "study": render_study,
    "criteria": render_criteria,
    "comparison": render_comparison,
}
SEMANTIC_LAYOUTS.update(source_supports.layouts(sys.modules[__name__]))


def presenter_notes(frame, timing, rendered):
    sections = {}
    labels = {"visible_detail": "Detalle para la explicación oral", "question_bank": "Banco de preguntas",
              "scaffolding": "Andamiaje y recuperación", "observation": "Observación", "continuity": "Transición",
              "timeline": "Ritmo fuente", "timeline_context": "Organización del aula"}
    for function, heading, text in frame.notes:
        if re.fullmatch(r"\s*(?:Pregunta(?: principal| complementaria)?|Cierra en voz alta|Cuando proceda|Di en voz alta|Pregunta antes de probar):\s*", text, re.I):
            continue
        body = fenced_body(text)
        equivalent = prose_text(body[1] if body else text)
        if function not in {"question_bank", "closure", "continuity"} and equivalent and re.sub(r"\s+", " ", equivalent) in re.sub(r"\s+", " ", prose_text(rendered)):
            continue
        key = labels.get(function, "Facilitación docente") + " · " + heading
        sections.setdefault(key, []).append(text)
    def without_orphan_labels(texts):
        unique = list(dict.fromkeys(texts))
        label = lambda text: "\n" not in text.strip() and text.rstrip().endswith(":")
        return [text for index, text in enumerate(unique)
                if not label(text) or index + 1 < len(unique) and not label(unique[index + 1])]
    sections = {heading: retained for heading, texts in sections.items()
                if (retained := without_orphan_labels(texts))}
    return "NOTAS DEL PRESENTADOR\n\nTIEMPO ORIENTATIVO (no proyectado)\n" + timing.presenter_notes + "\n\n" + "\n\n".join(
        heading + "\n" + "\n\n".join(texts) for heading, texts in sections.items())


def metadata_code_blocks(spec, frame):
    """Inventory represented Java from its source blocks, not a lossy pair language."""
    indices = sorted({index for atom in frame.atoms for index in atom.source_indices})
    blocks = []
    for index in indices:
        fenced = fenced_body(spec.visible_content[index])
        if fenced and fenced[0] == "java":
            blocks.append(fenced[1])
    return blocks


def render_semantic_presentation(prs, session, plan):
    frames = expand_semantic_frames(session, plan)
    timings = allocate_slide_timings(session, frames)
    for frame, timing in zip(frames, timings):
        slide = SEMANTIC_LAYOUTS[frame.kind](prs, session, frame)
        validate_semantic_slide_geometry(slide)
        spec = plan[frame.plan_index]
        rendered = "\n".join(shape.text for shape in slide.shapes if shape.has_text_frame)
        slide.notes_slide.notes_text_frame.text = presenter_notes(frame, timing, rendered)
        indices = sorted({i for atom in frame.atoms for i in atom.source_indices})
        write_metadata(slide, {
            "session": session.number,
            "source_files": {"teacher": str(session.teacher_source), "student_fallback": str(session.student_source)},
            "layout": frame.kind, "plan_index": frame.plan_index, "recognition": frame.recognition,
            "unit_ids": [unit.unit_id for unit in frame.units],
            "roles": {unit.unit_id: unit.role for unit in frame.units},
            "source_refs": [asdict(ref) for unit in frame.units for ref in unit.source_refs],
            "visible_sources": [{"index": i, "sha256": hashlib.sha256(spec.visible_content[i].encode()).hexdigest()} for i in indices],
            "notes_sources": [{"function": f, "heading": h, "sha256": hashlib.sha256(t.encode()).hexdigest()} for f, h, t in frame.notes],
            "relations": frame.relations, "timeline_refs": frame.timeline_refs,
            "composition": {"origin_slides": frame.origin_slides},
            "timing": asdict(timing),
            "code_blocks": metadata_code_blocks(spec, frame),
            "representation_needs": [{"source_need": need, "status": "resolved", "resolution": "Vistas por unidad y fronteras fuente; código íntegro y tipografía fija"}
                                     for need in spec.representation_needs],
        })
    return len(prs.slides)
