#!/usr/bin/env python3
"""Reconstruye Drive operativo, paquete Moodle y ZIP reproducibles de MiniJarvis."""
from __future__ import annotations

import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "01-ALUMNADO-HTML"
MASTERS = ROOT / "02-PROFESORADO/05-ECOSISTEMA-DIGITAL/PLANTILLAS-MAESTRAS"
TASKS = ROOT / "02-PROFESORADO/05-ECOSISTEMA-DIGITAL/TAREAS-MOODLE"
DRIVE = ROOT / "04-DRIVE-5-EQUIPOS"
MOODLE = ROOT / "05-PAQUETE-MOODLE"

MOODLE_README = """# Paquete Moodle MiniJarvis — Programación 1.º DAW

Este paquete prepara la publicación progresiva de MiniJarvis en Moodle.

## Función de Moodle

Moodle:

- distribuye las instrucciones y recursos que estén activos;
- identifica la versión que se presenta a evaluación;
- conserva la entrega y el feedback;
- no sustituye al repositorio, al diario, a Scrum ni a Sites.

## Recursos del alumnado

La carpeta:

```text
02-RECURSOS-ALUMNADO-HTML/
```

es una **salida derivada** de los originales de:

```text
01-ALUMNADO/
```

No se corrige manualmente.

Cuando cambien los Markdown canónicos del alumnado, se debe:

```text
1. regenerar 01-ALUMNADO-HTML;
2. comprobar el resultado;
3. actualizar 02-RECURSOS-ALUMNADO-HTML.
```

## Tareas de los hitos

La carpeta:

```text
03-TAREAS-HITOS/
```

contiene las instrucciones de entrega que se trasladan a Moodle.

Para H1, la entrega normal identifica:

- el tag `h1-entrega` o un commit estable;
- que los enlaces estables siguen siendo válidos;
- que diario y Scrum están actualizados solo si hubo algo significativo que registrar;
- una evidencia no-code excepcional únicamente si realmente existe.

No se vuelven a subir de forma rutinaria:

- código;
- README;
- capturas de consola o GitHub;
- copias de diario o Scrum;
- registros independientes de IA;
- exportaciones PDF o XLSX.

## Regla de publicación

Los materiales se publican progresivamente según avance el curso.

Los ejemplos completos de Laura permanecen privados hasta después del intento propio del alumnado.

## Idea clave

```text
Moodle identifica y registra la entrega.
GitHub conserva el producto técnico.
Diario y Scrum conservan proceso significativo.
Drive guarda solo evidencia no-code excepcional.
Sites seleccionan evidencias en los cierres previstos.
```
"""


def clean(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def build_drive() -> None:
    clean(DRIVE)
    base = DRIVE / "PROGRAMACION_1DAW_MINIJARVIS_2026_2027"
    base.mkdir()
    (base / "LEEME-DRIVE.md").write_text(
        "# Drive operativo MiniJarvis\n\n"
        "Moodle distribuye las guías y GitHub conserva código, tests y README. "
        "Este Drive solo mantiene enlaces estables, Scrum y evidencia no-code sin mejor ubicación. "
        "No hay copias del material de Moodle, del código ni exportaciones cerradas rutinarias.\n",
        encoding="utf-8",
    )
    for number in range(1, 6):
        team = base / "01_EQUIPOS" / f"EQUIPO_{number:02d}"
        links = team / "00_ENLACES"
        scrum = team / "01_SCRUM"
        evidence = team / "02_EVIDENCIAS_NO_CODE"
        links.mkdir(parents=True)
        scrum.mkdir()
        evidence.mkdir()
        (links / "LEEME.md").write_text(
            "# Enlaces estables\n\nRegistra una vez GitHub, diario, Scrum y Sites. Corrige aquí solo si cambian.\n",
            encoding="utf-8",
        )
        shutil.copy2(MASTERS / "02-Scrum-equipo-MiniJarvis.xlsx", scrum / "Scrum-equipo-MiniJarvis.xlsx")
        (evidence / "LEEME.md").write_text(
            "# Evidencias no-code\n\nGuarda solo fotografías, torre H0 u otra evidencia no-code sin fuente mejor. "
            "Crea una carpeta de hito únicamente cuando exista una evidencia real.\n",
            encoding="utf-8",
        )
    teacher = base / "02_PLANTILLAS_DOCENTE"
    teacher.mkdir()
    for source in sorted(MASTERS.glob("*.xlsx")):
        shutil.copy2(source, teacher / source.name)
    private = base / "03_ADMIN_DOCENTE_PRIVADO"
    private.mkdir()
    (private / "LEEME.md").write_text(
        "# Administración docente privada\n\nNo compartir con alumnado. No almacenar credenciales ni datos personales innecesarios.\n",
        encoding="utf-8",
    )


def render_markdown(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(source), "--from", "gfm", "--to", "html5", "--standalone", "-o", str(target)],
        check=True,
    )


def build_moodle() -> None:
    clean(MOODLE)
    (MOODLE / "LEEME-MOODLE.md").write_text(
        MOODLE_README,
        encoding="utf-8",
    )
    shutil.copytree(HTML, MOODLE / "02-RECURSOS-ALUMNADO-HTML")
    task_target = MOODLE / "03-TAREAS-HITOS"
    task_target.mkdir()
    for source in sorted(TASKS.glob("*.md")):
        render_markdown(source, task_target / source.with_suffix(".html").name)


def zip_tree(source: Path, target: Path) -> None:
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT))


def build_zips() -> None:
    mapping = {
        "01-ALUMNADO": "Minijarvis-alumnado.zip",
        "01-ALUMNADO-HTML": "Minijarvis-alumnado-html.zip",
        "02-PROFESORADO": "Minijarvis-profesorado.zip",
        "03-EJEMPLOS-LAURA-PRIVADOS": "Minijarvis-ejemplos-Laura-privados.zip",
        "04-DRIVE-5-EQUIPOS": "Minijarvis-drive-5-equipos.zip",
        "05-PAQUETE-MOODLE": "Minijarvis-paquete-moodle.zip",
        "02-PROFESORADO/03-PRESENTACIONES/POR-SESION": "Minijarvis-presentaciones-sesiones.zip",
    }
    for source, target in mapping.items():
        zip_tree(ROOT / source, ROOT / target)


def main() -> None:
    if not HTML.is_dir():
        raise SystemExit("Falta 01-ALUMNADO-HTML; ejecuta primero exportar_alumnado_html.py")
    build_drive()
    build_moodle()
    build_zips()
    print("Drive, Moodle y siete ZIP reconstruidos")


if __name__ == "__main__":
    main()
