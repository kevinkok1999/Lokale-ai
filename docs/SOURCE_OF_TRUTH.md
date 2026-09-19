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


## Precedence and supersession

When two repository sources disagree, use this precedence for current execution:

1. explicit user-approved current policy recorded in the canonical repository;
2. `.ai/project-state.yaml` for current phase/task/blocker status;
3. `.ai/final-scope.yaml` and `docs/FINAL_COMPLETION_CRITERIA.md` for project-level completion;
4. `docs/PRODUCT_CONSTITUTION.md` for required product identity/capabilities;
5. the newest Accepted/Superseding ADR that explicitly addresses the topic;
6. current non-legacy architecture/security/resource/test documentation;
7. historical/superseded material.

A newer accepted canonical decision may supersede an older one without deleting history. Old or explicitly superseded documents must never silently re-impose obsolete status, architecture, task order or completion rules.

If two active sources at the same precedence level conflict, create or update an ADR/source-of-truth record before implementing the conflicting part. Do not let unrelated work stall.

## Final project completion

Task or milestone DONE does not mean the Local AI OS is finished. Project-level `FINAL_COMPLETE` is governed only by `.ai/final-scope.yaml` and `docs/FINAL_COMPLETION_CRITERIA.md`.
