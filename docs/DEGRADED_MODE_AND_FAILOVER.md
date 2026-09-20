# Degraded mode and failover

## Core rule

**Blocked lane != blocked project.**

GitHub, a plugin, the single Actions runner, the internet, or a compute node may be temporarily unavailable without freezing every other useful task.

Machine-readable policy: `.ai/resilience-policy.yaml`.

## GitHub outage

When GitHub is unavailable, local Git remains the development transaction layer.

Allowed work continues:

- local branches/worktrees and commits;
- implementation;
- local tests;
- review;
- documentation;
- local evidence;
- unrelated Context7/Exa/Neon/Vercel/Figma/Canva lanes when their own connectivity exists.

Remote operations are queued conceptually for later reconciliation. Until GitHub is live again, Codex must not claim GitHub CI, PR review, merge, release or remote artifact evidence.

When GitHub returns:

VERIFY REMOTE → FETCH → COMPARE → RECONCILE → REVALIDATE IF BASE CHANGED → FLUSH QUEUED REMOTE OPERATIONS → RESUME CI/REVIEW.

Never use force-push as automatic outage recovery.

## Single Actions runner

Exactly one Actions runner slot exists.

A busy or stuck runner blocks only runner-consuming jobs. It does not block local coding, local tests, research, documentation, design or database analysis.

If the runner appears stuck, capture evidence, avoid duplicate equivalent runs, cancel only when safe, keep the CI gate pending, and continue other work.

## GitHub coding assistant

Any GitHub coding worker is extra capacity, not a required singleton.

If it becomes unavailable, the Controller may return its bounded task to the queue and reassign it to Codex or another safe executor. Acceptance criteria, base checkpoint and receipts remain unchanged.

## Plugin outages

Each plugin is its own failure domain. The Controller recalculates runnable work after a failure.

Examples:

- Context7 down → pause only work that genuinely needs current version-specific external API semantics.
- Exa down → pause only decisions needing fresh broad research.
- Neon down → pause Neon-dependent DB evidence/operations; local schema/code work can continue when safe.
- Vercel down → preview/deploy evidence waits; local web implementation continues.
- Figma/Canva down → only dependent design/media work waits.

## Two-machine target

The target architecture also applies the same principle to CONTROL and COMPUTE.

COMPUTE unavailable:
heavy jobs queue/pause; CONTROL remains alive.

CONTROL unavailable:
the developer machine should eventually be able to continue isolated safe repository work and reconcile after CONTROL recovers. Full CONTROL failover must be implemented and verified later; it is not currently claimed as working.

## Evidence rule

A missing service does not convert UNKNOWN into PASS.

Local tests may still be valid local evidence. Remote CI/release/deployment evidence remains PENDING until the relevant live system verifies it.
