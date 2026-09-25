#!/usr/bin/env python3
"""Sincroniza el staging Moodle y crea un ZIP reproducible."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent
STUDENT_HTML = ROOT / "01-ALUMNADO-HTML"
PACKAGE = ROOT / "05-PAQUETE-MOODLE"
EMBEDDED_STUDENT_HTML = PACKAGE / "02-RECURSOS-ALUMNADO-HTML"
TASK_SOURCES = ROOT / "02-PROFESORADO" / "05-ECOSISTEMA-DIGITAL" / "TAREAS-MOODLE"
TASK_TARGET = PACKAGE / "03-TAREAS-HITOS"
ZIP_PATH = ROOT / "Minijarvis-paquete-moodle.zip"
ZIP_ROOT = PACKAGE.name
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
RUBRIC_COPIES = {
    STUDENT_HTML / "00-EMPIEZA-AQUI" / "04A-enunciados-y-entregables-alumnado.html":
        PACKAGE / "04-RUBRICAS-Y-CRITERIOS" / "04A-enunciados-y-entregables-alumnado.html",
    STUDENT_HTML / "00-EMPIEZA-AQUI" / "06-rubricas-hitos.html":
        PACKAGE / "04-RUBRICAS-Y-CRITERIOS" / "06-rubricas-hitos.html",
}


@dataclass(frozen=True)
class TreeReport:
    missing: tuple[str, ...]
    extra: tuple[str, ...]
    different: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not (self.missing or self.extra or self.different)


def file_map(root: Path) -> dict[str, bytes]:
    if not root.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def compare_trees(expected: Path, actual: Path) -> TreeReport:
    expected_files = file_map(expected)
    actual_files = file_map(actual)
    common = expected_files.keys() & actual_files.keys()
    return TreeReport(
        missing=tuple(sorted(expected_files.keys() - actual_files.keys())),
        extra=tuple(sorted(actual_files.keys() - expected_files.keys())),
        different=tuple(sorted(path for path in common if expected_files[path] != actual_files[path])),
    )


def sync_tree(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target, copy_function=shutil.copy2)


def render_task(source: Path) -> bytes:
    result = subprocess.run(
        [
            "pandoc",
            str(source),
            "--from",
            "gfm",
            "--to",
            "html5",
            "--standalone",
            "--metadata",
            f"title={source.stem}",
        ],
        check=True,
        capture_output=True,
    )
    return result.stdout


def expected_tasks() -> dict[Path, bytes]:
    return {
        TASK_TARGET / f"{source.stem}.html": render_task(source)
        for source in sorted(TASK_SOURCES.glob("*.md"))
        if source.name != "README.md"
    }


def write_deterministic_zip(source: Path, target: Path, archive_root: str) -> None:
    with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(item for item in source.rglob("*") if item.is_file()):
            relative = path.relative_to(source).as_posix()
            info = ZipInfo(f"{archive_root}/{relative}", FIXED_ZIP_TIME)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)


def zip_report(package: Path, zip_path: Path, archive_root: str) -> TreeReport:
    expected = file_map(package)
    if not zip_path.exists():
        return TreeReport(tuple(sorted(expected)), (), ())
    prefix = f"{archive_root}/"
    with ZipFile(zip_path) as archive:
        actual = {
            name[len(prefix):]: archive.read(name)
            for name in archive.namelist()
            if name.startswith(prefix) and not name.endswith("/")
        }
    common = expected.keys() & actual.keys()
    return TreeReport(
        missing=tuple(sorted(expected.keys() - actual.keys())),
        extra=tuple(sorted(actual.keys() - expected.keys())),
        different=tuple(sorted(path for path in common if expected[path] != actual[path])),
    )


def synchronize() -> None:
    if shutil.which("pandoc") is None:
        raise SystemExit("No se encontró pandoc.")
    sync_tree(STUDENT_HTML, EMBEDDED_STUDENT_HTML)
    TASK_TARGET.mkdir(parents=True, exist_ok=True)
    for target, content in expected_tasks().items():
        target.write_bytes(content)
    for source, target in RUBRIC_COPIES.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    with tempfile.NamedTemporaryFile(
        prefix="hermes-package-", suffix=".zip", dir=ROOT, delete=False
    ) as temporary:
        temporary_path = Path(temporary.name)
    try:
        write_deterministic_zip(PACKAGE, temporary_path, ZIP_ROOT)
        os.replace(temporary_path, ZIP_PATH)
    finally:
        temporary_path.unlink(missing_ok=True)


def check() -> list[str]:
    errors: list[str] = []
    student_report = compare_trees(STUDENT_HTML, EMBEDDED_STUDENT_HTML)
    if not student_report.ok:
        errors.append(
            "recursos alumnado: "
            f"faltan={len(student_report.missing)}, sobran={len(student_report.extra)}, "
            f"difieren={len(student_report.different)}"
        )
    for target, expected in expected_tasks().items():
        if not target.exists() or target.read_bytes() != expected:
            errors.append(f"tarea Moodle desactualizada: {target.relative_to(ROOT)}")
    for source, target in RUBRIC_COPIES.items():
        if not target.exists() or target.read_bytes() != source.read_bytes():
            errors.append(f"copia desactualizada: {target.relative_to(ROOT)}")
    archive_report = zip_report(PACKAGE, ZIP_PATH, ZIP_ROOT)
    if not archive_report.ok:
        errors.append(
            "ZIP: "
            f"faltan={len(archive_report.missing)}, sobran={len(archive_report.extra)}, "
            f"difieren={len(archive_report.different)}"
        )
    if not errors:
        with tempfile.NamedTemporaryFile(
            prefix="hermes-verify-package-", suffix=".zip", delete=False
        ) as temporary:
            temporary_path = Path(temporary.name)
        try:
            write_deterministic_zip(PACKAGE, temporary_path, ZIP_ROOT)
            if temporary_path.read_bytes() != ZIP_PATH.read_bytes():
                errors.append("el ZIP contiene los mismos archivos, pero no es determinista")
        finally:
            temporary_path.unlink(missing_ok=True)
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Comprueba sin modificar archivos.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if not args.check:
        synchronize()
    errors = check()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(
        f"PASS: {len(file_map(PACKAGE))} archivos; "
        "staging, fuentes HTML y ZIP sincronizados."
    )


if __name__ == "__main__":
    main()
