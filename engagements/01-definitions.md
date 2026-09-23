# Engagements — Definitions

Status: Draft
Ratified: No
Last updated: 2026-09-23

Scope: the unit-of-work layer sitting on top of the domain axis — how a
raw idea becomes a governed, fully-planned Engagement (Project,
Maintenance, Monitoring & Alerting, Incident Response, Request/Ad Hoc,
Governance/Review, Decommission) before any Agent is spun up to act on
it. Not a domain (00-framework/domain-axis-definition.md) — it doesn't
add a new technology-layer row; it's the process layer that consumes
every domain's content (Anchor layer: governance, taxonomies,
ontologies, conventions, org chart) and Harness's Agent machinery to
plan and execute work. Reviewed with the user in a standalone design
pass before being written here — see 09-open-decisions.md for what's
still open.

Anchor convention: `eng-<term-slug>`.

---

## Referenced Terms (owned elsewhere)

- **Agent, Agent Type, Capability Scope, Tool Permission Scope,
  Escalation Path, Human-in-the-Loop Gate, Approval Gate, Agent
  Trace/Transcript, Model Version Pin** — owned by Harness →
  [08-harness/01-definitions.md](../08-harness/01-definitions.md). Every
  Agent role this file defines (Vetting Agent, Engagement Planning
  Agent) is configured using these fields, not a parallel schema.
- **Requester, Approver, Owning Team Lead** — owned by Cross-Cutting
  Roles & Departments →
  [cross-cutting/roles-and-departments/01-definitions.md](../cross-cutting/roles-and-departments/01-definitions.md)
  (`ccrole-requester`, `ccrole-approver`, `ccrole-owning-team-lead`).
- **Department** — owned by Cross-Cutting Roles & Departments →
  same file, `ccdept-department` (a specific department, e.g.
  `ccdept-business-intelligence-analytics`, is the value used; not
  redefined here).
- **Sandbox** — owned by Cross-Cutting →
  [cross-cutting/sandbox-activation.md#cc-sandbox](../cross-cutting/sandbox-activation.md#cc-sandbox).
  An Agent role defined here is Sandbox-tested before being trusted
  org-wide, same requirement Harness already places on any Agent.

---

## Terms

### Engagement {#eng-engagement}
A bounded unit of work an organization asks one or more Agents (and
humans) to take on, of one of seven Engagement Types (`eng-engagement-type`).
The thing an Engagement Document plans and an Agent is ultimately spun
up to execute. Source: ITIL 4 practice mapping (02-engagement-types.md),
Anthropic's "Building Effective AI Agents" (plan fully before acting).

### Engagement Type {#eng-engagement-type}
One of seven fixed categories an Engagement falls into — Project,
Maintenance, Monitoring & Alerting, Incident Response, Request/Ad Hoc,
Governance/Review, Decommission — each mapped to an ITIL 4 practice.
Determines which sections of the Engagement Document (below) are
required vs. optional. Full mapping table: 02-engagement-types.md.
Source: ITIL 4 practices (already cited in
07-workflow-process/00-standards-alignment.md).

### Engagement Document {#eng-engagement-document}
The single shared schema (YAML front matter + Markdown body) used to
plan every Engagement before any Agent acts on it — one schema, not
seven, with Engagement Type driving required/optional sections. Two
instances: Project Document (`eng-project-document`) and Task Document
(`eng-task-document`). Mirrors this framework's own `_status.yaml`
(machine-readable) + Markdown (human-readable) split, applied at the
document level. Source: this framework's own term-linking-convention.md
pattern, generalized.

### Project Document {#eng-project-document}
Extends: eng-engagement-document
Adds: the top-level planning document for an Engagement — goal, scope,
owning department, risk tier, applicable governance, and the list of
Agents and Tasks required. Required for Project and Decommission types;
optional (wraps a recurring program) for Maintenance and
Governance/Review; not used for Monitoring & Alerting or the standalone
types. Full template: 03-project-document-template.md.

### Task Document {#eng-task-document}
Extends: eng-engagement-document
Adds: a single unit of assigned work under a Project (or standalone,
for Ad Hoc/Incident/Maintenance) — one Agent, one Capability Scope, the
Skills it invokes, and its result. Never starts work without
`assigned_agent`, `skills_invoked`, and (if required) `approved_by` all
filled. Full template: 04-task-document-template.md.

### Intake Brief {#eng-intake-brief}
The structured, confirmed output of the Vetting Agent
(`eng-vetting-agent`) — not an Engagement Document itself, a
lighter-weight input to one. Turns a raw idea (meeting notes, a chat
thread, a ticket) into the core+type-pack question answers the
Engagement Planning Agent needs to draft a Project or Task Document.
Full schema: 05-intake-and-vetting.md.

### Participant {#eng-participant}
A human or Agent named on an Engagement Document's Participants list,
each carrying a Role and a RACI tag (Responsible, Accountable,
Consulted, Informed). Humans and Agents are addressed identically in
this list — see 06-participants-collaboration-and-channels.md and, for
where Agent participation stops short of full parity, its
Accountability Boundary in 07-planning-and-advisory-agents.md.

### Collaboration Log {#eng-collaboration-log}
The discussion mechanism for an Engagement Document — threaded
comments anchored to a specific passage, open to any Participant, human
or Agent. Not a new mechanism: the same substrate this framework's own
review documents are built on, applied one level down. Gives an
append-only, who-said-what-when record without separate tooling. See
06-participants-collaboration-and-channels.md.

### Channel {#eng-channel}
Extends: harness-tool-permission-scope
Adds: the specific medium a human or Agent uses to communicate (chat,
email, a ticketing system, Slack, voice/transcription). Not a new
category to govern — every Channel is a registered Tool under an
Agent's Tool Permission Scope, scoped and permissioned the same as any
other Tool. Adding a new Channel means registering a new Tool; no
framework or schema change required. See
06-participants-collaboration-and-channels.md.

### Vetting Agent {#eng-vetting-agent}
The Agent role (Agent Type: Assistant) that turns a raw, possibly
unstructured request into a confirmed Intake Brief
(`eng-intake-brief`) — asking a human directly for anything it cannot
confidently extract, never guessing. Distinct from the Engagement
Planning Agent (below): narrower Capability Scope, no
governance-mapping responsibility. Full spec: 05-intake-and-vetting.md.

### Engagement Planning Agent {#eng-planning-agent}
The Agent role (Agent Type: Assistant) that drafts a Project Document
and its Task Documents from a confirmed Intake Brief plus the Anchor
layer (every domain's governance, taxonomies, ontologies, conventions,
org chart) and the Skill/Agent Library (registries, not yet specced —
see 09-open-decisions.md). Drafts only — every Engagement Document it
produces still requires a human Approver's sign-off (CCAR-1/CCAR-2,
cross-cutting/access-rules.md) before any Task's assigned Agent starts.
Full spec: 07-planning-and-advisory-agents.md.

