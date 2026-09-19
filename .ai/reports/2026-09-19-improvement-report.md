# 10/10 improvement run

## Changes

- recorded baseline scorecard and separate design/verification scores;
- made `docs/SOURCE_OF_TRUTH.md` authoritative and removed temporary/starter artifacts;
- expanded Product Constitution to the full future capability map, including media;
- added canonical schemas for Run, Artifact, Approval, Agent, Node, ResourceState, Model and Tool;
- fixed schema-version invariant on HealthStatus;
- added executable contract smoke validation and tests;
- added technology review with current primary-source references and resource-aware decisions;
- split architecture, implementation, hardware, release and production gates;
- updated resource calibration thresholds;
- synchronized project state and Codex handoff to Git history.

## New findings

The design needs a durable workflow adapter but should not deploy Temporal or a full event stack on the 16 GB CONTROL node before a measured need. The first slice should remain dependency-light. Remote GitHub parity cannot be asserted from this workspace and is explicitly recorded as unverified.
