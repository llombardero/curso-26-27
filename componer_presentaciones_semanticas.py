"""Composición de apoyos H1 por relación fuente; no cambia el plan ni el reloj.

Separada de las primitivas geométricas para conservar su contrato. Las fusiones
solo se aceptan si caben con las mismas cajas de línea y tamaños de 3C.1.
"""
from dataclasses import replace
import re


def combine(parts, **changes):
    first = parts[0]
    fields = dict(
        units=list({u.unit_id: u for p in parts for u in p.units}.values()),
        atoms=[a for p in parts for a in p.atoms],
        timeline_refs=sorted({r for p in parts for r in p.timeline_refs}),
        relations={k: v for p in parts for k, v in p.relations.items()},
        notes=list(dict.fromkeys(n for p in parts for n in p.notes)),
        recognition=all(p.recognition for p in parts),
        origin_slides=tuple(n for p in parts for n in p.origin_slides),
    )
    fields.update(changes)
    return replace(first, **fields)


def presentation_atom(r, atom):
    """Measure the physical atom kind produced by the normalization stage."""
    return r.source_supports.normalize_presentation_atom(atom, set())[0]


def physical_height(r, atom, recognition=False):
    atom = presentation_atom(r, atom)
    if atom.kind == "cards":
        return r.cards_geometry(atom.text.splitlines(), rendered=True)[1]
    size = 22 if atom.kind == "code" or atom.language else 24 if recognition else 28
    if atom.kind == "pair":
        return min(max(r.rendered_height(atom.text, 5.65, size), r.rendered_height(atom.alternative, 5.65, size)),
                   r.rendered_height(atom.text, 11.9, size) + r.rendered_height(atom.alternative, 11.9, size) + 0.45) + 0.55
    return r.rendered_height(atom.text, 11.9, size)


def study_height(r, frame):
    atoms = [presentation_atom(r, atom) for atom in frame.atoms]
    columns = ([a for a in atoms if a.kind == "code"], [a for a in atoms if a.kind != "code"])
    return max(sum(r.rendered_height(a.text, width, 22 if a.kind == "code" else 24) + 0.1 for a in atoms)
               for atoms, width in zip(columns, (7.25, 4.2)))


def frame_start(r, frame):
    """Physical top of the first atom after a possibly wrapped title/header."""
    if frame.kind == "prediction":
        top = r.frame_content_top(frame, 1.5)
        header = max(0.5, r.rendered_height("Proceso: PREDICE → EJECUTA → CONTRASTA", 11.9, 24))
        return top + header + 0.30
    if frame.kind in {"check", "activity"}:
        top = r.frame_content_top(frame, 1.5)
        label = "QUÉ COMPROBAR" if frame.kind == "check" else "QUÉ HACER"
        return top + max(0.4, r.rendered_height(label, 11.9, 20)) + 0.15
    if frame.kind == "study":
        return r.frame_content_top(frame, 2.05)
    return r.frame_content_top(frame, 1.55)


def fit_existing_part(r, frame):
    """Select study for an original part only when its normalized atoms need it."""
    start = frame_start(r, frame)
    height = sum(physical_height(r, atom, frame.recognition) + 0.1 for atom in frame.atoms)
    if (start + height > 6.84 and frame.kind in {"activity", "check"}
            and all(atom.kind == "cards" for atom in frame.atoms)):
        alternative = replace(frame, kind="focus")
        if frame_start(r, alternative) + height <= 6.84:
            return alternative
    if (start + height > 6.84 and any(atom.kind == "code" for atom in frame.atoms)
            and all(atom.kind != "pair" for atom in frame.atoms) and study_height(r, frame) <= 4.79):
        return replace(frame, kind="study")
    return frame


