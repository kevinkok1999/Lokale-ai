# Acceptance criteria

## READY FOR CODEX IMPLEMENTATION

The repository has one canonical state, versioned required Phase 1 schemas, an executable next task, explicit architecture and security boundaries, and tests that can run without target hardware.

## First vertical slice

A harmless goal creates a persisted project/task/run; Master emits a DAG; Coder changes only an isolated workspace; Tester produces pass/fail evidence; Reviewer is independent; Git diff and artifact hashes are recorded; the report reaches a human approval boundary; compute loss pauses or queues without losing state.

## Stable/release later gates

Actual node detection, mutual authentication, inference, resource thresholds, offline operation, recovery, signed artifacts, SBOM, upgrade/rollback, backup restore and production health must pass on target machines before `PRODUCTION_VERIFIED`.
