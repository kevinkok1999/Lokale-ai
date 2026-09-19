# Agent architecture

## Product runtime roles

Phase 1 product roles are Master, Coder, Tester and Reviewer. Roles have explicit input/output contracts and capability-scoped tools. Delegation is bounded by max depth, count, runtime, retries and resource budgets. No agent can author, review and approve a high-impact change. Specialist agents and media workflows are later additions only when measured value exceeds coordination cost.

## Build-time Codex control loop

Repository implementation uses three logical roles:

- **Controller:** validates canonical state, task/dependencies, risk, context, resource budget and test plan.
- **Assistant/Executor:** performs the smallest coherent implementation and root-cause fixes.
- **Verifier:** reviews diff/evidence and applies the appropriate test/security gate.

These are logical execution phases and do not require three separate heavyweight model processes for every small task. Spawn independent reviewers/specialists only when risk or measurable value justifies coordination overhead.

One writer per repository is the default. Independent read-only work and controlled isolated worktrees may parallelize within resource budgets.

See `.ai/execution-policy.yaml`.
