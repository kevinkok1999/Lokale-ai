# Project scorecard — baseline before 10/10 improvement

Scoring is evidence-based. Design score measures the quality of the documented design for this phase; verification score measures what is actually executed and evidenced. Weighted total uses 60% design and 40% verification because this repository is pre-implementation.

| Category | Design | Verification | Evidence / good | Missing, risk and required path to 10 |
|---|---:|---:|---|---|
| Product Vision Completeness | 8.5 | 4.0 | North Star and first vertical slice exist | Long-term capability map and media must be explicit; verify traceability |
| Architecture Quality | 8.0 | 3.5 | Control/compute separation, bounded agents | Durable execution and placement alternatives need decision; integration tests |
| Architecture Consistency | 6.5 | 2.5 | Core invariants documented | Prior states and candidate dependencies can drift; canonical commit + ADR |
| Repository / Source-of-Truth | 6.0 | 2.0 | Harness files and Git history exist | Temporary files, starter copy, no remote sync proof; clean canonical repo |
| Codex Readiness | 7.0 | 3.0 | Handoff and first task exist | T001 is incomplete; exact commands and authoritative files need tightening |
| Task / Agent Architecture | 7.5 | 2.5 | Master/Coder/Tester/Reviewer and DAG | Run/agent contracts and receipts missing; contract tests |
| Cross-Language Contracts | 4.5 | 1.5 | Four JSON Schemas exist | Run/Artifact/Approval/Agent/Node/ResourceState/Model/Tool absent |
| Data / Memory Architecture | 6.5 | 2.0 | Relational canonical + optional retrieval | No schemas or migration/recovery evidence |
| Model / Compute Strategy | 6.5 | 1.5 | Provider-neutral intent and routing rules | No measured model registry/benchmark |
| Hardware / Resource Realism | 6.0 | 1.0 | Conservative placement intent | No live node measurements or calibration |
| Security | 7.5 | 2.5 | Deny-by-default, approvals, untrusted input | Key lifecycle, pairing, signing and supply chain need executable controls |
| Reliability / Self-Healing | 7.0 | 1.5 | Retry, rollback, recovery goals | No durable workflow/recovery implementation or chaos evidence |
| Offline-First Capability | 7.0 | 2.0 | Control-plane continuity is explicit | Offline behavior unexecuted |
| Observability / Auditability | 7.0 | 2.0 | Correlation fields and redaction rules | No telemetry implementation |
| Testing / Evidence | 5.5 | 2.0 | Acceptance categories listed | No schema harness, contract fixtures or recovery results |
| Installer / Upgrade / Recovery UX | 6.5 | 1.5 | Product path and prototype gaps documented | No implementation, signing or rollback evidence |
| Git / CI / One-Runner Efficiency | 7.5 | 3.0 | Runner capacity-one policy | Canonical remote synchronization unverified |
| Maintainability | 7.0 | 3.0 | Compact docs and ADR convention | Generated contracts and dependency policy absent |
| Extensibility / Future Readiness | 8.0 | 3.0 | Extension points and roadmap | Capability contracts and compatibility policy need formalization |
| Overall System Engineering Quality | 6.9 | 2.2 | Strong pre-coding foundation | Evidence and canonical synchronization are the limiting factors |

**Baseline weighted total: 5.0/10** (design 6.9 × 0.6 + verification 2.2 × 0.4 = 5.02). This is a repository-foundation score, not a product score.

10/10 requires passing the applicable design, implementation, contract, hardware and release gates in `docs/TEST_STRATEGY.md` and `docs/ACCEPTANCE_CRITERIA.md`; documentation alone cannot produce 10.

# After-improvement scorecard

Scores below are after the repository/doc/schema improvements from the 2026-09-19 Work improvement run. They measure this pre-implementation phase; no hardware or production claim is implied.

| Category | Before | After design | After verification | Evidence / remaining gap |
|---|---:|---:|---:|---|
| Product Vision Completeness | 8.5 | 9.5 | 4.5 | Full capability constitution and media map; future implementations pending |
| Architecture Quality | 8.0 | 8.8 | 4.0 | Boundaries and technology trade-offs recorded; no running slice |
| Architecture Consistency | 6.5 | 8.8 | 4.0 | Source-of-truth policy, ADRs and gates |
| Repository / Source-of-Truth | 6.0 | 9.0 | 6.0 | Clean canonical files and history; remote parity was pending at scoring time |
| Codex Readiness | 7.0 | 9.2 | 6.0 | Executable T001 definition and handoff; Codex implementation not started |
| Task / Agent Architecture | 7.5 | 8.5 | 3.0 | Bounded first roles and future factory; runtime absent |
| Cross-Language Contracts | 4.5 | 9.0 | 6.0 | 12 closed schemas and tests; generated multi-language consumer pending |
| Data / Memory Architecture | 6.5 | 7.5 | 2.5 | Clear canonical/projection rule; persistence unimplemented |
| Model / Compute Strategy | 6.5 | 8.0 | 2.0 | Provider-neutral registry and benchmark requirement; no measured models |
| Hardware / Resource Realism | 6.0 | 8.0 | 1.5 | Calibration policy and reservations; live doctor absent |
| Security | 7.5 | 8.7 | 3.0 | Threats, approvals, signing direction; key/pairing implementation absent |
| Reliability / Self-Healing | 7.0 | 8.2 | 2.0 | Failure matrix and bounded recovery; no chaos evidence |
| Offline-First Capability | 7.0 | 8.0 | 2.0 | Policy is explicit; offline execution unverified |
| Observability / Auditability | 7.0 | 8.2 | 2.5 | Correlation model and OTel direction; telemetry absent |
| Testing / Evidence | 5.5 | 8.5 | 6.0 | Work-side schema tests/evidence; broader pyramid pending |
| Installer / Upgrade / Recovery UX | 6.5 | 8.2 | 2.0 | Product path and release gates; installer absent |
| Git / CI / One-Runner Efficiency | 7.5 | 8.8 | 4.0 | Capacity-one policy; remote sync was pending at scoring time |
| Maintainability | 7.0 | 8.8 | 5.0 | ADR/docs/schema convention; implementation maintenance pending |
| Extensibility / Future Readiness | 8.0 | 9.2 | 3.5 | Capability map and adapters; extension contracts not all implemented |
| Overall System Engineering Quality | 6.9 | 8.7 | 3.8 | Strong foundation; implementation and hardware intentionally pending |

**After weighted total recorded by Work: 6.7/10.**

## GitHub synchronization addendum — 2026-09-20

The remote-parity gap noted above is now resolved for the canonical Work handoff: the synchronized content is present on `kevinkok1999/Lokale-ai` `main` through commit `5377e75d9ca0f5dbe1c78bf4b102cde322e330d5`. T001 was not executed by this sync. No new overall numeric score is assigned here because synchronization improves source-of-truth verification but adds no implementation or hardware evidence.
