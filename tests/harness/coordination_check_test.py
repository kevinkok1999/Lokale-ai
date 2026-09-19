from __future__ import annotations

import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "coordination_check.py"
SPEC = importlib.util.spec_from_file_location("coordination_check", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

def lane(lane_id: str, state: str = "RUNNING", scope: str = "src/a.py", runner: int = 0):
    return {
        "lane_id": lane_id,
        "state": state,
        "dependencies": [],
        "read_set": [],
        "write_set": [scope],
        "resource_claims": {
            "github_actions_runner": runner,
            "heavy_gpu": 0,
            "git_writer": 0,
        },
    }

class CoordinationCheckTest(unittest.TestCase):
    def board(self, lanes):
        return {
            "canonical_writer": "controller-only",
            "active_lanes": lanes,
        }

    def test_independent_running_lanes_pass(self):
        self.assertEqual(MODULE.validate(self.board([
            lane("a", scope="src/a.py"),
            lane("b", scope="src/b.py"),
        ])), [])

    def test_duplicate_write_scope_fails(self):
        errors = MODULE.validate(self.board([
            lane("a", scope="src/a.py"),
            lane("b", scope="src/a.py"),
        ]))
        self.assertTrue(any("write scope collision" in item for item in errors))

    def test_runner_semaphore_fails(self):
        errors = MODULE.validate(self.board([
            lane("a", scope="src/a.py", runner=1),
            lane("b", scope="src/b.py", runner=1),
        ]))
        self.assertTrue(any("github_actions_runner" in item for item in errors))

if __name__ == "__main__":
    unittest.main()
