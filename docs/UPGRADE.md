# Upgrade

Upgrade downloads a signed immutable artifact, verifies compatibility and checksum, snapshots state, applies idempotent migrations, runs health/acceptance tests, and returns to last-known-good on failure. Channel progression is dev → test → preview → stable.
