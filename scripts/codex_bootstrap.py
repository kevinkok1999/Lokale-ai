#!/usr/bin/env python3
"""Fast, dependency-light Codex bootstrap for Local AI OS.

Read-only by default. It does not execute product tasks, mutate Git, or upgrade
verification state. Its job is to make session startup deterministic and cheap.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import platform
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

REQUIRED = [
    "AGENTS.md",
    ".ai/project-state.yaml",
    ".ai/execution-policy.yaml",
    "docs/SOURCE_OF_TRUTH.md",
    "docs/CODEX_HANDOFF.md",
]

def run(cmd: list[str], cwd: pathlib.Path, timeout: int = 5) -> str | None:
    try:
        return subprocess.check_output(
            cmd, cwd=str(cwd), stderr=subprocess.STDOUT, text=True, timeout=timeout
        ).strip()
    except Exception:
        return None

def git_root(start: pathlib.Path) -> pathlib.Path:
    value = run(["git", "rev-parse", "--show-toplevel"], start)
    return pathlib.Path(value).resolve() if value else start.resolve()

def scalar(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?([^\n\"']+)", text)
    return match.group(1).strip() if match else None

def fingerprint(root: pathlib.Path, paths: list[str]) -> str:
    digest = hashlib.sha256()
    for rel in paths:
        path = root / rel
        digest.update(rel.encode())
        if path.is_file():
            digest.update(path.read_bytes())
    return digest.hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", help="Optional JSON evidence/output path")
    args = parser.parse_args()

    root = git_root(pathlib.Path.cwd())
    state_path = root / ".ai/project-state.yaml"
    state_text = state_path.read_text(encoding="utf-8") if state_path.is_file() else ""

    next_task = scalar(state_text, "next_task")
    task_rel = f".ai/tasks/{next_task}.yaml" if next_task else None
    missing = [rel for rel in REQUIRED if not (root / rel).is_file()]
    if task_rel and not (root / task_rel).is_file():
        missing.append(task_rel)

    branch = run(["git", "branch", "--show-current"], root)
    head = run(["git", "rev-parse", "HEAD"], root)
    remote = run(["git", "remote", "get-url", "origin"], root)
    porcelain = run(["git", "status", "--porcelain"], root)
    changed = [line for line in (porcelain or "").splitlines() if line.strip()]

    canonical = REQUIRED + ([task_rel] if task_rel else [])
    result = {
        "schema_version": "v1",
        "kind": "codex-fast-preflight",
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "branch": branch,
        "head": head,
        "origin": remote,
        "working_tree_dirty": bool(changed),
        "changed_entry_count": len(changed),
        "project_status": scalar(state_text, "status"),
        "next_task": next_task,
        "next_task_file": task_rel,
        "missing_required_files": missing,
        "canonical_fingerprint_sha256": fingerprint(root, canonical),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "tools": {
            name: shutil.which(name)
            for name in ("git", "python", "python3", "node", "npm", "docker")
        },
        "recommended_initial_read_set": canonical,
        "notes": [
            "Read-only fast preflight; not hardware verification.",
            "Use progressive disclosure after the initial read set.",
            "Do not infer task completion from existing evidence files.",
        ],
    }

    encoded = json.dumps(result, indent=2) + "\n"
    if args.write:
        out = (root / args.write).resolve() if not os.path.isabs(args.write) else pathlib.Path(args.write)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 2 if missing else 0

if __name__ == "__main__":
    raise SystemExit(main())
