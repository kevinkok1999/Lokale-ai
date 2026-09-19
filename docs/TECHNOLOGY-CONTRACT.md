# Technology Contract

This document fixes implementation boundaries before production coding. Exact package/image versions will be pinned at implementation kickoff and stored in lockfiles/digests.

## Control-plane service layer

Preferred service implementation:
- Python service processes
- FastAPI for HTTP/OpenAPI control APIs
- explicit application lifespan for startup/shutdown resource ownership
- long-running jobs are NOT executed as in-process web background tasks

Reason:
The API must remain responsive while durable jobs are owned by the scheduler/worker system.

## Durable job model

Source of truth:
- PostgreSQL stores jobs, states, dependencies, leases, attempts, receipts and approvals.

Dispatch / wake-up:
- Redis Streams consumer groups.

Required Redis semantics:
- producer appends work;
- worker consumes using a consumer group;
- successful work is acknowledged;
- unacknowledged work remains pending;
- abandoned messages can be reclaimed;
- handlers remain idempotent because queue delivery is at-least-once, not exactly-once.

Redis is never the sole durable business-state store.

## Vector / retrieval memory

Qdrant owns vector indexes and searchable payload metadata.

Backup contract:
- periodic Qdrant snapshots;
- snapshot checksum;
- off-node copy;
- restore verification;
- aliases/configuration are captured separately when required.

Authoritative provenance and user/project records remain in PostgreSQL.

## Contracts

All cross-service payloads use versioned typed schemas.

Minimum envelope:
- schema_version
- message_id
- correlation_id
- producer
- created_at
- payload
- trace_context

Breaking contract changes require a new schema version and compatibility test.

## Eventing

Internal events are append-oriented and idempotent.

Consumers:
- use correlation/idempotency keys;
- may safely process a duplicate;
- never assume exactly-once delivery.

## Control Center

The user-facing Control Center is a separate application from the orchestration core.

Rules:
- simple view first;
- advanced technical detail on demand;
- no raw secret display;
- no terminal required for normal operation;
- degraded state is visible;
- every important action shows status, evidence and rollback capability.

## Compute worker

RTX worker exposes only authenticated, whitelisted capabilities.

It is not a generic remote shell.

Examples:
- inference
- model inventory
- GPU telemetry
- media generation
- controlled render
- controlled test/build task

Every request:
- is authenticated;
- has Job ID;
- has timeout;
- has resource class;
- emits progress;
- is cancellable where supported;
- returns an execution receipt.

## Media engines

The orchestrator calls replaceable adapters:
- ImageEngine
- VideoEngine
- VoiceEngine
- AudioEngine
- EditingEngine
- RenderEngine

No product workflow depends directly on one specific model/vendor.

## Persistence rule

Local control-plane operation must not depend on Neon being available.

Neon remains:
- development/testing branch backend;
- optional cloud app backend;
- optional off-site recovery integration.

## Dependency rule

Stable releases:
- pin package versions;
- pin OCI images by immutable digest;
- generate lockfiles;
- generate SBOM;
- hash release artifacts.
