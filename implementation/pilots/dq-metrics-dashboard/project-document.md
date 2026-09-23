# Project Document — dq-metrics-dashboard

Drafted independently from the Intake Brief and the real Anchor/Library
content by the Engagement Planning Agent, per engagements/07 scope. Not
copied from engagements/08-worked-example.md — see the comparison note
in implementation/pilots/dq-metrics-dashboard/pilot-log.md (this Agent's
report to its caller) for how this draft was checked against it after
the fact.

## Front matter

```yaml
project_id: dq-metrics-dashboard
engagement_type: Project
status: proposed
created_by: Engagement Planning Agent + J. Rivera
created_date: 2026-09-23
last_updated: 2026-09-23

owning_department: ccdept-business-intelligence-analytics
owning_team_lead: OPEN — no instance named. ccrole-owning-team-lead
  (cross-cutting/roles-and-departments/01-definitions.md) is scoped
  narrowly to a Service/Application/API/Database's Owning Team metadata
  field (03-system-architecture); a Report/Dashboard has no equivalent
  named-individual field in 06-bi-reporting/04-metadata-standards.md —
  the closest analog is "Report Owner" (Business Analyst/Report Builder
  or BI Analyst/Developer), also not yet named in the Intake Brief.
  Human decision needed: name a Report Owner, or confirm Owning Team
  Lead genuinely doesn't apply to this entity type.
requester: J. Rivera (ccrole-requester)
approver: OPEN — no human Approver named yet. Per CCAR-2 this must be a
  human distinct from J. Rivera (the Requester). Must be assigned before
  any Task's approval_required gate can be satisfied.

risk_tier: Moderate   # computed — see Reasoning below; diverges from
  the abridged worked example's "Low" and the divergence is deliberate,
  not an error — see Reasoning.
cost_center_tag: OPEN — not provided anywhere in the Intake Brief; CCP-2
  hard-blocks provisioning of any real resource without one. Needed
  before Task 2 (build) can move past Draft/Sandbox.
target_timeline: "before end of quarter" (~2026-09-30) — explicitly
  flagged by the Intake Brief as a soft preference, NOT confirmed as a
  firm commitment. Carried forward as unconfirmed, not asserted as a
  real deadline.

applicable_domains: [04-data-platform, 05-data-metadata, 06-bi-reporting]
applicable_policies: [BIPOL-1, BIPOL-4, DPPOL-5, CCP-1, CCP-2, CCP-4]
  # BIPOL-1 (Certified status required for broad distribution) and
  # BIPOL-4 (refresh schedule required for any Data Extract) both
  # confirmed independently against 06-bi-reporting/06-policies.md.
  # DPPOL-4/DPPOL-1/DPPOL-2/DPPOL-3 checked and do not apply (no schema
  # migration, streaming, vector DB, or lakehouse table-format work
  # here). DPPOL-5 (Semantic Layer as sole source for Certified
  # Metrics) added beyond the worked example — relevant if this
  # dashboard is ever certified, since BIPOL-1 requires Certified
  # status for anything beyond Internal/Departmental scope and the
  # audience is still unconfirmed (see open items). CCP-1/CCP-2 apply
  # as cross-cutting baseline (Production Metadata Completeness, Cost
  # Attribution); CCP-4 applies because this Project names an Agent
  # participant and risk_tier is Moderate, not Low, so CCP-4's
  # human-only Accountable floor plainly applies regardless of how
  # open decision #6 eventually resolves.
applicable_taxonomy_terms:
  - data-quality (05-data-metadata/01-definitions.md#data-quality)
  - data-quality-rule (05-data-metadata/01-definitions.md#data-quality-rule)
  - dp-semantic-layer (04-data-platform/01-definitions.md#dp-semantic-layer)
  - bi-dashboard (06-bi-reporting/01-definitions.md#bi-dashboard)
  - bi-report-data-model (06-bi-reporting/01-definitions.md#bi-report-data-model)
  - bi-certified (06-bi-reporting/01-definitions.md#bi-certified)
  - bi-data-extract (06-bi-reporting/01-definitions.md#bi-data-extract)
  - bi-refresh-schedule (06-bi-reporting/01-definitions.md#bi-refresh-schedule)
applicable_conventions:
  - 06-bi-reporting/05-conventions.md — Report/Dashboard Naming
    Convention (`[<status>] <Domain> - <Subject> (<audience/scope>)`).
    Working title until Distribution Scope is confirmed:
    "BI - DQ Weekly Metrics (Departmental)" — bracketed status omitted
    (not yet Certified); audience segment is a placeholder, not
    confirmed (see open items).
sandbox_required: true
  # Ties to cc-sandbox / HPOL-1: the Agent Template and Skill this
  # Project needs do not exist yet in the real Library (see Reasoning)
  # and must be Sandbox-tested before any Production-scoped grant.

storage_location: OPEN — the BI tool/platform that will host the
  dashboard is not named anywhere in the Intake Brief (open_gap #2 in
  the Intake Brief itself). Cannot be filled without guessing.

source_control_and_delivery:
  # Note on applicability: applicable_domains includes Data Platform,
  # which literally triggers this block's "required" condition per
  # 03-project-document-template.md's own comment. But the template's
  # parenthetical clarifies the intent is "a deliverable that is code,
  # config, or infrastructure" — and nothing here is being built as
  # code/infra; this Project reads existing Data Platform output, it
  # doesn't provision Data Platform resources. Filling this block
  # anyway, per the literal trigger, but every sub-field is genuinely
  # unknown rather than guessed — flagged as an open tension between
  # the literal field-trigger rule and its stated intent, worth a
  # human/template-author decision, not resolved unilaterally here.
  repository:
    name: OPEN — not applicable unless the BI tool's report definition
      is itself source-controlled (tool not yet named).
    location: OPEN
    scaffolding_template: OPEN
    branching_strategy: OPEN
  ci_cd:
    pipeline: OPEN
    deployment_gates: []
    rollback_plan: OPEN — required once risk_tier is Moderate/High per
      the template's own comment; risk_tier here IS Moderate, so this
      must be resolved before Task 2 can reach approval, not left open
      indefinitely.
  iac:
    used: false   # no infrastructure is being provisioned by this Project
    state_file_location: null
    plan_review_required: false

participants:
  - name: J. Rivera
    kind: human
    role: Requester
    raci: Accountable
  - name: BI Report Builder Agent
    kind: agent
    role: Report/dashboard implementation
    raci: Responsible

tools_and_mcp_servers: OPEN — Intake Brief open_gaps flags that the
  source system(s) producing the existing DQ checks, and the intended
  BI/dashboard tool, are both unnamed. Cannot be filled without asking
  the Requester.
tool_configurations: OPEN — depends on tools_and_mcp_servers above.

workflow_pattern: sequential
  # Task 1 (define metrics) -> two Factory Runs (Agent + Skill, can run
  # in parallel with each other but both gate Task 2) -> Task 2 (build).
  # Not orchestrator-workers: there is exactly one execution Agent
  # (BI Report Builder Agent) plus the pre-built Factory Agent, not a
  # pool of workers under one orchestrator.

agents_required:
  - role_name: BI Report Builder Agent
    templated_agent_used: NOT FOUND. engagements/11-agent-library.md
      was read directly and contains only the schema/lifecycle
      definition — zero populated entries. The
      "agent-lib/bi-analyst-developer-v1" id referenced in
      engagements/08-worked-example.md is illustrative narrative only,
      not a real registered Library row. Per this Agent's explicit
      scope boundary, this is a Factory escalation, not something
      drafted around — see factory-run-bi-report-builder-agent.md.
    capability_scope: "Read: dp-semantic-layer and/or the existing
      Data Quality check outputs named in Task 1's findings (source
      system currently unconfirmed). Write: bi-report-data-model,
      bi-dashboard — Draft Certification Status only until BIAR-1
      review."
    tool_permission_scope: OPEN — set by the Factory's draft, confirmed
      by Sandbox testing, finalized only at human Approval.
    prompt_template: OPEN — Factory output, not invented here.
    escalation_path: "Factory Agent draft -> Sandbox (HPOL-1) -> Eval
      Suite -> human Approver (CCAR-1/CCAR-2), per engagements/13-factory.md."
    model_version_pin: OPEN. engagements/12-model-catalog.md was read
      directly and also contains only the schema/rubric — zero
      populated Catalog entries. Per that file's own Selection
      Criteria ("No match -> ask a human, don't guess a model"), this
      is left open rather than asserted.
    sandbox_tested_flag: false

tasks:
  - dq-dash-t1-define-metrics
  - factory-run-bi-report-builder-agent
  - factory-run-build-bi-report-skill
  - dq-dash-t2-build-report
```

