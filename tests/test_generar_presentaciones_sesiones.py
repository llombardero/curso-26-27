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
        density_scope = [slide for slide in plan if slide.kind in {"timeline", "activity", "evidence"}]
        assert generator.plan_density_errors(density_scope) == [], (session.number, generator.plan_density_errors(density_scope))
        for slide in plan:
            if slide.kind == "activity":
                assert not any(item.startswith(boilerplate) for item in slide.items), session.number

    # Contextos integrados, incluida S212: no se excluye ninguna sesión H1.
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


def test_semantic_dispatch_is_explicit_and_slide_items_are_one_projection(generator):
    session = generator.parse_session(*source_pair("206"))
    plan = generator.plan_slides(session)
    assert generator.SEMANTIC_PLANNER_HITOS == {"h1"}
    assert plan == generator.plan_slides_semantic(session)
    assert any(slide.pedagogical_units for slide in plan)
    assert all(slide.items is slide.visible_content for slide in plan)
    assert generator.plan_slides(generator.parse_session(*source_pair("203"))) == generator.plan_slides_legacy(generator.parse_session(*source_pair("203")))
    diagnostics = generator.unit_coverage(session, plan)
    assert diagnostics["sin_disposicion"] == 0
    assert diagnostics["total"] == len(generator.build_pedagogical_units(session))
    assert len(plan) <= 15


def test_semantic_s212_keeps_practice_before_mechanism_contrast(generator):
    session = generator.parse_session(*source_pair("212"))
    plan = generator.plan_slides(session)
    def location(heading):
        return next(index for index, slide in enumerate(plan) if any(unit.source_refs[0].heading == heading
                    and "visible" in slide.unit_dispositions[unit.unit_id].channels for unit in slide.pedagogical_units))
    assert location("Leer, convertir, predecir y probar — INDIVIDUAL") < location("Conversión implícita")
    assert location("Comparar, probar y explicar — PAREJAS") < location("Casting y pérdida de información")
    assert plan[location("Conversión implícita")].timeline_refs
    casting = next(unit for unit in generator.build_pedagogical_units(session) if unit.source_refs[0].heading == "Casting y pérdida de información")
    slide = plan[location("Casting y pérdida de información")]
    assert all(text in slide.items for text in casting.visible_content if text != "Pregunta:")
    assert "Pregunta:" in slide.presenter_content and "Pregunta:" not in slide.items


def visible_location(plan, heading):
    return next(index for index, slide in enumerate(plan) if any(unit.source_refs[0].heading == heading
                and "visible" in slide.unit_dispositions[unit.unit_id].channels for unit in slide.pedagogical_units))


def test_activity_modality_beats_an_incidental_explanatory_verb(generator):
    from types import SimpleNamespace

    session = SimpleNamespace(timeline=[
        generator.TimelineBlock("0–3 min", "Explicar el ejemplo."),
        generator.TimelineBlock("3–6 min", "Práctica individual: construir y probar."),
        generator.TimelineBlock("6–9 min", "Práctica por parejas: contrastar los resultados."),
    ])
    unit = generator.PedagogicalUnit("activity", [generator.SourceRef("teacher", "Comparar, probar y explicar — PAREJAS", 0)],
                                     "activity", "core")
    assert generator.semantic_timeline_index(session, unit) == 2


def test_s212_individual_attempt_precedes_pairs_and_uses_the_source_intervals(generator):
    session = generator.parse_session(*source_pair("212"))
    plan = generator.plan_slides(session)
    individual = visible_location(plan, "Leer, convertir, predecir y probar — INDIVIDUAL")
    pairs = visible_location(plan, "Comparar, probar y explicar — PAREJAS")
    assert individual < pairs
    assert plan[individual].timeline_refs == [2]
    assert plan[pairs].timeline_refs == [3]
    assert session.timeline[2].time == "12–22 min"
    assert session.timeline[3].time == "22–30 min"


