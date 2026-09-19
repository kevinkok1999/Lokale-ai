from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "codex_bootstrap.py"
SPEC = importlib.util.spec_from_file_location("codex_bootstrap", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class BootstrapUnitTest(unittest.TestCase):
    def test_scalar_reads_simple_yaml_scalar(self):
        text = 'status: "READY"\nnext_task: T001\n'
        self.assertEqual(MODULE.scalar(text, "status"), "READY")
        self.assertEqual(MODULE.scalar(text, "next_task"), "T001")

    def test_fingerprint_changes_with_content(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            path = root / "a.txt"
            path.write_text("one", encoding="utf-8")
            first = MODULE.fingerprint(root, ["a.txt"])
            path.write_text("two", encoding="utf-8")
            second = MODULE.fingerprint(root, ["a.txt"])
            self.assertNotEqual(first, second)


if __name__ == "__main__":
    unittest.main()
