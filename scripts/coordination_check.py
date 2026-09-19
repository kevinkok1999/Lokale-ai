#!/usr/bin/env python3
"""Validate the Local AI OS shared parallel-work board.

Dependency-light and safe by default: this command only reads repository state
and reports coordination conflicts. It does not mutate tasks, Git or the board.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from collections import Counter

ACTIVE = {"RUNNING"}
KNOWN = {"READY", "PLANNED", "RUNNING", "VERIFYING", "STANDBY", "BLOCKED", "DONE", "CANCELLED"}
LIMITS = {"github_actions_runner": 1, "heavy_gpu": 1, "git_writer": 1}

def git_root(start: pathlib.Path) -> pathlib.Path:
    try:
        value = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=str(start),
            stderr=subprocess.STDOUT,
            text=True,
            timeout=5,
        ).strip()
        return pathlib.Path(value).resolve()
    except Exception:
        return start.resolve()

def load_board(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def validate(board: dict) -> list[str]:
    errors: list[str] = []
    lanes = board.get("active_lanes", [])
    if not isinstance(lanes, list):
        return ["active_lanes must be an array"]

    ids = [lane.get("lane_id") for lane in lanes]
    duplicates = [x for x, n in Counter(ids).items() if x and n > 1]
    if duplicates:
        errors.append(f"duplicate lane_id(s): {', '.join(sorted(duplicates))}")

    running = []
    for lane in lanes:
        lane_id = lane.get("lane_id") or "<missing>"
        state = lane.get("state")
        if state not in KNOWN:
            errors.append(f"{lane_id}: unknown state {state!r}")
        if state in ACTIVE:
            running.append(lane)
        if not isinstance(lane.get("dependencies", []), list):
            errors.append(f"{lane_id}: dependencies must be an array")
        if not isinstance(lane.get("read_set", []), list):
            errors.append(f"{lane_id}: read_set must be an array")
        if not isinstance(lane.get("write_set", []), list):
            errors.append(f"{lane_id}: write_set must be an array")
        if not isinstance(lane.get("resource_claims", {}), dict):
            errors.append(f"{lane_id}: resource_claims must be an object")

    # Exact-scope collision detection. Controller must additionally reason about
    # semantic/contract overlap that string comparison cannot detect.
    scope_owner: dict[str, str] = {}
    for lane in running:
        for scope in lane.get("write_set", []):
            if not scope or not isinstance(scope, str):
                continue
            if scope in scope_owner:
                errors.append(
                    f"write scope collision: {scope!r} claimed by "
                    f"{scope_owner[scope]} and {lane.get('lane_id')}"
                )
            else:
                scope_owner[scope] = lane.get("lane_id", "<missing>")

    totals = {name: 0 for name in LIMITS}
    for lane in running:
        claims = lane.get("resource_claims", {})
        for name in LIMITS:
            value = claims.get(name, 0)
            if not isinstance(value, int) or value < 0:
                errors.append(f"{lane.get('lane_id')}: invalid {name} claim {value!r}")
                continue
            totals[name] += value

    for name, limit in LIMITS.items():
        if totals[name] > limit:
            errors.append(f"resource semaphore exceeded: {name}={totals[name]} > {limit}")

    if board.get("canonical_writer") != "controller-only":
        errors.append("canonical_writer must remain 'controller-only'")

    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--board", default=".ai/workboard.json")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    root = git_root(pathlib.Path.cwd())
    board_path = root / args.board
    if not board_path.is_file():
        print(f"ERROR: missing workboard: {board_path}", file=sys.stderr)
        return 2

    try:
        board = load_board(board_path)
    except Exception as exc:
        print(f"ERROR: invalid workboard JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate(board)
    result = {
        "schema_version": "v1",
        "kind": "parallel-coordination-check",
        "workboard": str(board_path.relative_to(root)),
        "coordination_epoch": board.get("coordination_epoch"),
        "mode": board.get("mode"),
        "lane_count": len(board.get("active_lanes", [])),
        "running_lanes": [
            lane.get("lane_id")
            for lane in board.get("active_lanes", [])
            if lane.get("state") in ACTIVE
        ],
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "notes": [
            "Exact write-scope collisions are machine-checked.",
            "Semantic contract overlap still requires Controller review.",
            "This check does not execute any project task."
        ],
    }

    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['status']}: coordination_epoch={result['coordination_epoch']} lanes={result['lane_count']}")
        for error in errors:
            print(f"- {error}")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
