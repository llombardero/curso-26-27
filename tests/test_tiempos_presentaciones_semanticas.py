from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import re
import sys
from types import SimpleNamespace

import pytest

from test_generar_presentaciones_sesiones import load_module, source_pair

ROOT = Path(__file__).resolve().parents[1]


def timing_module():
    path = ROOT / "tiempos_presentaciones_semanticas.py"
    assert path.exists(), "Falta el asignador de tiempos semánticos"
    spec = importlib.util.spec_from_file_location("tiempos_presentaciones_semanticas", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def session_with(*times, duration="no especificada"):
    return SimpleNamespace(
        timeline=[SimpleNamespace(time=time, action="Trabajo", details={}) for time in times],
        duration=duration,
    )


def slides_with(*refs):
    generator = load_module()
    slides = [generator.SlideSpec("concept", f"Diapositiva {i}") for i in range(len(refs))]
    for slide, indices in zip(slides, refs):
        slide.timeline_refs = list(indices)
    return slides


def test_shared_interval_conserves_every_second_without_mutating_plan():
    module = timing_module()
    session = session_with("0–1 min", duration="1 minuto")
    plan = slides_with([0], [0], [0], [0], [0], [0], [0])
    before = copy.deepcopy([vars(slide) for slide in plan])

    timings = module.allocate_slide_timings(session, plan)

    # Los soportes comparten el reloj completo; no reciben cuotas por cantidad.
    assert sorted(timing.seconds for timing in timings) == [0, 0, 0, 0, 0, 0, 60]
    assert sum(timing.seconds for timing in timings) == 60
    assert [vars(slide) for slide in plan] == before
    for timing in timings:
        assert isinstance(timing, module.SlideTiming)
        assert timing.clock_intervals == [0]
        assert timing.allocations[0].source_index == 0
        assert timing.allocations[0].seconds == timing.seconds
        shared = timing.shared_intervals[0]
        assert shared.source_index == 0
        assert shared.source_time == "0–1 min"
        assert shared.seconds == 60
        assert shared.is_owner == (timing.seconds == 60)
        assert timing.allocations[0].source_seconds == 60
        assert timing.allocations[0].is_owner == shared.is_owner
        assert "duración" in timing.presenter_notes.lower()
        assert "60" in timing.presenter_notes
        assert "reparto" not in timing.presenter_notes.lower()
        assert timing.description == timing.presenter_notes


def activity_frame(title, function, refs, *, role="core", kind="concept"):
    unit = SimpleNamespace(function=function, timeline_refs=list(refs), role=role, id=title)
    return SimpleNamespace(kind=kind, title=title, timeline_refs=[], units=[unit])


def test_activity_owner_is_semantic_and_invariant_under_duplicate_supports():
    module = timing_module()
    session = session_with("0–45 min", duration="45 minutos")
    session.timeline[0].action = "Trabajo por parejas: implementar y probar"
    concept = activity_frame("Explicación", "concept", [0])
    activity = activity_frame("Trabajo por parejas", "activity", [0], kind="activity")
    recognition = activity_frame("Reconocimiento", "activity", [0], role="recognition")
    plan = [concept, recognition, activity]
    result = module.allocate_slide_timings(session, plan)
    assert [t.seconds for t in result] == [0, 0, 2700]
    assert all(t.clock_intervals == [0] for t in result)
    assert all(t.shared_intervals[0].function for t in result)
    assert "actividad" in result[2].presenter_notes.lower()
    assert "reparto" not in result[2].allocations[0].decision.lower()
    for expanded in ([concept] * 80 + [recognition, activity], [activity, recognition, concept]):
        timings = module.allocate_slide_timings(session, expanded)
        assert sum(t.seconds for t in timings) == 2700
        assert sum(t.shared_intervals[0].is_owner for t in timings) == 1
        assert next(frame for frame, t in zip(expanded, timings) if t.seconds) is activity
        assert all(t.shared_intervals[0].seconds == 2700 for t in timings)


def test_frame_recognition_and_title_cannot_capture_activity_accounting():
    module = timing_module()
    session = session_with("0–45 min", duration="45 minutos")
    session.timeline[0].action = "Trabajo en equipo"
    recognition = activity_frame("A reconocimiento", "activity", [0], kind="activity")
    recognition.recognition = True
    title = activity_frame("A portada", "activity", [0], kind="title")
    activity = activity_frame("Z trabajo", "activity", [0], kind="activity")
    result = module.allocate_slide_timings(session, [recognition, title, activity])
    assert [t.seconds for t in result] == [0, 0, 2700]


def test_unanchored_slides_and_intervals_have_explicit_traceable_decisions():
    module = timing_module()
    session = session_with("0–1 min", "1–2 min", "2–3 min")
    plan = slides_with([], [0], [], [2], [])
    timings = module.allocate_slide_timings(session, plan)
    assert all(type(timing.seconds) is int and timing.seconds >= 0 for timing in timings)
    assert sum(timing.seconds for timing in timings) == 180
    for source_index in range(3):
        assert sum(a.seconds for t in timings for a in t.allocations
                   if a.source_index == source_index) == 60
    for index in (0, 2, 4):
        assert "sin ancla" in timings[index].allocations[0].decision.lower()
        assert "sin ancla" not in timings[index].presenter_notes.lower()
        assert "desempate por orden" not in timings[index].presenter_notes.lower()
    assert any("intervalo sin ancla" in a.decision.lower()
               for t in timings for a in t.allocations if a.source_index == 1)


@pytest.mark.parametrize("times,duration,refs,message", [
    (["sin rango"], "", [[0]], "intervalo"),
    (["5–3 min"], "", [[0]], "intervalo"),
    (["0–0 min"], "", [[0]], "intervalo"),
    (["-1–3 min"], "", [[0]], "intervalo"),
    (["0–5 min", "4–8 min"], "", [[0], [1]], "solapamiento"),
    (["5–8 min", "0–5 min"], "", [[0], [1]], "orden"),
    (["0–5 min"], "45 minutos", [[0]], "duración"),
    (["0–5 min"], "", [[1]], "referencia"),
    (["0–5 min"], "", [[-1]], "referencia"),
    (["0–5 min"], "", [[True]], "referencia"),
    (["0–5 min"], "", [["0"]], "referencia"),
    ([], "45 minutos", [[0]], "timeline"),
    (["0–5 min"], "", [], "plan"),
])
def test_invalid_source_or_plan_is_rejected_without_inventing_time(times, duration, refs, message):
    module = timing_module()
    with pytest.raises(ValueError, match=message):
        module.allocate_slide_timings(session_with(*times, duration=duration), slides_with(*refs))


@pytest.mark.parametrize("duration", ["45 minutos", "45 min", "0,75 horas", "0.75 h", "0 h 45 min"])
def test_parseable_duration_metadata_agrees_with_source(duration):
    module = timing_module()
    result = module.allocate_slide_timings(session_with("0–45 min", duration=duration), slides_with([0, 0]))
    assert result[0].seconds == 2700
    assert len(result[0].allocations) == 1


@pytest.mark.parametrize("duration", ["1 hora", "1 h 30 min", "0,5 horas"])
def test_parseable_hour_metadata_mismatch_is_rejected(duration):
    module = timing_module()
    with pytest.raises(ValueError, match="duración"):
        module.allocate_slide_timings(session_with("0–45 min", duration=duration), slides_with([0]))


def test_title_presenter_only_timeline_is_restricted_to_opening_with_duck_frames():
    module = timing_module()
    session = session_with("0–5 min", "5–10 min", "10–15 min")
    frames = [
        SimpleNamespace(kind="title", title="Portada", timeline_refs=[0, 1, 2], relations={}),
        SimpleNamespace(kind="concept", title="Contenido", timeline_refs=[0], relations={}),
    ]
    before = copy.deepcopy([vars(frame) for frame in frames])
    result = module.allocate_slide_timings(session, frames)
    assert result[0].clock_intervals == [0]
    assert "apertura" in result[0].allocations[0].decision.lower()
    assert "presenter-only" not in result[0].presenter_notes.lower()
    assert result[1].clock_intervals == [0, 1, 2]
    assert sum(t.seconds for t in result) == 900
    assert [vars(frame) for frame in frames] == before


def test_s215_concurrent_support_uses_one_clock_not_defense_turns():
    module = timing_module()
    generator = load_module()
    session = generator.parse_session(*source_pair("215"))
    plan = slides_with([1], [1], [0, 2, 3, 4, 5])
    timings = module.allocate_slide_timings(session, plan)
    assert sum(t.seconds for t in timings) == 2700
    assert timings[0].seconds + timings[1].seconds == 600
    for timing in timings[:2]:
        note = timing.presenter_notes.lower()
        assert "soporte concurrente" in note
        assert "no son turnos de defensa" in note
        assert "duración individual" not in note
        assert timing.shared_intervals[0].seconds == 600
        assert timing.shared_intervals[0].concurrent
        assert timing.allocations[0].source_time == session.timeline[1].time
        assert "ensayo y revisión por parejas" in note


@pytest.mark.parametrize("number", [str(n) for n in range(206, 216)])
def test_h1_real_semantic_plans_preserve_each_source_interval(number):
    module = timing_module()
    generator = load_module()
    session = generator.parse_session(*source_pair(number))
    plan = generator.plan_slides_semantic(session)
    before = copy.deepcopy([vars(slide) for slide in plan])
    result = module.allocate_slide_timings(session, plan)
    assert len(result) == len(plan)
    assert all(type(t.seconds) is int and t.seconds >= 0 for t in result)
    assert all(t.shared_intervals and all(s.seconds > 0 for s in t.shared_intervals) for t in result)
    assert sum(t.seconds for t in result) == 2700
    for index, block in enumerate(session.timeline):
        match = re.search(r"(\d+)\s*[–-]\s*(\d+)", block.time)
        assert match is not None
        expected = (int(match[2]) - int(match[1])) * 60
        assert sum(a.seconds for t in result for a in t.allocations
                   if a.source_index == index) == expected
    assert [vars(slide) for slide in plan] == before
    for slide, timing in zip(plan, result):
        if slide.kind == "title":
            assert timing.clock_intervals == [0]


def test_expanded_child_frames_share_parent_interval_exactly():
    module = timing_module()
    frames = [SimpleNamespace(kind="code", title=f"Código {i}", timeline_refs=[0], relations={})
              for i in range(11)]
    result = module.allocate_slide_timings(session_with("0–1 min"), frames)
    assert sum(t.seconds for t in result) == 60
    # Expandir código no fragmenta el reloj en once cuotas.
    assert sorted(t.seconds for t in result) == [0] * 10 + [60]
    assert all(t.shared_intervals[0].seconds == 60 for t in result)


def test_gaps_are_not_invented_as_teaching_time():
    module = timing_module()
    result = module.allocate_slide_timings(session_with("5–10 min", "15–20 min"), slides_with([0], [1]))
    assert sum(t.seconds for t in result) == 600


def test_all_unanchored_slides_are_supported_without_default_global_duration():
    module = timing_module()
    result = module.allocate_slide_timings(session_with("0–1 min", "1–3 min"), slides_with([], [], []))
    assert sum(t.seconds for t in result) == 180
    assert all(t.shared_intervals for t in result)
    assert all("sin ancla" not in t.presenter_notes.lower() for t in result)
    assert all("sin ancla" in t.allocations[0].decision.lower() for t in result)


@pytest.mark.parametrize("number", ["212", "213", "214", "215"])
def test_real_shared_groups_keep_source_clock_when_supports_are_duplicated(number):
    module = timing_module()
    generator = load_module()
    session = generator.parse_session(*source_pair(number))
    plan = generator.plan_slides_semantic(session)
    original = module.allocate_slide_timings(session, plan)
    support_index = next(i for i, t in enumerate(original) if t.seconds == 0 and plan[i].kind != "title")
    # Copias físicas de un soporte no añaden actividades ni cuotas de duración.
    expanded = plan + [copy.deepcopy(plan[support_index]) for _ in range(20)]
    result = module.allocate_slide_timings(session, expanded)
    assert [t.seconds for t in result[:len(plan)]] == [t.seconds for t in original]
    assert all(t.seconds == 0 for t in result[len(plan):])
    assert sum(t.seconds for t in result) == 2700
    assert any(len([t for t in result if index in t.clock_intervals]) > 1
               for index in range(len(session.timeline)))
    for index, block in enumerate(session.timeline):
        match = re.fullmatch(r"(\d+)\s*[–-]\s*(\d+) min", block.time)
        assert match is not None
        seconds = (int(match[2]) - int(match[1])) * 60
        shared = [s for t in result for s in t.shared_intervals if s.source_index == index]
        assert sum(s.is_owner for s in shared) == 1
        assert all(type(s.seconds) is int and s.seconds == seconds and s.source_time == block.time for s in shared)
        allocations = [a for t in result for a in t.allocations if a.source_index == index]
        assert sum(a.seconds for a in allocations) == seconds
        assert all(a.seconds == (seconds if a.is_owner else 0) for a in allocations)
        if number == "215":
            assert all(s.concurrent and s.parallel_work for s in shared)
    for timing in result:
        assert not any(word in timing.presenter_notes.lower() for word in
                       ("sin ancla", "desempate por orden", "propietario", "contable", "timeline_context"))


@pytest.mark.parametrize("ref", [True, "0", -1, 1])
def test_invalid_unit_timeline_reference_is_not_hidden_by_valid_frame_reference(ref):
    module = timing_module()
    frame = activity_frame("Actividad", "activity", [ref])
    frame.timeline_refs = [0]
    with pytest.raises(ValueError, match="referencia"):
        module.allocate_slide_timings(session_with("0–45 min"), [frame])


def test_existing_dataclass_constructors_keep_default_additions():
    module = timing_module()
    allocation = module.TimingAllocation(0, 60, "diagnóstico", "0–1 min")
    timing = module.SlideTiming(60, [allocation], [0], "nota")
    assert allocation.source_seconds == 0
    assert allocation.is_owner is False
    assert allocation.function == ""
    assert timing.shared_intervals == []
    assert timing.description == "nota"


def test_title_only_plan_cannot_absorb_intervals_after_opening():
    module = timing_module()
    frame = SimpleNamespace(kind="title", timeline_refs=[0, 1])
    with pytest.raises(ValueError, match="portadas"):
        module.allocate_slide_timings(session_with("0–1 min", "1–2 min"), [frame])
def test_concurrency_overview_is_not_owner_of_the_specific_defense_activity():
    from test_generar_presentaciones_sesiones import load_module, source_pair
    from render_presentaciones_semanticas import expand_semantic_frames
    module = load_module()
    session = module.parse_session(*source_pair("215"))
    frames = expand_semantic_frames(session, module.plan_slides(session))
    timings = timing_module().allocate_slide_timings(session, frames)
    owner = next(frame for frame, timing in zip(frames, timings)
                 if any(item.source_index == 1 and item.is_owner for item in timing.shared_intervals))
    assert owner.kind != "parallel"
    assert any(unit.function == "defense" for unit in owner.units)


def test_s206_session_purpose_is_anchored_to_the_opening_interval():
    from render_presentaciones_semanticas import expand_semantic_frames

    generator = load_module()
    session = generator.parse_session(*source_pair("206"))
    frames = expand_semantic_frames(session, generator.plan_slides(session))
    timings = timing_module().allocate_slide_timings(session, frames)
    index = next(i for i, frame in enumerate(frames) if frame.title == "Finalidad de la sesión")
    assert timings[index].clock_intervals == [0]
    assert timings[index].shared_intervals[0].source_time == "0–6 min"
    assert "Presentar H1" in timings[index].shared_intervals[0].action
    assert "conectar con S207" not in timings[index].shared_intervals[0].action