def conservative_partition(r, parts):
    """Split an oversized unit without dropping atoms, alternatives or provenance."""
    merged = combine(parts)
    unit = merged.units[0]

    def candidate(atoms):
        kind = "comparison" if any(atom.kind == "pair" for atom in atoms) else (
            "linked_prediction" if "prediction_cycle" in unit.relations else
            "focus" if parts[0].kind in {"source_support", "readme_support"} else parts[0].kind
        )
        relations = dict(merged.relations)
        if kind == "focus":
            relations.pop("support_columns", None)
        return replace(merged, atoms=list(atoms), kind=kind, relations=relations)

    def fits(frame):
        pair = next((atom for atom in frame.atoms if atom.kind == "pair"), None)
        if pair:
            return comparison_height(r, frame) <= 6.84 - frame_start(r, frame)
        start = frame_start(r, frame)
        height = sum(physical_height(r, atom, frame.recognition) + 0.1 for atom in frame.atoms)
        return start + height <= 6.84 or (
            any(atom.kind == "code" for atom in frame.atoms)
            and study_height(r, frame) <= 4.79
        )

    chunks = []
    current = []
    for atom in merged.atoms:
        proposed = candidate([*current, atom])
        if current and not fits(proposed):
            chunks.append(candidate(current))
            current = [atom]
        else:
            current.append(atom)
    if current:
        chunks.append(candidate(current))

    result = []
    for frame in chunks:
        pair = next((atom for atom in frame.atoms if atom.kind == "pair"), None)
        if pair and comparison_height(r, frame) <= 6.84 - frame_start(r, frame):
            result.append(frame)
            continue
        fitted = fit_existing_part(r, frame)
        start = frame_start(r, fitted)
        height = sum(physical_height(r, atom, fitted.recognition) + 0.1 for atom in fitted.atoms)
        if fitted.kind != "study" and start + height > 6.84:
            raise r.RepresentationError(
                f"{unit.unit_id} ({unit.source_refs[0].heading}): átomo indivisible no cabe; no se descarta"
            )
        result.append(fitted)
    return result


