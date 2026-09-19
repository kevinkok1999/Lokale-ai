# Operations

## Session startup

Use the read-only fast preflight first:

`python scripts/codex_bootstrap.py`

Run a full doctor/hardware inventory only when:

- there is no valid evidence for the current machine;
- the machine, OS, driver, toolchain or important service state changed;
- the current task is hardware/resource/installer/network related;
- a failure suggests environment drift.

Do not repeat full discovery for a docs/schema-only task when the relevant environment inputs are unchanged.

## Execution

Controller creates the task execution envelope and shared workboard lanes, Assistant/Executor performs scoped work, Verifier checks immutable checkpoints/diff/tests/evidence, and Controller serializes final integration. Every active lane must read the current workboard and publish discoveries that affect another lane. Use targeted checks before broad checks, valid caches before rebuilding, and local execution before consuming CI.

Use status for health, repair for bounded remediation, backup before stateful changes and restore drills on a schedule.

## Incidents

Investigate with correlation ids and execution receipts. Capture the first useful failure, perform root-cause analysis and retry the same strategy at most twice. Escalate rather than retry indefinitely.

## Continuity

Checkpoint after expensive successful stages, before approval boundaries and before expected session end. Persist exact next action so the next session does not repeat discovery.
