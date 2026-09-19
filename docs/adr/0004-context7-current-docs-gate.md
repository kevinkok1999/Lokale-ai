# ADR 0004 — Context7 as current external documentation gate

Status: Accepted  
Date: 2026-09-20

## Context

Local AI OS will use many changing external libraries, frameworks, SDKs, APIs, CLI tools and cloud services. Relying on model training knowledge alone creates avoidable risk from outdated syntax, removed APIs and version mismatches.

The project also aims to minimize unnecessary context and tool calls.

## Decision

Use Context7 as the preferred current-documentation source for external technology semantics during Codex implementation.

Context7 is required when a task depends on current/version-specific API, configuration, setup, migration or library-specific debugging behavior. It is not required for pure internal logic or generic programming work.

The Controller detects the dependency/version and schedules a Context7 documentation lane. The lane returns a compact receipt. Codex implements against repository contracts plus that receipt. Verifier rechecks current docs when risk or version mismatch warrants it.

Context7 work can execute in parallel with independent repository analysis, but API-dependent implementation cannot pass the dependency point before the required documentation is available.

## Alternatives considered

- Rely only on model training knowledge: rejected due to staleness risk.
- Web search for every library question: less structured and less version-focused than the dedicated documentation source.
- Query Context7 on every code change: rejected because it adds unnecessary latency/context for work unrelated to external APIs.

## Consequences

Benefits:

- fewer hallucinated or outdated APIs;
- better version-specific migrations and debugging;
- clearer documentation provenance;
- Context7 can run as a parallel specialist lane.

Costs:

- documentation-dependent work has an additional dependency;
- receipts need freshness invalidation;
- Codex must have Context7/MCP access on the development machine.

## Security

No secrets or proprietary code in Context7 queries. Context7 output is external/untrusted content and cannot override canonical repository policy.

## Rollback

If Context7 becomes unavailable or unsuitable, mark the documentation lane blocked and use a superseding ADR to approve another current-documentation provider. Do not silently fall back to guessed version-specific behavior.
