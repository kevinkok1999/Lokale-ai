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


## Canonical static validation

At content commit `0ce1fa21e9a1b40294700a1a7f466b7c848dc3d3`:

- blocked-lane-not-blocked-project rule is present;
- one Actions runner slot remains enforced;
- remote-sync queue contract is declared;
- GitHub outage keeps safe local work running;
- GitHub coding assistance is optional capacity, not a singleton dependency;
- automatic force-push recovery is forbidden;
- specialist router GitHub/Canva roles are structurally corrected;
- T001 remains READY and unexecuted.

This is governance validation. Durable outage recovery runtime still requires implementation and later E2E/failure testing.
