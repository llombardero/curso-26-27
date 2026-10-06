from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
COORD = ROOT / "02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION"
H1_STUDENT = ROOT / "01-ALUMNADO/02-HITOS/h1-primer-asistente"
H1_STUDENT_SESSIONS = ROOT / "01-ALUMNADO/03-SESIONES/h1"
H1_TEACHER = ROOT / "02-PROFESORADO/01-GUIAS-POR-HITO/h1-primer-asistente"
H1_TEACHER_SESSIONS = ROOT / "02-PROFESORADO/02-SESIONES/h1"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_teacher_readme_declares_document_precedence_and_generated_artifacts_are_derivatives():
    text = read(ROOT / "02-PROFESORADO/README.md").lower()
    required = (
        "normativa y las programaciones didácticas aprobadas",
        "modelo_hexa_completo.pdf",
        "modelo_hexa_aplicado_a_minijarvis.md",
        "ficha de cada hito",
        "las sesiones desarrollan la secuencia",
        "html, pptx, pdf y zip son derivados",
    )
    for phrase in required:
        assert phrase in text


def test_ra7_ra9_remain_explicitly_pending_normative_validation():
    marker = "PENDIENTE DE DECISIÓN DOCENTE / VALIDACIÓN NORMATIVA"
    assert marker in read(COORD / "01-matriz-integrada-ra-ce-evidencias-tareas.md")
    assert marker in read(COORD / "01A-anexo-programacion-ra-ce.md")


def test_active_global_documents_do_not_use_legacy_hexa_taxonomy():
    active = (
        COORD / "00-mapa-maestro-curso-2026-2027.md",
        COORD / "01-matriz-integrada-ra-ce-evidencias-tareas.md",
        COORD / "02-calendario-hitos-sprints-2026-2027.md",
    )
    forbidden = ("H–E–X–A", "H-E-X-A", "Momento HEXA", "cuatro fases")
    for path in active:
        text = read(path)
        for phrase in forbidden:
            assert phrase not in text, (path, phrase)


def test_s212_is_executar_in_h1_instruments():
    for path in (
        H1_TEACHER / "13-guia-docente-h1-primer-asistente.md",
        H1_TEACHER / "13C-checklist-correccion-h1.md",
    ):
        text = read(path)
        row = next(line for line in text.splitlines() if "H1.7" in line and line.startswith("|"))
        assert "Ejecutar" in row, path
        assert "Investigar" not in row, path


def test_h1_master_script_is_active_and_synchronized_with_the_closed_contract():
    script = H1_TEACHER_SESSIONS / "00-GUION-DOCENTE-H1-COMPLETO.md"
    text = read(script).lower()
    assert script.is_file()
    assert "comparación" in text and "boolean" in text
    assert "sin bifurcar" in text or "sin bifurcación" in text
    assert not re.search(r"(?m)^\s*(?:}\s*else|else\s+if|if\s*\()", text)


def test_h1_contract_requires_boolean_comparison_without_branching():
    sources = (
        H1_STUDENT / "13B-ficha-alumnado-h1-primer-asistente.md",
        H1_TEACHER / "13-guia-docente-h1-primer-asistente.md",
        H1_TEACHER / "13C-checklist-correccion-h1.md",
        COORD / "06-rubricas-hitos.md",
        ROOT / "01-ALUMNADO/00-EMPIEZA-AQUI/06-rubricas-hitos.md",
    )
    for path in sources:
        text = read(path)
        assert "comparación" in text.lower(), path
        assert "boolean" in text.lower(), path
        assert "sin bifurc" in text.lower() or "sin decisión" in text.lower(), path


def test_h1_checklist_covers_all_closed_minimums_without_h2_control_flow():
    text = read(H1_TEACHER / "13C-checklist-correccion-h1.md").lower()
    required = (
        "compila", "ejecuta", "variable", "tipo", "constante", "scanner",
        "nextline", "conversión", "cálculo", "salida", "comparación",
        "boolean", "nombres", "readme", "evidencia", "defensa",
    )
    for phrase in required:
        assert phrase in text
    assert "sin bifurcación" in text or "sin decisión" in text
    assert "rama `true`" not in text
    assert "rama `false`" not in text


def test_h1_active_materials_contain_no_branching_code():
    paths = [
        *H1_STUDENT.glob("*.md"),
        *H1_STUDENT_SESSIONS.glob("S*-alumnado.md"),
        *H1_TEACHER.glob("*.md"),
        *H1_TEACHER_SESSIONS.glob("S*-docente.md"),
    ]
    branching_code = re.compile(r"(?m)^\s*(?:}\s*else|else\s+if|if\s*\()")
    for path in paths:
        assert not branching_code.search(read(path)), path


def test_h1_moodle_contract_is_single_and_minimal():
    canonical = read(ROOT / "02-PROFESORADO/05-ECOSISTEMA-DIGITAL/TAREAS-MOODLE/H1-tarea-moodle.md").lower()
    for phrase in (
        "tag `h1-entrega` o commit estable",
        "no volver a copiar urls estables",
        "no adjuntar",
        "evidencia no-code excepcional",
    ):
        assert phrase in canonical
    for path in (
        H1_STUDENT / "ENTREGA-DIGITAL.md",
        H1_STUDENT_SESSIONS / "S215-defensa-y-cierre-h1-alumnado.md",
        H1_TEACHER_SESSIONS / "S215-defensa-y-cierre-h1-docente.md",
        ROOT / "03-EJEMPLOS-LAURA-PRIVADOS/ENTREGAS-MOODLE/H1-entrega.md",
    ):
        text = read(path).lower()
        assert "h1-entrega" in text and "commit estable" in text, path
        assert any(phrase in text for phrase in (
            "no volver a copiar urls estables",
            "no vuelvas a copiar urls estables",
            "enlaces estables que ya fueron proporcionados",
        )), path


def test_active_global_h1_references_do_not_link_to_removed_paths():
    active = [
        *COORD.glob("*.md"),
        *H1_TEACHER.glob("*.md"),
        *H1_TEACHER_SESSIONS.glob("S*-docente.md"),
        *H1_STUDENT.glob("*.md"),
    ]
    forbidden_destinations = (
        "99-ejemplos-alumna",
        "15-guia-basica-github-alumnado",
        "documentacion/Propuesta Ciclos Superiores IESHLanz 2026-27.pdf",
        "perfil-salida-diseno-inverso-dam-daw.md",
    )
    for path in active:
        text = read(path)
        destinations = re.findall(r"\[[^]]*\]\(([^)]+)\)", text)
        for stale in forbidden_destinations:
            assert not any(stale in destination for destination in destinations), (path, stale)


def test_h1_temporalization_gap_is_explicitly_pending_teacher_decision():
    marker = "PENDIENTE DE DECISIÓN DOCENTE"
    assert marker in read(COORD / "02-calendario-hitos-sprints-2026-2027.md")


def test_published_h1_javac_commands_use_separate_output_directory():
    for path in (
        ROOT / "01-ALUMNADO/01-LIBRO-POR-HITOS/01-primeros-programas-java.md",
        H1_STUDENT_SESSIONS / "S214-readme-y-evidencia-de-ejecucion-alumnado.md",
    ):
        text = read(path)
        assert "javac -d out src/Main.java" in text, path
        assert "java -cp out Main" in text, path
        assert "javac src/Main.java" not in text, path
