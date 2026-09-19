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
