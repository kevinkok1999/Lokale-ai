# Unified plugin project team — 2026-09-20

## Goal

Turn project-helpful plugins into one coordinated project team with shared awareness, bounded authority, receipts, and one serialized GitHub Actions runner.

## Implemented

- `.ai/plugin-team.yaml`
- `.ai/plugin-registry.yaml`
- `docs/PLUGIN_PROJECT_TEAM.md`
- `scripts/plugin_team_check.py`
- Vercel/Figma/Canva standby lanes
- single-runner queue metadata in the workboard
- cross-lane discovery channel metadata
- AGENTS/handoff/bootstrap/router integration

## Plugin discovery

Three additional optional plugins were surfaced for user installation/connection:

- Mixpanel — product/UX analytics and evaluation evidence
- Airtable — optional structured operational/evaluation workspace
- monday.com — optional human-facing project/status dashboard

They are not canonical and are not assumed connected until a live check succeeds.

## Boundaries

The GitHub repository remains canonical. Plugin outputs cannot independently change project-state, final scope or verification level. The single runner constrains only GitHub Actions jobs; unrelated specialist lanes continue in parallel.

T001 remains READY and was not executed by this governance update.


## Canonical static validation

At content commit `ec1f4ec4dc1f995647f6717dd506dd1e33b2c6d9`:

- core plugin registry contains Context7, Exa, Neon, GitHub, Vercel, Figma and Canva;
- all corresponding workboard lanes are present;
- lane IDs are unique;
- canonical writer remains Controller-only;
- single GitHub Actions runner queue declares exactly one slot;
- T001 remains READY.

Local Codex connectivity is intentionally still verified at startup rather than inferred from ChatGPT-side connections.
