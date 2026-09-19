# Execution efficiency — Local AI OS

## Goal

Optimize for **verified throughput**: the most correct, reviewable progress per unit of time, context, runner capacity, CPU/RAM/VRAM and human attention.

The fastest workflow is not the one that skips tests. It is the one that avoids rereading, duplicate work, unnecessary agents, unnecessary services, repeated failed approaches and expensive checks before cheap checks have passed.

Machine-readable policy: `.ai/execution-policy.yaml`.

## Controller → Assistant/Executor → Verifier

Each task uses three logical passes.

**Controller pass** creates a compact Task Execution Envelope: task, objective, dependencies, risk/approval class, relevant files, outputs, tests, resource class, cache inputs, evidence and stop conditions. The Controller also checks whether another task on the critical path is already complete or blocked.

**Assistant/Executor pass** makes the smallest coherent implementation, using existing contracts and abstractions before introducing dependencies. Failures are captured once, root-caused, fixed narrowly and retested.

**Verifier pass** reviews the final diff and evidence, checks for secrets/regressions/policy drift, and runs the next required test tier. High-impact changes still require independent review/approval according to repository policy.

These are logical roles, not a requirement to spawn three expensive agents for every tiny edit.

## Fast session startup

Run:

`python scripts/codex_bootstrap.py`

The command performs a dependency-light, read-only repository preflight and reports branch, HEAD, remote, dirty state, canonical-file presence, current next task and a canonical fingerprint.

Then load only the minimum canonical set:

1. `AGENTS.md`
2. `.ai/project-state.yaml`
3. `docs/SOURCE_OF_TRUTH.md`
4. `.ai/execution-policy.yaml`
5. `docs/CODEX_HANDOFF.md`
6. current `.ai/tasks/<next_task>.yaml`

Use progressive disclosure after that. Read architecture/security/resource/test/subsystem docs and ADRs only when the current task or gate requires them. Load full final-scope/completion material at milestone/final-gate decisions rather than repeatedly injecting all of it into every implementation step.

## Shared team awareness

Parallel speed is coordinated through `.ai/coordination-policy.yaml` and `.ai/workboard.json`. The Controller partitions work into non-conflicting lanes and publishes dependencies, read/write scopes and resource claims. Every lane reads the current board before starting and reports cross-lane discoveries. Workers return receipts; the Controller serializes canonical workboard/project-state integration.

Verification can run against an immutable checkpoint while the implementation team works on a different non-conflicting lane. If the verified behavior changes before integration, that receipt must be revalidated.

## Scheduling and parallelism

A blocked task must not freeze unrelated unblocked work.

Default scheduling priority:

1. explicit user priority;
2. highest-priority unblocked task on the critical path;
3. release/security blocker;
4. highest-value independent unblocked task;
5. cleanup/optimization.

Only one process/agent writes the same Git repository at a time unless changes are isolated in separate worktrees with a controlled merge plan. Read-only research, independent analysis and non-conflicting isolated tests may run in parallel when resource budgets allow.

The environment currently has one GitHub Actions runner available to this project, so runner-consuming CI is serialized. Heavy GPU work also starts at one concurrent job until measured evidence supports more.

## Test ladder

Use a fail-fast ladder:

- **Tier 0:** schema/config/format/lint/type/static checks.
- **Tier 1:** targeted unit tests and negative fixtures for changed code.
- **Tier 2:** contracts and component tests.
- **Tier 3:** relevant integration tests.
- **Tier 4:** E2E, hardware, chaos/recovery, installer, release and production gates.

Do not run expensive Tier 4 work when Tier 0/1 for the same change already fails. Do not omit a later tier when the task's Definition of Done requires it.

## Cache and incremental-work rules

Reuse dependency/build/model caches and previously verified unchanged artifacts when their inputs and environment fingerprint still match.

Invalidate evidence when the thing it proves changed. Examples:

- dependency or security-policy change → security evidence must be refreshed;
- artifact change → release/production evidence must be refreshed;
- machine/driver/runtime change → hardware evidence must be refreshed;
- contract/schema change → affected contract consumers must be revalidated.

Never call stale evidence “fresh” to save time.

## Failure handling

One failure should produce evidence, not panic.

Use:

CAPTURE → CLASSIFY → ROOT CAUSE → TARGETED FIX → RETEST → REGRESSION CHECK.

The same strategy gets at most two attempts by default. After that, change the hypothesis/approach instead of looping. Escalate only at a real human/security/resource/credential/hardware boundary.

## Git and CI economy

Prefer local execution. Use GitHub Actions for independent evidence, platform-specific validation, release gates or cases that cannot reasonably be reproduced locally.

Before occupying the single runner, local relevant checks should normally be green. Avoid workflow churn that repeatedly queues equivalent runs.

Create small coherent commits at verified checkpoints, not a commit for every microstep. Preserve unrelated working-tree changes.

## Context economy

Do not continuously reread every architecture document.

Keep the current task's context focused on:

- task file;
- files being changed;
- directly referenced contracts;
- directly relevant ADRs;
- required test/operation docs;
- current state/evidence.

Expand context only when a symbol, dependency, architecture boundary or failure requires it. Historical/superseded docs are opt-in context, not startup context.

## Session continuity

Before a real session boundary, persist the exact state needed to resume:

- completed work;
- evidence;
- current task status;
- blocker, if any;
- exact next action;
- relevant commit/hash.

Do not repeat a discovery/review step in the next session if its inputs are unchanged and evidence remains valid.

## Optimization guardrails

Optimization must never:

- lower the evidence bar;
- skip required approvals;
- create hidden architecture drift;
- convert an unverified claim into a verified one;
- oversubscribe the CONTROL or COMPUTE node;
- introduce a second source of truth;
- silently reduce final scope.

Measure first, optimize second.
