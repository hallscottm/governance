# Engagements — Skill Library

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-skill` (01-definitions.md). Reviewed with the user in a
standalone design pass before being written here.

## Build-on-Demand Principle

Resolves a question raised earlier and never settled: predict and
pre-build the skills an org might need, or compose fresh each time?
**Neither, wholesale.** A Skill gets built the first time a Task
genuinely needs that exact capability and nothing close enough already
exists in the Library — never in anticipation of a need that hasn't
shown up yet. Once built, it's registered and every subsequent match
reuses it. Grows from real usage, not upfront guessing — the same
instinct behind not enumerating every task a company might need, and
Anthropic's own "start simple, add complexity only when necessary"
guidance (00-standards-alignment.md).

**"Close enough" test:** required Capability Scope and Tool Permission
Scope must match exactly — these are the governance-load-bearing
fields; an inexact match on either is a different Skill, not a reuse.

## Skill Library entry

```yaml
skill_id: skill-lib/<slug>-v<N>
name: <human name>
description: <what it does>
version: N
status: draft | sandbox-tested | approved | deprecated
owning_domain: <domain this skill's knowledge draws from, if any>
requires_capability_scope: <ref>
requires_tool_permission_scope: <ref>
typical_risk_tier: Low | Moderate | High
eval_suite: <harness-eval-suite reference>
provenance: hand-authored | factory-built <factory run id>
created_date: <date>
last_updated: <date>
used_by: [Task IDs that reference this Skill — reuse visibility, not a permission list]
```

A new version (`-v2`, etc.) is minted rather than editing a Skill in
place once it's `approved` — same reasoning as Harness's Model Version
Pin requiring a fresh Eval Suite Run on change, not a silent in-place
update.

## Lookup, reuse, escalation

1. The Engagement Planning Agent needs a Skill for a Task (07's Skill
   Library Lookup step).
2. **Found** — reference it directly. The common path (see
   08-worked-example.md).
3. **Not found** — the Planning Agent's existing Escalation Path
   already covers this: route to the Factory (build something new) or
   a human Approver (if it's a governance gap, not a capability gap).
4. **Built** — once the Factory (next spec) produces, Sandbox-tests,
   and Eval-passes a new Skill, it's registered here with
   `status: approved` and becomes reusable. The Library only grows
   through this gate, never by direct edit.

## Deprecation

Never a hard delete — append-only, same discipline as `_qa` logs.
Three named triggers: a provider/dependency-forced retirement; a
Behavioral Drift or repeated Eval Suite failure (parallels HPOL-4's
automatic tightening — auto-flags for review, doesn't auto-remove); or
superseded-and-unused (`used_by` empty, safe low-urgency cleanup).
`status: deprecated` stops new Lookups from picking it; Tasks that
already reference it keep their historical record.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one registry, one build trigger, one deprecation rule set
- [x] Modular — a Skill's Capability/Tool Permission Scope is independently replaceable per version
- [x] Easy to update — new Skills are additive; nothing here regenerates
- [x] Easy to maintain — reuses Harness's Eval Suite and Model Version Pin discipline rather than inventing new review machinery
- [x] Easy to replace — plain YAML registry, no tooling dependency
