# API contracts

Phase 1 gateway operations: create task, get task, approve task, get run, get health and retrieve report. Requests carry `schema_version`, correlation id and project id. Responses are typed envelopes with status, data, errors and evidence references. JSON Schema under `.ai/schemas` is authoritative; unknown fields are rejected at boundaries.
