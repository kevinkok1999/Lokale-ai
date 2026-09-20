#!/usr/bin/env python3
"""Static validation for degraded-mode/failure-domain governance."""
from __future__ import annotations
import argparse
import json
import pathlib
import sys

ROOT=pathlib.Path(__file__).resolve().parents[1]

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", dest="as_json")
    args=parser.parse_args()

    required=[
        ROOT/".ai"/"resilience-policy.yaml",
        ROOT/".ai"/"github-policy.yaml",
        ROOT/".ai"/"plugin-team.yaml",
        ROOT/".ai"/"workboard.json",
        ROOT/"docs"/"DEGRADED_MODE_AND_FAILOVER.md",
    ]
    errors=[f"missing {p.relative_to(ROOT)}" for p in required if not p.is_file()]
    board={}
    if not errors:
        try:
            board=json.loads((ROOT/".ai"/"workboard.json").read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid workboard JSON: {exc}")

    if board:
        resilience=board.get("resilience",{})
        if resilience.get("project_rule")!="blocked_lane_is_not_blocked_project":
            errors.append("workboard resilience project rule missing")
        runner=board.get("runner_queue",{})
        if runner.get("slots")!=1:
            errors.append("runner_queue must keep exactly one slot")
        remote=board.get("remote_sync_queue")
        if not isinstance(remote,dict):
            errors.append("remote_sync_queue missing")
        elif remote.get("pending_operations") is None:
            errors.append("remote_sync_queue.pending_operations missing")

    texts={}
    for p in required[:3]:
        if p.is_file():
            texts[p.name]=p.read_text(encoding="utf-8")
    rp=texts.get("resilience-policy.yaml","")
    gp=texts.get("github-policy.yaml","")
    if "A blocked lane is not a blocked project." not in rp:
        errors.append("resilience core principle missing")
    if "github_unavailable_does_not_stop_safe_local_work: true" not in gp:
        errors.append("GitHub local-progress outage rule missing")
    if "no_force_push_as_automatic_recovery: true" not in rp:
        errors.append("automatic force-push recovery prohibition missing")

    result={
        "schema_version":"v1",
        "kind":"resilience-governance-check",
        "status":"PASS" if not errors else "FAIL",
        "errors":errors,
        "checks":{
            "lane_local_failure_isolation": "PASS" if "A blocked lane is not a blocked project." in rp else "FAIL",
            "single_runner_slot": "PASS" if board.get("runner_queue",{}).get("slots")==1 else "FAIL",
            "remote_sync_queue_declared": "PASS" if isinstance(board.get("remote_sync_queue"),dict) else "FAIL",
            "automatic_force_push_forbidden": "PASS" if "no_force_push_as_automatic_recovery: true" in rp else "FAIL",
        },
        "limitations":[
            "Static governance validation only.",
            "Does not prove GitHub outage recovery is implemented in runtime code.",
            "Does not prove CONTROL/COMPUTE failover.",
        ]
    }
    if args.as_json:
        print(json.dumps(result,indent=2))
    else:
        print(f"{result['status']}: resilience governance")
        for e in errors:
            print(f"- {e}")
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
