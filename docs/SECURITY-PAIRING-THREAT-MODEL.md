# Security and Pairing Threat Model

## Trust boundary

mDNS/DNS-SD is discovery only.

A discovered device is NEVER trusted merely because it appears on the LAN.

## Enrollment

Default UX:
1. AI-Core opens a time-limited enrollment window.
2. RTX node discovers the service.
3. An authenticated key agreement is initiated using a reviewed cryptographic library/protocol.
4. Both screens display the same short authentication string.
5. User confirms the match.
6. AI-Core enrolls the compute node identity.
7. Enrollment window closes.
8. Future communication uses mutual authenticated encrypted transport.

Do not invent custom cryptography.

## Persistent identity

Each node owns its private key locally.
Private keys:
- are generated on-node;
- never enter Git;
- never ship inside an installer;
- never travel to Neon;
- are permission-restricted;
- can be rotated/revoked.

The control plane stores trust metadata and public fingerprints only.

## Transport

Post-pairing node traffic:
- encrypted;
- mutually authenticated;
- certificate/fingerprint validated;
- rejects unknown/revoked nodes.

Discovery metadata must reveal as little identity detail as practical.

## Pairing threats considered

- malicious device advertising a fake AI-Core
- malicious device advertising a fake RTX node
- man-in-the-middle during first pairing
- replay of expired pairing material
- stolen/reused pairing code
- rogue device on same LAN
- revoked node reconnecting
- private-key theft
- stale node identity after reinstall

Required controls:
- time-limited enrollment;
- short authentication string confirmation;
- ephemeral pairing state;
- replay protection;
- key rotation/revocation;
- explicit factory-reset/re-pair path;
- audit event for trust changes.

## Agent security

Specialists use least privilege.

Agents do not receive:
- root by default;
- unrestricted Docker socket;
- arbitrary host filesystem;
- production write permission by default;
- reusable secrets unrelated to the task.

High-impact changes require independent verification and human approval where policy requires it.

## Runner security

The one GitHub runner is a scarce execution boundary.

Required:
- isolated checkout/worktree per job;
- no secret echoing;
- cleanup after job;
- artifact checksums;
- timeout;
- cancellation;
- least-privilege repository token;
- no untrusted PR code with production credentials.

## Installer security

Stable installers/updates must be signed with a trusted production signing identity appropriate to the chosen Windows distribution path.

Signing is necessary but is not itself proof that code is safe.

Installer package contains no reusable cluster secret.

## Secret handling

Secrets are:
- generated at installation or injected securely;
- excluded from logs/diagnostics;
- never committed;
- rotatable;
- scoped to minimum purpose.

Diagnostics must redact tokens, passwords, private keys and connection strings.

## Production gates

Explicit human approval remains required for:
- irreversible destructive operations;
- production promotion;
- trust revocation/reset when it can disconnect a node;
- account/billing actions;
- final external media publishing.