## Body

### Goal / Objective
Give the BI/analytics team a recurring, low-effort way to see their own
weekly data-quality metrics — a dashboard they check each Monday,
built entirely on data their existing DQ checks already produce. No new
DQ checks, rules, or monitoring logic are created by this Project; it
is a presentation layer over an existing signal.

### Scope boundary
**In scope:** confirming which existing DQ check outputs feed the
dashboard; defining the metric set and refresh cadence; building and
(if warranted) certifying a Report/Dashboard entity presenting them.
**Out of scope:** building or modifying any Data Quality Rule
(`data-quality-rule`) itself; building new data pipelines; anything
beyond a read path from wherever the existing checks already write
their output.

### Definition of Done
- The two data-facing open_gaps from the Intake Brief are resolved
  (source system named; audience/Distribution Scope confirmed) — Task 1.
- A BI Report Builder Agent capability exists, Sandbox-tested, and is
  Approved for Production use — Factory Run tasks.
- A Dashboard entity exists, populated from the confirmed metrics,
  meeting BIPOL-4 (declared Refresh Schedule) at minimum; BIPOL-1/
  BIPOL-2 (Certified status) only if Distribution Scope ends up wider
  than Internal — Task 2.
- A named human Report Owner and Approver are on record (currently open
  items above).

