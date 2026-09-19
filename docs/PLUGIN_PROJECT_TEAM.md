# Plugin project team

## Goal

The project uses plugins as a coordinated engineering team, not as unrelated tools.

Codex is the Controller. Every active plugin is assigned a bounded specialist role, reads the same task/workboard context, returns a receipt, and publishes discoveries that affect another lane.

Machine-readable files:

- `.ai/plugin-team.yaml`
- `.ai/plugin-registry.yaml`
- `.ai/specialist-router.yaml`
- `.ai/workboard.json`

## Core project team

**Context7** keeps external technical documentation current and version-specific.

**Exa** performs broader current research: architecture landscape, papers, benchmarks, failure modes and practitioner evidence.

**Neon** handles relevant Postgres/backend work with branch-first testing and strict data-safety/approval boundaries.

**GitHub** is canonical remote history plus PR/review/CI/artifact evidence.

**Vercel** supports preview/deployment for web/app work when that phase needs it.

**Figma** supports UI/UX architecture, design review and design-to-code work.

**Canva** supports media/design production where useful to the media pipeline.

None of these replaces the repository as source of truth.

## Single runner, parallel team

There is one GitHub Actions runner slot.

That does **not** mean the whole team works serially.

While one runner job is executing, independent lanes may continue:

- Context7 documentation;
- Exa research;
- Neon read-only analysis or isolated branch preparation;
- Figma/Canva design work;
- local implementation/tests that do not need the runner;
- Vercel planning/read-only inspection;
- GitHub read-only review/status inspection.

Only runner-consuming CI jobs are queued behind the single-runner semaphore.

The Controller owns the queue and cancels duplicate/superseded runs where safe.

## Shared-awareness contract

Before work starts, every active plugin lane knows:

- current task and objective;
- base commit/checkpoint;
- dependencies;
- its own read/write scope;
- which other lanes are active;
- resource/runner claims;
- what evidence it must return.

If one plugin discovers something that invalidates another lane's assumption, it publishes that discovery to the Controller immediately. The Controller updates the board and dependent lanes revalidate before integration.

No plugin independently edits canonical project-state.

## Optional plugins discovered for later use

Three additional plugins are useful enough to keep as optional project-team candidates:

- **Mixpanel** — later product/UX analytics and evaluation evidence.
- **Airtable** — optional structured external operations/evaluation workspace.
- **monday.com** — optional human-facing project/status dashboard.

They are **not** assumed connected until the user installs/connects them. They also never replace GitHub/project-state as canonical truth.

Further plugins should be discovered only when a real capability gap appears. More plugins are not automatically better: redundant integrations increase context, auth surfaces and failure modes.

## Approval and security

Plugin access does not bypass project approvals.

Production deploys, paid resources, destructive changes, secrets, public exposure and other high-impact actions retain the existing approval rules.

No API keys, database URLs, tokens or credentials may be written to this public repository.
