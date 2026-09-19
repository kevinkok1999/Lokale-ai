# Acceptance Matrix

## Platform
- clean AI-Core start
- clean RTX node start
- AI-Core reboot
- RTX reboot
- RTX offline during job
- internet offline
- orchestrator restart
- Redis restart
- Qdrant restart
- PostgreSQL restart
- stuck job lease
- retry exhaustion
- queue backpressure
- disk pressure
- RAM pressure
- VRAM pressure
- bad update
- automatic rollback
- backup restore

## Team OS
- dynamic team formation
- dependency DAG fan-out
- fan-in after verification
- critic disagreement
- verifier failure
- no-self-approval enforcement
- missing specialist / degraded team
- duplicate work detection
- disagreement escalation
- execution receipt generation

## One Runner
- exactly one runner-required job admitted at a time
- waiting jobs preserve order/priority
- cancellation
- timeout
- retry
- failed job does not block next job
- artifact hash recorded
- runner restart does not lose durable job state

## Installer
- clean install
- reinstall
- repair
- upgrade
- failed upgrade
- rollback
- discovery
- ambiguous discovery
- pairing confirmation
- pairing recovery
- wrong/untrusted node rejected
- missing dependency
- local offline operation after setup
- diagnostics bundle contains no reusable secrets

## Media
- image generation project
- short-form video
- multi-scene video
- long-form/documentary pipeline
- factual source provenance
- fact-check gate
- missing asset detection
- broken audio detection
- subtitle timing validation
- interrupted generation
- checkpoint/resume
- preview before final
- final render integrity
- final publish approval

## Security
- least privilege agent permissions
- secret never committed
- private node key stays local
- untrusted node cannot pair silently
- production promotion requires approval
- destructive action requires approval
- signed stable release required

## Release Gate

Stable is blocked when any mandatory acceptance test is:
- failed
- skipped without waiver
- unavailable without explicit degraded-mode marking
