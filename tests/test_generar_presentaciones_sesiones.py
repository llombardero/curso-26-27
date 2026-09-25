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

def test_presentation_uses_named_hexa_phase_from_canonical_model(generator, tmp_path):
    teacher, student = source_pair("212")
    session = generator.parse_session(teacher, student)
    target = tmp_path / "S212.pptx"

    generator.build_presentation(session, target)
    rendered_text = " ".join(
        shape.text
        for slide in generator.Presentation(target).slides
        for shape in slide.shapes
        if hasattr(shape, "text")
    )

    assert session.moment == "Ejecutar — crear"
    assert "Fase HEXA: Ejecutar — crear" in rendered_text
    assert "Momento HEXA:" not in rendered_text

def test_h1_v3_sources_cover_topic_one_without_stealing_h2_application(generator):
    teacher_213, student_213 = source_pair("213")
    teacher_220, student_220 = source_pair("220")

    h1 = generator.parse_session(teacher_213, student_213)
    h2 = generator.parse_session(teacher_220, student_220)
    h1_text = " ".join([h1.objective, *h1.key_concepts, *h1.activity])

    assert "if/else" in h1_text
    assert "micropráctica" in h1_text.lower()
    assert "aplicar" in h2.objective.lower()
    assert "varios comandos" in h2.objective.lower()

def test_generated_presentation_contains_synchronised_speaker_notes(generator, tmp_path):
    teacher, student = source_pair("213")
    session = generator.parse_session(teacher, student)
    target = tmp_path / "S213.pptx"

    generator.build_presentation(session, target)
    presentation = generator.Presentation(target)
    notes = [slide.notes_slide.notes_text_frame.text.strip() for slide in presentation.slides]
    combined = " ".join(notes)

    assert all(notes)
    assert "Objetivo docente" in notes[0]
    assert session.objective in combined
    assert any(block.time in combined for block in session.timeline)

def test_h1_keeps_teacher_guidance_in_speaker_notes(generator):
    forbidden_visible = (
        "PÍLDORA DOCENTE",
        "PÍLDORA BREVE",
        "Secuencia de aula",
        "Objetivo docente:",
        "Fuente docente:",
    )

    for number in range(206, 216):
        teacher, student = source_pair(str(number))
        session = generator.parse_session(teacher, student)
        plan = generator.plan_slides(session)
        visible = " ".join(
            text
            for slide in plan
            for text in (slide.title, slide.subtitle, *slide.items)
        )
        title_notes = generator.speaker_notes(session, plan[0], 1, len(plan))

        assert not any(marker in visible for marker in forbidden_visible), number
        assert not any(slide.kind in {"timeline", "concepts"} for slide in plan), number
        assert session.duration not in plan[0].subtitle, number
        assert all(block.action in title_notes for block in session.timeline), number
        assert all(item in title_notes for item in session.key_concepts), number

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

    for number in ("232", "245", "290", "304"):
        teacher, student = source_pair(number)
        kinds = [slide.kind for slide in generator.plan_slides(generator.parse_session(teacher, student))]
        assert "focus" in kinds, number
        assert "concepts" not in kinds, number
        assert "example" not in kinds, number

    teacher, student = source_pair("212")
    kinds = [slide.kind for slide in generator.plan_slides(generator.parse_session(teacher, student))]
    assert "concepts" not in kinds
    assert "example" in kinds

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
