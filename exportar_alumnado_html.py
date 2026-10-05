#!/usr/bin/env python3
"""Exporta los materiales Markdown de alumnado a HTML navegable."""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "01-ALUMNADO"
TARGET = ROOT / "01-ALUMNADO-HTML"
CSS_FILE = "estilos-minijarvis.css"


CSS = """
:root {
  color-scheme: light;
  --bg: #f7f3ea;
  --paper: #fffdf7;
  --ink: #1f2933;
  --muted: #5f6c7b;
  --line: #ded6c8;
  --accent: #2457a6;
  --accent-soft: #e8f0ff;
  --code-bg: #f0eadf;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.6;
}

main {
  width: min(960px, calc(100% - 32px));
  margin: 32px auto;
  padding: 32px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: 0 16px 40px rgb(31 41 51 / 8%);
}

h1, h2, h3, h4 { line-height: 1.25; }
h1 { margin-top: 0; font-size: clamp(2rem, 5vw, 3rem); }
h2 { margin-top: 2.2rem; border-top: 1px solid var(--line); padding-top: 1.1rem; }

a { color: var(--accent); font-weight: 650; }
a:hover { text-decoration-thickness: 0.16em; }

blockquote {
  margin: 1.2rem 0;
  padding: 0.85rem 1rem;
  background: var(--accent-soft);
  border-left: 5px solid var(--accent);
  border-radius: 0 12px 12px 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  overflow-wrap: anywhere;
}

th, td { border: 1px solid var(--line); padding: 0.65rem; vertical-align: top; }
th { background: #efe7d8; text-align: left; }

code {
  background: var(--code-bg);
  border-radius: 0.35rem;
  padding: 0.08rem 0.28rem;
}

pre {
  overflow-x: auto;
  padding: 1rem;
  background: var(--code-bg);
  border-radius: 12px;
}

pre code { padding: 0; background: transparent; }

img { max-width: 100%; height: auto; }

.topbar {
  margin-bottom: 1.5rem;
  color: var(--muted);
  font-size: 0.95rem;
}

.topbar a { color: var(--muted); }

@media (max-width: 640px) {
  main { width: 100%; margin: 0; padding: 20px; border-radius: 0; border-left: 0; border-right: 0; }
  table { display: block; overflow-x: auto; }
}
""".strip()


def relative_css_path(html_path: Path) -> str:
    return os.path.relpath(TARGET / CSS_FILE, html_path.parent).replace(os.sep, "/")


def rewrite_internal_links(text: str) -> str:
    """Conserva enlaces locales y adapta enlaces Markdown a HTML."""

    pattern = re.compile(r'href="([^"]+)"', re.IGNORECASE)

    def replace(match: re.Match[str]) -> str:
        href = match.group(1)

        if re.match(r"^(?:https?://|mailto:|#)", href, re.IGNORECASE):
            return match.group(0)

        href = re.sub(
            r"\.md(?=([?#]|$))",
            ".html",
            href,
            flags=re.IGNORECASE,
        )
        return f'href="{href}"'

    return pattern.sub(replace, text)


def wrap_html(title: str, body: str, html_path: Path) -> str:
    css = relative_css_path(html_path)
    home = os.path.relpath(
        TARGET / "LEEME-ALUMNADO.html",
        html_path.parent,
    ).replace(os.sep, "/")
    escaped_title = html.escape(title or "MiniJarvis")
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escaped_title}</title>
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <main>
    <nav class="topbar"><a href="{home}">Inicio alumnado</a></nav>
{body}
  </main>
