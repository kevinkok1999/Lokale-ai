# Local AI OS

Status: **READY_FOR_CODEX_IMPLEMENTATION**

This repository is the canonical GitHub source for the Local AI OS pre-implementation handoff. It is not yet a finished AI product and is not production- or hardware-verified.

## Start here

Read in this order:

1. `AGENTS.md`
2. `.ai/project-state.yaml`
3. `docs/SOURCE_OF_TRUTH.md`
4. `docs/CODEX_HANDOFF.md`
5. relevant architecture, security, resource, test docs and ADRs

## Current next task

`T001` is **READY** and has **not been executed by this synchronization step**. Do not infer completion from the presence of schemas, scripts, tests or historical evidence files; follow the task state and Definition of Done in `.ai/tasks/T001.yaml`.

## Product direction

Local AI OS is a local-first AI operating system intended to coordinate a Master AI, bounded specialist agents, local models, tools, memory and multiple computers. Long-term extension points include ProjectForge, ToolForge, KnowledgeMesh, media production, website/app development, ZeroDeploy, AgentFactory, multi-user support, shadow evaluation and controlled self-improvement.

## Legacy documents

Older pre-coding freeze documents remain in `docs/` for history. Their status language is superseded by `.ai/project-state.yaml`, `docs/SOURCE_OF_TRUTH.md`, `docs/CODING_READY_REPORT.md` and `docs/CODEX_HANDOFF.md`. See `docs/LEGACY_PRECODING_DOCS.md`.

## Final project boundary

A working core or stable partial release is not the end state. Tasks and milestones can be DONE while the overall project remains non-final. The project can only become `FINAL_COMPLETE` after all required capabilities in `.ai/final-scope.yaml` and all gates in `docs/FINAL_COMPLETION_CRITERIA.md` have verified evidence and the user accepts the final system.

## Safety boundary

`READY_FOR_CODEX_IMPLEMENTATION` means the repository is ready for Codex to begin the implementation phase. It does **not** mean `HARDWARE_VERIFIED`, `STABLE_RELEASE` or `PRODUCTION_VERIFIED`.
