# Final architecture (freeze candidate)

Local AI OS is a local-first personal AI operating system with a durable control plane and optional compute nodes. The first vertical slice is intentionally small: Gateway → Master → isolated Coder → Tester → Reviewer → Git diff/report → approval.

## Boundaries

- **Control plane**: intent, policy, task state, DAG, approvals, audit, queue, health and artifact metadata. It must remain useful when compute or internet is unavailable.
- **Compute node**: authenticated worker for model inference and heavy jobs. It is replaceable and may be offline without losing state.
- **Workspace runner**: creates isolated branches/worktrees, executes bounded commands and emits evidence.
- **Model provider**: interface only; concrete runtimes are replaceable and selected by measured capability/resource data.
- **Persistence**: relational state first. Vector retrieval is optional and permission-aware.

PostgreSQL, Redis, Qdrant and NATS are candidates, not frozen dependencies. They may be introduced only after measured resource budgets and a Phase 1 need. A single-node SQLite/embedded queue is acceptable for the first vertical slice if it preserves contracts and recovery semantics.

## Frozen invariants

Deny by default, Git as transaction log, no self-approval for high-impact changes, bounded retries, idempotent commands, explicit evidence, and human approval for production, credentials, payments, deletion, public exposure or material host changes.

## Quality gate

Plan → isolated workspace → change → tests → security/static checks → independent review → evidence → approval boundary → commit/push. A written architecture is not implementation evidence.
