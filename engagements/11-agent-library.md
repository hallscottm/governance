# Engagements — Agent Library

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-agent-template` (01-definitions.md). Reviewed with the user
in a standalone design pass before being written here.

## Build-on-Demand Principle

Same rule as the Skill Library (10-skill-library.md), applied to
Agents: no wholesale pre-building or predicting the Agents an org might
need. **One deliberate exception:** the Vetting Agent and Engagement
Planning Agent (05, 07) are pre-built because they're not a guess about
domain-specific work — they're the fixed entry point every Engagement
passes through, used regardless of domain. Nothing else gets that
treatment by default; everything else is built the first time a Task
genuinely needs it.

## Agent Library entry

```yaml
agent_template_id: agent-lib/<slug>-v<N>
role_name: <string>
agent_type: Assistant | Autonomous | Multi-Agent
capability_scope: <ref>
tool_permission_scope: <ref>
default_skills: [skill-lib/... ids]
model_version_pin: <Model Catalog entry — see 12-model-catalog.md>
escalation_path: <ref>
sandbox_tested: true | false
status: draft | approved | deprecated
provenance: hand-authored | factory-built <factory run id>
created_date: <date>
last_updated: <date>
used_by: [Project IDs that reference this Template]
```

An Agent Template is a *default configuration*, not a lock — a Project
can narrow the Capability Scope or Tool Permission Scope it inherits
from a Template (same as a Task Document already narrows a
Project-level Capability Scope), but can't widen it. Widening means
it's not this Template anymore; that's a new version or a new
Template, decided the same way Skill versioning is.

## Registered Agents

First entry, registered 2026-09-23 via factory-run-bi-report-builder-agent
(implementation/factory-runs/bi-report-builder-agent/) - the first real
Agent Template this registry has ever held (the pre-built Vetting and
Planning agents are framework machinery, not registry entries).
Compiled definition lives at implementation/agents/bi-report-builder-agent.md.
Drafted directly by the orchestrating session acting as Factory Agent
(a Template is a role/schema definition, not executable code, so its
Eval is scope/schema conformance against the real Task that needs it,
not a runtime test - see sandbox/eval-result.md for the 7/7 cases
checked).

```yaml
agent_template_id: agent-lib/bi-report-builder-agent-v1
role_name: BI Report Builder Agent
agent_type: Assistant
capability_scope: >
  Read the routing Task's confirmed metric list, source location,
  Distribution Scope, and Sensitivity Level, and 06-bi-reporting's
  Anchor layer. Write a Report Data Model and Dashboard to the
  routing Task's own declared output location only. Never authors a
  new Data Quality Rule; never decides Distribution Scope/Sensitivity
  itself.
tool_permission_scope: >
  Read: Grep, Glob, Read (repo-wide read). Write: implementation/pilots/**/report/**
  only (narrowed per-Project by the assigning Task to that Project's
  own report path). Execute: skill-lib/build-bi-report-v1 only for the
  actual chart/report construction step.
default_skills: [skill-lib/build-bi-report-v1]
model_version_pin: OPEN - Model Catalog (engagements/12-model-catalog.md)
  has zero populated entries; human decision required, not guessed -
  same open item as every other Agent/Skill registered so far.
escalation_path: >
  A confirmed source that doesn't fit skill-lib/build-bi-report-v1's
  scope is named explicitly and routed as a new Factory Run Task, not
  handled with ad hoc code outside any registered Skill.
sandbox_tested: true
status: approved
provenance: factory-built factory-run-bi-report-builder-agent
created_date: 2026-09-23
last_updated: 2026-09-23
approved_by: user (hallscottm@gmail.com), direct chat confirmation, 2026-09-23
used_by: [dq-metrics-dashboard]
```

## Lookup, reuse, escalation, deprecation

Identical mechanism to the Skill Library (10-skill-library.md) — same
"close enough" test (exact Capability Scope + Tool Permission Scope
match), same Lookup → Found/Not-found → Factory-or-human path, same
three deprecation triggers, same append-only discipline. Not
re-specced twice; see there.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one registry, reusing the Skill Library's exact lifecycle rather than a parallel one
- [x] Modular — a Template's scope can narrow per-Project without touching the Template itself
- [x] Easy to update — new Templates are additive
- [x] Easy to maintain — fields mirror Harness's Agent schema exactly, one place to keep in sync
- [x] Easy to replace — plain YAML registry, no tooling dependency
