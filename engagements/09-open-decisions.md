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
3. **Skill Library and Agent Library** — open, next piece of work.
   Referenced throughout (`skill-lib/...`, `agent-lib/...`) but not yet
   designed. Model Catalog & Selection Criteria (#8, below) folds into
   this same pass.
4. **Where this lives in the repo** — resolved: `engagements/`, a
   top-level area alongside `00-framework/` and `cross-cutting/`, not a
   domain (00-framework/domain-axis-definition.md).
5. **The Factory itself** (draft -> sandbox -> eval -> approve ->
   register) — open, referenced repeatedly, not yet specced. Natural
   next piece after the Skill/Agent Library.
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
8. **Model Catalog & Selection Criteria** — open. Harness already has
   Model Version Pin (`harness-model-version-pin`) per Agent, but not
   the decision rubric (frontier vs. local, which model, why) it should
   be set from. Fold into the Skill/Agent Library pass (#3) — same
   shape of problem, one registry effort.
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
