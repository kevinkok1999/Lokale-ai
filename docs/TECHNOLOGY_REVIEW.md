# Technology review — 2026-09-19

Research was checked against primary project documentation. NATS JetStream provides durable streams and replay; OpenTelemetry provides vendor-neutral traces, metrics, logs and context propagation; Sigstore/Cosign supports signing and verification of files, containers and SBOMs; Temporal provides durable workflows with persisted state, retries, timers and task queues. Sources: https://docs.nats.io/ , https://opentelemetry.io/ , https://docs.sigstore.dev/ , https://docs.temporal.io/ .

| Decision area | Current | Alternative | Decision for this phase |
|---|---|---|---|
| Durable workflow | Custom leases/checkpoints | Temporal | Keep an interface; do not deploy Temporal on 16 GB CONTROL before a measured need. A small local state machine is Phase 1. Re-evaluate when long-running workflows require replay. |
| Events/queue | Candidate Redis/NATS | NATS JetStream | Prefer a queue abstraction. NATS JetStream is a strong later fit for durable replay, but a second always-on service is not justified for the first vertical slice. |
| Telemetry | Structured logs intended | OpenTelemetry | Adopt OpenTelemetry semantic context at the interface boundary; backend remains replaceable. |
| Artifact signing | Design-only | Sigstore/Cosign or offline key | Require digest/SBOM/signature interfaces for stable releases. Choose keyless Sigstore when internet is available; support offline verification policy for air-gapped installs. |
| Contracts | JSON Schema | OpenAPI/AsyncAPI/Protobuf | JSON Schema is canonical Phase 1. Generate OpenAPI/AsyncAPI projections when HTTP/event implementations exist. |
| Persistence | Relational candidate | PostgreSQL | Start with the smallest durable store that meets Phase 1; PostgreSQL is the later multi-user canonical store after resource measurement. |
| Retrieval | Optional vector DB | Qdrant | Do not install until semantic retrieval has a measured use case; keep a permission-aware adapter. |
| Git/CI | GitHub mirror + one runner | Forgejo/local Git | Keep local Git transaction semantics now; evaluate Forgejo after vertical slice, not as a prerequisite. |

No choice is frozen merely because it is popular. A future ADR must include resource footprint, Windows/Linux behavior, offline behavior, migration and rollback.
