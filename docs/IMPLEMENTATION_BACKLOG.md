# Implementation backlog

## Fast software path

- T001 canonical schemas and validators (READY)
- T004 gateway/interface skeleton (depends T001)
- T005 isolated workspace and Git receipt (depends T004)
- T006 Master/Coder/Tester/Reviewer E2E (depends T005)
- T007 persistence and recovery (depends T006)
- T008 queue/events/resource governor (depends T007)

## Hardware calibration lane

- T002 live CONTROL/COMPUTE doctor evidence (BLOCKED on machine access)
- T003 measured resource placement matrix (depends T002)

T002/T003 should be executed as soon as target machines are available, but they do not freeze the fast software path when that path has no dependency on them.

## Join/release lane

- T009 installer prototype and acceptance suite (depends T003,T008)

After T009, continue through the cumulative product roadmap in `docs/ROADMAP.md`; T009 is not project completion.

Scheduling and concurrency are governed by `.ai/execution-policy.yaml`.
