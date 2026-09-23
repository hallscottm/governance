# Engagements — Intake & Vetting

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-vetting-agent` and `eng-intake-brief` (01-definitions.md) —
the step before an Engagement Document exists. Separate from the
Engagement Planning Agent (07-planning-and-advisory-agents.md): narrower
Capability Scope (extract and clarify, not map to governance), no
self-approval either (CCAR-1/CCAR-2 applies the same way).

## Vetting Agent

| Field | Value |
|---|---|
| Agent Type | Assistant — responds to a raised request, never initiates vetting on its own |
| Capability Scope | Extract and confirm Intake Brief fields from a raw request; ask a human directly for anything it cannot confidently extract. Excludes governance mapping (that's the Planning Agent's job) and any system change. |
| Tool Permission Scope | Read: the request itself and any attached source (meeting notes, chat, ticket). Write: the Intake Brief store only. |
| Escalation Path | A required field can't be confidently extracted -> ask a human directly. Never guesses past that point — same discipline as the Planning Agent's own Escalation Path. |
| Own Risk Tier | Low (extraction and clarification only, no execution) |
| Sandbox Tested | Required before org-wide trust |
| Approval boundary | None needed to hand off to the Planning Agent — the Intake Brief isn't itself binding on anything; the Engagement Document it feeds still requires a human Approver |

## What's fixed: the core question set

Every Engagement, regardless of type or source, must have these
answered before handoff to the Planning Agent:

- Problem / goal
- Requester
- Urgency
- Rough affected domains/systems
- Known constraints
- Any risk signal (security, compliance, sensitive data mentioned at all)

## What's fixed but extensible: Engagement-Type question packs

Additional required questions per Engagement Type
(`eng-engagement-type`) — a registry, not hardcoded here, so a new pack
doesn't require rewriting this file:

| Engagement Type | Additional required questions |
|---|---|
| Incident Response | Severity, detection time, current impact |
| Decommission | What's being retired, dependency check |
| Maintenance | Recurrence cadence |
| Monitoring & Alerting | What triggers the alert, who's notified (pending resolution of 09-open-decisions.md #1) |
| Project | Core set is generally sufficient; Planning Agent expands per applicable_domains |
| Request / Ad Hoc | Core set is generally sufficient |
| Governance/Review | Review cycle, prior cycle reference if any |

## What's genuinely dynamic

The wording of follow-up questions put to a human. Bounded freedom: the
Vetting Agent can only ever be probing for answers to the fixed core +
type-pack fields above, never inventing a new category of question.

## Fast path vs. full vetting

Not every request needs a conversation. If input already arrives
structured (a filled-in ticket template), the Vetting Agent validates it
against the core + type-pack question set and passes straight through.
It only engages in back-and-forth when input is incomplete or
unstructured. One Agent, one branch — not two Agents.

## Intake Brief schema

```yaml
intake_id: <slug>
source: meeting-notes | chat | ticket | direct-request
raised_by: <human>
core_answers:
  problem_goal: <text>
  urgency: <text>
  rough_domains: [list]
  risk_signals: [list, possibly empty]
type_pack_used: <engagement-type question pack, if applicable>
type_pack_answers: {}
open_gaps: [fields still unconfirmed, if handed off before fully resolved]
recommended_engagement_type: <Vetting Agent's best read, confirmed or corrected by the Planning Agent>
```

**Quality bar check:**
- [x] Simple — one agent role, one fixed core set, one extensible pack registry
- [x] Modular — question packs can grow without touching the core set or the Vetting Agent's own spec
- [x] Easy to update — new Engagement Type or new pack question is a table row, not a schema change
- [x] Easy to maintain — same Escalation Path discipline as every other Agent in this framework, no separate rule to remember
- [x] Easy to replace — plain YAML + Markdown
