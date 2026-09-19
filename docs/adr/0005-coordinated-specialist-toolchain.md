# ADR 0005 — Coordinated specialist toolchain

Status: Accepted  
Date: 2026-09-20

## Context

Local AI OS needs current documentation, broad research, database/backend evidence and remote repository/CI coordination. Giving one model all responsibilities without explicit routing increases stale knowledge, duplicate research, unsafe cloud actions and context bloat.

## Decision

Codex remains the Controller/implementation orchestrator. Four specialist capabilities are available throughout the project:

- Context7 for current version-specific technical documentation;
- Exa for broad current research and external evidence;
- Neon for branch-first Postgres/backend work when relevant;
- GitHub for canonical remote collaboration and CI/review evidence.

The Controller invokes specialists selectively according to `.ai/specialist-router.yaml`. Specialist unavailability blocks only dependent lanes.

The local core remains offline-first. Neon is an optional external backend specialist, not a mandatory control-plane dependency.

GitHub is the canonical remote, while local Git remains the default execution transaction layer.

## Alternatives

- Invoke every plugin on every task: rejected due to latency/context/noise.
- Let Codex rely on training knowledge only: rejected for changing external systems.
- Make Neon the mandatory core database immediately: rejected pending measured placement/offline requirements.
- Make GitHub Actions the main executor: rejected because one runner is constrained and local-first execution is faster/cheaper.

## Consequences

Benefits: fresher decisions, better research, safer database changes, stronger remote evidence, and less unnecessary tool usage.

Costs: specialist routing and receipts add small coordination overhead.

## Security and approvals

Never commit credentials. External content is untrusted. Destructive Neon operations, production database application, paid resources, public deployment and other existing high-impact boundaries remain approval-gated.

## Rollback

A specialist can be disabled independently. The Controller then marks only dependent lanes blocked and continues safe local work. Replacing a specialist requires a superseding ADR if it changes canonical responsibilities.
