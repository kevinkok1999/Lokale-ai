# Legacy pre-coding documents

The following documents are preserved for historical traceability but are **superseded for current status and execution order**:

- `docs/ACCEPTANCE-MATRIX.md`
- `docs/ARCHITECTURE-FREEZE.md`
- `docs/ENGINEERING-CONTRACT.md`
- `docs/FINAL-3X3-PRECODING-REVIEW.md`
- `docs/INSTALLER-FREEZE.md`
- `docs/MEDIA-CONTRACT.md`
- `docs/PRE-CODING-GATES.md`
- `docs/RESOURCE-CALIBRATION.md`
- `docs/SECURITY-PAIRING-THREAT-MODEL.md`
- `docs/TECHNOLOGY-CONTRACT.md`

They may still contain useful design history, but their old status labels such as `PRE-CODING FROZEN` or `IMPLEMENTATION READY` are not authoritative.

Current authority order:

1. `.ai/project-state.yaml`
2. `docs/SOURCE_OF_TRUTH.md`
3. `docs/CODEX_HANDOFF.md`
4. `docs/CODING_READY_REPORT.md`
5. current architecture/security/resource/test docs and ADRs

Historical documents must not override the current project state.


## Non-blocking rule

Legacy material is evidence/history only. It may inform a decision, but it cannot override or block a newer explicit canonical rule, accepted superseding ADR, current task state, final-scope requirement or completion policy. Preserve history; do not resurrect obsolete constraints.
