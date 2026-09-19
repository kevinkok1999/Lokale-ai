# Roadmap

This roadmap is cumulative. Completing an earlier phase does not end the project.

0. **Canonical harness and contracts** — schemas, source-of-truth, task/evidence model, doctor/preflight.
1. **Reliable AI engineering core** — Gateway + Master → Coder → Tester → Reviewer, isolated workspaces, Git receipts and approval boundary.
2. **Durable state and recovery** — projects/tasks/runs/artifacts/approvals, persistence, checkpoints, resume and rollback.
3. **Execution fabric** — DAG scheduling, queues/events, bounded retries, leases, backpressure and one-runner coordination.
4. **Security and observability** — identity, least privilege, audit, traces/metrics/logs, secret handling and policy enforcement.
5. **CONTROL + COMPUTE cluster** — secure discovery/pairing, authenticated workers, actual hardware/resource calibration, model runtime integration and compute-loss recovery.
6. **Installer lifecycle** — role detection, zero/low-config setup, repair, diagnostics, update, signed artifacts, SBOM, last-known-good rollback and uninstall.
7. **Memory and KnowledgeMesh** — structured/semantic/episodic/temporal/causal memory, provenance, permissions and project-aware retrieval.
8. **Model and resource intelligence** — model registry, benchmarks, routing, fallbacks, RAM/VRAM/CPU/disk admission and adaptive scheduling.
9. **ProjectForge + software/web/app factory** — idea → requirements → research → architecture → implementation → tests → preview → approved deployment → monitoring/maintenance.
10. **ToolForge + extensibility** — capability registry, plugins/MCP/tools, risk/permission schemas, adapters and versioned extension contracts.
11. **Media production system** — image, storyboard, video, voice, audio, editing, subtitles, provenance, checkpoint/resume, preview/final render and publish approval.
12. **Multi-user and shared projects** — accounts/RBAC, personal vs shared memory, project permissions and safe collaboration.
13. **AgentFactory and specialist teams** — bounded dynamic specialists, critic/verifier separation, conflict resolution and evidence-based fan-in.
14. **Self-healing and simulation** — health automation, bounded repair, incident records, digital-twin/chaos scenarios and recovery validation.
15. **Shadow evaluation and controlled self-improvement** — observe → propose → benchmark → shadow → review → approve/promote with rollback.
16. **Full-system integration and usability** — one coherent Master experience across coding, apps, websites, research, memory, media and operations.
17. **Final verification gate** — full E2E, hardware, offline, security, recovery, installer, upgrade/rollback, performance, benchmark and user-acceptance evidence.

The project may only become `FINAL_COMPLETE` after phase 17 satisfies `docs/FINAL_COMPLETION_CRITERIA.md`. A stable partial release is not the end of the roadmap.
