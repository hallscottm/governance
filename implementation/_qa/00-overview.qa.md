# Q&A Log — 00-overview
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-23 — Q10: How do we test this, and how/when do agents get built?

**Bucket:** [Judgment]/User-confirmed — direct question after the
Factory + CCAR-4 round: "how will we test this? how will we create the
agents to vet and create plan and how and when will we create template
agents and then create a project and have our system use or spin up
agents...and make stuff."

**Answer:** Everything built so far is spec, not a running system.
implementation/ is a new top-level area (not a domain, not
engagements/) that compiles Agent Library entries into real subagent
definitions and runs one pilot Engagement for real, to find where the
paper spec and a live run disagree. User confirmed: keep it in this
repo for now (Recommended option - traceability matters more than
separation during a single-person POC); explicitly flagged that in a
real org this would be a separate repo, and asked for that migration to
be possible later without a rewrite - addressed via the "nothing in
implementation/ is referenced back from governance content" design
note in 00-overview.md. Pilot scope confirmed: hand-build Vetting +
Planning Agents, run dq-metrics-dashboard for real.

**Applied to:** implementation/00-overview.md,
00-framework/domain-axis-definition.md (areas-outside-the-axis note).

**Status:** Pending explicit review.
