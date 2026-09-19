# Coordinated parallel execution review — 2026-09-20

## Goal

Enable parallel work while preserving one-team awareness, deterministic integration and the project's single-runner/GPU/resource constraints.

## Controller review

Checked dependency safety, canonical state ownership, conflicting write sets, stale-base risk, approval boundaries and global-vs-lane-local blockers.

## Assistant/Executor review

Optimized for useful concurrency: read-only research, static analysis, immutable-checkpoint tests and disjoint isolated worktrees can overlap. Overlapping writes, canonical state, main integration, runner use and heavy GPU work remain serialized.

## Verifier review

Added immutable-checkpoint verification, per-lane receipts, stale-base revalidation, targeted post-merge regression and cross-lane discovery propagation.

## Implemented

- machine-readable `.ai/coordination-policy.yaml`;
- shared `.ai/workboard.json`;
- `docs/PARALLEL_EXECUTION.md`;
- bootstrap awareness of coordination files;
- explicit shared-blackboard/receipt rules in AGENTS, DAG, operations and handoff;
- controller-only canonical coordination writer;
- lane-local blocker semantics;
- deterministic integration and resource semaphores.

T001 remains READY and was not executed by this optimization change.


## Coordination validator

Added `scripts/coordination_check.py` with dependency-light checks for duplicate lanes, exact running write-scope collisions, resource semaphore over-allocation and canonical-writer drift. Added harness unit tests. Bootstrap now exposes workboard epoch/mode/lane summaries directly so a new Codex session sees team state without rereading the full board first.


## Static canonical validation

Connector-side validation at content commit `94e2386cd850d89b92a7b814dfe05e43f368881d` confirmed:

- shared workboard JSON parses;
- lane IDs are unique;
- current RUNNING-lane resource claims do not exceed configured semaphores;
- canonical workboard writer remains `controller-only`;
- T001 is READY, T002 is BLOCKED on machine access, verifier lane is STANDBY.

The Python coordination/bootstrap harness still needs to be executed in the actual Codex/local environment before its runtime result is treated as local execution evidence.