</body>
</html>
"""


def markdown_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def export_markdown(path: Path) -> None:
    rel = path.relative_to(SOURCE)
    out = (TARGET / rel).with_suffix(".html")
    out.parent.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        ["pandoc", str(path), "--from", "gfm", "--to", "html5"],
        check=True,
        capture_output=True,
        text=True,
    )
    body = rewrite_internal_links(result.stdout)
    out.write_text(wrap_html(markdown_title(path), body, out), encoding="utf-8")


def copy_asset(path: Path) -> None:
    rel = path.relative_to(SOURCE)
    out = TARGET / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, out)


def include_in_scope(path: Path, scope: str) -> bool:
    """Decide qué fuentes se exportan en una generación parcial."""

    if scope == "all":
        return True

    rel = path.relative_to(SOURCE)
    parts = rel.parts

    # Archivos situados directamente en la raíz de alumnado.
    if len(parts) == 1:
        return True

    # Documentación común del curso.
    if parts[0] == "00-EMPIEZA-AQUI":
        return True

    # Plantillas y recursos globales.
    if parts[0] == "04-PLANTILLAS-GLOBALES":
        return True

    # Libro necesario para H1.
    if parts[0] == "01-LIBRO-POR-HITOS":
        return rel.name in {
            "README.md",
            "00-como-usar-este-libro.md",
            "01-primeros-programas-java.md",
            "02-variables-constantes-entrada-salida.md",
        }

    # Material específico del hito H1.
    if parts[:2] == ("02-HITOS", "h1-primer-asistente"):
        return True

    # Índice de sesiones y sesiones H1.
    if parts[0] == "03-SESIONES":
        if rel.name == "00-INDICE.md":
            return False
        return len(parts) >= 2 and parts[1] == "h1"

    return False


def write_h1_session_index() -> None:
    """Genera un índice navegable solo con las sesiones incluidas en H1."""

    source_dir = SOURCE / "03-SESIONES" / "h1"
    out = TARGET / "03-SESIONES" / "00-INDICE.html"
    out.parent.mkdir(parents=True, exist_ok=True)

    items = []

    for source in sorted(source_dir.glob("*.md")):
        target_name = source.with_suffix(".html").name
        title = html.escape(markdown_title(source))
        items.append(
            f'<li><a href="h1/{target_name}">{title}</a></li>'
        )

    body = """
<h1>Sesiones de H1 — Primer asistente</h1>
<p>Este índice pertenece a la exportación piloto global + H1.</p>
<p>Incluye únicamente las sesiones de H1 que forman parte de este alcance validado.</p>
<ol>
""" + "\n".join(items) + """
</ol>
"""

    out.write_text(
        wrap_html(
            "Sesiones H1 — Primer asistente",
            body.strip(),
            out,
        ),
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Exporta materiales de alumnado a HTML."
    )
    parser.add_argument(
        "--scope",
        choices=("all", "h1"),
        default="all",
        help=(
            "all: exportación completa; "
            "h1: piloto con documentación global y H1."
        ),
    )
    return parser.parse_args()


def main(scope: str = "all") -> None:
    if not SOURCE.exists():
        raise SystemExit(f"No existe la carpeta fuente: {SOURCE}")

    if scope == "all":
        if TARGET.exists():
            shutil.rmtree(TARGET)
        TARGET.mkdir(parents=True)
    else:
        # La exportación piloto H1 no debe borrar H0 ni H2-HF.
        TARGET.mkdir(parents=True, exist_ok=True)

        # Directorios completos pertenecientes al alcance global + H1.
        for relative in (
            "00-EMPIEZA-AQUI",
            "04-PLANTILLAS-GLOBALES",
            "02-HITOS/h1-primer-asistente",
            "03-SESIONES/h1",
        ):
            target = TARGET / relative
            if target.exists():
                shutil.rmtree(target)

        # Archivos concretos del libro incluidos en el piloto.
        for relative in (
            "01-LIBRO-POR-HITOS/README.html",
            "01-LIBRO-POR-HITOS/00-como-usar-este-libro.html",
            "01-LIBRO-POR-HITOS/01-primeros-programas-java.html",
            "01-LIBRO-POR-HITOS/02-variables-constantes-entrada-salida.html",
            "03-SESIONES/00-INDICE.html",
        ):
            target = TARGET / relative
            if target.exists():
                target.unlink()

    (TARGET / CSS_FILE).write_text(CSS + "\n", encoding="utf-8")

    for path in sorted(SOURCE.rglob("*")):
        if path.is_dir():
            continue
        if not include_in_scope(path, scope):
            continue
        if path.suffix.lower() == ".md":
            export_markdown(path)
        else:
            copy_asset(path)

    guia = TARGET / "LEEME-ALUMNADO.html"
    guia.write_text(
        wrap_html(
            "Cómo usar estos materiales",
            """
<h1>Cómo usar estos materiales</h1>
<p>Estos son los materiales de alumnado de MiniJarvis.</p>
<ol>
  <li>Consulta primero el documento de inicio que indique Moodle.</li>
  <li>Trabaja únicamente con el reto, sesión o plantilla que esté activa.</li>
  <li>Consulta en Moodle el documento que corresponda a cada sesión, hito o plantilla.</li>
  <li>Entrega en Moodle solo lo que indique cada hito.</li>
</ol>
<p>Si tienes dudas sobre Drive o GitHub, consulta sus guías básicas antes de realizar la entrega.</p>
""".strip(),
            guia,
        ),
        encoding="utf-8",
    )

    if scope == "h1":
        write_h1_session_index()


if __name__ == "__main__":
    args = parse_args()
    main(args.scope)
