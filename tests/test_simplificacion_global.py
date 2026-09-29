from pathlib import Path
import re
from zipfile import ZipFile

from openpyxl import load_workbook
from pptx import Presentation

ROOT = Path(__file__).resolve().parents[1]
ALUMNADO = ROOT / "01-ALUMNADO"
PROFESORADO = ROOT / "02-PROFESORADO"


def test_hitos_sin_formularios_redundantes():
    hitos = sorted((ALUMNADO / "02-HITOS").iterdir())
    assert len(hitos) == 9
    for hito in hitos:
        assert not (hito / "plantillas").exists()
        names = {p.name for p in hito.iterdir() if p.is_file()}
        assert names == {"README.md", "ENTREGA-DIGITAL.md", next(n for n in names if "ficha-alumnado" in n)}


def test_sesiones_sin_bloque_administrativo_automatico():
    files = list((ALUMNADO / "03-SESIONES").rglob("S*-alumnado.md"))
    assert len(files) == 106
    for path in files:
        text = path.read_text(encoding="utf-8")
        assert "## Registro breve" not in text
        assert "## Evidencia mínima antes de salir" not in text


def test_modelo_transversal_minimo():
    diario = load_workbook(
        PROFESORADO / "05-ECOSISTEMA-DIGITAL/PLANTILLAS-MAESTRAS/01-Diario-individual-MiniJarvis.xlsx",
        read_only=True,
    )
    scrum = load_workbook(
        PROFESORADO / "05-ECOSISTEMA-DIGITAL/PLANTILLAS-MAESTRAS/02-Scrum-equipo-MiniJarvis.xlsx",
        read_only=True,
    )
    assert diario.sheetnames == ["DIARIO", "INSTRUCCIONES"]
    assert diario["DIARIO"].max_column == 7
    assert scrum.sheetnames == [
        "EQUIPO_Y_ACUERDOS", "BACKLOG_OPERATIVO", "DECISIONES_Y_BLOQUEOS",
        "REVIEW", "RETROSPECTIVA", "IA_EQUIPO", "INSTRUCCIONES",
    ]


def test_drive_operativo_no_es_espejo():
    files = [p for p in (ROOT / "04-DRIVE-5-EQUIPOS").rglob("*") if p.is_file()]
    assert len(files) == 19
    assert not any(p.suffix.lower() in {".html", ".java", ".pptx"} for p in files)
    assert len([p for p in files if p.name == "Scrum-equipo-MiniJarvis.xlsx"]) == 5


def test_moodle_distribuye_sin_ejemplos_privados():
    package = ROOT / "05-PAQUETE-MOODLE"
    assert len(list((package / "03-TAREAS-HITOS").glob("*.html"))) == 10
    assert not any("laura" in p.name.lower() for p in package.rglob("*"))
    h0 = (PROFESORADO / "05-ECOSISTEMA-DIGITAL/TAREAS-MOODLE/H0-tarea-moodle.md").read_text(encoding="utf-8")
    assert "no exige GitHub, tag, Site personal, Site de equipo" in h0


def test_html_y_presentaciones_sin_derivados_huerfanos():
    markdown = {p.relative_to(ALUMNADO).with_suffix(".html") for p in ALUMNADO.rglob("*.md")}
    html_root = ROOT / "01-ALUMNADO-HTML"
    html = {p.relative_to(html_root) for p in html_root.rglob("*.html")}
    assert html == markdown | {Path("LEEME-ALUMNADO.html")}
    pptx = sorted((PROFESORADO / "03-PRESENTACIONES/POR-SESION").rglob("S*-presentacion.pptx"))
    assert len(pptx) == 106
    for path in pptx:
        assert len(Presentation(path).slides) >= 7


def test_zips_validos_y_sin_temporales():
    archives = sorted(ROOT.glob("Minijarvis-*.zip"))
    assert len(archives) == 7
    for archive in archives:
        with ZipFile(archive) as zf:
            assert zf.testzip() is None
            assert not any(re.search(r"(^|/)(__pycache__|\.obsidian)(/|$)|\.pyc$", name) for name in zf.namelist())
