# Canonical source-of-truth

The canonical technical truth is the checked-out Git repository at the commit named by `.ai/project-state.yaml`. Read in this order: `AGENTS.md`, `.ai/project-state.yaml`, this file, `docs/CODEX_HANDOFF.md`, then the architecture/security/resource/test docs and ADRs.

Authoritative artifacts:

- product identity: `docs/PRODUCT_CONSTITUTION.md`
- current phase/tasks/blockers: `.ai/project-state.yaml` and `.ai/tasks/`
- contracts: `.ai/schemas/`
- decisions: `docs/adr/`
- implementation sequence: `docs/IMPLEMENTATION_BACKLOG.md`
- Codex continuation: `docs/CODEX_HANDOFF.md`
- evidence: `.ai/evidence/` and `.ai/reports/`

The earlier starter ZIP and any copied historical status are superseded by this repository and are not part of the active source. Historical decisions remain in ADRs/reports. A remote GitHub mirror must be verified separately; this checkout is the canonical working repository until a matching remote commit is confirmed.
