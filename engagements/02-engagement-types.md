# Engagements — Engagement Types

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

One shared Engagement Document schema (`eng-engagement-document`,
01-definitions.md), not seven separate templates. Engagement Type
(`eng-engagement-type`) is the field that drives which sections are
required vs. optional — seven templates would repeat most fields and
drift out of sync; one schema with type-driven requiredness stays
consistent and easier to extend.

| Engagement Type | ITIL 4 Practice | Project Document? | Task Documents? |
|---|---|---|---|
| Project | Change Enablement | Required | One or more |
| Maintenance | Service Configuration Management | Optional — a recurring maintenance program may wrap one | Yes, usually standalone |
| Monitoring & Alerting | Monitoring and Event Management | No — a standing configuration, not a bounded engagement (open, see 09-open-decisions.md #1) | N/A — defines what *triggers* Tasks, doesn't contain them |
| Incident Response | Incident Management | No | Yes, standalone, time-critical |
| Request / Ad Hoc | Service Request Management | No | Exactly one |
| Governance/Review | Continual Improvement | Optional — a recurring review program may wrap one | One per review cycle |
| Decommission | IT Asset Management | Required — same rigor as standing something up | One or more |

Documentation was considered as an 8th Engagement Type and deliberately
not added — it's the substrate every type produces (the Engagement
Document itself), not a peer category.

**Quality bar check:**
- [x] Simple — one table, 7 fixed rows
- [x] Modular — Project/Task applicability doesn't affect the shared schema underneath
- [x] Easy to update — a new type is one more row plus a question pack (05-intake-and-vetting.md), not a schema change
- [x] Easy to maintain — traces directly to a named ITIL 4 practice per row, no invented categories
- [x] Easy to replace — plain markdown table
