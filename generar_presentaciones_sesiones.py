#!/usr/bin/env python3
"""Genera una presentación PPTX para cada sesión de MiniJarvis."""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parent
STUDENT_ROOT = ROOT / "01-ALUMNADO" / "03-SESIONES"
TEACHER_ROOT = ROOT / "02-PROFESORADO" / "02-SESIONES"
OUTPUT_ROOT = ROOT / "02-PROFESORADO" / "03-PRESENTACIONES" / "POR-SESION"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

INK = RGBColor(28, 35, 48)
MUTED = RGBColor(88, 98, 112)
PAPER = RGBColor(249, 247, 242)
WHITE = RGBColor(255, 255, 255)
SOFT = RGBColor(235, 238, 242)
DARK = RGBColor(18, 24, 36)
GREEN = RGBColor(36, 126, 92)
RED = RGBColor(177, 58, 58)

COLORS = {
    "h0": RGBColor(204, 79, 62),
    "h1": RGBColor(47, 91, 168),
    "h2": RGBColor(20, 124, 136),
    "h3": RGBColor(53, 129, 84),
    "c1": RGBColor(111, 79, 154),
    "h4": RGBColor(105, 75, 157),
    "h5": RGBColor(200, 112, 34),
    "c2": RGBColor(111, 79, 154),
    "h6": RGBColor(33, 89, 122),
    "h7": RGBColor(156, 57, 117),
    "hf": RGBColor(109, 87, 37),
}


@dataclass
class Session:
    number: str
    folder: str
    topic: str
    hito: str
    duration: str
    objective: str
    evidence: str
    materials: list[str]
    steps: list[str]
    concepts: list[str]
    activity: list[str]
    checklist: list[str]
    safety: list[str]
    close_question: str
    source: Path


