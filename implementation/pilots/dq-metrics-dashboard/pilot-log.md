# Pilot Log — dq-metrics-dashboard (Run 1)

Date: 2026-09-23
Compiled agents used: implementation/agents/vetting-agent.md,
implementation/agents/planning-agent.md
Raw request: Slack DM from J. Rivera, "stand up an internal dashboard
summarizing weekly data-quality metrics."

## What happened

1. **Vetting Agent run** (real subagent, real system prompt, no repo
   write access beyond the Intake Brief path). Produced
   `intake-brief.yaml`. Stayed in scope: did not resolve engagement-type
   ambiguity itself, did not guess the source data system, did not
   start scoping the dashboard. Since no human was available mid-run to
   answer a follow-up question, it logged unresolved fields to
   `open_gaps` instead of blocking — a deliberate, documented deviation
   from "ask a human directly," necessary for this pilot only.

2. **Planning Agent run** (real subagent, given the Intake Brief, real
   read access to the Anchor layer and Library via the repo). Produced
   `project-document.md` and 4 Task Documents, `status: proposed`
   throughout, no self-approval. Independently re-derived
   `engagement_type: Project` from `02-engagement-types.md` rather than
   deferring to the brief's recommendation. Left every field it
   couldn't support open, with a stated reason, rather than guessing.

## Findings — things the paper spec didn't anticipate

**1. The Skill/Agent Library and Model Catalog are genuinely empty.**
`engagements/10-skill-library.md`, `11-agent-library.md`,
`12-model-catalog.md` are schema-only — no populated rows. The
`agent-lib/bi-analyst-developer-v1` and `skill-lib/build-bi-report-v3`
ids used in `08-worked-example.md` and `13-factory.md` are illustrative
narrative, not real registered entries. This is *expected* under
Build-on-Demand (nothing gets pre-built), and the Planning Agent handled
it correctly — it drafted two Factory Run Task Documents instead of
inventing entries. But it means the worked example's Project Document
was never actually reachable from a cold start; a real first-ever
Project always has to route through the Factory first. Worth stating
explicitly somewhere in 08-worked-example.md so it doesn't read as if
the reference already existed. **Not fixed yet — flagged for a
decision on whether/where to note this.**

**2. Risk Tier conflict, BI/Reporting domain vs. cross-cutting
narrative — a real finding, not resolved by this pilot.**
`06-bi-reporting/09-risk-tiers.md`'s Determining Factors table puts
Environment = Production in the **High** column by itself (maximum-tier
rule). `cross-cutting/risk-tiers.md`'s general interpretation text says
"most Production resources" land at **Moderate**. Taken literally, the
domain table is the authoritative mechanism (`cross-cutting/risk-tiers.md`
says so directly — the domain table computes the tier, cross-cutting's
text is descriptive framing) — so *any* Production BI report would be
High risk tier under a strict reading, which seems too aggressive for
an internal, no-PII, internally-distributed dashboard like this one.
The Planning Agent flagged the tension rather than silently picking a
side (correct behavior per its Escalation Path — "no matching
governance found, stop and name it"). This needs your call:
  - Is Environment=Production alone genuinely meant to force High for
    every BI/Reporting resource, or
  - is Environment supposed to combine with the other factors (not
    override them), meaning the domain table's phrasing needs a small
    correction to avoid reading as "any single High factor wins
    regardless of the others."
  Not fixed yet — this is domain content, not implementation content,
  so it belongs in `06-bi-reporting/`, not here.

**3. Owning Team Lead has no analog for a Report/Dashboard entity.**
`owning_team_lead`'s role definition is scoped to
Service/Application/API/Database. A Report/Dashboard isn't one of
those. The Planning Agent left the field open rather than force-fitting
a person into a role definition that doesn't cover this entity type.
Minor - likely just needs the role definition's entity list extended
in `cross-cutting/roles-and-departments/`, or an explicit note that
Report/Dashboard entities don't get this field. Not fixed yet.

**4. `source_control_and_delivery`'s trigger condition is broader than
its stated intent.** The block's own comment says it exists for
code/config/infrastructure deliverables, but its literal trigger
(`applicable_domains` includes Data Platform) fires for this Project
too, even though a BI dashboard has no repository/CI/CD/IaC of its own.
The Planning Agent filled the block with everything left open rather
than skip it (following the literal trigger) — technically compliant,
but produces a mostly-empty block that adds noise. Worth tightening the
trigger condition to name the domains more precisely, or explicitly
listing Data Platform as "only when the deliverable itself is
code/config," not "whenever this domain merely applies." Not fixed
yet.

**5. The Factory Agent has not actually been compiled yet.**
`implementation/agents/` only has `vetting-agent.md` and
`planning-agent.md`. The Factory Run Task Documents this pilot produced
describe what needs building but nothing can actually execute them
until a real Factory Agent subagent definition exists. Expected — not a
finding against the spec, just the next piece of this pilot.

## What this run validated

- The Capability Scope / Tool Permission Scope language in
  `engagements/05` and `07` was concrete enough to compile into a real
  system prompt without inventing anything.
- Both agents held their scope boundary under real conditions (see each
  agent's self-reported "moments I was tempted to go outside scope" in
  this run's raw output) without being told to.
- The Escalation Path pattern ("stop and name it" rather than guess)
  worked exactly as designed when the Library turned out to be empty
  and when risk-tier guidance conflicted.
- Neither agent self-approved anything; `approved_by` is blank
  everywhere it should be.

## Not yet tested (next pilot steps)

- A real human Approval Gate on this Project Document (CCAR-1/2/4) —
  this run stopped at `status: proposed`, by design.
- The Factory Agent actually running (needs compiling first).
- Sandbox execution of a Task once an Agent/Skill exists for real.

## Run 2 (2026-09-23) — Task 1 and Task 2 actually executed

Both remaining Tasks closed for real, not just drafted:

- **dq-dash-t1-define-metrics:** resolved by direct human decision
  (hallscottm@gmail.com) standing in for the fictional J. Rivera/BI
  Analyst participants - source: skill-lib/dq-metrics-dummy-data-generator-v1
  (no real DQ-check source connected), Distribution Scope: Internal.
- **dq-dash-t2-build-report:** the report was built - a self-contained
  HTML dashboard at implementation/pilots/dq-metrics-dashboard/report/dq_dashboard.html,
  also published as a Claude artifact. **Honest deviation, not hidden:**
  the Task's real dependencies (factory-run-bi-report-builder-agent,
  factory-run-build-bi-report-skill) were skipped - no Agent Template or
  Skill was actually built and registered through the Factory process
  this framework prescribes. The orchestrating session built the report
  by hand instead. This is the same "why is the orchestrator doing so
  much work" gap already named in implementation/00-overview.md, now
  with a second concrete instance: getting an actual deliverable in
  hand was prioritized over running the full prescribed process for a
  one-off pilot report. Worth a real decision before this pattern
  repeats on non-pilot work: either build the Report Builder
  Agent/Skill for real next time, or decide by-hand orchestrator
  execution is an accepted path for low-risk, Internal-scope work and
  say so explicitly in engagements/13-factory.md rather than leaving it
  implicit.
