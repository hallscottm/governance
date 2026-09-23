# Engagements — Worked Example (abridged)

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Request: *"Stand up an internal dashboard summarizing weekly
data-quality metrics."*

## Project Document excerpt

```yaml
project_id: dq-metrics-dashboard
engagement_type: Project
status: approved
owning_department: ccdept-business-intelligence-analytics
risk_tier: Low
applicable_domains: [04-data-platform, 05-data-metadata, 06-bi-reporting]
applicable_policies: [BIPOL-1, BIPOL-4]
sandbox_required: false
participants:
  - name: J. Rivera
    kind: human
    role: Requester
    raci: Accountable
  - name: BI Report Builder Agent
    kind: agent
    role: Report implementation
    raci: Responsible
agents_required:
  - role_name: BI Report Builder Agent
    templated_agent_used: agent-lib/bi-analyst-developer-v1
    capability_scope: read dp-semantic-layer, write bi-report-data-model
tasks: [dq-dash-t1-define-metrics, dq-dash-t2-build-report]
```

## Task Document excerpt (dq-dash-t2-build-report)

```yaml
task_id: dq-dash-t2-build-report
parent_project: dq-metrics-dashboard
skills_invoked: [skill-lib/build-bi-report-v3]
knowledge_references: [bi-certified, bi-row-level-security]
risk_tier: Low
approval_required: false
dependencies: [dq-dash-t1-define-metrics]
```

Notice what *didn't* need re-deriving: the BI Report Builder role, its
Capability Scope, and the report-building Skill are shown here already
registered in the Agent/Skill Library. **Illustrative, not live:** as of
2026-09-23 the Library (10-skill-library.md, 11-agent-library.md) is
genuinely empty — Build-on-Demand means nothing gets pre-populated.
`agent-lib/bi-analyst-developer-v1` and `skill-lib/build-bi-report-v3`
show the *reference* shape once they exist, not a claim that they do
yet; a real first run of this Project routes through the Factory
(13-factory.md) first — see implementation/pilots/dq-metrics-dashboard/
for that actual run. That's still the efficiency payoff this whole area
is for: once built once, most Engagements after the first should read
like this, mostly references, not fresh reasoning every time.

**Quality bar check:**
- [x] Simple — one abridged example, both document types
- [x] Modular — swapping the Agent/Skill referenced doesn't change the template shape
- [x] Easy to update — a second worked example is additive, not a rewrite
- [x] Easy to maintain — traces to real anchors used elsewhere (ccdept-*, real policy IDs)
- [x] Easy to replace — plain YAML
