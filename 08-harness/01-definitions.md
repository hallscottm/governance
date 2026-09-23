# Harness Domain — Definitions

Status: Draft
Ratified: No
Last updated: 2026-09-23

Scope: how an AI agent is defined and scoped, prompted and given context,
guarded, observed and evaluated, and escalated to a human — the
mechanisms that let an organization run an AI agent (including one
building this framework) safely rather than the agent's own reasoning or
model weights, which are out of scope. Distinct from Cross-Cutting Roles &
Departments (`ccrole-ai-agent-harness`), which classifies an agent as a
System Actor within the org chart's permission model — this domain owns
the technical configuration that actor runs under. Distinct from
Workflow/Process's CI Runner/Agent (`wf-ci-runner`), a name-collision
flagged explicitly below rather than left implicit — a CI Runner/Agent is
compute that executes a Pipeline Stage; the Agent this domain defines is
an AI system that reasons and acts. Built fresh 2026-09-23, after
Standards Alignment (00-standards-alignment.md).

Anchor convention: `harness-<term-slug>`.

---

## Referenced Terms (owned elsewhere)

- **AI Agent/Harness (System Actor role)** — owned by Cross-Cutting Roles & Departments →
  [cross-cutting/roles-and-departments/01-definitions.md#ccrole-ai-agent-harness](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-ai-agent-harness) —
  that term is the org-chart/permission-boundary classification of an
  agent as a System Actor; this domain's Agent (below) is the technical
  configuration record that classification is applied to. Two views of
  the same thing, owned by different domains on purpose, same pattern
  used for Database (System Architecture's usage vs. Data Platform's
  ownership).
- **Sandbox** — owned by Cross-Cutting →
  [cross-cutting/sandbox-activation.md#cc-sandbox](../cross-cutting/sandbox-activation.md#cc-sandbox) —
  this domain's primary consumer, per that file's Primary Uses section:
  an Agent's Capability Scope and Guardrails are tested in a Sandbox
  before being granted against Production.
- **CI Runner/Agent** — owned by Workflow/Process →
  [07-workflow-process/01-definitions.md#wf-ci-runner](../07-workflow-process/01-definitions.md#wf-ci-runner) —
  name-collision boundary stated above; not the same concept as this
  domain's Agent.
- **Drift Detection (IaC state drift)** — owned by Workflow/Process →
  [07-workflow-process/01-definitions.md#wf-drift-detection](../07-workflow-process/01-definitions.md#wf-drift-detection) —
  distinct from this domain's Behavioral Drift (below), which is a
  model/agent concept, not an infrastructure-state one.
- **Inference Workload, Training Workload, GPU Memory (VRAM), Model-Serving Node** — owned by Infrastructure →
  [01-infrastructure/01-definitions.md#infra-inference-workload](../01-infrastructure/01-definitions.md#infra-inference-workload) —
  those 4 terms were marked "Referenced by: ... Harness (pending — domains
  not yet built)"; this domain is the resolution. An Agent (below) runs
  its Inference Workload on a Model-Serving Node.
- **Data Classification** — owned by Data/Metadata →
  [05-data-metadata/01-definitions.md#data-classification](../05-data-metadata/01-definitions.md#data-classification) —
  a Memory/State Store's contents (below) are classified using this
  domain's existing levels, not a Harness-specific scheme.

---

## Agent Definition & Scope

### Agent {#harness-agent}
An AI system configured to perceive input, reason over it, and take
action (respond, call a Tool, modify state) toward a goal, running under
a defined Capability Scope and Tool Permission Scope (below) — the
technical configuration record for what Cross-Cutting Roles & Departments
classifies as a System Actor (`ccrole-ai-agent-harness`). Source: Common
industry usage; aligned with NIST AI RMF's treatment of an AI system as
the unit of risk management.

### Agent Type {#harness-agent-type}
The interaction pattern an Agent (`harness-agent`) is configured for —
**Assistant** (responds to a human's direct request, does not act
without one), **Autonomous** (acts toward a goal across multiple steps
without a human request per step, subject to its Escalation Path), or
**Multi-Agent** (multiple Agents with distinct Capability Scopes
coordinate on a shared goal, e.g. one Agent delegating a sub-task to
another). Source: Common industry usage (no single named standard;
distinction is functional, not vendor-specific).

### Capability Scope {#harness-capability-scope}
The bounded set of tasks and Tool Permission Scope (below) an Agent is
configured to operate within — the record ISO/IEC 42001's required AI
system impact assessment resolves to at the instance level. An Agent
requesting or acting outside its Capability Scope is a Guardrail
violation (`harness-guardrail`). Source: ISO/IEC 42001 (AI Management
System).

### Tool Permission Scope {#harness-tool-permission-scope}
The specific set of Tools (functions, APIs, file/shell access, other
Agents) an Agent is permitted to invoke, and under what conditions (e.g.
read-only vs. read-write, which Environments per
`infra-environment-lifecycle`). The Capability Scope's what; this is its
how. Source: NIST SP 800-53 (AC family — Access Control), applied at
agent-instance granularity.

### Model Version Pin {#harness-model-version-pin}
The specific, identified model version (and, where applicable, a
specific Model-Serving Node deployment of it) an Agent is configured to
run on — pinned rather than "latest" so a Capability Scope grant and its
Eval Suite (below) results stay valid for a known, unchanging model
behavior until deliberately re-evaluated. Source: Common ML industry
practice (model/version pinning, analogous to `sysarch-semver` pinning
for software dependencies).

---

## Prompting & Context Management

### System Prompt {#harness-system-prompt}
The instructions provided to an Agent before any user or task input,
establishing its role, Capability Scope, and behavioral constraints for
the session — the primary mechanism by which a Guardrail (below) is
expressed to the model itself, as opposed to enforced externally by
tooling. Source: Common industry usage.

### Prompt Template {#harness-prompt-template}
A reusable, parameterized structure for constructing a System Prompt or
a task-specific prompt, so that prompt content is version-controlled and
consistent across Agent Runs rather than authored ad hoc per use.
Version-controlled the same way `wf-repository` version-controls source
code. Source: Common industry practice.

### Context Window Budget {#harness-context-window-budget}
The allocated portion of an Agent's model Context Window (the maximum
input the model can process at once) reserved for each input source —
System Prompt, conversation history, Retrieval Source results, tool
output — so that no single source can silently crowd out the others.
Source: Common ML industry practice.

### Retrieval Source {#harness-retrieval-source}
An external knowledge source (a document store, a Database per
`dp-database`, a search index) an Agent queries to ground its reasoning
in information outside its Model Version Pin's training data (commonly
"RAG," retrieval-augmented generation). Source: Common ML industry
practice.

### Memory/State Store {#harness-memory-store}
Persistent storage an Agent reads from and writes to across separate
Agent Runs (distinct from a single run's Context Window, which does not
persist) — its contents are classified using Data/Metadata's existing
Data Classification levels (`data-classification`), same as any other
stored data. Source: Common ML industry practice.

---

## Guardrails & Safety Controls

### Guardrail {#harness-guardrail}
A control — enforced in the System Prompt, in surrounding tooling, or
both — that constrains what an Agent can do or say, independent of what
the underlying model would otherwise produce. The general concept this
subdomain's other terms (Content Filter, Action Allowlist/Denylist,
Human-in-the-Loop Gate) are specific instances of. Source: NIST AI RMF
(Manage function); OWASP Top 10 for LLM Applications.

### Content Filter {#harness-content-filter}
A Guardrail that inspects an Agent's input or output against defined
categories (e.g. harmful content, PII, secrets) and blocks, redacts, or
flags a match. Source: OWASP Top 10 for LLM Applications (Sensitive
Information Disclosure, Insecure Output Handling categories).

### Agent Rate Limit {#harness-rate-limit}
A Guardrail bounding how many actions, Tool calls, or Agent Runs an
Agent may perform within a time window — distinct from any
Infrastructure-level request rate limit (a capacity control); this one
is a safety control, bounding blast radius from a misbehaving or looping
Agent regardless of available capacity. Source: Common industry practice;
OWASP Top 10 for LLM Applications (Unbounded Consumption, Excessive
Agency categories).

### Action Allowlist/Denylist {#harness-action-allowlist}
A Guardrail explicitly naming which specific actions (Tool calls,
destructive operations, external communications) an Agent may or may not
take, independent of its broader Tool Permission Scope — the fine-grained
instance-level control underneath that coarser grant. Source: OWASP Top
10 for LLM Applications (Excessive Agency category).

### Human-in-the-Loop Gate {#harness-hitl-gate}
A Guardrail requiring explicit human approval before an Agent's proposed
action is carried out — the general mechanism; Approval Gate (below,
Escalation & Human-in-the-Loop subdomain) is the record of one specific
approval decision made at one of these gates. Source: NIST AI RMF
(Govern function — human oversight); common industry practice.

---

## Observability & Evaluation

### Agent Trace/Transcript {#harness-trace}
The complete, ordered record of an Agent Run's inputs, reasoning steps,
Tool calls, and outputs — the audit record a Human-in-the-Loop Gate
decision or a post-incident review is made against, analogous to
`wf-pipeline-run`'s log for a CI/CD Pipeline. Source: NIST SP 800-53 (AU
family — Audit and Accountability), applied at agent-instance
granularity.

### Eval Suite {#harness-eval-suite}
A defined, repeatable set of test cases run against an Agent (and its
pinned Model Version, `harness-model-version-pin`) to measure its
behavior before a Capability Scope grant is widened or a Model Version
Pin is changed — the agent-specific analogue of `sysarch-unit-test`/
`sysarch-integration-test`, run against reasoning and behavior rather
than code. Source: Common ML industry practice; NIST AI RMF (Measure
function).

### Eval Metric {#harness-eval-metric}
A single measured dimension an Eval Suite reports (e.g. task success
rate, refusal rate, groundedness against a Retrieval Source) — the
per-metric result that, in aggregate, an Eval Suite Run produces. Source:
Common ML industry practice.

### Behavioral Drift {#harness-behavioral-drift}
A detected change in an Agent's outputs or Eval Metric results over time
without a corresponding Model Version Pin change — signals that
something in the Agent's environment (a Retrieval Source's contents, an
upstream API, a subtly-changed System Prompt) shifted its behavior.
Distinct from Workflow/Process's Drift Detection (`wf-drift-detection`),
which detects infrastructure *state* diverging from its IaC definition,
not model/agent *behavior* diverging from its evaluated baseline. Source:
Common ML industry practice (model monitoring / drift detection).

