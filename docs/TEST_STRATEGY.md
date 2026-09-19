# Test strategy and gates

## Gate classes

- **Architecture gate:** contracts, boundaries, failure semantics, resource assumptions and approvals documented.
- **Implementation gate:** schemas, unit tests, contract tests, static/security checks and deterministic scripts pass.
- **Hardware gate:** doctor, drivers, pairing, inference, pressure and reboot/offline tests pass on target nodes.
- **Release gate:** signed reproducible artifact, SBOM, upgrade/rollback and backup restore pass.
- **Production gate:** deployment approval, health SLOs, monitoring and operator runbook accepted.

## Pyramid

Schema validation → contract fixtures → unit → component → integration → E2E → hardware integration → chaos/recovery → security/supply-chain → installer/upgrade/offline. Later gates never pretend to be satisfied by earlier gates.

## First milestone tests

T001 runs `python3 scripts/validate_contracts.py` and checks closed, versioned schemas plus negative fixtures. T004–T006 add API contract tests, isolated-workspace tests, harmless end-to-end execution, independent review and evidence receipt. T002/T003 are hardware/resource gates and may remain release blockers without blocking contract implementation.

## Failure matrix

CONTROL reboot, COMPUTE reboot/offline, internet loss, queue/database restart, orchestrator crash, worker failure, stuck lease, retry exhaustion, disk/RAM/VRAM pressure, failed update, rollback and backup restore are required scenarios. Mark each as `planned`, `implemented`, `hardware_verified` or `production_verified` in evidence; never infer status.