def test_semantic_timeline_orders_real_actions_not_incidental_verbs(generator):
    plan = generator.plan_slides(generator.parse_session(*source_pair("212")))
    assert visible_location(plan, "Pedir, leer, guardar y utilizar") <= visible_location(plan, "Parsear texto para obtener un número")
    assert visible_location(plan, "Parsear texto para obtener un número") <= visible_location(plan, "Leer, convertir, predecir y probar — INDIVIDUAL")
    plan = generator.plan_slides(generator.parse_session(*source_pair("206")))
    assert visible_location(plan, "Activación — INDIVIDUAL") < visible_location(plan, "Actividad de clasificación — EQUIPO")
    plan = generator.plan_slides(generator.parse_session(*source_pair("214")))
    assert visible_location(plan, "Consolidación — EQUIPO") < visible_location(plan, "Comprobación externa — PAREJAS")
    plan = generator.plan_slides(generator.parse_session(*source_pair("213")))
    assert visible_location(plan, "Comprender, traducir y predecir — INDIVIDUAL") < visible_location(plan, "Contrastar, implementar y probar — PAREJAS")
    assert visible_location(plan, "Contrastar, implementar y probar — PAREJAS") < visible_location(plan, "Comprobar comprensión — INDIVIDUAL")


def test_syntax_error_named_cierre_is_not_a_closure_slide(generator):
    plan = generator.plan_slides(generator.parse_session(*source_pair("208")))
    index = visible_location(plan, "Llave de cierre ausente")
    assert plan[index].kind != "closure"
    assert index < visible_location(plan, "Comparar, depurar y explicar — PAREJAS")


def test_semantic_parent_context_is_merged_with_its_children(generator):
    plan = generator.plan_slides(generator.parse_session(*source_pair("214")))
    context = plan[visible_location(plan, "Actividad central")]
    assert any(unit.source_refs[0].heading != "Actividad central" and any(ref.heading == "Actividad central" for ref in unit.source_refs[1:]) for unit in context.pedagogical_units)
    plan = generator.plan_slides(generator.parse_session(*source_pair("215")))
    assert visible_location(plan, "Defensa práctica individual") == visible_location(plan, "Protocolo básico")
    assert visible_location(plan, "Entrega oficial Moodle y evidencias que permanecen") == visible_location(plan, "Contenido de la entrega")


def test_s215_plan_preserves_parallel_lanes_and_a_traceable_bank_sample(generator):
    session = generator.parse_session(*source_pair("215"))
    plan = generator.plan_slides(session)
    concurrency = plan[0].relations["concurrency"]
    assert concurrency["intervals"] == [{"time":block.time, "teacher":block.action, "details":block.details} for block in session.timeline]
    assert all(concurrency["lanes"][lane] for lane in ("DOCENTE", "PAREJAS", "EQUIPO"))
    assert all(slide.relations.get("schedule") == "concurrent_support" for slide in plan[1:] if slide.kind != "closure")
    bank = [unit for unit in generator.build_pedagogical_units(session) if unit.function == "question_bank"]
    defense = plan[visible_location(plan, "Protocolo básico")]
    presenter = "\n".join(text for slide in plan for text in slide.presenter_content)
    assert all(text in presenter for unit in bank for text in unit.presenter_content)
    samples = defense.relations["question_samples"]
    assert len(samples) == 6
    assert all(sample in defense.visible_content for sample in samples.values())
    assert all(sample in unit_text(next(unit for unit in bank if unit.unit_id == unit_id)) for unit_id, sample in samples.items())
    recovery = next(unit for unit in generator.build_pedagogical_units(session) if unit.source_refs[0].heading == "Recuperación ante una defensa insuficiente")
    assert any("recuper" in text.lower() for text in defense.visible_content)
    assert recovery.unit_id in defense.unit_dispositions


@pytest.mark.parametrize("number", ["212", "213", "215"])
def test_semantic_closure_prefers_the_complete_source_question(generator, number):
    import re
    session = generator.parse_session(*source_pair(number))
    units = generator.build_pedagogical_units(session)
    closing = next(unit for unit in units if unit.source_refs[0].heading in {"Comprueba lo aprendido", "Cierre de H1"})
    question = next(text for text in closing.visible_content if text.startswith("> ¿"))
    assert question in semantic_text(session, *session.semantic_blocks.keys())
    plan = generator.plan_slides(session)
    slide = plan[visible_location(plan, closing.source_refs[0].heading)]
    assert slide.kind == "closure" and slide.items[-1] == question
    assert not any(re.fullmatch(r"Pregunta[^?\n]*:", text) for text in slide.items)
    assert all(text in "\n".join([*slide.items, *slide.presenter_content]) for text in closing.visible_content)


