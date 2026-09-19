# Observability

Every meaningful run records project_id, task_id, run_id, agent/role, model, tools, timestamps, duration, retries, failure class, tests, commit and artifact hashes.

For execution efficiency also record, when available:

- cache hit/miss for expensive reusable stages;
- test tier reached;
- queue wait time;
- runner/GPU admission delay;
- context files loaded;
- repeated-attempt count;
- checkpoint/resume reason.

Logs are structured and redacted; metrics cover queue depth, latency, resource pressure, health and recovery; traces correlate gateway-to-worker execution. No secret values are logged.

Avoid high-volume duplicate logging that adds cost without improving diagnosis. Prefer one concise execution receipt per coherent stage plus detailed logs only for failures/debugging.
