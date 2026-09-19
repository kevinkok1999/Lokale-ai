# Parallel lane receipts

Parallel workers return receipts to the Controller; the Controller is responsible for canonical integration.

Recommended receipt name:

`<coordination-epoch>-<lane-id>-<task-id>.json`

Required fields are defined in `.ai/coordination-policy.yaml`.

A receipt is evidence about a lane execution, not permission to merge. The Controller must check base commit freshness, scope, required tests, cross-lane discoveries and conflicts before integration.
