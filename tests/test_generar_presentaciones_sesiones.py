from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "generar_presentaciones_sesiones.py"


def load_module():
    spec = importlib.util.spec_from_file_location("generar_presentaciones_sesiones", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def generator():
    return load_module()


def source_pair(number: str) -> tuple[Path, Path]:
    teacher = next((ROOT / "02-PROFESORADO" / "02-SESIONES").rglob(f"S{number}-*-docente.md"))
    student = next((ROOT / "01-ALUMNADO" / "03-SESIONES").rglob(f"S{number}-*-alumnado.md"))
    return teacher, student


def semantic_text(session, *categories: str) -> str:
    return " ".join(
        block.heading + " " + block.content
        for category in categories
        for block in session.semantic_blocks[category]
    )


def timeline_minutes(session) -> int:
    total = 0
    for block in session.timeline:
        match = __import__("re").search(r"(\d+)\s*[–-]\s*(\d+)", block.time)
        assert match, block.time
        total += int(match.group(2)) - int(match.group(1))
    return total


def test_teacher_guide_is_primary_source_for_special_h0_session(generator):
    teacher, student = source_pair("203")

    session = generator.parse_session(teacher, student)

    assert session.number == "203"
    assert "Mapa HADA" in session.objective
    assert "funciones justificadas" in session.objective
    assert session.duration == "45 minutos"
    assert any("0–4" in block.time for block in session.timeline)
    assert any("HADA" in item for item in session.key_concepts)
    assert "Comprender y aplicar el objetivo" not in session.objective


def test_parser_accepts_numbered_and_unnumbered_headings(generator):
    teacher, student = source_pair("203")

    session = generator.parse_session(teacher, student)

    assert session.materials
    assert session.timeline
    assert session.closure


def test_restored_h1_title_comes_from_primary_heading_not_stale_student_title(generator):
    teacher, student = source_pair("213")

    session = generator.parse_session(teacher, student)

    assert session.number == "213"
    assert session.topic == "Comparaciones, lógica y decisiones"
    assert session.field_sources["topic"] == "teacher"
    assert session.field_sources["objective"] == "teacher"
    assert session.topic != "Limpieza, nombres claros y simplicidad"
    assert "Limpieza, nombres claros y simplicidad" not in session.objective


def test_semantic_model_preserves_unknown_teacher_headings(generator):
    teacher, student = source_pair("215")
    teacher_text = teacher.read_text(encoding="utf-8")

    session = generator.parse_session(teacher, student)

    parsed_teacher_headings = {
        block.heading
        for blocks in session.semantic_blocks.values()
        for block in blocks
        if block.source == "teacher"
    }
    source_headings = {heading for heading, _ in generator.heading_blocks(teacher_text)}
    assert parsed_teacher_headings == source_headings


@pytest.mark.parametrize("number", ("208", "210", "213", "215"))
def test_restored_h1_temporalization_is_parsed_in_order(generator, number):
    teacher, student = source_pair(number)

    session = generator.parse_session(teacher, student)

    assert session.timeline
    assert session.field_sources["timeline"] == "teacher"
    assert session.timeline[0].time.startswith("0")
    assert all(block.action for block in session.timeline)


def test_s210_temporalization_totals_45_minutes(generator):
    teacher, student = source_pair("210")

    session = generator.parse_session(teacher, student)

    assert timeline_minutes(session) == 45


def test_s215_timeline_preserves_parallel_work(generator):
    teacher, student = source_pair("215")

    session = generator.parse_session(teacher, student)

    combined = " ".join(
        block.action + " " + " ".join(block.details.values())
        for block in session.timeline
    )
    assert "Defensas individuales" in combined
    assert "Ensayo y revisión por parejas" in combined
    assert any(block.details for block in session.timeline)


def test_s206_semantic_model_preserves_quality_concepts(generator):
    teacher, student = source_pair("206")

    session = generator.parse_session(teacher, student)
    text = semantic_text(session, "concepts", "explanations").lower()

    assert "correcto" in text
    assert "eficiente" in text
    assert "mantenible" in text


def test_s212_semantic_contract_preserves_conversions(generator):
    teacher, student = source_pair("212")

    session = generator.parse_session(teacher, student)
    text = semantic_text(session, "concepts", "explanations", "examples", "predictions")

    for fragment in (
        "Scanner",
        "nextLine",
        "Integer.parseInt",
        "Double.parseDouble",
        "conversión implícita",
        "casting",
        "pérdida de información",
    ):
        assert fragment in text
    assert session.moment == "Ejecutar — crear"
    assert session.grouping == "INDIVIDUAL → PAREJAS"
    assert session.field_sources["moment"] == "teacher"
    assert session.field_sources["grouping"] == "teacher"


def test_s213_semantic_contract_preserves_core_and_recognition_signals(generator):
    teacher, student = source_pair("213")

    session = generator.parse_session(teacher, student)
    text = semantic_text(session, "concepts", "explanations", "examples", "predictions")

    for fragment in ("comparadores", "true", "false", "&&", "||", "!", "if/else"):
        assert fragment in text
    recognition_blocks = [
        block
        for block in session.semantic_blocks["concepts"]
        if "anidad" in (block.heading + block.content).lower()
        or "ternario" in (block.heading + block.content).lower()
    ]
    recognition = " ".join(
        block.heading + " " + block.content + " " + " ".join(block.signals)
        for block in recognition_blocks
    )
    assert "anidad" in recognition
    assert "ternario" in recognition
    assert "sin profundizar" in recognition
    assert "limitad" in recognition
    assert all(block.role == "recognition" for block in recognition_blocks)


def test_s214_semantic_contract_preserves_reproducibility_and_delivery_preparation(generator):
    teacher, student = source_pair("214")

    session = generator.parse_session(teacher, student)
    text = semantic_text(
        session,
        "concepts",
        "explanations",
        "student_activity",
        "evidence",
        "moodle_delivery",
    )

    for fragment in ("README", "reproducible", "permiso", "Moodle"):
        assert fragment in text


def test_s215_semantic_contract_keeps_closure_components_separate(generator):
    teacher, student = source_pair("215")

    session = generator.parse_session(teacher, student)

    assert "defensa" in semantic_text(session, "defense").lower()
    assert "banco de preguntas" in semantic_text(session, "questions").lower()
    assert "review" in semantic_text(session, "review").lower()
    assert "retrospectiva" in semantic_text(session, "retrospective").lower()
    assert "moodle" in semantic_text(session, "moodle_delivery").lower()
    assert session.grouping == "Defensa INDIVIDUAL; ensayo y revisión por PAREJAS; review, retrospectiva y entrega en EQUIPO"
    assert all(word in session.grouping for word in ("INDIVIDUAL", "PAREJAS", "EQUIPO"))


def test_timeline_preserves_operational_content_after_introductory_labels(generator):
    teacher, student = source_pair("203")

    session = generator.parse_session(teacher, student)
    timeline_text = " ".join(block.action for block in session.timeline)

    assert "Ayer obtuvimos una hipótesis" in timeline_text
    assert "¿Qué diferencia hay entre una preferencia HADA y una función?" in timeline_text
    assert all(not block.action.rstrip().endswith(":") for block in session.timeline)


def test_slide_plan_is_adaptive_and_preserves_content_without_ellipsis(generator):
    teacher_225, student_225 = source_pair("225")
    teacher_267, student_267 = source_pair("267")

    simple = generator.plan_slides(generator.parse_session(teacher_225, student_225))
    dense = generator.plan_slides(generator.parse_session(teacher_267, student_267))

    assert [slide.kind for slide in dense] != [slide.kind for slide in simple]
    assert any(slide.kind == "debugger" for slide in simple)
    assert any(slide.kind == "pattern" for slide in dense)
    assert all("…" not in text for slide in dense for text in [slide.title, *slide.items])
    combined = " ".join(text for slide in dense for text in [slide.title, *slide.items])
    assert "Command" in combined
    assert "Tool" in combined
    assert "sobreingeniería" in combined
    assert "problema real" in combined


def test_cli_exposes_safe_generation_modes(generator, tmp_path):
    parser = generator.build_arg_parser()

    args = parser.parse_args([
        "--check",
        "--dry-run",
        "--session",
        "S203",
        "--output-dir",
        str(tmp_path),
    ])

    assert args.check is True
    assert args.dry_run is True
    assert args.sessions == ["S203"]
    assert args.output_dir == tmp_path


def test_partial_generation_requires_an_explicit_output_directory(generator):
    args = generator.build_arg_parser().parse_args(["--session", "S203"])

    with pytest.raises(SystemExit, match="--output-dir"):
        generator.validate_cli_safety(args)


def test_atomic_publish_preserves_previous_output_in_backup(generator, tmp_path):
    output = tmp_path / "POR-SESION"
    staging = tmp_path / "staging"
    backup_root = tmp_path / "backups"
    output.mkdir()
    staging.mkdir()
    (output / "old.txt").write_text("old", encoding="utf-8")
    (staging / "new.txt").write_text("new", encoding="utf-8")

    backup = generator.atomic_publish(staging, output, backup_root)

    assert (output / "new.txt").read_text(encoding="utf-8") == "new"
    assert backup is not None
    assert (backup / "old.txt").read_text(encoding="utf-8") == "old"
    assert not staging.exists()


def test_check_reports_fallbacks_and_truncation_as_errors(generator):
    teacher, student = source_pair("225")
    session = generator.parse_session(teacher, student)

    report = generator.validate_session(session)

    assert report.errors == []
    assert report.warnings == []


def test_pilot_plans_exclude_teacher_template_noise_and_malformed_questions(generator):
    forbidden = (
        "Guion breve sugerido",
        "Hoy necesitamos comprender y practicar lo justo",
        "Producto o evidencia que debe quedar",
    )
    for number in ("203", "225", "267", "284", "306"):
        teacher, student = source_pair(number)
        session = generator.parse_session(teacher, student)
        combined = " ".join(text for slide in generator.plan_slides(session) for text in slide.items)
        assert all(marker not in combined for marker in forbidden)

    teacher, student = source_pair("284")
    assert generator.parse_session(teacher, student).close_question == "¿qué invariante debe mantener siempre Memory?"


def test_pilot_plans_preserve_session_specific_operational_content(generator):
    expected_fragments = {
        "203": (
            "La tabla orienta una conversación",
            "Ciclo 1",
            "backlog",
            "Mi responsabilidad inicial",
        ),
        "225": (
            "modo Debug",
            "command",
            "running",
            "userName",
            "docs/depuracion-h2.md",
        ),
        "267": (
            "una semejanza con Command",
            "una diferencia",
            "sobreingeniería",
        ),
        "284": (
            "throws",
            "MemoryStorageException",
            "recuerdos nulos",
            "docs/incidencia-h6.md o docs/seguridad-h6.md",
        ),
        "306": (
            "producto funcional",
            "trazabilidad",
            "plan personal de mejora",
            "Afirmación",
            "Artefacto",
        ),
    }

    for number, fragments in expected_fragments.items():
        teacher, student = source_pair(number)
        plan = generator.plan_slides(generator.parse_session(teacher, student))
        combined = " ".join([text for slide in plan for text in [slide.title, *slide.items]])
        for fragment in fragments:
            assert fragment.lower() in combined.lower(), (number, fragment)


def test_pilot_uses_content_specific_visual_structures(generator):
    expected_kind = {
        "203": "relationship",
        "225": "debugger",
        "267": "pattern",
        "284": "exception_flow",
        "306": "defense",
    }

    for number, kind in expected_kind.items():
        teacher, student = source_pair(number)
        kinds = [slide.kind for slide in generator.plan_slides(generator.parse_session(teacher, student))]
        assert kind in kinds, (number, kinds)


def test_pilot_content_specific_visuals_are_renderable(generator, tmp_path):
    for number in ("203", "225", "267", "284", "306"):
        teacher, student = source_pair(number)
        target = tmp_path / f"S{number}.pptx"

        slide_count = generator.build_presentation(generator.parse_session(teacher, student), target)

        assert target.is_file()
        assert slide_count > 0
        rendered_text = " ".join(
            shape.text
            for slide in generator.Presentation(target).slides
            for shape in slide.shapes
            if hasattr(shape, "text")
        )
        assert "…" not in rendered_text


def test_parser_uses_named_hexa_phase_from_canonical_model(generator):
    teacher, student = source_pair("212")
    session = generator.parse_session(teacher, student)

    assert session.moment == "Ejecutar — crear"
    assert session.field_sources["moment"] == "teacher"


def test_pilot_avoids_sparse_duplicate_slides(generator):
    for number in ("203", "225", "267", "284", "306"):
        teacher, student = source_pair(number)
        plan = generator.plan_slides(generator.parse_session(teacher, student))
        assert len(plan) <= 15, number
        assert all(len(slide.items) != 1 for slide in plan if slide.kind in {"timeline", "activity"}), number

    for number in ("225", "284", "306"):
        teacher, student = source_pair(number)
        kinds = [slide.kind for slide in generator.plan_slides(generator.parse_session(teacher, student))]
        assert "concepts" not in kinds, number
        assert "example" not in kinds, number


def test_full_collection_avoids_sparse_and_template_only_slides(generator):
    boilerplate = (
        "Lee el objetivo",
        "Atiende el ejemplo",
        "Atiende al ejemplo",
        "Realiza esta tarea",
        "no basta con decir",
    )
    sessions = generator.collect_sessions(None)
    assert len(sessions) == 106
    for session in sessions:
        plan = generator.plan_slides(session)
        assert len(plan) <= 15, session.number
        assert all(
            len(slide.items) != 1
            for slide in plan
            if slide.kind in {"timeline", "activity", "evidence"}
        ), session.number
        for slide in plan:
            if slide.kind == "activity":
                assert not any(item.startswith(boilerplate) for item in slide.items), session.number

    # TODO Fase 2: S212 se excluye temporalmente porque el parser semántico restaurado expone más contenido del que plan_slides puede representar actualmente. Debe reincorporarse cuando el planner use semantic_blocks.
    for number in ("212", "232", "245", "290", "304"):
        teacher, student = source_pair(number)
        kinds = [slide.kind for slide in generator.plan_slides(generator.parse_session(teacher, student))]
        assert "focus" in kinds, number
        assert "concepts" not in kinds, number
        assert "example" not in kinds, number


def test_projectable_lists_do_not_contain_join_artifacts(generator):
    for number in ("203", "225", "267", "284", "306"):
        teacher, student = source_pair(number)
        plan = generator.plan_slides(generator.parse_session(teacher, student))
        combined = " ".join(item for slide in plan for item in slide.items)

        assert ".," not in combined
        assert ";," not in combined
        assert "…" not in combined


def test_evidence_paths_are_unambiguous_in_every_pilot_slide(generator):
    for number in ("225", "284"):
        teacher, student = source_pair(number)
        plan = generator.plan_slides(generator.parse_session(teacher, student))
        combined = " ".join(text for slide in plan for text in [slide.title, *slide.items])
        assert "docs/depuracion-h2 con" not in combined
        assert "docs/incidencia-h6.md/docs/seguridad-h6.md" not in combined
        assert "docs/incidencia-h6/docs/seguridad-h6" not in combined


def test_activity_numbering_continues_across_slides_and_skips_intro(generator):
    teacher, student = source_pair("267")
    activity_slides = [
        slide
        for slide in generator.plan_slides(generator.parse_session(teacher, student))
        if slide.kind == "activity"
    ]

    assert [slide.subtitle for slide in activity_slides] == ["1", "6"]
    assert not any(item.rstrip().endswith("con:") for slide in activity_slides for item in slide.items)


def test_all_special_h0_guides_have_real_timeline_and_concepts(generator):
    for number in ("201", "202", "204", "205"):
        teacher, student = source_pair(number)
        session = generator.parse_session(teacher, student)
        assert session.timeline, number
        assert session.key_concepts, number
        assert generator.validate_session(session).errors == [], number


def test_clean_preserves_java_operators_and_removes_real_html(generator):
    text = "2 < 1 -> false\n5 > 3 -> true\nhoras >= 4\n5 != 4"
    assert generator.clean(text) == "2 < 1 -> false 5 > 3 -> true horas >= 4 5 != 4"
    assert generator.clean('<strong>Java</strong><br /> <span class="nota">dato</span>') == "Java dato"


def test_timeline_respects_markdown_pipe_escaping(generator):
    text = "## Temporalización orientativa\n\n| Tiempo | Acción | Modalidad |\n|---|---|---|\n| 0–5 min | Traducir &&, \\|\\| y ! entre lenguaje natural y Java | INDIVIDUAL |"
    block = generator.parse_markdown_timeline(text)[0]
    assert block.action == "Traducir &&, || y ! entre lenguaje natural y Java"
    assert block.details == {"Modalidad": "INDIVIDUAL"}
    assert block.modality == "INDIVIDUAL"
    assert generator.markdown_table_cells(r"| A | B \| C | D |") == ["A", "B | C", "D"]
    assert generator.markdown_table_cells(r"| A || B |") == ["A", "", "B"]
    assert generator.markdown_table_cells(r"| A \|\| B |") == ["A || B"]
    assert generator.markdown_table_cells(r"| A \\| B |") == ["A \\", "B"]


@pytest.mark.parametrize("fence", ["```", "```markdown", "```java", "~~~", "~~~~markdown"])
def test_headings_ignore_fenced_content_but_keep_the_complete_example(generator, fence):
    closing = fence[:len(fence) - len(fence.lstrip("`~"))]
    text = f"## Modelo de README\n\n{fence}\n# MiniJarvis\n## Ejecución\n## Pruebas\n{closing}\n\n## Prueba externa\nActúa."
    blocks = generator.heading_blocks(text)
    assert [heading for heading, _ in blocks] == ["Modelo de README", "Prueba externa"]
    assert "## Pruebas" in blocks[0][1]
    assert "## Pruebas" in generator.section(text, "Modelo de README")


def unit_text(unit):
    return "\n".join([*unit.visible_content, *unit.presenter_content])


def test_s212_units_preserve_numeric_chains_and_local_recognition(generator):
    session = generator.parse_session(*source_pair("212"))
    units = generator.build_pedagogical_units(session)
    for method, target in (("Integer.parseInt", "int horas"), ("Double.parseDouble", "double nota")):
        matching = [unit for unit in units if method in unit_text(unit) and target in unit_text(unit)]
        assert matching
        assert any(unit.role == "core" and "String" in "\n".join(unit.visible_content) for unit in matching)
    boolean = [unit for unit in units if "Boolean.parseBoolean" in unit_text(unit)]
    assert boolean and all(unit.role == "recognition" for unit in boolean)
    assert any("(int) valor" in unit_text(unit) and "3.999" in unit_text(unit)
               and "predicción" in unit_text(unit) and "no redondea" in unit_text(unit)
               and "pierde" in unit_text(unit) for unit in units)
    assert all(unit.source_refs for unit in units)
    assert all(unit.items is unit.visible_content for unit in units)


def test_s213_units_preserve_branches_predictions_and_recognition(generator):
    units = generator.build_pedagogical_units(generator.parse_session(*source_pair("213")))
    visible = "\n".join(text for unit in units for text in unit.visible_content)
    assert "2 < 1 -> false" in visible
    assert all(operator in visible for operator in ("&&", "||", "!"))
    branch_units = [unit for unit in units if "if (horas >= 4)" in unit_text(unit) and "else" in unit_text(unit)]
    assert any(unit.relations.get("branches") == ("condition", "true", "false") for unit in branch_units)
    assert any("prediction_cycle" in unit.relations for unit in branch_units)
    for heading in ("Lectura introductoria de decisiones anidadas", "Operador ternario como elección sencilla"):
        assert any(unit.role == "recognition" and unit.visible_content and unit.source_refs[0].heading == heading for unit in units)
    question_unit = next(unit for unit in units if unit.source_refs[0].heading == "Comprueba lo aprendido")
    assert "¿Qué condición se evalúa" in "\n".join(question_unit.visible_content)
    assert question_unit.relations.get("question_context")


def test_s214_units_preserve_readme_and_complete_reproducible_test(generator):
    session = generator.parse_session(*source_pair("214"))
    units = generator.build_pedagogical_units(session)
    assert not any(unit.source_refs[0].heading in {"Ejecución", "Pruebas", "Límites de H1", "Cómo ejecutar"} for unit in units)
    readme = [unit for unit in units if unit.source_refs[0].heading == "Modelo pedagógico de README"]
    assert len(readme) == 1 and "## Cómo ejecutar" in unit_text(readme[0])
    tests = [unit for unit in units if "Entrada usada: Laura" in unit_text(unit)]
    assert len(tests) == 1
    assert all(token in unit_text(tests[0]) for token in ("Salida esperada:", "Salida obtenida:", "Demuestra:"))
    assert tests[0].relations.get("reproducible_test") == ("input", "expected", "obtained", "meaning")


def test_s215_units_preserve_simultaneous_timeline(generator):
    session = generator.parse_session(*source_pair("215"))
    units = generator.build_pedagogical_units(session)
    for index, block in enumerate(session.timeline):
        matching = [unit for unit in units if index in unit.timeline_refs and unit.function == "timeline"]
        assert len(matching) == 1
        unit = matching[0]
        assert block.action in unit_text(unit)
        assert all(value in unit_text(unit) for value in block.details.values())
        assert "simultaneous" in unit.relations
        assert unit.modality == session.grouping


def test_units_deduplicate_parent_child_and_associate_support_without_projecting_other(generator):
    session = generator.parse_session(*source_pair("212"))
    text = """## Ideas y ejemplos
### Scanner
Pide un dato ficticio.

```java
Scanner teclado = new Scanner(System.in);

String nombre = teclado.nextLine();
```

¿Dónde almacenas lo leído con Scanner?

## Errores frecuentes
No crear otro Scanner para cada lectura.

## Andamiaje
Pregunta dónde se reutiliza Scanner.

## Nota desconocida
No hay entrega Moodle. No eliminar esta condición.
"""
    session.semantic_blocks = generator.parse_semantic_blocks(text, "")
    session.timeline = []
    units = generator.build_pedagogical_units(session)
    learning = next(unit for unit in units if unit.source_refs[0].heading == "Scanner")
    assert sum(unit_text(unit).count("Scanner teclado =") for unit in units) == 1
    assert "Scanner teclado = new Scanner(System.in);\n\nString nombre = teclado.nextLine();" in unit_text(learning)
    assert any(ref.heading == "Ideas y ejemplos" for ref in learning.source_refs)
    for function in ("common_error", "scaffolding"):
        support = next(unit for unit in units if unit.function == function)
        assert not support.visible_content and support.presenter_content
        assert learning.unit_id in support.relations["supports"]
    other = next(unit for unit in units if unit.source_refs[0].heading == "Nota desconocida")
    assert other.role == "unknown" and not other.visible_content
    assert "No hay entrega Moodle" in unit_text(other)


def test_s215_full_question_bank_is_presenter_content(generator):
    units = generator.build_pedagogical_units(generator.parse_session(*source_pair("215")))
    bank = [unit for unit in units if any(ref.heading == "Banco de preguntas para seleccionar" for ref in unit.source_refs)]
    assert bank and all(unit.presenter_content and not unit.visible_content for unit in bank)
    assert all(token in "\n".join(unit_text(unit) for unit in bank) for token in ("main", "nextLine", "constante", "rama"))


def test_mixed_learning_outcome_has_local_roles(generator):
    session = generator.parse_session(*source_pair("213"))
    units = generator.build_pedagogical_units(session)
    outcome = [unit for unit in units if unit.source_refs[0].heading == "Qué vas a aprender"]
    assert any(unit.role == "core" and "if/else" in unit_text(unit) for unit in outcome)
    assert any(unit.role == "recognition" and "ternario" in unit_text(unit) for unit in outcome)


def test_units_preserve_all_session_code_and_timeline_without_slide_planning(generator):
    import re

    sessions = generator.collect_sessions(None)
    assert len(sessions) == 106
    for session in sessions:
        units = generator.build_pedagogical_units(session)
        assert units, session.number
        assert all(unit.source_refs and unit.modality == session.grouping
                   for unit in units if unit.function != "timeline"), session.number
        content = "\n".join(unit_text(unit) for unit in units)
        teacher = session.teacher_source.read_text(encoding="utf-8")
        codes = re.findall(r"(?ms)^ {0,3}(`{3,}|~{3,})[^\n]*\n(.*?)^ {0,3}\1[ \t]*$", teacher)
        for _, code in codes:
            assert code.strip() in content, (session.number, code)
        structural = {heading for heading, _ in generator.heading_blocks(teacher)}
        assert all(ref.heading in structural for unit in units for ref in unit.source_refs
                   if ref.source == "teacher" and ref.block_index is not None), session.number
        for index, block in enumerate(session.timeline):
            intervals = [unit for unit in units if unit.function == "timeline" and unit.timeline_refs == [index]]
            assert len(intervals) == 1, session.number
            assert block.action in unit_text(intervals[0]), session.number
            assert all(value in unit_text(intervals[0]) for value in block.details.values()), session.number
            assert intervals[0].modality == (block.modality or session.grouping), session.number


def test_s215_recovery_supports_the_individual_defense(generator):
    units = generator.build_pedagogical_units(generator.parse_session(*source_pair("215")))
    defense = next(unit for unit in units if unit.source_refs[0].heading == "Defensa práctica individual")
    for heading in ("Recuperación ante una defensa insuficiente", "Andamiaje durante la defensa"):
        support = next(unit for unit in units if unit.source_refs[0].heading == heading)
        assert defense.unit_id in support.relations.get("supports", ())


def test_timeline_units_also_preserve_simultaneous_organization_instructions(generator):
    units = generator.build_pedagogical_units(generator.parse_session(*source_pair("215")))
    content = "\n".join(unit_text(unit) for unit in units)
    assert "No organices la sesión como una única actividad" in content
    assert "Distribuye funciones dentro de cada equipo" in content
