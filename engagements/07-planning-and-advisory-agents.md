# Engagements — Planning & Advisory Agents

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-planning-agent` (01-definitions.md), and where Agent
participation in Engagements stops short of full parity with humans.

## Engagement Planning Agent

One role, not several — Project creation and Task decomposition are
sequential steps of the same planning phase. Fields reuse Harness's
existing Agent schema exactly (08-harness/01-definitions.md) — no
parallel schema invented.

| Field | Value |
|---|---|
| Agent Type | Assistant — always responds to a human-initiated (or Vetting-Agent-handed-off) request, never initiates a Project on its own |
| Capability Scope | Draft and edit Engagement Documents (Project/Task) only — explicitly excludes executing any change to a real system |
| Tool Permission Scope | Read: entire Anchor layer (governance, taxonomies, ontologies, conventions, org chart), the Agent/Skill Library, prior Engagement Documents for precedent. Write: the Engagement Document store only |
| Skills (composable, not hardcoded) | Project Scoping, Task Decomposition, Governance Mapping, Skill Library Lookup, Cost/Timeline Estimation, Documentation Drafting |
| Escalation Path | No matching governance or Skill found -> route to the Factory (new Skill) or a human Approver (new governance decision) — never guesses past that point |
| Own Risk Tier | Low (drafting only, no execution) — tracked separately from the Risk Tier of the Project it's drafting, which is computed from what that Project actually touches |
| Sandbox Tested | Required before org-wide trust — validated against sample requests first |
| Approval boundary | Drafts only. Every Engagement Document it produces still requires a human/Approver sign-off (CCAR-1/CCAR-2) before any Task's assigned Agent starts — never self-approves its own plan |

Separation of duties: the Planning Agent proposes; the human/Approver
reviews and signs off; only then do Task-level Worker Agents (templated
or dynamically composed) get spun up. Three distinct actors, never
collapsed into one — mirrors the Requester/Approver split (CCAR-2)
already enforced everywhere else in this framework.

## Agent Citizenship & Accountability Boundary {#eng-accountability-boundary}

Agents are first-class Participants
(06-participants-collaboration-and-channels.md): named, not a faceless
"system" actor; eligible for Responsible or Consulted RACI tags; able to
propose — including proposing direction and pushing back on a human's
framing; contributions carry the same provenance rigor in the
Collaboration Log as a human's.

**Deliberately not a new Agent Type.** An Agent taking on this kind of
advisory/strategic role stays Agent Type: Assistant
(08-harness/01-definitions.md's existing three values — Assistant,
Autonomous, Multi-Agent — are not extended); what distinguishes it is
Role Name and a wide Read Capability Scope across the Anchor layer, not
a new enum value. Keeps Harness's own schema untouched.

**Where it stops:** the Accountable RACI tag stays human for anything
at High risk tier — formalized as CCP-4 in cross-cutting/policies.md,
not left as an unenforced convention. Not because Agents reason poorly
about strategy, but because accountability is already a human-only
category everywhere else in this framework: CCAR-1/CCAR-2's
no-self-approval rule, the Requester/Approver split, Harness's own
Escalation Path pattern. An advisory-role Agent's Escalation Path
terminates at a human Approver before its proposed direction becomes
binding — the same shape as this Agent's own drafting boundary above,
not a new exception for a higher-status role.

Whether this line should ever flex below High risk tier is still open —
see 09-open-decisions.md #6.

**Quality bar check:**
- [x] Simple — one Agent role, reusing Harness's exact schema; the accountability rule is one cross-cutting policy, not a new mechanism
- [x] Modular — Advisory/strategic participation is a Role Name pattern, not a schema fork
- [x] Easy to update — CCP-4 lives in one place (cross-cutting/policies.md); every Engagement Document references it, none restate it
- [x] Easy to maintain — mirrors CCAR-1/CCAR-2 exactly, no separate rule to remember
- [x] Easy to replace — plain markdown table + one cross-cutting policy entry
