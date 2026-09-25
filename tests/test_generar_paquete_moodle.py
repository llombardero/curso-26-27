from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "generar_paquete_moodle.py"


def load_module():
    spec = importlib.util.spec_from_file_location("generar_paquete_moodle", MODULE_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_deterministic_zip_is_stable_and_sorted(tmp_path):
    generator = load_module()
    source = tmp_path / "package"
    source.mkdir()
    (source / "z.txt").write_text("z", encoding="utf-8")
    nested = source / "a"
    nested.mkdir()
    (nested / "b.txt").write_text("b", encoding="utf-8")
    first = tmp_path / "first.zip"
    second = tmp_path / "second.zip"

    generator.write_deterministic_zip(source, first, "package")
    (source / "z.txt").touch()
    generator.write_deterministic_zip(source, second, "package")

    assert first.read_bytes() == second.read_bytes()
    with ZipFile(first) as archive:
        assert archive.namelist() == ["package/a/b.txt", "package/z.txt"]
        assert archive.testzip() is None


def test_compare_trees_reports_missing_extra_and_different(tmp_path):
    generator = load_module()
    expected = tmp_path / "expected"
    actual = tmp_path / "actual"
    expected.mkdir()
    actual.mkdir()
    (expected / "same.txt").write_text("same", encoding="utf-8")
    (actual / "same.txt").write_text("same", encoding="utf-8")
    (expected / "changed.txt").write_text("new", encoding="utf-8")
    (actual / "changed.txt").write_text("old", encoding="utf-8")
    (expected / "missing.txt").write_text("missing", encoding="utf-8")
    (actual / "extra.txt").write_text("extra", encoding="utf-8")

    report = generator.compare_trees(expected, actual)

    assert report.missing == ("missing.txt",)
    assert report.extra == ("extra.txt",)
    assert report.different == ("changed.txt",)
    assert not report.ok


def test_sync_tree_removes_stale_files_and_copies_source(tmp_path):
    generator = load_module()
    source = tmp_path / "source"
    target = tmp_path / "target"
    source.mkdir()
    target.mkdir()
    (source / "current.txt").write_text("current", encoding="utf-8")
    (target / "stale.txt").write_text("stale", encoding="utf-8")

    generator.sync_tree(source, target)

    assert generator.compare_trees(source, target).ok
    assert not (target / "stale.txt").exists()
