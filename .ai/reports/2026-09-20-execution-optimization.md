# Execution optimization review — 2026-09-20

## Review method

The process was reviewed in three passes:

1. **Controller pass:** canonical precedence, dependency flow, final-completion policy, approval boundaries and failure modes.
2. **Assistant/Executor pass:** startup/context cost, task scheduling, caching, runner/GPU contention, test order, retries, Git/checkpoint overhead.
3. **Verifier pass:** checked that optimization does not weaken evidence, security, final scope, hardware truthfulness or single-runner constraints.

## Main bottlenecks found

- too much documentation could be loaded at every session instead of progressively;
- blocked hardware tasks could be mistaken for a global stop;
- no machine-readable execution policy existed;
- test order was correct conceptually but not explicit enough for fail-fast operation;
- cache/evidence invalidation rules were implicit;
- full doctor/discovery could be repeated unnecessarily;
- controller/executor/reviewer responsibilities were not separated for build-time Codex work;
- runner/GPU/Git-writer serialization was spread across docs rather than centralized.

## Implemented

- added `.ai/execution-policy.yaml`;
- added `docs/EXECUTION_EFFICIENCY.md`;
- added read-only `scripts/codex_bootstrap.py` and unit tests;
- changed startup to progressive disclosure;
- defined Controller → Assistant/Executor → Verifier;
- defined critical-path/work-conserving scheduling;
- made blocked-task-not-global-block explicit;
- defined one Git writer, one Actions runner slot and one initial heavy GPU slot;
- defined fail-fast test tiers and evidence/cache invalidation;
- defined bounded same-strategy retries;
- separated fast software path from hardware calibration lane;
- preserved T001 as READY and did not execute the Codex implementation phase.

## Verification boundary

This review updates repository policy/harness only. It does not prove the new bootstrap script on the user's brother's machine, does not execute T001, and does not upgrade hardware/release/production verification.


## Harness validation performed during policy update

The new bootstrap helper was checked outside the target hardware:

- Python syntax compilation: PASS.
- Simulated clean Git repository with all canonical startup files: PASS.
- Detected branch, HEAD, origin, project status and T001 correctly.
- Missing-required-file behavior remains explicit via non-zero exit.
- This is workspace-level validation only and is not CONTROL/COMPUTE hardware evidence.