@pytest.mark.parametrize("number", ["214", "215"])
def test_internal_continuity_is_never_student_evidence(generator, number):
    session = generator.parse_session(*source_pair(number))
    plan = generator.plan_slides(session)
    continuation = next(unit for unit in generator.build_pedagogical_units(session) if unit.function == "continuity")
    locations = [slide for slide in plan if continuation.unit_id in slide.unit_dispositions]
    assert len(locations) == 1
    assert locations[0].unit_dispositions[continuation.unit_id].channels == ("presenter",)
    assert all(text in locations[0].presenter_content for text in continuation.presenter_content)
    assert not any(text in slide.items for slide in plan for text in continuation.presenter_content)


def test_teaching_model_inside_observation_is_shared_not_hidden(generator):
    session = generator.parse_session(*source_pair("210"))
    unit = next(unit for unit in generator.build_pedagogical_units(session) if unit.function == "observation")
    model = next(text for text in unit.presenter_content if text.startswith("```text"))
    plan = generator.plan_slides(session)
    assert model in "\n".join(text for slide in plan for text in slide.items)
    target = next(slide for slide in plan if model in slide.items)
    assert any("planificar" in member.source_refs[0].heading.lower() for member in target.pedagogical_units)
    assert model in target.presenter_content


def test_pedagogical_density_accepts_an_atomic_program_but_rejects_residues(generator):
    valid = generator.SlideSpec("example", "Predice antes de ejecutar", ["```java\npublic class Main {\n    public static void main(String[] argumentos) {\n        System.out.println(2 < 1);\n    }\n}\n```"])
    assert generator.plan_density_errors([valid]) == []
    for text in ("Pregunta principal:", "La función creada.", "Lee el objetivo", "Atiende el ejemplo"):
        assert generator.plan_density_errors([generator.SlideSpec("activity", "Actividad", [text])])
    duplicate = generator.SlideSpec("example", valid.title, list(valid.items))
    assert generator.plan_density_errors([valid, duplicate])


@pytest.mark.parametrize("number", [str(number) for number in range(206, 216)])
def test_every_h1_unit_has_one_destination_and_preserves_its_content(generator, number):
    session = generator.parse_session(*source_pair(number))
    units = generator.build_pedagogical_units(session)
    plan = generator.plan_slides(session)
    assert len(plan) <= 15
    assert generator.plan_density_errors(plan) == []
    assert generator.unit_coverage(session, plan)["sin_disposicion"] == 0
    for unit in units:
        locations = [slide for slide in plan if unit.unit_id in slide.unit_dispositions]
        assert len(locations) == 1, unit.unit_id
        slide = locations[0]
        assert unit in slide.pedagogical_units
        assert all(ref in slide.source_refs for ref in unit.source_refs)
        assert slide.relations["roles"][unit.unit_id] == unit.role
        disposition = slide.unit_dispositions[unit.unit_id]
        assert disposition.reason
        content = "\n".join([*slide.visible_content, *slide.presenter_content])
        assert all(text in content for text in [*unit.visible_content, *unit.presenter_content]), (number, unit.source_refs[0].heading)
    assert plan[0].relations["modality"] == session.grouping
    assert {index for slide in plan for index in slide.timeline_refs} == set(range(len(session.timeline)))
    # Missing disposition is observable, rather than silently counted as coverage.
    del next(slide for slide in plan if units[0].unit_id in slide.unit_dispositions).unit_dispositions[units[0].unit_id]
    assert generator.unit_coverage(session, plan)["sin_disposicion"] == 1


