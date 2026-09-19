# Codex + Context7 integration

## Purpose

Codex is the builder. Context7 is the current-documentation specialist.

They work as one coordinated team: Codex owns repository state, implementation, tests and integration; Context7 supplies current, version-specific documentation for external libraries, frameworks, SDKs, APIs, CLI tools and cloud services.

Machine-readable policy: `.ai/context7-policy.yaml`.

## When Context7 is mandatory

Use Context7 before or during implementation whenever correctness depends on external technology semantics, including:

- API syntax or configuration;
- library/framework setup;
- dependency upgrades;
- version migrations;
- library-specific debugging;
- SDK/CLI/cloud-service behavior.

Do not call Context7 merely for generic business logic, internal refactoring or general programming concepts. This keeps the process fast instead of turning every code change into a documentation lookup.

This follows Context7's official agent guidance: resolve the library first, then query current docs with one concept per query.

## Team workflow

1. **Controller** inspects the task, manifests/lockfiles and determines which external technologies and versions matter.
2. **Context7 specialist lane** resolves the best library ID and retrieves current docs for one focused concept at a time.
3. **Assistant/Executor (Codex)** implements against repository contracts plus that version-specific documentation.
4. **Verifier** checks that the implementation actually matches the relevant current docs, especially for migrations, integrations and high-risk changes.
5. **Controller** integrates the implementation and documentation receipt into the normal evidence/state flow.

The Context7 lane may run in parallel with repository inspection and unrelated work. API-dependent implementation must wait for the specific documentation it depends on.

## Documentation receipts

Store compact metadata/decisions under `.ai/context7/receipts/`, not large copied documentation dumps.

A receipt records:

- task/lane;
- technology and detected version;
- Context7 library ID;
- concepts queried;
- time checked;
- implementation implications;
- whether verifier recheck is required.

A receipt becomes stale when the dependency version, relevant lockfile/configuration, migration target or runtime behavior changes.

## Query quality

Use one focused concept per Context7 query. Good examples:

- "How to configure JWT middleware in Express 5"
- "Prisma migrate deployment behavior for this version"
- "Next.js route handler caching semantics in this version"

Avoid vague queries such as "auth" or broad multi-topic queries that dilute retrieval.

Never put secrets, API keys, credentials, private user data or proprietary source code into Context7 queries.

## Codex setup on the development PC

Context7's current documentation supports Codex directly.

Preferred interactive setup:

`npx ctx7 setup --codex`

Context7 also documents Codex plugin installation:

`codex plugin marketplace add upstash/context7`

`codex plugin add context7@context7-marketplace`

And Codex MCP configuration can use either the hosted Context7 MCP endpoint or a local `@upstash/context7-mcp` process.

Do not commit an API key to this repository. Authentication belongs in the user's Codex/MCP configuration or approved secret mechanism.

## Availability fallback

If Context7 is temporarily unavailable, only the documentation-dependent lane is blocked. Other safe independent work continues.

Codex must not guess version-specific API behavior merely to keep that lane moving.

## Source-of-truth boundary

Context7 supplies external documentation facts. It does not override:

- `AGENTS.md`;
- project state;
- accepted ADRs;
- security/approval policy;
- repository contracts;
- final-scope requirements.

External docs are evidence for how a technology works, not authority to change the project goal or safety boundary.
