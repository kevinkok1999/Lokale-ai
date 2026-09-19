# Final Completion Criteria — Local AI OS

## Purpose

This document defines the only project-level gate for declaring Local AI OS `FINAL_COMPLETE`.

A task, milestone, preview, beta, stable subsystem or even an initial production release can be complete without the overall project being final.

## Absolute completion rule

The project may be set to `FINAL_COMPLETE` only when all of the following are true:

1. Every entry marked `required: true` in `.ai/final-scope.yaml` is implemented, integrated into the coherent Master-AI experience, and backed by evidence.
2. Every mandatory final gate in `.ai/final-scope.yaml` is PASS/VERIFIED.
3. No unresolved critical or high-severity defect, security issue, data-loss risk or architecture contradiction remains.
4. CONTROL and COMPUTE have passed real-hardware acceptance, pairing, resource-pressure, reboot/offline and recovery tests.
5. Installer, repair, update, rollback, backup/restore and uninstall paths have passed their supported-platform acceptance suites.
6. Offline-first behavior has been verified for the local core; loss of internet or COMPUTE degrades safely without corrupting durable state.
7. Security/permission boundaries, secret handling, supply-chain integrity, artifact signing/SBOM and auditability have verified evidence.
8. The full end-to-end product paths work across coding/software, websites/apps, research/knowledge, memory, tools, media and operations.
9. Multi-user isolation/sharing behavior is verified.
10. Shadow mode and controlled self-improvement cannot promote an unverified change and have rollback evidence.
11. Performance/resource behavior is measured on target hardware and remains inside approved budgets under representative workloads.
12. The current benchmark suite is passed and the system shows measured improvement against its previous stable baseline and selected contemporary reference systems on the dimensions relevant to this product.
13. Documentation/runbooks/state/evidence are sufficient for a fresh approved machine/session to install, operate, recover and continue the project without chat-history dependence.
14. The user explicitly accepts the final system.

## “Best system” rule

“Best” is a North Star, not an unverifiable label. Before final acceptance, maintain a versioned benchmark scorecard covering at least:

- task correctness and success rate;
- coding/build/test quality;
- tool-use reliability;
- latency and throughput;
- RAM/VRAM/CPU/disk efficiency;
- recovery success and mean time to recover;
- offline continuity;
- security/permission failures;
- long-context/project-memory retrieval quality;
- model-routing quality;
- end-to-end website/app/project completion;
- media pipeline completion/QA;
- operator/user effort.

Where practical, compare against current relevant reference systems or prior best-known local baselines under documented conditions. Do not claim universal superiority where the benchmark cannot establish it.

## Scope protection

Do not make completion easier by silently deleting required scope.

A capability can be removed from the final requirement only when the user explicitly requests the scope change and the canonical repository records:

- what is removed;
- why;
- impact/trade-offs;
- migration/compatibility consequences;
- an accepted superseding ADR or equivalent decision.

Otherwise every required capability remains required.

## Old-versus-new rule

Explicitly superseded legacy documents are history only. A newer current canonical policy or accepted superseding ADR takes precedence. Old material must not block implementation of a newer approved design.

If two current sources genuinely conflict, resolve only the conflicting area in the source-of-truth/ADR and then continue unaffected work.

## Continuous execution

After a task or milestone becomes DONE, Codex should continue to the next highest-priority unblocked task. It should stop only at:

- a real human approval boundary;
- a missing credential/permission/hardware action that cannot be performed;
- a safety/resource/security boundary;
- an unresolved contradiction requiring owner decision;
- or practical session/context limits.

A session ending is not project completion. Persist exact state/evidence/next task so the next session can resume.

## Final evidence package

Before `FINAL_COMPLETE`, produce a final evidence bundle with:

- final-scope matrix;
- test/benchmark results;
- hardware/resource reports;
- security review;
- recovery/chaos results;
- installer/update/rollback/restore results;
- release artifact hashes/signatures/SBOM;
- known residual risks;
- final architecture/state;
- user acceptance record.

Only then may the project-level state change to `FINAL_COMPLETE`.