def quoted_literal_wrap_risk(r, atom, width=5.65):
    """A visual wrap inside a Java string makes valid source look invalid."""
    if atom.kind != "pair" or atom.language != "java":
        return False
    quoted = [{value for value in re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', code) if value}
              for code in (atom.text, atom.alternative)]
    if not quoted[0].intersection(quoted[1]):
        return False
    columns = max(1, int((width - 0.24) * 72 / (22 * 0.6)))
    return any('"' in line and len(line) > columns for code in (atom.text, atom.alternative)
               for line in code.splitlines())


def java_pair_wrap_risk(atom, width=5.65):
    if atom.kind != "pair" or atom.language != "java":
        return False
    columns = max(1, int((width - 0.24) * 72 / (22 * 0.6)))
    return any(len(line) > columns for code in (atom.text, atom.alternative)
               for line in code.splitlines())


def stacked_comparison_height(r, frame):
    pair = next(a for a in frame.atoms if a.kind == "pair")
    pair_height = sum(r.rendered_height(code, 11.9, 22) + 0.55 + 0.03
                      for code in (pair.text, pair.alternative))
    context = sum(physical_height(r, atom, True) + 0.03
                  for atom in frame.atoms if atom is not pair)
    return pair_height + context


def compose(r, session, frames):
    for number, frame in enumerate(frames, 1):
        frame.origin_slides = (number,)
        if frame.kind != "title" and frame.units:
            frame.timeline_refs = list(frame.units[0].timeline_refs or frame.timeline_refs)
            unit = frame.units[0]
            raw = "\n\n".join(unit.visible_content + unit.presenter_content)
            if unit.relations.get("recognition_context"):
                frame.atoms = [replace(a, kind="mixed_question") if
                               "cuándo necesitas parsear" in a.text and "y por qué Integer.parseInt" in a.text else a
                               for a in frame.atoms]
            if frame.kind == "closure":
                frame.notes += [("closure", unit.source_refs[0].heading, text)
                                for text in unit.visible_content + unit.presenter_content if "¿" in text]
                if "con este valor" in "\n".join(a.text for a in frame.atoms) and "tu código" in raw:
                    frame.atoms.insert(0, r.RenderAtom("REFERENTE · tu código, su condición y el valor de prueba", ()))
    result = []
    index = 0
    while index < len(frames):
        first = frames[index]
        if first.kind in {"title", "parallel", "classification"}:
            result.append(first)
            index += 1
            continue
        end = index + 1
        while end < len(frames) and frames[end].plan_index == first.plan_index and frames[end].units[0].unit_id == first.units[0].unit_id:
            end += 1
        parts = frames[index:end]
        regrouped = []
        part_index = 0
        while part_index < len(parts):
            part = parts[part_index]
            following = parts[part_index + 1] if part_index + 1 < len(parts) else None
            card = next((a for a in part.atoms if a.kind == "cards"), None)
            local_warning = next((a for a in part.atoms
                                  if a.kind == "prose" and a.text.startswith("No ") and len(a.text) < 90), None)
            warning = (next((a for a in following.atoms
                             if a.kind == "prose" and a.text.startswith("No ") and len(a.text) < 90), None)
                       if following else None)
            boundaries = [a for a in part.atoms if a.kind == "boundary"]
            if card and local_warning and not boundaries:
                atoms = [replace(local_warning, kind="boundary"), card] + [a for a in part.atoms
                                                                           if a not in [card, local_warning]]
                candidate = replace(part, atoms=atoms)
                if frame_start(r, candidate) + sum(physical_height(r, a, candidate.recognition) + 0.1
                              for a in candidate.atoms) <= 6.84:
                    regrouped.append(candidate)
                    part_index += 1
                    continue
            if card and warning and len(boundaries) == 1:
                atoms = [replace(warning, kind="boundary"), card] + [a for a in part.atoms
                                                                     if a not in boundaries + [card]]
                candidate = combine([part, following], atoms=atoms)
                if frame_start(r, candidate) + sum(physical_height(r, a, candidate.recognition) + 0.1
                              for a in candidate.atoms) <= 6.84:
                    candidate.notes.append(("facilitation", part.title, boundaries[0].text))
                    regrouped.append(candidate)
                    part_index += 2
                    continue
            regrouped.append(part)
            part_index += 1
        parts = regrouped
        merged = combine(parts)
        unit = first.units[0]
        raw = "\n\n".join(unit.visible_content + unit.presenter_content)
        cards = [a for a in merged.atoms if a.kind == "cards"]
        warnings = [a for a in merged.atoms if a.kind == "prose" and a.text.startswith("No ") and len(a.text) < 90]
        if len(cards) == 1 and warnings:
            card = cards[0]
            expanded = replace(card, text=card.text + "\n" + "\n".join("ADVERTENCIA · " + a.text for a in warnings),
                               source_indices=card.source_indices + tuple(i for a in warnings for i in a.source_indices))
            candidate = combine(parts, atoms=[expanded] + [a for a in merged.atoms if a not in cards + warnings],
                                kind="linked_prediction" if first.kind == "prediction" else first.kind)
            if frame_start(r, candidate) + sum(physical_height(r, a, candidate.recognition) + 0.1 for a in candidate.atoms) <= 6.84:
                merged = candidate
            else:
                boundaries = [a for a in merged.atoms if a.kind == "boundary"]
                if len(boundaries) <= 1:
                    warning = replace(warnings[0], kind="boundary")
                    atoms = [warning, card] + [a for a in merged.atoms
                                               if a not in cards + warnings + boundaries]
                    candidate = combine(parts, atoms=atoms)
                    if frame_start(r, candidate) + sum(physical_height(r, a, candidate.recognition) + 0.1
                                  for a in candidate.atoms) <= 6.84:
                        if boundaries:
                            candidate.notes.append(("facilitation", unit.source_refs[0].heading,
                                                    boundaries[0].text))
                        merged = candidate
        if unit.relations.get("recognition_context"):
            merged.atoms = [replace(a, kind="mixed_question") if
                            "cuándo necesitas parsear" in a.text and "y por qué Integer.parseInt" in a.text else a
                            for a in merged.atoms]
        if merged.kind == "closure":
            merged.notes += [("closure", unit.source_refs[0].heading, text)
                             for text in unit.visible_content + unit.presenter_content if "¿" in text]
            if "con este valor" in "\n".join(a.text for a in merged.atoms) and "tu código" in raw and not any("REFERENTE ·" in a.text for a in merged.atoms):
                merged.atoms.insert(0, r.RenderAtom("REFERENTE · tu código, su condición y el valor de prueba", ()))
        has_explicit_boolean_reveal = any(
            "¿" not in atom.text and re.search(r"(?:->|→)\s*(?:true|false)\b", atom.text)
            for atom in merged.atoms
        )
        explicit_explanations = [
            atom for atom in merged.atoms
            if "¿" not in atom.text and re.search(
                r"\b(?:no redondea|descarta la parte|(?:el )?resultado (?:es|será)|la respuesta es)\b",
                atom.text, re.I,
            )
        ]
        requests_prediction_before_reveal = (
            re.search(r"(?:pregunta|predice)\s+antes\s+de\s+(?:probar|ejecutar)", raw, re.I)
            or ("question_context" in unit.relations and (has_explicit_boolean_reveal or explicit_explanations)
                and re.search(r"\bpredi(?:c|g)\w*", raw, re.I))
        )
        if requests_prediction_before_reveal:
            questions = [a for a in merged.atoms if "¿" in a.text]
            answers = [a for a in merged.atoms if a not in questions]
            if questions and answers:
                if explicit_explanations and not has_explicit_boolean_reveal:
                    question_part = next(part for part in parts if any("¿" in atom.text for atom in part.atoms))
                    first_question = min(merged.atoms.index(atom) for atom in questions)
                    last_question = max(merged.atoms.index(atom) for atom in questions)
                    references = [atom for atom in merged.atoms[:first_question]
                                  if atom.kind == "code" and atom.language == "java"]
                    reference = references[-1:] if references else []
                    reference_index = merged.atoms.index(reference[0]) if reference else first_question
                    prelude_ids = {id(atom) for atom in merged.atoms[:reference_index]}
                    for part in parts:
                        prelude = [atom for atom in part.atoms if id(atom) in prelude_ids]
                        if prelude:
                            result.append(replace(part, atoms=prelude))
                    relations = {**merged.relations, "reveal_phase": "prediction"}
                    result.append(replace(question_part, title="Antes de probar", kind="prediction",
                                          atoms=[*reference, *questions], relations=relations))
                    contrast = merged.atoms[last_question + 1:]
                    presentation_normalizations = {}
                    for position, atom in enumerate(contrast):
                        if atom not in explicit_explanations:
                            continue
                        original = next((text for text in unit.visible_content + unit.presenter_content
                                         if atom.text in r.prose_text(text)), None)
                        if original:
                            expanded = r.prose_text(original).removeprefix("Explica que ")
                            contrast[position] = replace(atom, text=expanded)
                            presentation_normalizations[original] = expanded
                    relations = {**merged.relations, "reveal_phase": "contrast"}
                    if presentation_normalizations:
                        relations["presentation_normalizations"] = presentation_normalizations
                    result.append(replace(question_part, kind="contrast", atoms=contrast, relations=relations))
                    index = end
                    continue
                relations = {**merged.relations, "reveal_phase": "prediction"}
                result.append(combine(parts, title="Antes de probar", kind="prediction", atoms=questions, relations=relations))
                relations = {**merged.relations, "reveal_phase": "contrast"}
                answer = combine(parts, atoms=answers, relations=relations)
                if frame_start(r, answer) + sum(physical_height(r, a, answer.recognition) + 0.1 for a in answers) > 6.84:
                    for part in parts:
                        remaining = [a for a in part.atoms if a not in questions]
                        if remaining:
                            result.append(replace(part, atoms=remaining, relations=relations))
                else:
                    result.append(answer)
                index = end
                continue
        codes = [a for a in merged.atoms if a.kind == "code" and a.language == "java"]
        if len(codes) >= 3 and "Misma elección" in raw:
            boundary = merged.atoms.index(codes[2])
            pair = r.RenderAtom(codes[0].text, codes[0].source_indices + codes[1].source_indices,
                                "pair", "java", codes[1].text, ("if/else · elección de valor", "?: · misma elección"))
            main = combine(parts, atoms=[pair] + [a for a in merged.atoms[:boundary] if a not in codes[:2]], kind="comparison")
            if quoted_literal_wrap_risk(r, pair):
                relations = {**main.relations, "comparison_layout": "stacked"}
                result.append(replace(main, atoms=[pair], relations=relations))
                context = [a for a in main.atoms if a is not pair]
                if context:
                    reference = r.RenderAtom("REFERENTE · las dos versiones de la pantalla anterior", (), "boundary")
                    result.append(replace(main, kind="concept", atoms=[reference, *context], relations=relations))
                merged = combine(parts, atoms=merged.atoms[boundary:])
                parts = [merged]
                codes = [a for a in merged.atoms if a.kind == "code" and a.language == "java"]
            elif comparison_height(r, main) <= 6.84 - frame_start(r, main):
                result.append(main)
                merged = combine(parts, atoms=merged.atoms[boundary:])
                parts = [merged]
                codes = [a for a in merged.atoms if a.kind == "code" and a.language == "java"]
        if len(codes) == 2 and ("Como contraste" in raw or "dos versiones" in raw):
            labels = (("Reutiliza la misma instancia", "Contraste · no modelo de H1") if "Como contraste" in raw
                      else ("Condición almacenada", "Condición directa"))
            pair = r.RenderAtom(codes[0].text, codes[0].source_indices + codes[1].source_indices,
                                "pair", "java", codes[1].text, labels)
            merged.atoms = [pair] + [a for a in merged.atoms if a not in codes]
        if not codes and unit.function == "diagnostic" and any("perder" in a.text for a in merged.atoms):
            previous = next((a for part in reversed(result) for a in reversed(part.atoms)
                             if a.kind == "code" and a.language == "java"), None)
            if previous:
                merged.atoms.insert(0, r.RenderAtom(previous.text, (), "code", "java", reference=True))
        start = frame_start(r, merged)
        height = sum(physical_height(r, a, merged.recognition) + 0.1 for a in merged.atoms)
        pair = next((a for a in merged.atoms if a.kind == "pair"), None)
        if pair and java_pair_wrap_risk(pair) and stacked_comparison_height(r, merged) <= 6.84 - start:
            relations = {**merged.relations, "comparison_layout": "stacked_with_context"}
            result.append(replace(merged, kind="comparison", relations=relations))
        elif pair and quoted_literal_wrap_risk(r, pair):
            relations = {**merged.relations, "comparison_layout": "stacked"}
            result.append(replace(merged, kind="comparison", atoms=[pair], relations=relations))
            context = [a for a in merged.atoms if a is not pair]
            if context:
                reference = r.RenderAtom("REFERENTE · las dos versiones de la pantalla anterior", (), "boundary")
                result.append(replace(merged, kind="concept", atoms=[reference, *context], relations=relations))
        elif pair and comparison_height(r, merged) <= 6.84 - start:
            result.append(replace(merged, kind="comparison"))
        elif start + height <= 6.84:
            result.append(merged)
        elif any(a.kind == "code" for a in merged.atoms) and all(a.kind != "pair" for a in merged.atoms) and study_height(r, merged) <= 4.79:
            result.append(replace(merged, kind="study"))
        else:
            result.extend(conservative_partition(r, parts))
        index = end
    index = 0
    while index < len(result):
        group = result[index:index + 3]
        headings = [f.units[0].source_refs[0].heading.lower() for f in group]
        if headings == ["correcto", "eficiente", "mantenible"]:
            criteria, extras = [], []
            parent = next((ref.heading for ref in group[0].units[0].source_refs[1:]), "")
            introduction = (result[index - 1] if index and result[index - 1].plan_index == group[0].plan_index
                            and result[index - 1].title == parent else None)
            for frame in group:
                unit = frame.units[0]
                paragraphs = [p for p in unit.visible_content + unit.presenter_content
                              if not p.endswith(":") and not p.startswith(">")]
                definition = r.prose_text(paragraphs[0]) if paragraphs else frame.atoms[0].text
                # Keep the efficiency scope limiter; details of the other criteria
                # remain verbatim in presenter notes, including compilation and names.
                if unit.source_refs[0].heading.lower() != "eficiente":
                    definition = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ])", definition)[0]
                criteria.append(r.RenderAtom(definition, frame.atoms[0].source_indices, "criterion",
                                             alternative=unit.source_refs[0].heading))
                extras.extend(a for a in frame.atoms if "¿" in a.text)
                if "Compilar no basta" in "\n".join(unit.presenter_content):
                    extras.insert(0, r.RenderAtom("Compilar no basta para decir que es correcto. Falta comprobar comportamiento.", ()))
            contextualized = [atom for atom in extras
                              if "el comportamiento que afirmáis haber construido" in atom.text]
            extras = [replace(atom, text=atom.text.replace(
                "el comportamiento que afirmáis haber construido", "el comportamiento esperado de vuestro H1"))
                if "¿" in atom.text else atom for atom in extras]
            parts = ([introduction] if introduction else []) + group
            start = index - 1 if introduction else index
            combined = combine(parts, title="Tres criterios para juzgar el alcance de H1",
                               kind="criteria", atoms=criteria + extras)
            if introduction:
                combined.notes += [("visible_detail", introduction.title, atom.text)
                                   for atom in introduction.atoms]
            combined.notes += [("visible_detail", combined.title, atom.text) for atom in contextualized]
            result[start:index + 3] = [combined]
        index += 1
    return result