def test_legacy_plans_match_the_clean_commit_for_all_non_adopted_hitos(generator):
    import hashlib
    import json
    import subprocess
    import types

    baseline = types.ModuleType("baseline_planner_22a")
    baseline.__file__ = str(MODULE_PATH)
    sys.modules[baseline.__name__] = baseline
    source = subprocess.check_output(["git", "show", "37ff8f1:generar_presentaciones_sesiones.py"], cwd=ROOT, text=True)
    exec(compile(source, str(MODULE_PATH), "exec"), baseline.__dict__)
    def signature(plan):
        payload = [(slide.kind, slide.title, slide.items, slide.subtitle) for slide in plan]
        return hashlib.sha256(json.dumps(payload, ensure_ascii=False).encode()).hexdigest()
    sessions = generator.collect_sessions(None)
    assert len(sessions) == 106
    checked = 0
    for session in sessions:
        if session.folder != "h1":
            expected = baseline.plan_slides(session)
            assert signature(generator.plan_slides_legacy(session)) == signature(expected), session.number
            assert signature(generator.plan_slides(session)) == signature(expected), session.number
            checked += 1
    assert checked == 96


def test_oversize_atomic_program_is_flagged_not_split(generator, monkeypatch):
    session = generator.parse_session(*source_pair("212"))
    code = "```java\npublic class Main {\n    public static void main(String[] argumentos) {\n" + "        System.out.println(2 < 1);\n" * 100 + "    }\n}\n```"
    unit = generator.PedagogicalUnit("complete-program", [generator.SourceRef("teacher", "Programa completo", 0)], "examples", "core", [code])
    monkeypatch.setattr(generator, "build_pedagogical_units", lambda session: [unit])
    plan = generator.plan_slides(session)
    projected = [slide for slide in plan if code in slide.items]
    assert len(projected) == 1 and projected[0].items == [code]
    assert projected[0].representation_needs
    assert generator.unit_coverage(session, plan)["sin_disposicion"] == 0


def test_semantic_planner_refuses_more_than_fifteen_irreducible_slides(generator, monkeypatch):
    session = generator.parse_session(*source_pair("212"))
    units = [generator.PedagogicalUnit(str(index), [generator.SourceRef("teacher", f"Actividad {index} — INDIVIDUAL", index)], "activity", "core", ["Explica y comprueba este caso. " * 100]) for index in range(16)]
    monkeypatch.setattr(generator, "build_pedagogical_units", lambda session: units)
    with pytest.raises(ValueError, match="no recorte automático"):
        generator.plan_slides(session)


