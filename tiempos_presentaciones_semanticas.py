"""Tiempo docente derivado del reloj fuente, sin modificar el plan de diapositivas.

Los tiempos son planificación para notas/metadatos, no contenido proyectable.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
import re
from typing import TYPE_CHECKING, Protocol, Sequence

if TYPE_CHECKING:
    from generar_presentaciones_sesiones import Session


class TimingFrame(Protocol):
    """SlideSpec o página expandida por el renderer: solo lectura estructural."""

    kind: str
    timeline_refs: list[int]



@dataclass(frozen=True)
class TimingAllocation:
    """Porción del presupuesto de un intervalo fuente (índice basado en cero)."""

    source_index: int
    seconds: int
    decision: str
    source_time: str
    source_seconds: int = 0
    is_owner: bool = False
    function: str = ""


@dataclass(frozen=True)
class SharedInterval:
    """Reloj compartido completo; seconds no es tiempo exclusivo de la slide."""

    source_index: int
    source_time: str
    seconds: int
    is_owner: bool
    function: str = ""
    action: str = ""
    concurrent: bool = False
    parallel_work: str = ""


@dataclass(frozen=True)
class SlideTiming:
    seconds: int
    allocations: list[TimingAllocation]
    clock_intervals: list[int]
    presenter_notes: str
    shared_intervals: list[SharedInterval] = field(default_factory=list)

    @property
    def description(self) -> str:
        return self.presenter_notes


def _units(frame):
    return getattr(frame, "units", None) or getattr(frame, "pedagogical_units", ())


_FUNCTION_PATTERNS = {
    "defense": r"defensa|defensas",
    "individual_check": r"comprobación individual|comprobar.*individual",
    "activity": r"práctic|practicar|implementar|parejas|equipo|consolidar|trabajo",
    "review": r"revis|review",
    "retrospective": r"retrospectiva",
    "moodle_delivery": r"entrega|moodle",
    "closure": r"cerrar|cierre",
    "predictions": r"predecir|predic",
    "counterexamples": r"contrastar|contraste",
    "concept": r"explicar|presentar|analizar|traducir",
}
_FUNCTION_LABELS = {
    "activity": "actividad", "defense": "defensa", "individual_check": "comprobación individual",
    "concept": "explicación", "concepts": "explicación", "review": "revisión",
    "retrospective": "retrospectiva", "moodle_delivery": "entrega",
    "closure": "cierre", "predictions": "predicción", "counterexamples": "contraste",
}


def _purpose(frame, source_index, action):
    """Prioridad por función y referencia de unidad, nunca por número de páginas."""
    units = list(_units(frame))
    anchored = [unit for unit in units if source_index in getattr(unit, "timeline_refs", ())]
    candidates = anchored or units
    functions = [(getattr(unit, "function", ""), getattr(unit, "role", "core"))
                 for unit in candidates]
    functions = functions or [(frame.kind, getattr(frame, "role", "core"))]
    def rank(pair):
        function, role = pair
        match = bool(re.search(_FUNCTION_PATTERNS.get(function, r"(?!)"), action, re.I))
        operative = function in {"activity", "defense", "individual_check", "review",
                                 "retrospective", "moodle_delivery", "closure"}
        core = role != "recognition" and not getattr(frame, "recognition", False)
        return (frame.kind not in {"title", "parallel"}, core, match, operative, bool(anchored),
                function not in {"title", "timeline_context", "other", "preparation"})
    function, role = max(functions, key=rank)
    priority = rank((function, role))
    # La identidad semántica estabiliza empates al reordenar/duplicar soportes.
    identity = (tuple(sorted(str(getattr(unit, "unit_id", "")) for unit in candidates)),
                str(getattr(frame, "title", "")), frame.kind)
    return priority, identity, function


def allocate_slide_timings(session: Session, plan: Sequence[TimingFrame]) -> list[SlideTiming]:
    """Asocia soportes a intervalos fuente completos, sin repartir por páginas.

    Cada intervalo tiene un único propietario contable elegido por función de
    actividad y referencias de unidad. Su seconds se contabiliza una vez; otros
    soportes tienen seconds=0 y conservan duración fuente en shared_intervals.
    No representa duración exclusiva ni un turno por diapositiva/persona.
    Valida duración, referencias y reloj ordenado sin solapamientos; no inventa
    huecos. Acepta units (renderer) o pedagogical_units (SlideSpec), opcionales.
    Diagnósticos de asociación permanecen en allocations, no en notas docentes.
    No modifica session ni plan.
    """
    if not session.timeline:
        raise ValueError("No hay timeline fuente; no se inventa una duración global")
    if not plan:
        raise ValueError("El plan no contiene diapositivas")
    budgets = []
    previous_start = previous_end = -1
    for index, block in enumerate(session.timeline):
        match = re.fullmatch(r"\s*(\d+)\s*[–—-]\s*(\d+)\s*(?:min(?:uto)?s?\.?)?\s*", block.time, re.I)
        if match is None:
            raise ValueError(f"Formato de intervalo fuente {index} inválido: {block.time!r}")
        start, end = int(match[1]), int(match[2])
        if end <= start:
            raise ValueError(f"El intervalo fuente {index} debe tener fin mayor que inicio")
        if start < previous_start:
            raise ValueError(f"El orden de los intervalos fuente es inválido en {index}")
        if start < previous_end:
            raise ValueError(f"Hay solapamiento de reloj en el intervalo fuente {index}")
        budgets.append((end - start) * 60)
        previous_start, previous_end = start, end
    duration_text = session.duration.strip().lower().replace(",", ".")
    number = r"\d+(?:\.\d+)?"
    duration_match = re.fullmatch(
        rf"(?:(?P<hours>{number})\s*(?:h|hora|horas)\s*)?"
        rf"(?:(?P<minutes>{number})\s*(?:min|minuto|minutos)\.?)?", duration_text,
    )
    if duration_match and any(duration_match.groups()):
        metadata_seconds = (Decimal(duration_match['hours'] or '0') * 3600
                            + Decimal(duration_match['minutes'] or '0') * 60)
        if metadata_seconds != sum(budgets):
            raise ValueError("La duración metadata no coincide con el reloj timeline fuente")
    allocations: list[list[TimingAllocation]] = [[] for _ in plan]
    refs = []
    for slide in plan:
        source_refs = list(getattr(slide, "timeline_refs", ()))
        for unit in _units(slide):
            source_refs.extend(getattr(unit, "timeline_refs", ()))
        if any(type(ref) is not int or not 0 <= ref < len(budgets) for ref in source_refs):
            raise ValueError("Hay una referencia timeline inválida en el plan o unidad")
        refs.append(list(dict.fromkeys(source_refs)))
    decisions: dict[tuple[int, int], str] = {}
    for i, slide in enumerate(plan):
        if slide.kind == "title":
            refs[i] = [0]
            decisions[i, 0] = (
                "Portada limitada a la apertura inicial: las referencias timeline "
                "presenter-only no convierten la portada en soporte de todos los tramos."
            )
    anchored = [i for i, indices in enumerate(refs) if indices]
    inferred_sources = {}
    for i, indices in enumerate(refs):
        if not indices:
            identity = (plan[i].kind, str(getattr(plan[i], "title", "")),
                        tuple(sorted(str(getattr(unit, "id", "")) for unit in _units(plan[i]))))
            # Una expansión física mantiene la asociación de su unidad, aunque
            # la copia aparezca lejos del soporte original dentro del plan.
            if identity in inferred_sources:
                source = inferred_sources[identity]
            else:
                nearest = min(anchored, key=lambda other: (abs(other - i), other)) if anchored else None
                source = refs[nearest][0] if nearest is not None else 0
                inferred_sources[identity] = source
            indices.append(source)
            decisions[i, source] = (
                "Diapositiva sin ancla: comparte el intervalo de la diapositiva "
                "anclada más cercana (desempate por orden); sin anclas, apertura fuente."
            )
    for index, seconds in enumerate(budgets):
        recipients = [i for i, indices in enumerate(refs) if index in indices]
        if not recipients:
            candidates = [i for i, slide in enumerate(plan) if slide.kind != "title" or index == 0]
            if not candidates:
                raise ValueError("El plan solo tiene portadas; faltan soportes para los intervalos posteriores")
            nearest = min(candidates, key=lambda i: (min(abs(ref - index) for ref in refs[i]), i))
            recipients = [nearest]
            decisions[nearest, index] = (
                "Intervalo sin ancla: se integra en el soporte con referencia fuente "
                "más cercana (desempate por orden del plan)."
            )
        block = session.timeline[index]
        parallel = " ".join(value for key, value in block.details.items()
                            if "paralel" in key.lower() or "concurrent" in key.lower())
        concurrency_note = (
            " Soporte concurrente del mismo reloj fuente: no son turnos de defensa "
            "ni una secuencia adicional. Trabajo paralelo: " + parallel
        ) if parallel else ""
        purposes = {i: _purpose(plan[i], index, block.action) for i in recipients}
        best_priority = max(purposes[i][0] for i in recipients)
        owner = min((i for i in recipients if purposes[i][0] == best_priority),
                    key=lambda i: purposes[i][1])
        for slide_index in recipients:
            allocations[slide_index].append(TimingAllocation(
                index, seconds if slide_index == owner else 0,
                "Intervalo compartido íntegro; propietario contable seleccionado por función "
                "de actividad y referencia timeline de unidad (identidad semántica en empates). "
                + ("Propietario. " if slide_index == owner else "Soporte, sin duplicación contable. ")
                + decisions.get((slide_index, index), "") + concurrency_note,
                block.time, seconds, slide_index == owner, purposes[slide_index][2],
            ))
    timings = []
    for items in allocations:
        shared = []
        notes = []
        for item in items:
            block = session.timeline[item.source_index]
            parallel = " ".join(value for key, value in block.details.items()
                                if "paralel" in key.lower() or "concurrent" in key.lower())
            shared.append(SharedInterval(
                item.source_index, item.source_time, item.source_seconds, item.is_owner,
                item.function, block.action, bool(parallel), parallel,
            ))
            notes.append(
                f"Reloj fuente {item.source_time}: duración compartida {item.source_seconds} segundos. "
                f"Trabajo: {block.action.rstrip('.')}. "
                f"Función del soporte: {_FUNCTION_LABELS.get(item.function, 'apoyo al trabajo')}."
                + (" Soporte concurrente del mismo reloj fuente: no son turnos de defensa "
                   "ni una secuencia adicional. Trabajo paralelo: " + parallel if parallel else "")
            )
        timings.append(SlideTiming(sum(item.seconds for item in items), items,
                                   [item.source_index for item in items], " ".join(notes), shared))
    return timings