### Skill {#eng-skill}
A registered, reusable capability an Agent invokes — what a Task Document's `skills_invoked` field points to (`skill-lib/<slug>-vN`). Not an actor; something an Agent does. Built on demand (see 10-skill-library.md's Build-on-Demand Principle), never predicted in advance. Source: this area's own review pass; reuses no external standard.

### Agent Template {#eng-agent-template}
A reusable, pre-configured Agent role (`agent-lib/<slug>-vN`) an Engagement's `agents_required` list references instead of composing an Agent from scratch. Fields mirror Harness's Agent schema exactly (`harness-agent`, 08-harness/01-definitions.md). Full spec: 11-agent-library.md.

### Model Catalog Entry {#eng-model-catalog-entry}
One approved, externally available model (frontier API or self-hosted/local) an Agent's Model Version Pin (`harness-model-version-pin`) can be set to. Not built in-house like a Skill or Agent Template — a curated list plus a Selection Criteria rubric, closer in spirit to Harness's Tooling column. Full spec: 12-model-catalog.md.

### Factory Agent {#eng-factory-agent}
The Agent role (Agent Type: Assistant) that drafts a candidate Skill or Agent Template when the Planning Agent's Skill/Agent Library Lookup finds no “close enough” match and escalates. A Factory Run is an ordinary Task Document (`eng-task-document`), not a new document type — the requesting Task lists it as a dependency. Pre-built like the Vetting Agent and Engagement Planning Agent (domain-agnostic infrastructure, not a guess about domain-specific work). Full spec: 13-factory.md.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 11 new terms, every existing Harness/Roles concept referenced rather than redefined
- [x] Modular — Engagement Document, Vetting Agent, Planning Agent are each independently replaceable
- [x] Easy to update — Engagement Type list and question packs live in one place (02, 05), not scattered
- [x] Easy to maintain — reuses Harness's Agent schema and cross-cutting's Role/Department registries rather than inventing parallel ones
- [x] Easy to replace — plain markdown, same anchor/reference-stub convention as every domain
