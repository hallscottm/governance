# Harness Domain — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Same posture as every prior domain: capability categories only, no
specific product/vendor recommendations.

## Capability Categories

### Agent Orchestration / Runtime Platform
Hosts Agent execution, enforces Model Version Pin selection and Tool
Permission Scope at runtime, and runs on Infrastructure's Model-Serving
Node (`infra-model-serving-node`) / Inference Workload
(`infra-inference-workload`) categories (01-infrastructure/10-tooling.md).

### Prompt Management Platform
Version-controls System Prompts and Prompt Templates (05-conventions.md's
SemVer-based versioning), typically as an instance of the same SCM
Platform category Workflow/Process already selected
(07-workflow-process/10-tooling.md) rather than a separate tool.

### Guardrail / Content Filtering Platform
Implements Content Filter, Action Allowlist/Denylist, and Agent Rate
Limit enforcement (HPOL-4's automatic tightening).

### Eval Suite / Evaluation Platform
Runs Eval Suites, computes Eval Metrics, and detects Behavioral Drift —
enforces HPOL-1's and HPOL-2's passing-run requirements.

### Observability / Tracing Platform
Captures the Agent Trace/Transcript for every Agent Run, and is the
system of record Human-in-the-Loop Gate decisions, Guardrail violations,
and Override/Break-glass events are all logged to (HPROC-3, HPROC-4,
HPROC-5).

### Escalation / Human-in-the-Loop Platform
Routes a Human-in-the-Loop Gate to the applicable human per an Agent's
Escalation Path, and records the resulting Approval Gate — typically
integrated with Workflow/Process's Incident Management/On-Call Platform
(07-workflow-process/10-tooling.md) so an Agent's escalation reaches the
same on-call surface a human-initiated Incident would.

### Vector Database Platform (shared, not separately selected)
The same Vector Database Platform category already selected by Data
Platform (04-data-platform/10-tooling.md) — this domain's Retrieval
Source (`harness-retrieval-source`) is frequently backed by exactly that
category's platform. Listed here for discoverability, not as a fifth
independent selection.

---

**Cross-category dependency notes:**
- Agent Orchestration / Runtime Platform depends directly on
  Infrastructure's AI-Specific Compute categories, the same 4 terms this
  domain's Definitions column resolved from "Harness (pending — domains
  not yet built)" reference stubs.
- Prompt Management Platform is very often the same product as
  Workflow/Process's SCM Platform (a prompt template is just
  version-controlled text) — noted, not asserted as universal, same
  caveat Workflow/Process used for its own SCM/CI-CD bundling.
- Escalation / Human-in-the-Loop Platform is very often the same product
  as Workflow/Process's Incident Management/On-Call Platform — an
  Agent's escalation and a human-initiated Incident frequently share
  on-call tooling rather than each getting a dedicated platform.
- Vector Database Platform is explicitly the same selection Data Platform
  already made — not reselected here.

**Open items:**
- No capability category is defined here for Sandbox provisioning itself
  — cross-cutting/sandbox-activation.md's own Scope and Provisioning
  section already covers that (CCPROC-1, same provisioning flow every
  other resource uses), so this domain doesn't duplicate it with its own
  Sandbox tooling category.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 6 capability categories, no product lock-in
- [x] Modular — each category maps to a specific Policy/Procedure it implements
- [x] Easy to update — a category can be filled in with a specific product later without touching this structure
- [x] Easy to maintain — cross-category dependency notes explicitly connect to Infrastructure's, Workflow/Process's, and Data Platform's already-selected categories, none left dangling
- [x] Easy to replace — no product or model provider named, so no migration cost baked into the framework itself
