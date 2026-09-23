# Engagements — Open Decisions

Status: Draft — tracked, not blocking
Ratified: No
Last updated: 2026-09-23

Carried over from the review pass (a Claude Docs draft, reviewed before
being written here). Resolved items are marked; open ones still need
your call.

1. **Monitoring & Alerting's "no Project Document" treatment** — open.
   Does a standing monitoring configuration need any wrapper document
   at all, or does it live entirely as configuration on the resource it
   watches? (02-engagement-types.md)
2. **YAML front matter + Markdown body format** — resolved by use:
   adopted throughout 03/04.
3. **Skill Library and Agent Library** — resolved: see
   10-skill-library.md and 11-agent-library.md. Build-on-Demand
   Principle answers the earlier "predict vs. compose fresh" question
   (neither — build on first genuine need, register on reuse).
4. **Where this lives in the repo** — resolved: `engagements/`, a
   top-level area alongside `00-framework/` and `cross-cutting/`, not a
   domain (00-framework/domain-axis-definition.md).
5. **The Factory itself** — resolved: see 13-factory.md. Factory Agent
   role, Factory Run = an ordinary Task Document (no new schema),
   standing Factory Project deferred (Build-on-Demand), explicit
   `attempt_count` field for retry tracking, deliberate Library re-check
   redundancy confirmed intentional.
6. **Agent Accountability boundary** — resolved as a floor, open at the
   edges: CCP-4 (cross-cutting/policies.md) fixes Accountable as
   human-only at High risk tier. Open whether that's a bright line at
   every risk tier, or whether an Agent could ever be Accountable at
   Low.
7. **Post-POC: multi-tenant productization** — flagged, not scoped,
   explicitly out of scope until this POC is solid. Intent: a
   repeatable, largely agent-automated way to extract another
   organization's own governance, policies, ontologies, and
   institutional knowledge into this same structure quickly, without
   losing detail.
8. **Model Catalog & Selection Criteria** — resolved: see
   12-model-catalog.md. Add/Update/Deprecate triggers defined; approver
   is `ccrole-security-compliance` (Infrastructure Admin consulted on
   cost, not approving).
10. **"Close enough" threshold** — resolved: Capability Scope and
    Tool Permission Scope must match exactly for a Skill/Agent Template
    to count as reusable; Skills invoked may differ/be a subset; Model
    Version Pin never factors into the match (Selection Criteria sets
    it per-Task independently). Role Name is a label, not part of the
    test.
11. **Deprecation policy** (Skill/Agent/Model) — resolved: never a hard
    delete. Three triggers — provider/dependency retirement,
    Behavioral Drift or repeated Eval failure (auto-flags for review,
    parallels HPOL-4), or superseded-and-unused (`used_by` empty).
    `status: deprecated` blocks new Lookups; existing references keep
    their historical record.

9. **A2A protocol** — resolved for now: not adopted. All Agents share
   one harness and one owner; internal coordination is the
   Collaboration Log + orchestrator pattern. Revisit only if #7
   (productization) has this framework's Agents talking to another
   organization's existing agent stack. Already flagged as a future
   candidate in 08-harness/00-standards-alignment.md.

**Quality bar check:**
- [x] Simple — one running list, resolved items marked in place rather than deleted
- [x] Modular — each item traces to the specific file it affects
- [x] Easy to update — append, don't rewrite; same append-only discipline as `_qa` logs
- [x] Easy to maintain — nothing here duplicates content decided elsewhere
- [x] Easy to replace — plain markdown list
