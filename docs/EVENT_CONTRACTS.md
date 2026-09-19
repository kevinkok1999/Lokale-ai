# Event contracts

Canonical events include `task.created`, `task.started`, `task.completed`, `task.failed`, `tests.completed`, `review.completed`, `resource.pressure`, `compute.offline` and `compute.online`. Every event has id, type, schema version, timestamp, project id, optional task/run ids and object payload. Consumers must be idempotent and tolerate duplicates; event retention and replay are operational decisions recorded by ADR.
