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
