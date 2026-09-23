# Harness Domain — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Reference panel for this domain, consulted before drafting Definitions —
built fresh, same order used for Workflow/Process. Scope per
00-framework/domain-axis-definition.md: how AI agents are defined, scoped,
prompted, guarded, observed, and escalated to a human. Both standards
below were flagged as deferred back when System Architecture's own
Standards Alignment was drafted, explicitly reserved for this domain.
Five subdomains this pass covers: Agent Definition & Scope, Prompting &
Context Management, Guardrails & Safety Controls, Observability &
Evaluation, and Escalation & Human-in-the-Loop.

| Standard | Body | Covers |
|---|---|---|
| **NIST AI Risk Management Framework (AI RMF 1.0)** | NIST | The primary source for this domain's risk vocabulary — Govern/Map/Measure/Manage functions ground this domain's Guardrail, Eval, and Risk Tier concepts; NIST's own AI RMF Generative AI Profile (NIST-AI-600-1) is the closest existing precedent for agent-specific risk factors (the "process, not resource" Risk Tier factors Workflow/Process's 09-risk-tiers.md flagged as worth watching for here). |
| **ISO/IEC 42001 (AI Management System)** | ISO/IEC | The management-system standard for organizations that develop, provide, or use AI systems — grounds this domain's Agent Definition & Scope subdomain (Capability Scope, Tool Permission Scope as the instance-level record of ISO 42001's required AI system impact assessment and access controls) and its Observability & Evaluation subdomain (continual improvement / monitoring requirements). |
| **NIST SP 800-53 (AC, AU, SI families — Access Control, Audit and Accountability, System and Information Integrity)** | NIST | Already cited by Infrastructure and Data Platform; reused here since an Agent's Tool Permission Scope (AC), Agent Trace/Transcript (AU), and Guardrail/Content Filter (SI) concepts are the agent-specific instance of controls those families already require for any system actor. |
| **OWASP Top 10 for Large Language Model Applications** | OWASP | Community-originated but the most widely adopted practical taxonomy of LLM-specific failure modes (prompt injection, excessive agency, insecure output handling); grounds the Guardrails & Safety Controls subdomain's Action Allowlist/Denylist and Content Filter concepts with concrete, named threats rather than only abstract risk-management language. |

**Noted but not cited as a formal standard:**
- **Anthropic's own Responsible Scaling Policy (RSP) and usage policies** —
  organization-specific, not a cross-industry standard; not cited here to
  keep this framework vendor/provider-agnostic, same reasoning applied
  throughout this framework to any single vendor's practices. An
  organization adopting this framework with a specific model provider may
  choose to cite its provider's policy in a local Conventions/Policies
  pass.
- **Model Context Protocol (MCP), Agent-to-Agent (A2A) and similar
  interoperability specifications** — candidate source of vocabulary for
  this domain's Tool Permission Scope and multi-agent Agent Type concepts
  if/when this framework formalizes tool-calling wire-format details; not
  assumed here since that's an implementation choice, not a governance
  concept.

**Not yet consulted, candidate for future passes:**
- **METR's and similar third-party autonomous-capability evaluation
  frameworks** — directly relevant to this domain's Eval Suite / Eval
  Metric concepts (Observability & Evaluation subdomain) but not yet
  mature/standardized enough across the industry to cite as a formal
  reference; flagged the same way SLSA was flagged for Workflow/Process.

**Note on citation confidence:** NIST AI RMF, ISO/IEC 42001, and NIST SP
800-53 are formal frameworks/standards (NIST AI RMF is non-mandatory
guidance rather than a certifiable standard, same authority tier as NIST
SP 800-53 elsewhere in this framework). OWASP's LLM Top 10 is a
widely-adopted community reference, not an ISO/NIST standard — cited
distinctly in authority, same treatment ITIL and Conventional Commits
received in Workflow/Process.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, scoped to what this domain actually covers
- [x] Modular — independent of every other domain's panel; reuses NIST SP 800-53 families already cited elsewhere rather than restating them
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — drafted proactively, before Definitions, same order used for Infrastructure/Networking/Workflow-Process; will be reconciled against actual Definitions citations once column 1 is drafted
- [x] Easy to replace — no single standard is load-bearing for the whole domain
