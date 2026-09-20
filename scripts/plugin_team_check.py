#!/usr/bin/env python3
"""Validate plugin-team coordination metadata without contacting external services."""
from __future__ import annotations
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".ai" / "plugin-registry.yaml"
TEAM = ROOT / ".ai" / "plugin-team.yaml"
RESILIENCE = ROOT / ".ai" / "resilience-policy.yaml"
BOARD = ROOT / ".ai" / "workboard.json"

REQUIRED_CORE = {"context7","exa","neon","github","vercel","figma","canva"}

def ids_from_registry(text: str) -> set[str]:
    return set(re.findall(r"(?m)^\s*- id:\s*([^\s#]+)\s*$", text))

def main() -> int:
    errors=[]
    for p in (REGISTRY,TEAM,RESILIENCE,BOARD):
        if not p.is_file():
            errors.append(f"missing required file: {p.relative_to(ROOT)}")
    if errors:
        print(json.dumps({"status":"FAIL","errors":errors}, indent=2))
        return 1

    ids=ids_from_registry(REGISTRY.read_text(encoding="utf-8"))
    missing=sorted(REQUIRED_CORE-ids)
    if missing:
        errors.append("missing core plugin(s): "+", ".join(missing))

    board=json.loads(BOARD.read_text(encoding="utf-8"))
    if board.get("canonical_writer")!="controller-only":
        errors.append("canonical_writer must remain controller-only")

    team=TEAM.read_text(encoding="utf-8")
    resilience=RESILIENCE.read_text(encoding="utf-8")
    if not re.search(r"(?m)^\s*github_actions_slots:\s*1\s*$", team):
        errors.append("plugin-team must declare exactly one GitHub Actions slot")

    if "A blocked lane is not a blocked project." not in resilience:
        errors.append("resilience policy must preserve lane-local failure isolation")
    if "github_unavailable_does_not_stop_safe_local_work: true" not in (ROOT / ".ai" / "github-policy.yaml").read_text(encoding="utf-8"):
        errors.append("GitHub policy must preserve local progress during outage")

    result={
        "schema_version":"v1",
        "kind":"plugin-team-check",
        "status":"PASS" if not errors else "FAIL",
        "core_plugins":sorted(REQUIRED_CORE),
        "registered_plugins":sorted(ids),
        "canonical_writer":board.get("canonical_writer"),
        "errors":errors,
        "notes":[
            "This validates coordination metadata only.",
            "It does not prove local Codex plugin connectivity.",
            "Suggested optional plugins remain unavailable until user installation/connection succeeds."
        ],
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
