# Resilience and degraded-mode governance — 2026-09-20

## User requirement

GitHub, the single Actions runner, or any other chain component must not freeze the entire Local AI OS project when independent useful work can still continue.

## Implemented as canonical policy

- explicit failure domains;
- blocked-lane-not-blocked-project invariant;
- GitHub local-first degraded mode;
- remote operation queue contract;
- single-runner outage behavior;
- optional GitHub coding-worker failover to Codex/local executor;
- plugin-specific outage isolation;
- internet and COMPUTE degraded-mode behavior;
- future CONTROL recovery target;
- evidence rules that keep remote claims PENDING instead of fabricating PASS;
- static `scripts/resilience_check.py`.

## Important implementation boundary

This commit establishes governance, state contracts and validation. It does not claim that the durable remote queue or full CONTROL/COMPUTE failover runtime is already built. Those capabilities remain implementation work and must be evidenced later.

T001 remains READY and is not executed by this governance update.
