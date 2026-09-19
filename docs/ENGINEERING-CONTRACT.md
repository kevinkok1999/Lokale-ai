# Engineering Contract

## Repository rule

Production code may start only after the three pre-coding gates are marked PASS.

## Planned layout

/apps/control-center
/services/orchestrator
/services/scheduler
/services/health-manager
/services/worker-api
/services/media-orchestrator
/packages/contracts
/packages/events
/packages/policies
/packages/sdk
/packages/ui
/infra/ai-core
/infra/rtx-node
/infra/docker
/installers/ai-core
/installers/rtx-node
/tests/unit
/tests/integration
/tests/e2e
/tests/chaos
/tests/media
/docs/architecture
/docs/adr
/docs/runbooks
/docs/preservation

## Team workflow

Parallel preparation is allowed for:
- planning
- research
- code drafting
- static analysis
- test design
- review
- security analysis

Runner-required work is serialized through one central queue.

Every implementation task must define:
- Job ID
- goal contract
- dependencies
- isolated workspace/worktree
- expected outputs
- resource class
- timeout
- retry budget
- required tests
- artifact hash
- rollback point
- reviewer/verifier requirements

## Mandatory pipeline

Plan
→ Preflight
→ Isolated Work
→ Static Checks
→ Unit Tests
→ Integration Tests
→ Security Checks
→ Independent Review
→ Runner Build
→ Artifact
→ Verification
→ Preview
→ Approval when required
→ Stable Release

## No-self-approval

A high-impact change cannot have the same agent as sole:
- author;
- reviewer;
- verifier;
- approver.

## Merge/fan-in

Parallel outputs can merge only after:
- dependency check;
- conflict check;
- deterministic tests;
- independent review;
- evidence is attached.

## Release channels

dev → test → preview → stable

No direct development-to-stable promotion.

## Definition of Done

Code existing is not sufficient.

Done =
- build passes;
- required tests pass;
- security gate passes;
- independent review passes;
- recovery path exists;
- execution receipt exists;
- required verification is complete.

Any skipped required verification keeps the task explicitly unverified.