@pytest.mark.parametrize("number", ["206", "212", "213", "214", "215"])
def test_critical_plan_contracts_bind_source_units_roles_and_destinations(generator, number):
    session = generator.parse_session(*source_pair(number))
    source = session.teacher_source.read_text(encoding="utf-8")
    units = generator.build_pedagogical_units(session)
    plan = generator.plan_slides(session)
    visible = "\n".join(text for slide in plan for text in [slide.title, *slide.items])
    def projected(heading):
        unit = next(unit for unit in units if unit.source_refs[0].heading == heading)
        slide = plan[visible_location(plan, heading)]
        assert generator.heading_blocks(source)[unit.source_refs[0].block_index][0] == heading
        assert any(block.heading == heading for blocks in session.semantic_blocks.values() for block in blocks)
        assert unit in slide.pedagogical_units and unit.source_refs[0] in slide.source_refs
        assert "visible" in slide.unit_dispositions[unit.unit_id].channels
        return unit, slide
    if number == "206":
        criteria = [projected(heading) for heading in ("Correcto", "Eficiente", "Mantenible")]
        assert all(slide is criteria[0][1] for _, slide in criteria)
        classification, slide = projected("Actividad de clasificación — EQUIPO")
        assert all(text in "\n".join(slide.items) for text in ("saludar", "entra en H1", "más adelante", "fuera del reto"))
        projected("Acuerdo y Scrum del equipo")
        assert not any(slide.kind == "evidence" for slide in plan)
        assert session.grouping == "INDIVIDUAL → EQUIPO"
    elif number == "212":
        for heading, tokens in (("Pedir, leer, guardar y utilizar", ("import java.util.Scanner", "public class Main", "nextLine")),
                                ("Parsear texto para obtener un número", ("String", "Integer.parseInt", "int horas")),
                                ("parseDouble y parseBoolean", ("String", "Double.parseDouble", "double nota")),
                                ("Error de ejecución: NumberFormatException", ("NumberFormatException", "compilación", "ejecución"))):
            unit, slide = projected(heading)
            assert all(token in "\n".join(slide.items) for token in tokens)
            assert all(text in "\n".join([*slide.items, *slide.presenter_content]) for text in [*unit.items, *unit.presenter_content])
        boolean = next(unit for unit in units if "Boolean.parseBoolean" in unit_text(unit))
        slide = next(slide for slide in plan if boolean.unit_id in slide.unit_dispositions)
        assert slide.relations["roles"][boolean.unit_id] == "recognition"
        assert any(unit.role == "core" and "Double.parseDouble" in unit_text(unit) for unit in slide.pedagogical_units)
    elif number == "213":
        assert plan[0].title == "Comparaciones, lógica y decisiones"
        assert "Limpieza, nombres claros y simplicidad" not in visible
        assert "2 < 1 -> false" in visible and all(operator in visible for operator in ("&&", "||", "!"))
        unit, slide = projected("Dos caminos con if/else")
        assert slide.relations["unit_relations"][unit.unit_id]["branches"] == ("condition", "true", "false")
        practice, slide = projected("Micropráctica defendible — PAREJAS")
        assert all(token in "\n".join(slide.items) for token in ("rama true", "rama false", "Salida esperada", "Salida obtenida"))
        for heading in ("Lectura introductoria de decisiones anidadas", "Operador ternario como elección sencilla"):
            unit, slide = projected(heading)
            assert unit.role == "recognition" and any(member.role == "core" for member in slide.pedagogical_units)
    elif number == "214":
        unit, slide = projected("Qué convierte una prueba en reproducible")
        assert all(token in "\n".join(slide.items) for token in ("Entrada usada", "Salida esperada", "Salida obtenida", "Demuestra"))
        assert slide.relations["unit_relations"][unit.unit_id]["reproducible_test"] == ("input", "expected", "obtained", "meaning")
        projected("Modelo pedagógico de README")
        projected("Comprobación externa — PAREJAS")
        assert "S214 prepara enlaces, permisos y documentación; S215 realiza la entrega oficial de H1." in visible
    else:
        for heading in ("Protocolo básico", "Ensayo y revisión por parejas", "Review del incremento H1 — EQUIPO", "Retrospectiva H1 — EQUIPO", "Contenido de la entrega", "Comprobación de enlaces y permisos", "Cierre de H1"):
            projected(heading)
        assert plan[0].relations["concurrency"]


@pytest.mark.parametrize("number,headings", [
    ("207", ("1. Código fuente", "2. Compilación", "3. Ejecución", "4. Consola", "Programa mínimo y salida esperada")),
    ("208", ("Programa mínimo: archivo, clase, método, instrucción y salida", "Main no es main", "Orden de ejecución")),
    ("209", ("La consola como primera interfaz", "Literal textual", "El significado contextual de +")),
    ("210", ("Mapa mínimo de tipos de Java", "Tipos primitivos y tipo de referencia")),
    ("211", ("Constante frente a variable", "División entera y división real", "Actualizaciones y estado paso a paso")),
])
def test_other_h1_sessions_keep_their_disciplinary_learning(generator, number, headings):
    plan = generator.plan_slides(generator.parse_session(*source_pair(number)))
    assert all(visible_location(plan, heading) > 0 for heading in headings)
    if number == "209":
        assert visible_location(plan, "Diseño sin IDE — PAREJAS") < visible_location(plan, "Literal textual")
    if number == "211":
        assert visible_location(plan, "Predecir y construir — INDIVIDUAL") < visible_location(plan, "División entera y división real")


def test_documentation_model_and_access_instructions_precede_external_reproduction(generator):
    plan = generator.plan_slides(generator.parse_session(*source_pair("214")))
    assert visible_location(plan, "Modelo pedagógico de README") <= visible_location(plan, "Qué convierte una prueba en reproducible")
    assert visible_location(plan, "Enlace profundo y permiso útil") < visible_location(plan, "Comprobación externa — PAREJAS")


def test_density_diagnoses_a_unit_silently_cut_after_projection(generator):
    session = generator.parse_session(*source_pair("213"))
    plan = generator.plan_slides(session)
    unit = next(unit for unit in generator.build_pedagogical_units(session) if unit.source_refs[0].heading == "Dos caminos con if/else")
    slide = plan[visible_location(plan, "Dos caminos con if/else")]
    code = next(text for text in unit.visible_content if text.startswith("```java"))
    slide.visible_content[slide.visible_content.index(code)] = code.split("else")[0]
    assert any("partida" in error for error in generator.plan_density_errors(plan))


