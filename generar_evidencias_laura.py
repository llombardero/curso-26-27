#!/usr/bin/env python3
"""Regenera los ejemplos privados de Laura con la arquitectura mínima del curso.

Los ejemplos son material docente privado y se publican de forma diferida. Hay un
único diario individual y un único Scrum de equipo, ambos evolutivos; Moodle
recibe una entrega mínima por hito; los Sites solo aparecen en C1, C2 y HF.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent
EXAMPLES = ROOT / "03-EJEMPLOS-LAURA-PRIVADOS"
MASTERS = ROOT / "02-PROFESORADO/05-ECOSISTEMA-DIGITAL/PLANTILLAS-MAESTRAS"

HITOS = {
    "h0-torre-papel": ("H0", "Torre de papel y Scrum", "Organizar un sprint y comprobar una torre estable.", "La base inicial era estrecha; el equipo decidió ensancharla antes de ganar altura.", "Torre estable durante 10 segundos, backlog y retrospectiva actualizados.", "No aplica"),
    "h1-primer-asistente": ("H1", "Primer asistente por consola", "Crear y ejecutar la primera versión básica de MiniJarvis.", "Se mantuvo el alcance sin menú ni bucles para poder explicar cada línea.", "El programa saluda, solicita el nombre y termina sin errores.", "h1-entrega"),
    "h2-decisiones-depuracion": ("H2", "Decisiones y depuración", "Añadir menú, repetición, decisiones y salida controlada.", "Se corrigió la comparación de textos y se documentó una depuración con breakpoint.", "El menú responde a casos previstos y termina de forma controlada.", "h2-entrega"),
    "h3-memoria-colecciones": ("H3", "Memoria y colecciones", "Guardar y consultar recuerdos durante una ejecución.", "Se eligió una lista y se añadió tratamiento explícito de memoria vacía.", "Los recuerdos permanecen disponibles hasta cerrar el programa.", "h3-entrega"),
    "h4-agente-orientado-objetos": ("H4", "Agente orientado a objetos", "Separar responsabilidades mediante objetos.", "Main inicia, Agent coordina y Memory conserva recuerdos.", "El comportamiento anterior se conserva con un diseño más claro.", "h4-entrega"),
    "h5-extensible-clean-code-patrones": ("H5", "Extensibilidad, código limpio y patrones", "Añadir herramientas con bajo impacto y refactorizar sin romper.", "Se aplicó un Command simplificado mediante Tool sin introducir sobreingeniería.", "Las herramientas comparten contrato y las pruebas de regresión pasan.", "h5-entrega"),
    "h6-persistente-trazable": ("H6", "Persistencia y trazabilidad", "Conservar memoria e historial entre ejecuciones.", "Se usaron rutas relativas, errores controlados y datos ficticios.", "La memoria persiste y los errores de fichero dejan un estado seguro.", "h6-entrega"),
    "h7-integracion-ia-responsable": ("H7", "Integración responsable de IA", "Incorporar una ayuda simulada con límites y validación humana.", "Toda respuesta se presenta como propuesta y requiere validación humana.", "La simulación rechaza datos sensibles y registra la validación.", "h7-entrega"),
    "hf-presentacion-final-recuperacion-mejora": ("HF", "Presentación final, recuperación y mejora", "Demostrar la evolución de MiniJarvis y defender decisiones.", "Cada afirmación se enlaza con una versión estable y una prueba observable.", "La demostración es reproducible y Laura explica su aportación.", "hf-final"),
}


def set_row(ws, row: int, values: tuple[object, ...]) -> None:
    for column, value in enumerate(values, 1):
        ws.cell(row=row, column=column, value=value)


def clean_legacy() -> None:
    """Elimina únicamente la documentación antigua generada, no el código."""
    for folder in HITOS:
        hito = EXAMPLES / folder
        if not hito.is_dir():
            raise RuntimeError(f"No existe el hito {hito}")
        for name in ("docs", "evidencias-digitales"):
            shutil.rmtree(hito / name, ignore_errors=True)
        for path in hito.glob("*.md"):
            path.unlink()
    for name in ("FUENTES-CURSO", "ENTREGAS-MOODLE", "PORTFOLIOS-PERIODICOS"):
        shutil.rmtree(EXAMPLES / name, ignore_errors=True)


def create_course_workbooks() -> None:
    target = EXAMPLES / "FUENTES-CURSO"
    target.mkdir()
    diary = target / "01-Diario-individual-MiniJarvis.xlsx"
    scrum = target / "02-Scrum-equipo-MiniJarvis.xlsx"
    shutil.copy2(MASTERS / diary.name, diary)
    shutil.copy2(MASTERS / scrum.name, scrum)

    wb = load_workbook(diary)
    ws = wb["DIARIO"]
    for row, (_, data) in enumerate(HITOS.items(), 2):
        code, title, objective, decision, result, version = data
        set_row(ws, row, (
            f"Fecha de ejemplo {code}", code, objective,
            f"Prueba: {result}", "URL_RESTRINGIDA_EJEMPLO",
            f"Decisión o aprendizaje: {decision}",
            "Revisión de claridad con IA; contraste final con código y pruebas" if code in {"H3", "H7"} else "No procede",
        ))
    wb.save(diary)

    wb = load_workbook(scrum)
    for row, person in enumerate(("Laura", "Álex", "Noor"), 2):
        set_row(wb["EQUIPO_Y_ACUERDOS"], row, ("Equipo Ada", person, "Responsabilidad rotatoria", "Avisar bloqueos y revisar antes de integrar", "Siguiente hito"))
    for row, (_, data) in enumerate(HITOS.items(), 2):
        code, title, objective, decision, result, version = data
        set_row(wb["BACKLOG_OPERATIVO"], row, (f"{code}-01", code, objective, result, "Alta", "Equipo Ada", "Hecho", "Fechas de ejemplo", "URL_RESTRINGIDA_EJEMPLO"))
        set_row(wb["DECISIONES_Y_BLOQUEOS"], row, (f"Fecha {code}", code, "Decisión", decision, "Alternativas revisadas", "Reducir riesgo", "Laura", "Cerrada", "URL_RESTRINGIDA_EJEMPLO"))
        set_row(wb["REVIEW"], row, (f"Fecha {code}", code, title, result, "Conforme", "Feedback de ejemplo", "Siguiente incremento", "URL_RESTRINGIDA_EJEMPLO"))
        set_row(wb["RETROSPECTIVA"], row, (f"Fecha {code}", code, "Prueba visible", "Avisar antes los bloqueos", "Dividir tareas", "Equipo Ada", "Siguiente hito"))
        if code in {"H3", "H7"}:
            set_row(wb["IA_EQUIPO"], 2 if code == "H3" else 3, (f"Fecha {code}", code, "IA autorizada", "Revisar una explicación", "Sugerencias de redacción", "Contraste con código y pruebas", "Laura", "URL_RESTRINGIDA_EJEMPLO"))
    wb.save(scrum)


def technical_sections(code: str) -> str:
    sections = {
        "H0": """## Proceso de equipo [EQUIPO]\n\n- Backlog: diseñar base, construir, medir estabilidad, revisar y mejorar.\n- Definición de terminado: torre autoportante y prueba registrada.\n- Retrospectiva: ensanchar la base antes de aumentar altura.\n\n## Aportación de Laura [INDIVIDUAL]\n\nLaura documentó la prueba y puede explicar el cambio de diseño. H0 no usa GitHub, tags ni Sites; la fotografía no-code se conserva en Drive solo si aporta evidencia.""",
        "H1": """## Ejecución comprobable [EQUIPO]\n\n```text\nMiniJarvis: ¿Cómo te llamas?\nLaura\nHola, Laura. Soy MiniJarvis.\n```\n\nEl README contiene requisitos, compilación, ejecución y ejemplo. La versión evaluada es `h1-entrega`.""",
        "H2": """## Pruebas y depuración [EQUIPO]\n\nCasos: ayuda, saludo, estado, comando desconocido y salir. Un breakpoint después de leer el comando permitió observar `command`, `running` y `userName`; se corrigió la comparación con `equalsIgnoreCase`.""",
        "H3": """## Decisión sobre la colección [EQUIPO]\n\nSe usa `ArrayList<String>` porque conserva un número variable de recuerdos durante la ejecución. Se prueban memoria vacía, un recuerdo, varios y repetidos.""",
        "H4": """## Diseño de clases [EQUIPO]\n\n```mermaid\nclassDiagram\n  Main --> Agent\n  Agent --> Memory\n```\n\nEl diagrama de clases forma parte del README. El diagrama de comportamiento es práctica coordinada opcional de Entornos, no entrega obligatoria de Programación.""",
        "H5": """## Refactorización y patrón [EQUIPO]\n\n`Tool` define el contrato de las acciones. La semejanza con Command es encapsular cada acción ejecutable; no se añaden invocadores o fábricas sin necesidad. La revisión se acredita con historial y PR/revisión de código.""",
        "H6": """## Persistencia, errores y seguridad [EQUIPO]\n\nLas rutas son relativas, los fallos se controlan sin ocultarlos y los logs usan datos ficticios. La prueba guarda un recuerdo, reinicia el programa y verifica su recuperación.""",
        "H7": """## IA responsable [EQUIPO]\n\nLa integración es simulada o autorizada, rechaza datos sensibles y presenta las respuestas como propuestas. El registro relevante se mantiene en diario o Scrum, no en un archivo paralelo.""",
        "HF": """## Demostración final [EQUIPO → COMPROBACIÓN INDIVIDUAL]\n\nLa demo parte de un entorno limpio, usa `hf-final` y recorre una prueba representativa. Laura defiende una decisión propia, localiza el artefacto, muestra la prueba y explica una mejora. La recuperación se limita a evidencias concretas no superadas.""",
    }
    return sections[code]