def clean(text: str) -> str:
    text = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def shorten(text: str, limit: int = 150) -> str:
    text = clean(text)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def section(text: str, title_pattern: str) -> str:
    match = re.search(
        rf"^##\s+{title_pattern}.*?\n(.*?)(?=^##\s+|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return match.group(1).strip() if match else ""


def list_items(text: str, limit: int = 6) -> list[str]:
    items: list[str] = []
    for line in text.splitlines():
        match = re.match(r"\s*(?:\d+\.|[-*]\s*(?:\[[ xX]\])?)\s+(.+)", line)
        if match:
            value = shorten(match.group(1), 170)
            if value and value not in items:
                items.append(value)
        if len(items) >= limit:
            break
    return items


def meaningful_lines(text: str, limit: int = 5) -> list[str]:
    result: list[str] = []
    in_code = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not line or line.startswith("|") or re.match(r"^[-:| ]+$", line):
            continue
        if line.startswith("###"):
            value = clean(line.lstrip("# "))
        elif re.match(r"^(?:\d+\.|[-*])\s+", line):
            value = clean(re.sub(r"^(?:\d+\.|[-*])\s+", "", line))
        elif in_code or not line.startswith("#"):
            value = clean(line)
        else:
            continue
        value = re.sub(r"^\d+\.\s*", "", value)
        if value and not set(value) <= {".", "_"} and value not in result:
            result.append(shorten(value, 165))
        if len(result) >= limit:
            break
    return result


def first_table_values(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if "Hoy vas" in line and "Debe quedar" in line:
            for candidate in lines[index + 2 : index + 6]:
                if candidate.strip().startswith("|"):
                    cells = [clean(cell) for cell in candidate.strip().strip("|").split("|")]
                    if len(cells) >= 2:
                        return cells[0], cells[1]
    return "Comprender y aplicar el objetivo de la sesión.", "Una evidencia comprobable y defendible."


def extract_close(text: str) -> str:
    close = section(text, "Cierre")
    bold = re.search(r"\*\*(.+?)\*\*", close, flags=re.DOTALL)
    if bold:
        return shorten(bold.group(1), 190)
    lines = meaningful_lines(close, 2)
    return lines[0] if lines else "¿Qué has hecho y cómo sabes que funciona?"


def parse_session(student_path: Path, teacher_path: Path | None) -> Session:
    text = student_path.read_text(encoding="utf-8")
    teacher = teacher_path.read_text(encoding="utf-8") if teacher_path and teacher_path.exists() else ""
    number_match = re.search(r"S(\d{3})", student_path.name)
    number = number_match.group(1) if number_match else "000"
    headings = re.findall(r"^##\s+(.+)$", text, flags=re.MULTILINE)
    topic = clean(headings[0]) if headings else student_path.stem
    objective, evidence = first_table_values(text)
    duration_match = re.search(r"\*\*Tiempo previsto:\*\*\s*([^\n]+)", text)
    hito_match = re.search(r"\*\*Hito:\*\*\s*([^\n.]+)", text)
    duration = clean(duration_match.group(1)).rstrip(".  ") if duration_match else "45 minutos"
    hito = clean(hito_match.group(1)) if hito_match else student_path.parent.name.upper()

    materials = list_items(section(text, "Material que necesitas"), 4)
    steps = list_items(section(text, "Trabajo de hoy"), 5)
    checklist = list_items(section(text, "Evidencia mínima antes de salir"), 5)
    safety = list_items(section(text, "Seguridad y uso de IA"), 4)

    concepts = meaningful_lines(section(teacher, "Qué debes explicar"), 4)
    if not concepts:
        concepts = meaningful_lines(section(text, "Actividad incluida"), 4)
    if not concepts:
        concepts = [objective, "Relaciona la explicación con una prueba observable."]

    activity = meaningful_lines(section(text, "Actividad incluida"), 5)
    if not activity:
        activity = meaningful_lines(section(teacher, "Ejemplo o demostración preparada"), 3)
    if not activity:
        activity = steps[2:5] if len(steps) >= 3 else steps
    if len(set(concepts) & set(activity)) >= min(2, len(concepts), len(activity)):
        concepts = [
            objective,
            "Relaciona el producto con el proceso, la prueba y la explicación.",
            f"La evidencia esperada es: {evidence}",
        ]

    return Session(
        number=number,
        folder=student_path.parent.name,
        topic=topic,
        hito=hito,
        duration=duration,
        objective=shorten(objective, 220),
        evidence=shorten(evidence, 220),
        materials=materials,
        steps=steps,
        concepts=concepts,
        activity=activity,
        checklist=checklist,
        safety=safety,
        close_question=extract_close(text),
        source=student_path,
    )


def add_full_background(slide, color: RGBColor) -> None:
    shape = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_text(slide, x, y, w, h, text, size=24, color=INK, bold=False, font="Aptos", align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(x, y, w, h)
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = frame.margin_right = Inches(0.04)
    frame.margin_top = frame.margin_bottom = Inches(0.03)
    paragraph = frame.paragraphs[0]
    paragraph.text = text
    paragraph.alignment = align
    paragraph.font.name = font
    paragraph.font.size = Pt(size)
    paragraph.font.bold = bold
    paragraph.font.color.rgb = color
    return box


def add_bullets(slide, x, y, w, h, items: list[str], size=22, color=INK, numbered=False):
    box = slide.shapes.add_textbox(x, y, w, h)
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(0.08)
    frame.margin_right = Inches(0.05)
    frame.margin_top = Inches(0.04)
    for index, item in enumerate(items or ["Sigue la consigna indicada en clase."], start=1):
        paragraph = frame.paragraphs[0] if index == 1 else frame.add_paragraph()
        paragraph.text = f"{index}. {item}" if numbered else item
        paragraph.font.name = "Aptos"
        paragraph.font.size = Pt(size)
        paragraph.font.color.rgb = color
        paragraph.space_after = Pt(10)
        if not numbered:
            paragraph.text = f"•  {paragraph.text}"
    return box


def add_footer(slide, session: Session, accent: RGBColor) -> None:
    bar = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, 0, Inches(7.22), SLIDE_W, Inches(0.28))
    bar.fill.solid()
    bar.fill.fore_color.rgb = accent
    bar.line.fill.background()
    add_text(slide, Inches(0.45), Inches(7.25), Inches(12.3), Inches(0.18), f"MiniJarvis · 1.º DAW · Sesión {session.number} · {session.hito}", 9, WHITE)


def base_slide(prs: Presentation, session: Session, title: str, kicker: str = ""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_full_background(slide, PAPER)
    accent = COLORS.get(session.folder, RGBColor(47, 91, 168))
    side = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, 0, 0, Inches(0.18), SLIDE_H)
    side.fill.solid()
    side.fill.fore_color.rgb = accent
    side.line.fill.background()
    if kicker:
        add_text(slide, Inches(0.55), Inches(0.34), Inches(5.5), Inches(0.28), kicker.upper(), 10, accent, True)
    add_text(slide, Inches(0.55), Inches(0.68), Inches(12.1), Inches(0.58), title, 28, INK, True)
    add_footer(slide, session, accent)
    return slide, accent


def add_card(slide, x, y, w, h, title: str, body: str, accent: RGBColor, icon: str):
    card = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, x, y, w, h)
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = SOFT
    add_text(slide, x + Inches(0.25), y + Inches(0.22), Inches(0.48), Inches(0.45), icon, 24, accent, True, align=PP_ALIGN.CENTER)
    add_text(slide, x + Inches(0.82), y + Inches(0.25), w - Inches(1.05), Inches(0.4), title, 17, accent, True)
    add_text(slide, x + Inches(0.3), y + Inches(0.95), w - Inches(0.6), h - Inches(1.2), body, 22, INK)


def build_presentation(session: Session, target: Path) -> None:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    accent = COLORS.get(session.folder, RGBColor(47, 91, 168))

    # 1. Portada
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_full_background(slide, DARK)
    stripe = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, 0, 0, Inches(0.25), SLIDE_H)
    stripe.fill.solid(); stripe.fill.fore_color.rgb = accent; stripe.line.fill.background()
    badge = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(0.62), Inches(2.0), Inches(0.62))
    badge.fill.solid(); badge.fill.fore_color.rgb = accent; badge.line.fill.background()
    add_text(slide, Inches(0.78), Inches(0.74), Inches(1.84), Inches(0.28), f"SESIÓN {session.number}", 14, WHITE, True, align=PP_ALIGN.CENTER)
    add_text(slide, Inches(0.72), Inches(1.68), Inches(11.8), Inches(1.8), session.topic, 38, WHITE, True)
    add_text(slide, Inches(0.75), Inches(4.18), Inches(7.4), Inches(0.42), f"{session.hito}  ·  {session.duration}", 19, RGBColor(190, 200, 214), True)
    add_text(slide, Inches(0.75), Inches(5.55), Inches(11.2), Inches(0.7), "Hoy construiremos una evidencia que puedas comprobar y explicar.", 24, WHITE)
    add_text(slide, Inches(0.75), Inches(6.86), Inches(11.6), Inches(0.22), "MINIJARVIS · PROGRAMACIÓN + ENTORNOS DE DESARROLLO", 10, RGBColor(160, 170, 185), True)

    # 2. Objetivo y evidencia
    slide, accent = base_slide(prs, session, "Qué vamos a conseguir", "Punto de partida")
    add_card(slide, Inches(0.65), Inches(1.55), Inches(5.85), Inches(4.75), "Hoy vas a…", session.objective, accent, "01")
    add_card(slide, Inches(6.82), Inches(1.55), Inches(5.85), Inches(4.75), "Debe quedar…", session.evidence, accent, "02")

    # 3. Ruta
    slide, accent = base_slide(prs, session, "Ruta de trabajo", "Paso a paso")
    steps = session.steps[:5] or [session.objective, "Realiza una prueba observable.", "Guarda la evidencia y prepárate para explicarla."]
    y = 1.45
    for index, step in enumerate(steps, start=1):
        circle = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.OVAL, Inches(0.75), Inches(y), Inches(0.55), Inches(0.55))
        circle.fill.solid(); circle.fill.fore_color.rgb = accent; circle.line.fill.background()
        add_text(slide, Inches(0.75), Inches(y + 0.12), Inches(0.55), Inches(0.22), str(index), 14, WHITE, True, align=PP_ALIGN.CENTER)
        add_text(slide, Inches(1.55), Inches(y + 0.02), Inches(10.8), Inches(0.6), step, 20, INK)
        y += 1.02

    # 4. Claves y actividad
    slide, accent = base_slide(prs, session, "Claves para avanzar", "Comprender y aplicar")
    left = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.45), Inches(5.75), Inches(4.95))
    left.fill.solid(); left.fill.fore_color.rgb = WHITE; left.line.color.rgb = SOFT
    right = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.45), Inches(5.92), Inches(4.95))
    right.fill.solid(); right.fill.fore_color.rgb = WHITE; right.line.color.rgb = SOFT
    add_text(slide, Inches(0.95), Inches(1.75), Inches(5.1), Inches(0.4), "IDEAS CLAVE", 16, accent, True)
    add_bullets(slide, Inches(0.95), Inches(2.32), Inches(5.0), Inches(3.65), session.concepts[:4], 18)
    add_text(slide, Inches(7.05), Inches(1.75), Inches(5.0), Inches(0.4), "ACTIVIDAD CENTRAL", 16, accent, True)
    add_bullets(slide, Inches(7.05), Inches(2.32), Inches(5.05), Inches(3.65), session.activity[:5], 18)

    # 5. Evidencia
    slide, accent = base_slide(prs, session, "Antes de salir, comprueba", "Evidencia mínima")
    checklist = session.checklist[:5] or [f"He producido o actualizado: {session.evidence}", "Puedo señalar dónde está.", "Puedo explicar una decisión.", "Puedo mostrar una prueba."]
    y = 1.5
    for item in checklist:
        square = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.78), Inches(y), Inches(0.46), Inches(0.46))
        square.fill.solid(); square.fill.fore_color.rgb = WHITE; square.line.color.rgb = accent
        add_text(slide, Inches(1.52), Inches(y - 0.01), Inches(10.7), Inches(0.65), item, 20, INK)
        y += 0.98
    if session.materials:
        add_text(slide, Inches(0.8), Inches(6.48), Inches(11.8), Inches(0.3), "Necesitas: " + " · ".join(session.materials[:3]), 12, MUTED)

    # 6. Cierre
    slide, accent = base_slide(prs, session, "Cierre de la sesión", "Comprueba y explica")
    question_box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.68), Inches(1.42), Inches(11.95), Inches(2.15))
    question_box.fill.solid(); question_box.fill.fore_color.rgb = accent; question_box.line.fill.background()
    add_text(slide, Inches(1.05), Inches(1.77), Inches(11.15), Inches(0.35), "PREGUNTA DE SALIDA", 14, WHITE, True)
    add_text(slide, Inches(1.05), Inches(2.25), Inches(11.0), Inches(0.9), session.close_question, 27, WHITE, True)
    safety = session.safety[:3] or ["Usa datos ficticios.", "No compartas contraseñas ni claves.", "Registra y valida cualquier uso de IA."]
    add_text(slide, Inches(0.78), Inches(4.05), Inches(4.1), Inches(0.35), "RECUERDA", 15, accent, True)
    add_bullets(slide, Inches(0.78), Inches(4.5), Inches(7.2), Inches(1.85), safety, 17)
    done = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(8.45), Inches(4.15), Inches(4.05), Inches(1.75))
    done.fill.solid(); done.fill.fore_color.rgb = WHITE; done.line.color.rgb = SOFT
    add_text(slide, Inches(8.78), Inches(4.47), Inches(3.35), Inches(0.95), "La sesión termina cuando la evidencia existe, está comprobada y puedes defenderla.", 18, GREEN, True, align=PP_ALIGN.CENTER)

    target.parent.mkdir(parents=True, exist_ok=True)
    prs.save(target)