def test_teacher_delivery_instructions_stay_presenter_only_in_learning_context(generator):
    session = generator.parse_session(*source_pair("213"))
    instruction = "No lo presentes como una lista para memorizar. Para cada expresión, pide al alumnado que lea la relación en lenguaje natural y prediga el resultado."
    plan = generator.plan_slides(session)
    slide = plan[visible_location(plan, "Comparaciones y resultados booleanos")]
    assert instruction not in slide.visible_content
    assert instruction in slide.presenter_content
    unit = next(unit for unit in slide.pedagogical_units if unit.source_refs[0].heading == "Comparaciones y resultados booleanos")
    assert instruction in unit.presenter_content


@pytest.mark.parametrize("number,heading,expected", [
    ("214", "Localización y comprensión — INDIVIDUAL", [2]),
    ("215", "Contenido de la entrega", [3, 4]),
    ("215", "Comprobación de enlaces y permisos", [3]),
    ("215", "Entrega oficial Moodle y evidencias que permanecen", [4]),
])
def test_responsible_timeline_anchors_belong_to_the_unit_not_its_mixed_slide(generator, number, heading, expected):
    session = generator.parse_session(*source_pair(number))
    plan = generator.plan_slides(session)
    slide = plan[visible_location(plan, heading)]
    unit = next(unit for unit in slide.pedagogical_units if unit.source_refs[0].heading == heading)
    assert unit.timeline_refs == expected
    assert set(expected) <= set(slide.timeline_refs)
    # The lexical primary remains one source action; shared supports may also
    # include an explicitly preceding preparation action.
    assert generator.semantic_timeline_index(session, unit) in expected


def test_individual_check_keeps_secondary_reading_roles_local(generator):
    session = generator.parse_session(*source_pair("213"))
    plan = generator.plan_slides(session)
    members = [unit for slide in plan for unit in slide.pedagogical_units
               if unit.source_refs[0].heading == "Comprobar comprensión — INDIVIDUAL"]
    for text in ("- reconocer el flujo de un `if` anidado sencillo;",
                 "- explicar cuándo el ternario resulta adecuado y cuándo conviene volver a `if/else`."):
        unit = next(unit for unit in members if text in "\n".join(unit.visible_content))
        assert unit.role == "recognition"
        assert unit.relations["recognition_context"]
        assert unit.timeline_refs == [7]
    core = next(unit for unit in members if "- explicar la condición de un `if`;" in "\n".join(unit.visible_content))
    assert core.role == "core"
    assert len({unit.source_refs[0].fragment for unit in members}) == len(members)


def test_mixed_closing_question_preserves_context_and_links_recognition_without_promoting_it(generator):
    session = generator.parse_session(*source_pair("212"))
    plan = generator.plan_slides(session)
    closing = next(unit for slide in plan for unit in slide.pedagogical_units
                   if unit.source_refs[0].heading == "Comprueba lo aprendido")
    question = next(text for text in closing.visible_content if text.startswith("> ¿"))
    assert question in session.teacher_source.read_text(encoding="utf-8")
    assert closing.role == "core"
    seeds = {unit.unit_id: unit for slide in plan for unit in slide.pedagogical_units}
    scoped = [seeds[unit_id] for unit_id in closing.relations["recognition_context"]]
    assert any(unit.role == "recognition" and "NumberFormatException" in unit.source_refs[0].heading for unit in scoped)


def test_single_secondary_check_inherits_only_explicit_source_scope(generator):
    seed = generator.PedagogicalUnit("seed", [generator.SourceRef("teacher", "Decisión anidada", 0)],
                                    "concept", "recognition", ["Leer sin profundizar."])
    check = generator.PedagogicalUnit("check", [generator.SourceRef("teacher", "Comprueba", 1)],
                                     "individual_check", "core", ["- reconocer el recorrido anidado."])
    units = generator.scope_recognition_checks([seed, check])
    assert units[1].role == "recognition"
    assert units[1].relations["recognition_context"] == (units[0].unit_id,)
    assert units[1].visible_content == ["- reconocer el recorrido anidado."]


