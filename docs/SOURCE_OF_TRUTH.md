# Canonical source-of-truth

The canonical remote source for Local AI OS is the `main` branch of `kevinkok1999/Lokale-ai`. A fresh clone of that branch is the supported handoff starting point for Codex.

Read in this order:

1. `AGENTS.md`
2. `.ai/project-state.yaml`
3. this file
4. `docs/CODEX_HANDOFF.md`
5. current architecture/security/resource/test docs and relevant ADRs

Authoritative artifacts:

- product identity: `docs/PRODUCT_CONSTITUTION.md`
- current phase/tasks/blockers: `.ai/project-state.yaml` and `.ai/tasks/`
- contracts: `.ai/schemas/`
- decisions: `docs/adr/`
- implementation sequence: `docs/IMPLEMENTATION_BACKLOG.md`
- Codex continuation: `docs/CODEX_HANDOFF.md`
- evidence: `.ai/evidence/` and `.ai/reports/`

`last_verified_commit` in `.ai/project-state.yaml` points to the latest fully verified content commit. The repository HEAD may be one later state/receipt commit so the state file does not need to refer to its own commit hash.

The Work-to-GitHub synchronization was verified on 2026-09-20. The earlier ZIP/starter copies and the legacy pre-coding documents listed in `docs/LEGACY_PRECODING_DOCS.md` are not authoritative for current status.
