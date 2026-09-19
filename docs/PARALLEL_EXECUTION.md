# Parallel team coordination

## Objective

Local AI OS may work in parallel, but it must behave like one coordinated engineering team rather than several independent agents guessing what the others are doing.

The canonical machine-readable rules are in `.ai/coordination-policy.yaml`. Current shared coordination state is `.ai/workboard.json`.

## Shared-awareness protocol

Before a parallel lane starts, it reads the current workboard. The Controller publishes:

- coordination epoch and base commit;
- lane objective and task;
- dependencies;
- read scope and exclusive write scope;
- resource claims;
- expected checkpoint/evidence;
- integration order.

A worker does not silently expand its assignment. If it discovers something that changes another lane's assumptions, it reports the discovery to the Controller. The Controller updates the shared plan before integration.

Workers do not all edit the workboard at once. The Controller is the serialized canonical coordination writer. This avoids turning the blackboard itself into a race condition.

## Safe parallel lanes

Good parallel work includes:

- read-only research/analysis;
- static analysis on the same immutable commit;
- independent tests against a frozen checkpoint;
- isolated worktrees with disjoint write sets;
- documentation/evidence that does not overlap implementation files.

Work must be serialized when it touches the same files/contracts, canonical project state, main integration, the single GitHub Actions runner, heavy GPU capacity, destructive operations or privileged actions.

## Controller + Assistant + Verifier

**Controller** owns task partitioning, shared state, dependencies, duplicate prevention, resource semaphores and merge order.

**Assistant/Executor** owns a bounded implementation lane and returns a receipt rather than changing global coordination state on its own.

**Verifier** validates a frozen checkpoint/receipt independently. It can run in parallel with later non-conflicting work, but a verification result is stale if integration changes the behavior it covered.

## Per-lane receipt

Every completed lane reports:

- lane/task ID;
- base commit;
- objective;
- files read and changed;
- tests/checks;
- evidence;
- discoveries relevant to other lanes;
- blockers;
- residual risk;
- recommended next action.

A receipt from an old base must be rebased or revalidated before merge.

## Conflict prevention

Two active write sets may not overlap unless the Controller deliberately serializes or repartitions them.

A shared contract boundary counts as a conflict even when filenames differ if simultaneous changes could invalidate each other's assumptions.

If a lane becomes blocked, only that lane stops. Other safe unblocked lanes continue. A global stop occurs only when no safe useful lane remains or a true approval/security/resource conflict blocks everything.

## Resource coordination

Initial semaphores:

- GitHub Actions runner: 1;
- heavy GPU job: 1;
- main integrator: 1;
- canonical state/workboard writer: 1.

Concurrency can increase only after measurement proves headroom and recovery behavior.

## Integration

Controller integrates in dependency-topological, low-conflict order.

Before integration:

1. receipt complete;
2. base current or revalidated;
3. write scope respected;
4. required test tier passes;
5. secret/policy review passes;
6. merge conflicts and cross-lane assumptions resolved.

After integration, run targeted regression, update project state/workboard/evidence, and immediately schedule the next unblocked lanes.

This gives parallel speed without losing one-team awareness.
