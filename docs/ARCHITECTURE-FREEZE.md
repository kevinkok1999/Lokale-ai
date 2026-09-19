# Architecture Freeze

## Nodes

### AI-Core
Owns orchestration, state, policies, approvals, queues, memory, monitoring, recovery, backups and the Control Center.

### RTX Compute Node
Owns GPU inference, heavy model execution, image/video generation, media rendering, heavy local workers and telemetry.

### Neon
Complementary cloud/dev/recovery layer. It is never the only copy of critical offline control-plane state.

## Team Operating Model

Every meaningful task follows:

User Goal
→ Goal Contract
→ Executive Orchestrator
→ Dynamic Specialist Team
→ Dependency DAG
→ Parallel Fan-out
→ Resource Admission
→ Execution
→ Independent Critic
→ Independent Verifier
→ Fan-in
→ Acceptance Gate
→ Execution Receipt

Rules:
- parallel-by-default;
- one shared user goal;
- no self-approval for high-impact work;
- disagreement is resolved by evidence, not majority vote;
- specialists use least privilege;
- shared blackboard and explicit events coordinate teams;
- missing verification must remain visible.

## Core State

Local control-plane data:
- PostgreSQL: durable structured state
- Redis: queue and short-lived coordination
- Qdrant: retrieval/vector memory

## Scheduling

Scarce resources are centrally admitted:
- one physical GitHub runner slot;
- one heavy GPU slot by default;
- CPU/light work may run concurrently within measured limits;
- backpressure is mandatory;
- jobs use leases, retry budgets and checkpoints.

## Reliability

Required patterns:
- health probes
- heartbeats
- circuit breakers
- exponential/progressive backoff
- idempotent operations
- graceful degradation
- automatic rollback
- last-known-good release
- backup and restore verification
- chaos testing
- incident postmortems

## Media Production

Media is a first-class workload:
Brief → Research → Script → Fact-check → Storyboard → Shot list → Parallel Assets → Edit → Subtitles → QA → Preview → Final Render → Human Publish Approval.

Image, video, voice, audio and editing engines are replaceable adapters.