@pytest.mark.parametrize("number", [str(number) for number in range(206, 216)])
def test_owned_source_content_survives_role_fragmentation_and_channel_moves(generator, number):
    from collections import Counter

    session = generator.parse_session(*source_pair(number))
    units = generator.build_pedagogical_units(session)
    for index, (heading, body) in enumerate(generator.heading_blocks(session.teacher_source.read_text(encoding="utf-8"))):
        children = generator.markdown_headings(body)
        owned = body[:children[0].start()].strip() if children else body.strip()
        members = [unit for unit in units if unit.source_refs[0].source == "teacher"
                   and unit.source_refs[0].block_index == index]
        if not owned or any(unit.function in {"timeline", "timeline_context"} for unit in members):
            continue  # Source tables have the separate TimelineBlock contract.
        actual = "\n".join(text for unit in members for text in [*unit.visible_content, *unit.presenter_content])
        # Channels may move paragraphs; their source tokens must neither vanish nor duplicate.
        assert Counter(owned.split()) == Counter(actual.split()), (number, heading)
@pytest.mark.parametrize("number", ["206", "212", "213", "214", "215"])
def test_source_closure_has_the_final_clock_anchor(number):
    module = load_module()
    session = module.parse_session(*source_pair(number))
    closures = [u for u in module.build_pedagogical_units(session) if module.semantic_is_closure(u)]
    assert closures
    assert all(u.timeline_refs == [len(session.timeline) - 1] for u in closures)


def test_later_presentation_and_clear_source_activity_are_not_opening_or_modality_fallback():
    module = load_module()
    session = module.parse_session(*source_pair("213"))
    units = module.build_pedagogical_units(session)
    ternary = next(u for u in units if u.source_refs[0].heading == "Operador ternario como elección sencilla")
    clarity = next(u for u in units if u.source_refs[0].heading == "Revisar claridad y simplicidad — PAREJAS")
    validation = next(u for u in units if u.source_refs[0].heading == "Validación sencilla de datos")
    assert ternary.timeline_refs == [5], "Presentar el ternario es el intervalo 29–31, no la apertura"
    assert clarity.timeline_refs == [8], "Revisar claridad está explícito en el cierre 43–45"
    assert validation.timeline_refs == [3], "La explicación apoya la práctica central 18–27"


def test_source_registration_and_delivery_template_keep_their_real_intervals():
    module = load_module()
    scope = module.parse_session(*source_pair("206"))
    scrum = next(u for u in module.build_pedagogical_units(scope) if u.source_refs[0].heading == "Acuerdo y Scrum del equipo")
    assert scrum.timeline_refs == [5]
    defense = module.parse_session(*source_pair("215"))
    units = module.build_pedagogical_units(defense)
    template = next(u for u in units if u.source_refs[0].heading == "Contenido de la entrega")
    assert template.timeline_refs == [3, 4], "Preparar y después entregar usan el mismo soporte"
    central = next(u for u in units if u.function == "defense")
    assert central.timeline_refs == [1, 2, 3, 4], "Las defensas continúan durante el trabajo paralelo"


def test_enumerated_source_criteria_share_the_parent_instruction_interval():
    module = load_module()
    session = module.parse_session(*source_pair("214"))
    headings = {"Qué hace", "Qué límites tiene", "Cómo se ejecuta", "Qué pruebas demuestran que funciona"}
    criteria = [u for u in module.build_pedagogical_units(session) if u.source_refs[0].heading in headings]
    assert len(criteria) == 4
    assert all(u.timeline_refs == [1] for u in criteria)


def test_scanner_explanation_is_not_moved_after_its_reuse_contrast():
    module = load_module()
    session = module.parse_session(*source_pair("212"))
    units = module.build_pedagogical_units(session)
    creation = next(u for u in units if any('Scanner teclado = new Scanner(System.in);' in text
                                           for text in u.visible_content))
    reuse = next(u for u in units if u.source_refs[0].heading == "Reutilizar la misma instancia")
    assert creation.timeline_refs == reuse.timeline_refs == [1]
