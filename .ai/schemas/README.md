# Canonical contracts

JSON Schema is the language-neutral source for Phase 1 entities and events. Producers and consumers must validate at boundaries, preserve `schema_version`, and reject unknown fields unless an ADR explicitly permits extension. Generated language types belong in code and must not become a second source of truth.
