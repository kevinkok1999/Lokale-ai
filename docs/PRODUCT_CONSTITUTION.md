# Product constitution — Local AI OS

## Identity and authority

Local AI OS is one local-first personal AI operating system that behaves as an integrated digital technical organization. The user speaks to one Master interface; models, agents, tools, memory, projects, nodes and workflows remain explicit internally so that permissions, evidence and recovery are inspectable. The user is the final authority. The system may optimize execution but may not silently change the goal, constraints or approval boundary; Goal Guardian preserves the original intent throughout a run.

Priority is reliability, safety, recoverability, simplicity, observability, performance, resource efficiency, maintainability, extensibility and then autonomy. “Best AI” is an engineering hypothesis measured by correctness, latency, failure rate, resource use, recovery and user outcome.

## Capability map

- **Master AI:** interprets intent, asks only necessary questions, creates a dependency-aware plan, chooses capability/model/tool/node, delegates within policy, reconciles results and reports evidence.
- **ProjectForge:** idea → requirements → research → architecture → implementation → tests → security review → preview → approval → deployment → monitoring → maintenance.
- **Software engineering:** understand existing and new repositories, preserve working versions, create isolated workspaces, code, test, review, debug, document and maintain.
- **Website/App Factory:** assemble frontend, backend, API, database, authentication, responsive UI, tests, build and preview through provider-neutral adapters.
- **Zero-Deploy:** prefer free/local/self-hosted deployment and €0 recurring cloud spend by default. Paid infrastructure, domain purchase and public exposure require explicit approval.
- **ToolForge:** register tools/MCP/plugins with capability, schemas, filesystem/network scope, risk, timeout and approval metadata. Agents receive only needed capabilities.
- **KnowledgeMesh:** permission-aware, project-aware and traceable retrieval over repositories, manuals, docs, decisions, APIs and local files.
- **Memory:** structured project state first; semantic, episodic, temporal and causal memory can be added as indexed projections with provenance and retention controls.
- **Model routing:** multiple provider adapters and a registry route by task, quality, context, latency, availability and measured resource fit.
- **Resource routing:** select CONTROL/COMPUTE and workload admission from actual CPU, RAM, VRAM, disk, queue and model residency; queue under pressure.
- **AgentFactory:** later creates bounded specialist teams only when value exceeds coordination cost; depth, count, runtime, retries and permissions are capped.
- **Self-healing:** health → diagnosis → bounded recovery → verification → incident record.
- **Shadow mode:** compare candidate models, prompts, agents and workflows against the current version without controlling real actions.
- **Controlled self-improvement:** observe → propose → test → benchmark → review → shadow → approval/promote. No uncontrolled self-modifying production.
- **Multi-user:** support at least the owner and a second user with accounts, RBAC, separate personal context and explicitly shared project knowledge.
- **Digital twin/simulation:** later simulate compute loss, queue pressure, agent fan-out, upgrades and failure recovery.
- **Media production:** a first-class adapter family for brief → research → script → fact check → storyboard → shot list → image/video/voice/audio assets → edit → subtitles → QA → preview → final render → human approval/publish. Assets carry provenance/licensing metadata; jobs checkpoint and resume.

These capabilities are extension contracts and roadmap targets. The first reliable core is Master → Coder → Tester → Reviewer; future scope must not force premature infrastructure.

## Non-negotiable engineering rules

Deny by default, least privilege, untrusted input isolation, no secrets in Git or logs, Git as transaction/audit layer, deterministic scripts where reasoning adds no value, schema-first cross-language contracts, bounded retries, idempotency, immutable artifacts, evidence-linked decisions, and no self-approval for high-impact changes.

Verification levels are `UNVERIFIED`, `STATICALLY_CHECKED`, `UNIT_VERIFIED`, `CONTRACT_VERIFIED`, `INTEGRATION_VERIFIED`, `E2E_VERIFIED`, `HARDWARE_VERIFIED`, and `PRODUCTION_VERIFIED`. A claim may use only the highest level actually evidenced.
