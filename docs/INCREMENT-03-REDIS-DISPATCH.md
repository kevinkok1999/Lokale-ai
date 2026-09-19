# Increment 03 — Redis Streams Dispatch

Branch: `feature/redis-dispatch`

Purpose:
Redis is a wake-up/delivery layer only. PostgreSQL remains the authoritative job-state store.

Implemented:
- consumer-group bootstrap with idempotent BUSYGROUP handling;
- minimal routing-only stream messages;
- new-work consumption using consumer groups;
- explicit XACK support;
- stale pending-entry reclaim via XAUTOCLAIM;
- deleted PEL entry reporting for audit/dead-letter handling;
- byte/string normalization for Redis client configurations;
- unit tests using a deterministic fake Redis client.

Delivery guarantee:
At-least-once.

Therefore:
- handlers must remain idempotent;
- job state transitions remain guarded in PostgreSQL;
- a Redis message is never accepted as proof that a job completed.

Next:
wire dispatcher + PostgreSQL lease ownership into the scheduler worker loop.
