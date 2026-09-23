import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEACHER_SESSIONS = ROOT / "02-PROFESORADO" / "02-SESIONES"
METHODOLOGY_ROOT = ROOT / "02-PROFESORADO" / "04-RECURSOS-NORMATIVOS-Y-TEMARIOS"
OPERATIONAL_MODEL = METHODOLOGY_ROOT / "Modelo_HEXA_APLICADO_A_MINIJARVIS.md"
CANONICAL_PDF = METHODOLOGY_ROOT / "Modelo_HEXA_COMPLETO.pdf"
PHASES = (
    "Activar — entender el reto",
    "Investigar — aprender lo necesario",
    "Idear — proponer soluciones",
    "Planificar — organizar el trabajo",
    "Ejecutar — crear",
    "Comunicar — evaluar y reflexionar",
)


def marked_hexa_blocks():
    start = "<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->"
    end = "<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->"
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if start in text:
            yield path, text.split(start, 1)[1].split(end, 1)[0]


def test_operational_model_uses_canonical_pdf_and_six_phases():
    assert CANONICAL_PDF.is_file()
    text = OPERATIONAL_MODEL.read_text(encoding="utf-8")
    assert "Modelo_HEXA_COMPLETO.pdf" in text
    assert "Fase 0 — Equipos" in text
    for number, phase in enumerate(PHASES, 1):
        assert f"{number}. {phase}" in text


def test_every_marked_hexa_cycle_uses_all_six_canonical_phases():
    blocks = list(marked_hexa_blocks())
    assert len(blocks) == 27
    for path, block in blocks:
        for number, phase in enumerate(PHASES, 1):
            assert f"**{number} — {phase.split(' — ', 1)[0]}**" in block, path
        assert "H — Hecho" not in block, path
        assert "E — Exploración" not in block, path
        assert "X — eXplicación" not in block, path
        assert "A — Aplicación" not in block, path


def test_hexa_correction_checklists_preserve_six_phase_review_table():
    paths = sorted((ROOT / "02-PROFESORADO" / "01-GUIAS-POR-HITO").rglob("*C-checklist-correccion-*.md"))
    assert len(paths) == 8
    for path in paths:
        text = path.read_text(encoding="utf-8")
        assert "### Lista de comprobación del ciclo" in text, path
        for number, phase in enumerate(PHASES, 1):
            assert f"| {number} — {phase.split(' — ', 1)[0]}" in text, path


def test_all_teacher_sessions_use_named_hexa_phases():
    paths = sorted(TEACHER_SESSIONS.rglob("S*-docente.md"))
    assert len(paths) == 106
    allowed = {phase.split(" — ", 1)[0] for phase in PHASES} | {"Fase 0"}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        match = re.search(r"\| Fase HEXA(?: del hito)? \| ([^|]+) \|", text)
        assert match, path
        labels = {
            part.strip()
            for part in re.split(r"\s*(?:→|\+)\s*", match.group(1))
        }
        for label in labels:
            short = label.split(" — ", 1)[0]
            assert short in allowed, (path, label)
        assert not re.search(r"\| Momento HEXA", text), path


def test_project_no_longer_defines_hexa_as_four_letter_phases():
    forbidden = (
        "H — Hecho / reto",
        "E — Exploración",
        "X — eXplicación",
        "A — Aplicación",
        "HEXA: activar, idear, planificar, ejecutar, comunicar y reflexionar",
    )
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for value in forbidden:
            assert value not in text, (path, value)
