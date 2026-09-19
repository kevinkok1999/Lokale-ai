# Task files

Task files under this directory are the execution unit for Codex.

Each task should contain enough information to build a Task Execution Envelope without reading the entire repository.

Preferred fields:

- id/title/status/priority;
- dependencies/blocker;
- owner capability/risk/approval class;
- inputs and relevant context;
- expected outputs;
- commands/tests and required test tiers;
- acceptance criteria and Definition of Done;
- evidence target;
- resource class/node needs;
- parallelism limits;
- cache invalidation inputs;
- exact next action when blocked.

Do not add fields solely for ceremony. The purpose is faster, safer resume and less context loading.

Global execution rules live in `.ai/execution-policy.yaml`.
