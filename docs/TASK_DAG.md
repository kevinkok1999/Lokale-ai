# Task DAG

A task has id, title, priority, dependencies, status, owner capability, risk, inputs, expected output, tests, acceptance criteria, evidence, blocker and next action.

## Scheduling semantics

The scheduler is work-conserving but dependency-safe:

1. explicit user priority;
2. highest-priority unblocked task on the critical path;
3. release/security blockers;
4. highest-value independent unblocked work;
5. cleanup/optimization.

A blocked task is not a global project blocker unless every path to useful work depends on it.

Independent read-only work may run in parallel. Code-writing work may parallelize only in isolated worktrees with a controlled merge plan. There is one Git writer per repository by default.

The project currently assumes one GitHub Actions runner slot and one heavy GPU job until measurements justify more.

## Task Execution Envelope

Before implementation, Controller records or derives:

- objective and acceptance criteria;
- dependencies/blockers;
- approval/risk class;
- relevant files/contracts/ADRs;
- expected outputs;
- test tiers;
- resource/node class;
- cache invalidation inputs;
- evidence target;
- stop conditions.

Do not expand context or infrastructure beyond that envelope unless evidence shows it is needed.

## Recovery

Leases, timeouts, idempotency keys, checkpoints and bounded retries make recovery deterministic. The same failed strategy is attempted at most twice by default before root-cause assumptions are revised.

See `.ai/execution-policy.yaml`.
