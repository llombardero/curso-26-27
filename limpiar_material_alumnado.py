#!/usr/bin/env python3
"""Deja las fuentes del alumnado libres de contenido interno docente."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ALUMNADO = ROOT / "01-ALUMNADO"


RESUMENES_HITOS = {
    "h0-torre-papel-scrum": (
        "H0 - Equipo, Scrum y torre de papel",
        "Vivir un sprint breve, construir una torre de papel y trasladar lo aprendido a la organización de MiniJarvis.",
        "Completa la ficha del reto, registra el trabajo del equipo y revisa en Moodle las instrucciones de entrega de H0.",
    ),
    "h1-primer-asistente": (
        "H1 - Primer asistente básico",
        "Crear una primera versión sencilla de MiniJarvis por consola en Java.",
        "El programa debe ejecutarse, incluir un README básico y poder explicarse. Todavía no incluye menú, bucles, memoria ni IA real.",
    ),
    "h2-decisiones-depuracion": (
        "H2 - Decisiones y depuración",
        "Convertir MiniJarvis en un programa interactivo con menú, decisiones, repetición y salida controlada.",
        "Debes aportar código funcional, pruebas, una evidencia de depuración y una explicación defendible.",
    ),
    "h3-memoria-colecciones": (
        "H3 - Memoria y colecciones",
        "Añadir memoria temporal a MiniJarvis mediante una colección adecuada.",
        "Debes justificar la colección elegida, probar casos límite y explicar qué ocurre al cerrar el programa.",
    ),
    "h4-agente-orientado-objetos": (
        "H4 - Agente orientado a objetos",
        "Reorganizar MiniJarvis con clases, objetos y responsabilidades claras.",
        "El código y los diagramas deben coincidir, y cada integrante debe poder defender las decisiones principales.",
    ),
    "h5-extensible-clean-code-patrones": (
        "H5 - Agente extensible, código limpio y patrones",
        "Mejorar MiniJarvis para añadir herramientas o comandos sin romper el diseño.",
        "Debes mostrar la refactorización, pruebas, revisión de código y una decisión razonada sobre el patrón utilizado o descartado.",
    ),
    "h6-persistente-trazable": (
        "H6 - Persistencia y trazabilidad",
        "Conservar memoria e historial entre ejecuciones mediante ficheros y tratamiento seguro de errores.",
        "Debes demostrar el funcionamiento en dos ejecuciones, documentar pruebas y evitar secretos o datos personales.",
    ),
    "h7-integracion-ia-responsable": (
        "H7 - Integración responsable de IA",
        "Integrar o simular una ayuda de IA con límites, registro y validación humana.",
        "La integración real solo se realiza si está autorizada. Nunca se suben claves, tokens ni datos personales.",
    ),
    "hf-presentacion-final-recuperacion-mejora": (
        "HF - Presentación final, recuperación y mejora",
        "Seleccionar evidencias, demostrar la evolución de MiniJarvis y defender el aprendizaje individual.",
        "Prepara el portfolio, la demostración, la defensa y, si corresponde, una recuperación o mejora específica.",
    ),
}


def remove_marked_block(text: str, marker: str) -> str:
    pattern = re.compile(
        rf"\n?<!-- {re.escape(marker)}:START -->.*?<!-- {re.escape(marker)}:END -->\n?",
        re.DOTALL,
    )
    return pattern.sub("\n", text)


def remove_related_documents(text: str) -> str:
    return re.sub(
        r"\n?Documentos relacionados:\n\n(?:- .*\n)+\n---\n",
        "\n---\n",
        text,
    )


def clean_common(text: str) -> str:
    text = text.replace("TEMPLATE", "PLANTILLA")
    text = text.replace("Template", "Plantilla")
    text = text.replace("template", "plantilla")
    text = re.sub(r"\.md\b", "", text)
    text = re.sub(r"^Edición final para Moodle.*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"<!--.*?-->\n?", "", text, flags=re.DOTALL)
    text = re.sub(
        r"\s*\*\*(?:Momento|Fase) HEXA:\*\*\s*[^.\n]+\.?",
        "",
        text,
    )
    text = text.replace("RA/CE trabajados:", "Aprendizajes trabajados:")
    text = text.replace("RA/CE que creo haber trabajado:", "Aprendizajes que creo haber trabajado:")
    text = text.replace("RA pendientes", "aprendizajes pendientes")
    text = text.replace("RA pendiente", "aprendizaje pendiente")
    return re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"


def clean_general(path: Path, text: str) -> str:
    name = path.name

    if name in {
        "04A-enunciados-y-entregables-alumnado.md",
        "06-rubricas-hitos.md",
    } or path.parent.name == "01-LIBRO-POR-HITOS" and name == "README.md":
        text = remove_marked_block(text, "HEXA-POLITICA-TODOS-HITOS")

    if name in {
        "05-politica-uso-ia-semaforo-registro-defensa.md",
        "06-rubricas-hitos.md",
        "07-plantillas-entregables.md",
        "08-guia-alumnado-proyecto-agente-ia.md",
    }:
        text = remove_related_documents(text)

    if name == "04A-enunciados-y-entregables-alumnado.md":
        text = re.sub(
            r"\n### Relación con módulos\n.*?(?=\n### )",
            "\n",
            text,
            flags=re.DOTALL,
        )
        text = re.split(r"\n# 16\. Ajuste aplicado a los hitos MiniJarvis", text, maxsplit=1)[0]

    if name == "05-politica-uso-ia-semaforo-registro-defensa.md":
        text = re.split(r"\n## 14\. Próximo paso", text, maxsplit=1)[0]

    if name == "06-rubricas-hitos.md":
        text = re.sub(
            r"\nRA/CE principales:.*?(?=\n\| Dimensión)",
            "\n",
            text,
            flags=re.DOTALL,
        )
        text = re.sub(
            r"\n## 13\. Uso de la rúbrica con RA/CE.*?(?=\n## 14\.)",
            "\n",
            text,
            flags=re.DOTALL,
        )
        text = text.replace("## 14. Regla sobre IA y defensa", "## 13. Regla sobre IA y defensa")
        text = re.split(r"\n## 15\. Próximo paso", text, maxsplit=1)[0]
        text = text.replace(
            "- La rúbrica no sustituye a la calificación por RA/CE.\n- Sirve para valorar la calidad de evidencias asociadas a RA/CE.\n",
            "- La rúbrica explica la calidad esperada en las evidencias.\n- Programación y Entornos se califican por separado aunque compartan evidencias.\n",
        )

    if name == "07-plantillas-entregables.md":
        text = re.split(r"\n## 15\. Próximo paso", text, maxsplit=1)[0]

    if name == "08-guia-alumnado-proyecto-agente-ia.md":
        text = re.split(r"\n# 16\. Ajuste aplicado a los hitos MiniJarvis", text, maxsplit=1)[0]

    return text


def clean_hito_file(path: Path, text: str) -> str:
    if "ficha-alumnado" in path.name:
        text = remove_marked_block(text, "HEXA-CICLO-COMPLETO-POR-HITO")
        text = re.split(r"\n## Cobertura curricular de Programación", text, maxsplit=1)[0]
    return text


def rewrite_hito_readmes() -> None:
    hito_root = ALUMNADO / "02-HITOS"
    for folder, (title, objective, completion) in RESUMENES_HITOS.items():
        path = hito_root / folder / "README.md"
        path.write_text(
            f"# {title}\n\n"
            f"## Objetivo\n\n{objective}\n\n"
            f"## Para completar el hito\n\n{completion}\n\n"
            "## Entrega\n\n"
            "Consulta en Moodle la tarea del hito, los criterios visibles y las instrucciones de entrega digital. "
            "Comprueba los permisos y asegúrate de que puedes explicar lo entregado.\n",
            encoding="utf-8",
        )


def rewrite_entry_readmes() -> None:
    (ALUMNADO / "README.md").write_text(
        "# MiniJarvis - materiales del alumnado\n\n"
        "## Cómo trabajar\n\n"
        "1. Consulta en Moodle el reto o la sesión que esté activa.\n"
        "2. Lee solo los capítulos y plantillas indicados para ese momento.\n"
        "3. Usa la guía básica de Drive o GitHub si necesitas ayuda con esas herramientas.\n"
        "4. Revisa los criterios antes de empezar y las instrucciones de entrega antes de enviar.\n\n"
        "## Regla de trabajo\n\n"
        "Moodle indica qué hacer y registra la entrega. Drive conserva evidencias, Sheets registra el proceso, "
        "Sites selecciona aprendizajes y GitHub conserva el código. No mantengas dos copias editables del código.\n\n"
        "Los ejemplos resueltos se mostrarán después del intento propio o de una primera versión defendible.\n",
        encoding="utf-8",
    )

    (ALUMNADO / "01-LIBRO-POR-HITOS" / "README.md").write_text(
        "# Libro del alumnado - Programación y Entornos con MiniJarvis\n\n"
        "Este libro acompaña el proyecto anual. Cada capítulo se publica cuando es necesario para construir el hito activo.\n\n"
        "MiniJarvis crece así:\n\n"
        "```text\n"
        "programa básico -> menú -> memoria -> clases -> herramientas -> persistencia -> IA responsable -> portfolio final\n"
        "```\n\n"
        "## Capítulos\n\n"
        "| Capítulo | Contenido | Hito |\n"
        "|---:|---|---|\n"
        "| 00 | Cómo usar este libro | Todo el curso |\n"
        "| 01 | Primeros programas en Java | H1 |\n"
        "| 02 | Variables, constantes y entrada/salida | H1 |\n"
        "| 03 | Decisiones, bucles y menús | H2 |\n"
        "| 04 | Pruebas, depuración y errores | H2-H3 |\n"
        "| 05 | Colecciones y memoria temporal | H3 |\n"
        "| 06 | Programación orientada a objetos | H4 |\n"
        "| 07 | Encapsulación, responsabilidades y UML | H4 |\n"
        "| 08 | Interfaces, extensibilidad y patrones iniciales | H5 |\n"
        "| 09 | Ficheros, persistencia y registros | H6 |\n"
        "| 10 | IA responsable en proyectos de programación | H7 |\n"
        "| 11 | Portfolio, defensa y proyecto final | HF |\n\n"
        "## Cómo usar cada capítulo\n\n"
        "1. Lee el objetivo y los conceptos básicos.\n"
        "2. Reproduce los ejemplos pequeños.\n"
        "3. Aplica lo aprendido a MiniJarvis.\n"
        "4. Registra pruebas, errores y decisiones.\n"
        "5. Comprueba que puedes explicarlo con tus palabras.\n\n"
        "Los ejemplos resueltos sirven para comparar y mejorar después del intento propio, no para copiar antes de pensar.\n",
        encoding="utf-8",
    )


def rename_templates() -> None:
    paths = sorted(
        (p for p in ALUMNADO.rglob("*") if "template" in p.name.lower()),
        key=lambda p: len(p.parts),
        reverse=True,
    )
    for path in paths:
        new_name = re.sub("template", "plantilla", path.name, flags=re.IGNORECASE)
        target = path.with_name(new_name)
        if target.exists():
            raise RuntimeError(f"No se puede renombrar {path}: ya existe {target}")
        path.rename(target)


def update_project_template_references() -> None:
    for directory in (ROOT / "02-PROFESORADO", ROOT / "03-EJEMPLOS-LAURA-PRIVADOS"):
        for path in directory.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            text = text.replace("TEMPLATE", "PLANTILLA")
            text = text.replace("Template", "Plantilla")
            text = text.replace("template", "plantilla")
            path.write_text(text, encoding="utf-8")


def main() -> None:
    for path in sorted(ALUMNADO.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        text = clean_general(path, text)
        text = clean_hito_file(path, text)
        path.write_text(clean_common(text), encoding="utf-8")

    rewrite_hito_readmes()
    rewrite_entry_readmes()
    rename_templates()
    update_project_template_references()


if __name__ == "__main__":
    main()