def create_readmes() -> None:
    for folder, data in HITOS.items():
        code, title, objective, decision, result, version = data
        github = "H0 no exige GitHub, tag ni Sites." if code == "H0" else f"Versión estable: `{version}`. El repositorio y su README son la evidencia técnica canónica."
        (EXAMPLES / folder / "README.md").write_text(
            f"""# {code} — {title}\n\n> Ejemplo privado de Laura. Mostrar solo después del intento propio del alumnado.\n\n## Objetivo\n\n{objective}\n\n## Arquitectura de evidencias\n\n{github}\n\n- Diario individual evolutivo: `../FUENTES-CURSO/01-Diario-individual-MiniJarvis.xlsx`.\n- Scrum de equipo evolutivo: `../FUENTES-CURSO/02-Scrum-equipo-MiniJarvis.xlsx`.\n- Entrega Moodle mínima: `../ENTREGAS-MOODLE/{code}-entrega.md`.\n\n{technical_sections(code)}\n\n## Decisión y resultado\n\n- Decisión: {decision}\n- Resultado probado: {result}\n\n## Defensa de Laura [INDIVIDUAL]\n\nLaura localiza su aportación, reproduce una prueba y explica una decisión sin apoyarse en una plantilla de defensa separada.\n""",
            encoding="utf-8",
        )


