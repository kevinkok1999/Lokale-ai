# Implementation Plan

## Increment 1 — Foundation

This increment starts implementation on the `dev` branch.

Scope:
- pinned Python runtime dependencies;
- versioned shared contracts;
- first resource-admission controller;
- first control API health/capability surface;
- unit/integration tests;
- single-runner serialized CI workflow.

Explicitly not yet claimed:
- PostgreSQL job persistence;
- Redis Streams dispatch;
- Qdrant memory;
- node pairing;
- GPU telemetry;
- media engines;
- installers;
- production readiness.

## Next increments

2. Durable state + migrations + PostgreSQL repository layer  
3. Redis Streams dispatch + leases/reclaim/idempotency  
4. Node identity + secure pairing service  
5. RTX worker + telemetry + Ollama adapter  
6. Team OS / blackboard / event orchestration  
7. Qdrant memory + provenance  
8. Media adapter layer + checkpointed scene pipeline  
9. Control Center  
10. AI-Core and RTX installers  
11. Recovery, backups, chaos testing and signed release pipeline

Every increment must pass its tests before fan-in.
