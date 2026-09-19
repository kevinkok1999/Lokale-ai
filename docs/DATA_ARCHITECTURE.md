# Data and memory architecture

Relational state is canonical for projects, tasks, runs, agents, approvals, artifacts, releases, incidents and audit events. Structured project state is always available offline. Semantic memory is an optional indexed projection with source, permissions, timestamps and provenance; it is never the sole copy of critical state. Backups and restore tests precede stateful migrations.
