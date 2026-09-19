# Multi-specialist toolchain update — 2026-09-20

## Connected capability checks

- Exa connection was exercised with current web research.
- Neon connection was exercised read-only by listing existing projects/branches; no database mutation was performed.
- GitHub connection and canonical repository access were verified.
- Existing Context7 collaboration remains active.

## External research sanity-check

Exa research on current autonomous coding-agent practice reinforced the existing architecture: explicit task scopes, isolated worktrees, controller/specialist/verifier separation, deterministic test gates, structured handoffs, bounded parallelism and sequential/deterministic integration are recurring high-signal patterns.

## Implemented

- `.ai/specialist-router.yaml`;
- `.ai/exa-policy.yaml`;
- `.ai/neon-policy.yaml`;
- `.ai/github-policy.yaml`;
- `docs/SPECIALIST_TOOLCHAIN.md`;
- ADR 0005;
- Exa, Neon and GitHub standby lanes in the shared workboard;
- execution-envelope routing fields;
- AGENTS/source-of-truth/handoff/efficiency/README integration;
- bootstrap awareness of the specialist router.

## Important boundary

"From beginning to end" means all specialists remain available throughout the lifecycle. It does not mean all are called on every task.

Neon remains an optional external backend specialist and does not become a mandatory dependency of the offline-first control plane.

No Neon write/destructive operation, production database change, paid resource creation, deployment, or T001 implementation was performed by this update.


## Canonical static validation

At content commit `1c39c8d65659a9258db1906d6ee68f296c2aec3f`:

- shared workboard parsed successfully;
- specialist lane IDs are unique;
- Context7, Exa, Neon and GitHub lanes are present;
- canonical writer remains Controller-only;
- T001 remains READY;
- no production/cloud mutation was introduced by this policy update.