def teacher_for(student_path: Path) -> Path:
    relative = student_path.relative_to(STUDENT_ROOT)
    return TEACHER_ROOT / relative.with_name(relative.name.replace("-alumnado.md", "-docente.md"))


def generate_index(sessions: list[tuple[Session, Path]]) -> None:
    lines = [
        "# Presentaciones por sesión - MiniJarvis",
        "",
        "Cada presentación está diseñada para proyectarse al alumnado y se corresponde con una ficha de sesión.",
        "",
        "| Sesión | Hito | Tema | Presentación |",
        "|---:|---|---|---|",
    ]
    for session, target in sessions:
        relative = target.relative_to(OUTPUT_ROOT).as_posix()
        lines.append(f"| {session.number} | {session.hito} | {session.topic} | `{relative}` |")
    (OUTPUT_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True)
    generated: list[tuple[Session, Path]] = []
    for student_path in sorted(STUDENT_ROOT.rglob("S*-alumnado.md")):
        session = parse_session(student_path, teacher_for(student_path))
        filename = student_path.name.replace("-alumnado.md", "-presentacion.pptx")
        target = OUTPUT_ROOT / student_path.parent.name / filename
        build_presentation(session, target)
        generated.append((session, target))
    generated.sort(key=lambda item: int(item[0].number))
    generate_index(generated)
    print(f"Presentaciones generadas: {len(generated)}")


if __name__ == "__main__":
    main()
