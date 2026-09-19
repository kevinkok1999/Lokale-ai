# Backup and recovery

Control-plane state is backed up locally and optionally off-site only with approval. Recovery uses checkpoints, leases, idempotent replays and last-known-good artifacts. Required tests: service restart, worker loss, queue recovery, corrupted update rollback and backup restore. Recovery claims remain unverified until executed on target hardware.
