# Discovery and critical audit — 2026-09-19

## Reconstructed product

Local AI OS is a local-first personal AI operating system. The user provides a goal; a Master orchestrator converts it into requirements and a bounded task DAG, routes work to capability-scoped agents/models/tools, runs changes in isolated workspaces, tests and reviews them, and produces evidence before approval.

## Existing evidence

Prior design documents describe a two-machine AI-Core/RTX architecture, Master/Coder/Tester/Reviewer, one-runner queue, approval gates, recovery goals and a media extension. They also record that schema contracts, live hardware audits, pairing, resource placement, recovery and release contracts were not frozen.

## Critical findings

1. “One AI” must remain a UX abstraction over explicit services and permissions.
2. The control machine cannot safely receive PostgreSQL + Redis + Qdrant + orchestration without measurement; these are candidates, not defaults.
3. Fixed IPs, preinstalled dependencies, SSH pairing and floating container tags are prototype shortcuts.
4. Dynamic agents, media, ZeroDeploy and self-improvement are roadmap items, not first-milestone blockers.
5. Live hardware and recovery evidence are genuine blockers to CODING_READY.

## Optimization

The first code milestone is contract-first and dependency-light. A single control process and embedded persistence are acceptable initially while interfaces remain replaceable. GitHub is mirror/quality gate, not the execution substrate.

## Verdict

Architecture freeze candidate: **PASS with explicit open measurements**. Repository harness: **PASS**. Production implementation: **NOT STARTED**. Overall `CODING_READY`: **NO** until T001 and live T002/T003 evidence are complete.