def render_study(r, prs, session, frame):
    slide = r.semantic_base(prs, session, frame)
    for atoms, x, width in (([a for a in frame.atoms if a.kind == "code"], 0.7, 7.25),
                            ([a for a in frame.atoms if a.kind != "code"], 8.4, 4.2)):
        y = 2.05
        for atom in atoms:
            size = 22 if atom.kind == "code" else 24
            height = r.rendered_height(atom.text, width, size)
            if y + height > 6.84:
                raise r.RepresentationError("Código y referente no caben sin reducir tipografía")
            box = r.text_box(slide, "Código editable" if atom.kind == "code" else "Referente o acción",
                             atom.text, x, y, width, height, size=size, code=atom.kind == "code")
            box.fill.solid()
            box.fill.fore_color.rgb = r.WHITE
            y += height + 0.1
    return slide


def render_criteria(r, prs, session, frame):
    slide = r.semantic_base(prs, session, frame)
    criteria = [a for a in frame.atoms if a.kind == "criterion"]
    # Balance columns by physical line boxes, not by equal widths or font reduction.
    candidates = []
    for first in (3.1, 3.3, 3.5, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7):
        for second in (3.1, 3.3, 3.5, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7):
            widths = (first, second, 11.5 - first - second)
            if min(widths) < 2.9:
                continue
            height = max(r.rendered_height(a.text, w, 24) for a, w in zip(criteria, widths))
            candidates.append((height, widths))
    height, widths = min(candidates)
    bottom, x = 2.15 + height, 0.7
    for atom, width in zip(criteria, widths):
        if bottom > 6.0:
            raise r.RepresentationError("Criterios comparativos demasiado extensos")
        r.text_box(slide, "Criterio", atom.alternative, x, 1.55, width, 0.52, size=24, bold=True, color=r.ACCENT)
        box = r.text_box(slide, "Definición fuente", atom.text, x, 2.15, width, height, size=24)
        box.fill.solid()
        box.fill.fore_color.rgb = r.WHITE
        x += width + 0.2
    extras = [a for a in frame.atoms if a.kind != "criterion"]
    if len(extras) == 2:
        options = []
        for width in (3.5, 3.9, 4.3, 4.7, 5.1, 5.5, 5.9, 6.3, 6.7, 7.1, 7.5, 7.9, 8.3):
            widths = (width, 11.7 - width)
            options.append((max(r.rendered_height(a.text, w, 24) for a, w in zip(extras, widths)), widths))
        height, widths = min(options)
        if bottom + 0.1 + height > 6.84:
            raise r.RepresentationError("Pregunta de criterios sin espacio; no reducir fuente")
        x = 0.7
        for atom, width in zip(extras, widths):
            box = r.text_box(slide, "Comprobación del criterio", atom.text, x, bottom + 0.1, width, height, size=24)
            box.fill.solid()
            box.fill.fore_color.rgb = r.WHITE
            x += width + 0.2
    elif extras:
        cards = r.RenderAtom("\n".join(a.text for a in extras), tuple(i for a in extras for i in a.source_indices), "cards")
        if bottom + 0.1 + physical_height(r, cards) > 6.84:
            raise r.RepresentationError("Pregunta de criterios sin espacio; no reducir fuente")
        r.render_atom(slide, cards, bottom + 0.1)
    return slide


