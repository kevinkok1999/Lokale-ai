# Test strategy and gates

## Gate classes

- **Architecture gate:** contracts, boundaries, failure semantics, resource assumptions and approvals documented.
- **Implementation gate:** schemas, unit tests, contract tests, static/security checks and deterministic scripts pass.
- **Hardware gate:** doctor, drivers, pairing, inference, pressure and reboot/offline tests pass on target nodes.
- **Release gate:** signed reproducible artifact, SBOM, upgrade/rollback and backup restore pass.
- **Production gate:** deployment approval, health SLOs, monitoring and operator runbook accepted.

## Fail-fast test ladder

Run the cheapest required evidence first:

- **Tier 0 — fast static:** schema/config validation, formatting, lint, type/static analysis.
- **Tier 1 — targeted unit:** changed-module tests and negative fixtures.
- **Tier 2 — contract/component:** cross-boundary contracts and component behavior.
- **Tier 3 — integration:** only integrations affected by the change.
- **Tier 4 — E2E/hardware/release:** end-to-end, hardware, chaos/recovery, installer, signed-release and production gates.

If an earlier required tier fails, fix it before spending resources on later tiers. Passing a lower tier never substitutes for a required higher tier.

## Incremental evidence

Reuse a prior result only when code/config/lockfiles/toolchain/environment inputs that determine it are unchanged. Invalidate:

- contract evidence after schema/consumer change;
- security evidence after dependency/policy change;
- hardware evidence after machine/driver/runtime change;
- release/production evidence after artifact/deployment change.

## First milestone tests

T001 runs `python3 scripts/validate_contracts.py` and checks closed, versioned schemas plus negative fixtures. T004–T006 add API contract tests, isolated-workspace tests, harmless end-to-end execution, independent review and evidence receipt. T002/T003 are hardware/resource gates and may remain release blockers without blocking contract implementation.

## Failure matrix

CONTROL reboot, COMPUTE reboot/offline, internet loss, queue/database restart, orchestrator crash, worker failure, stuck lease, retry exhaustion, disk/RAM/VRAM pressure, failed update, rollback and backup restore are required scenarios. Mark each as `planned`, `implemented`, `hardware_verified` or `production_verified` in evidence; never infer status.
