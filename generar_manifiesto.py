#!/usr/bin/env python3
"""Regenera el inventario SHA-256 de los contenidos fuente del proyecto."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFIESTO-ARCHIVOS.md"
SOURCE_DIRS = (
    ROOT / "01-ALUMNADO",
    ROOT / "02-PROFESORADO",
    ROOT / "03-EJEMPLOS-LAURA-PRIVADOS",
)

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main() -> None:
    files = sorted(
        path
        for directory in SOURCE_DIRS
        for path in directory.rglob("*")
        if path.is_file()
    )
    lines = [
        "# Manifiesto de archivos - MiniJarvis",
        "",
        f"Archivos de contenido registrados: {len(files)}",
        "",
        "| SHA-256 | Ruta |",
        "|---|---|",
    ]
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        lines.append(f"| `{sha256(path)}` | `{relative}` |")
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