def comparison_context(r, frame):
    pair = next(a for a in frame.atoms if a.kind == "pair")
    context = [a for a in frame.atoms if a.kind != "pair"]
    heights = [0.55 + r.rendered_height(code, 5.65, 22) for code in (pair.text, pair.alternative)]
    columns = [[], []]
    for index, atom in enumerate(context):
        side = index % 2 if all(a.kind == "prose" for a in context) else min(range(2), key=heights.__getitem__)
        columns[side].append(atom)
        heights[side] += r.rendered_height(atom.text, 5.65, 22 if atom.kind == "code" else 24) + 0.1
    return heights, columns


def comparison_height(r, frame):
    return max(comparison_context(r, frame)[0])


def render_comparison(r, prs, session, frame):
    slide = r.semantic_base(prs, session, frame)
    pair = next(a for a in frame.atoms if a.kind == "pair")
    if frame.relations.get("comparison_layout") in {"stacked", "stacked_with_context"}:
        y = 1.55
        gap = .03 if frame.relations.get("comparison_layout") == "stacked_with_context" else .1
        for index, code in enumerate((pair.text, pair.alternative)):
            r.text_box(slide, f"Etiqueta alternativa {index}", pair.labels[index], .7, y, 11.9, .4,
                       size=20, bold=True, color=r.ACCENT)
            y += .55
            height = r.rendered_height(code, 11.9, 22)
            box = r.text_box(slide, f"Contraste {index}", code, .7, y, 11.9, height, size=22, code=True)
            box.fill.solid()
            box.fill.fore_color.rgb = r.WHITE
            y += height + gap
        if frame.relations.get("comparison_layout") == "stacked_with_context":
            for atom in frame.atoms:
                if atom is not pair:
                    y += r.render_atom(slide, atom, y, True) + gap
        if y > 6.84:
            raise r.RepresentationError("Comparación apilada no cabe sin reducir tipografía")
        return slide
    _, context = comparison_context(r, frame)
    for index, code in enumerate((pair.text, pair.alternative)):
        x, y = 0.7 + index * 6.15, 1.55
        r.text_box(slide, f"Etiqueta alternativa {index}", pair.labels[index], x, y, 5.65, 0.4,
                   size=20, bold=True, color=r.ACCENT)
        y += 0.55
        height = r.rendered_height(code, 5.65, 22)
        box = r.text_box(slide, f"Contraste {index}", code, x, y, 5.65, height, size=22, code=True)
        box.fill.solid()
        box.fill.fore_color.rgb = r.WHITE
        y += height
        for atom in context[index]:
            y += 0.1
            size = 22 if atom.kind == "code" else 24
            height = r.rendered_height(atom.text, 5.65, size)
            if y + height > 6.84:
                raise r.RepresentationError("Contraste y preguntas no caben sin reducir fuente")
            r.text_box(slide, "Código editable" if atom.kind == "code" else "Pregunta o límite del contraste",
                       atom.text, x, y, 5.65, height, size=size, code=atom.kind == "code")
            y += height
    return slide