### Cost-per-Task {#harness-cost-per-task}
The measured compute/inference cost (traceable to an Inference Workload,
`infra-inference-workload`) an Agent consumes to complete one task or
Agent Run — tracked alongside Eval Metrics so a Capability Scope decision
can weigh capability against cost, not capability alone. Source: Common
industry practice (FinOps principles applied to AI workloads).

---

## Escalation & Human-in-the-Loop

### Escalation Path {#harness-escalation-path}
The defined sequence of who (or what Human-in-the-Loop Gate) an Agent's
request for help, ambiguous situation, or Guardrail violation is routed
to, when the Agent cannot or should not resolve it autonomously —
mirrors `ccrole-approver`'s role in Workflow/Process's Change Request
flow, applied here to an Agent-initiated rather than human-initiated
request. Source: NIST AI RMF (Govern function — human oversight).

### Approval Gate (Agent-Triggered) {#harness-approval-gate}
A specific, recorded instance of a Human-in-the-Loop Gate
(`harness-hitl-gate`) being reached and resolved (approved, denied, or
modified) by a human — distinct from Workflow/Process's Deployment Gate
(`wf-deployment-gate`), which gates a Pipeline's promotion between
Environments rather than a single Agent action. Source: Common industry
practice.

### Override/Break-glass {#harness-override}
An Agent action taken outside its normal Capability Scope or Guardrails
under an explicit, logged human override, for situations an Escalation
Path is too slow to resolve — the same Break-glass/override concept
Workflow/Process's 09-risk-tiers.md flagged as a "process, not resource"
Risk Tier factor and explicitly noted to watch for here, now formally
defined. Source: Common industry practice (break-glass access pattern).

### Agent-Caused Incident Classification {#harness-agent-incident}
A classification applied to an Incident (`wf-incident`) whose root cause
was an Agent's own action (as opposed to a human error, infrastructure
failure, or external event) — recorded on the Incident so that
Post-Incident Review (`wf-postmortem`) and this domain's Eval Suite can
both draw on it: the former for process learning, the latter as a
candidate new test case. Source: Common industry practice; NIST AI RMF
(Manage function).

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one file, five subdomains, 24 terms
- [x] Modular — each term owned once; Roles & Departments', Sandbox's,
      Workflow/Process's, Infrastructure's, and Data/Metadata's terms
      referenced, not restated
- [x] Easy to update — a new guardrail/eval concept adds a term without
      touching existing ones
- [x] Easy to maintain — single owner per term, DRY via reference stubs;
      two name-collision boundaries (Agent vs. CI Runner/Agent;
      Behavioral Drift vs. Drift Detection) stated explicitly rather than
      left implicit
- [x] Easy to replace — no model provider, agent framework, or eval
      platform named as the definition of a concept (examples only,
      where given)
