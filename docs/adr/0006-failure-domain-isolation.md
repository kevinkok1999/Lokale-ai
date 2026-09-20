# ADR 0006 — Failure-domain isolation and degraded-mode progress

Status: Accepted  
Date: 2026-09-20

## Context

Local AI OS depends on multiple optional or remote capabilities: GitHub, one GitHub Actions runner, coding assistants, Context7, Exa, Neon, Vercel, design plugins, network connectivity, and eventually separate CONTROL/COMPUTE nodes.

If any one of these becomes a global blocker, the project becomes fragile and autonomy decreases.

## Decision

Treat each external service, runner and node as an explicit failure domain.

A failure blocks only lanes that require that domain. The Controller recomputes runnable lanes and continues the highest-priority safe work.

GitHub remains the canonical remote, but local Git is the development transaction layer. During GitHub outage, coherent local commits and evidence may continue and remote operations are deferred. Remote-dependent verification remains PENDING until GitHub returns and reconciliation succeeds.

The single Actions runner serializes only runner-consuming work.

GitHub coding assistance is optional capacity and may be reassigned if unavailable.

Recovery must reconcile state before flushing queued remote operations. Automatic force-push or fabricated remote evidence is forbidden.

## Consequences

Benefits:

- fewer global stalls;
- better use of both local machines and plugin lanes;
- clearer outage behavior;
- no false CI/release claims;
- simpler root-cause isolation.

Costs:

- queues and receipts need durable state;
- stale-base reconciliation can require retesting;
- final remote gates may remain pending while implementation continues.

## Future implementation work

The policy is canonical governance now. Durable remote-operation queues, CONTROL persistence and full CONTROL/COMPUTE failover still require actual implementation and verification in later tasks.

## Rollback

A superseding ADR may change failover mechanisms, but it must preserve explicit failure-domain handling or document why a global dependency is justified.