### Stakeholders
- J. Rivera — Requester, and the team that will actually consume the
  dashboard weekly.
- BI Analyst/Developer (ccrole-bi-analyst-developer) — the role that
  would review/certify per BIAR-1 if Distribution Scope reaches
  Departmental+ with Confidential+ underlying sensitivity, or reaches
  Org-wide/External at all (BIPOL-1).
- Whoever owns the source system producing the existing DQ checks
  (unnamed — open item) — Consulted, once identified.

### Reasoning
**Engagement Type — decided independently, not deferred to the
Intake Brief's recommendation.** engagements/02-engagement-types.md's
own table caps Request/Ad Hoc at "Exactly one" Task Document. This
work genuinely decomposes into more than one sequenced Task (define
metrics, then build) even before the Library gap forced two more
(the Factory Runs) — so Request/Ad Hoc is structurally the wrong fit
regardless of how "simple" the ask reads informally. Project is the
only Engagement Type this decomposition satisfies. This independently
reaches the same answer the Intake Brief recommended, but on the
Engagement Type table's own stated rule, not by deferring to the brief.

**risk_tier — computed, and it diverges from the worked example.**
Using 06-bi-reporting/09-risk-tiers.md's Determining Factors table
directly:
- Sensitivity Level/PII: nothing in the Intake Brief suggests the DQ
  metrics themselves carry PII or above Internal sensitivity -> Low on
  this factor.
- Distribution Scope: unconfirmed (open item); "the team" reads as
  Internal or Departmental, not Organization-wide/External -> at most
  Moderate on this factor, pending Task 1 confirming it.
- Certification Status: not applicable pre-build.
- **Environment: unconfirmed, and this is the genuinely ambiguous
  factor.** A dashboard the team checks every Monday is, once live, an
  operational/Production artifact by ordinary use — but nothing in the
  Intake Brief confirms it will be provisioned as Production rather
  than staying in a Staging/QA-equivalent state. The domain's own
  factor table maps Environment=Production directly to the **High**
  column, which sits in tension with cross-cutting/risk-tiers.md's own
  "General Interpretation" column, which describes "Most Production
  resources" as **Moderate**, reserving High for resources with
  regulated/highly-sensitive data or severe-consequence failure modes
  — neither of which applies here. Given that tension, and that every
  other known factor here tops out at Moderate, Moderate is the more
  defensible computed tier — but this is flagged explicitly as an
  ambiguity in the framework's own documents (a literal table-cell
  reading vs. its own general-interpretation guidance), not resolved
  by this Agent past that point. A human Approver should confirm
  Environment before this tier is locked in for Approval.

**Why the abridged worked example shows Low:** most likely because it
never showed its Determining-Factor computation (it's explicitly
abridged) and/or implicitly assumed Internal-only scope and a
non-Production/staging environment throughout. That's a plausible read,
not confirmed — flagged as a real, unresolved divergence rather than
silently overridden in either direction.

**Agent/Skill Library — genuinely not populated.** Both
engagements/10-skill-library.md and engagements/11-agent-library.md
were read directly; each contains only its schema, Build-on-Demand
principle, and lookup/escalation process — no actual registered rows.
A repo-wide search for "bi-analyst-developer" and "build-bi-report"
turns up those exact strings only in engagements/08-worked-example.md
(the abridged narrative example) and engagements/13-factory.md (its
own worked example of the Factory process) — never in the Library
files themselves. Per this Agent's explicit scope boundary ("do not
invent a new Agent/Skill entry yourself... if nothing matches, that is
a Factory escalation"), that's exactly what this draft does: Task 2
depends on two new Factory Run Tasks rather than referencing those ids
as if they already existed.

**Model Catalog — same situation.** engagements/12-model-catalog.md is
also schema-only, zero populated entries. `model_version_pin` is left
open throughout rather than guessed, per that file's own Selection
Criteria.

### Approval log
(none yet — `status: proposed` throughout this Project and every Task
in it; no Approver has signed off on anything here.)

### Collaboration Log
- 2026-09-23 — Engagement Planning Agent: drafted this Project
  independently from the Intake Brief and real Anchor/Library content,
  then compared against engagements/08-worked-example.md. See this
  pilot's log for the full comparison and the ambiguities surfaced
  above (risk_tier computation, owning_team_lead's fit for a
  Report/Dashboard entity, and the empty Agent/Skill/Model
  registries). Open items above need a human (J. Rivera or a
  designated Approver) before any Task here can proceed past
  `proposed`.
