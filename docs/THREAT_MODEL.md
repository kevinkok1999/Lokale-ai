# Threat model

Threats include prompt injection, malicious repository content, stolen pairing codes, compromised worker, secret leakage, supply-chain packages, runaway agents, resource exhaustion and corrupted updates. Controls: schema validation, capability-scoped tools, short-lived pairing, mTLS or equivalent, allowlisted commands, timeouts, quotas, immutable artifacts, dependency pinning, redacted logs, backups, rollback and independent review. Residual risk: host compromise and unverified third-party model behavior require operator controls.
