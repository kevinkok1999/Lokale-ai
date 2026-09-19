# Increment 02 — Durable State

Branch: `feature/durable-state`

This increment is prepared in parallel while the foundation CI occupies the single runner.

Implemented:
- explicit job state machine;
- guarded state transitions;
- PostgreSQL job repository interface/implementation;
- optimistic state transition check to detect concurrent updates;
- first local PostgreSQL migration for durable jobs/dependencies;
- unit tests proving verification stages cannot be skipped.

Merge rule:
This branch does not fan in to `dev` until the foundation increment passes its runner gate and this increment later passes its own verification.