def create_moodle_deliveries() -> None:
    target = EXAMPLES / "ENTREGAS-MOODLE"
    target.mkdir()
    for _, data in HITOS.items():
        code, title, objective, decision, result, version = data
        if code == "H0":
            items = "1. Ticket o texto breve del equipo.\n2. Confirmación de Scrum actualizado.\n3. Enlace opcional a una fotografía no-code en Drive.\n\nNo se entrega GitHub, tag ni Site."
        elif code == "HF":
            items = "1. Release o tag `hf-final`.\n2. Site personal final.\n3. Site de equipo final.\n4. Defensa individual.\n5. Recuperación concreta solo si procede."
        else:
            items = f"1. Tag `{version}` o commit estable.\n2. Confirmación de diario y Scrum actualizados.\n3. Evidencia no-code excepcional, solo si existe."
        (target / f"{code}-entrega.md").write_text(
            f"# Entrega Moodle de ejemplo — {code}\n\n- Equipo: Equipo Ada.\n- Alumna: Laura.\n- Enlaces: `URL_RESTRINGIDA_EJEMPLO`.\n\n{items}\n\nNo se adjuntan README, capturas, registros IA ni PDF/XLSX rutinarios.\n",
            encoding="utf-8",
        )


def create_sites() -> None:
    target = EXAMPLES / "PORTFOLIOS-PERIODICOS"
    target.mkdir()
    for checkpoint, scope in (("C1", "H1–H3"), ("C2", "H4–H5"), ("HF", "H1–H7")):
        (target / f"{checkpoint}-site-personal.md").write_text(
            f"# Site personal de Laura — {checkpoint}\n\nSíntesis de {scope}: aportación individual, aprendizaje, evidencia profunda y decisión que puede defender. No replica el diario ni el README.\n",
            encoding="utf-8",
        )
        (target / f"{checkpoint}-site-equipo.md").write_text(
            f"# Site del Equipo Ada — {checkpoint}\n\nSíntesis de {scope}: incremento, prueba principal, decisión de equipo y enlace al repositorio. No replica Scrum ni Moodle.\n",
            encoding="utf-8",
        )


def create_publication_readme() -> None:
    (EXAMPLES / "README-PUBLICACION.md").write_text(
        """# Ejemplos de Laura — publicación diferida\n\nMaterial docente privado. Cada ejemplo se muestra solo después del intento propio del alumnado o cuando existe una primera versión defendible.\n\n## Modelo canónico\n\n- `FUENTES-CURSO/`: un diario individual y un Scrum de equipo, evolutivos durante todo el curso.\n- cada hito: código y un README técnico integrado; no hay `docs/` paralelos.\n- `ENTREGAS-MOODLE/`: una entrega mínima por hito, alineada con las tareas reales.\n- `PORTFOLIOS-PERIODICOS/`: Sites únicamente en C1, C2 y HF.\n- las marcas `[INDIVIDUAL]`, `[EQUIPO]` y `[EQUIPO → COMPROBACIÓN INDIVIDUAL]` distinguen autoría y producto compartido.\n\nLos ejemplos ayudan a interpretar criterios y preparar la defensa; no son plantillas para copiar ni se incluyen en el paquete Moodle del alumnado.\n""",
        encoding="utf-8",
    )


def main() -> None:
    clean_legacy()
    create_course_workbooks()
    create_readmes()
    create_moodle_deliveries()
    create_sites()
    create_publication_readme()
    print("Ejemplos de Laura regenerados con arquitectura mínima")


if __name__ == "__main__":
    main()
