# Engagements — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Reference panel consulted before drafting this area, and the build-vs-buy
check run before any of it was written.

| Standard | Body | Covers |
|---|---|---|
| ITIL 4 practices | AXELOS/PeopleCert | The vetted mapping for the 7 Engagement Types (02-engagement-types.md) — Change Enablement, Service Configuration Management, Monitoring and Event Management, Incident Management, Service Request Management, Continual Improvement, IT Asset Management. Already cited in 07-workflow-process/00-standards-alignment.md; reused here rather than inventing a new taxonomy. |
| Anthropic, "Building Effective AI Agents" | Anthropic | Grounds this area's core discipline — plan fully, explicitly, before any Agent acts — and the Workflow-vs-Agent, Orchestrator-Worker distinctions the Engagement Planning Agent (07) and Vetting Agent (05) follow. |
| NIST AI RMF Agentic Profile (2026) | NIST (post-training-cutoff guidance) | Extends the AI RMF already cited in 08-harness/00-standards-alignment.md with autonomy-tier classification, oversight-boundary specs, and agent lifecycle/decommissioning concerns — validates Incident Response and Decommission as real, standards-recognized lifecycle stages rather than this framework's own invention. |

**Checked and explicitly not adopted:**
- **MAESTRO (Cloud Security Alliance)** — a 7-layer threat-modeling
  framework, not an engagement/lifecycle taxonomy; doesn't answer the
  question this area answers.
- **Generic multi-agent orchestration frameworks** (LangGraph, CrewAI,
  AutoGen, OpenAI Agents SDK, Google ADK) and **agent
  governance/control-plane platforms** — both checked (Sept 2026
  landscape) and ruled out as things to build here: the former is
  runtime/dev tooling, the latter is inventory/policy-enforcement for
  Agents that already exist. Neither offers org-specific engagement
  planning, taxonomies, or policy libraries. This area is exactly the
  gap between them — see the Build vs. Buy note below.
- **Agent2Agent (A2A) protocol** — already flagged as a candidate in
  08-harness/00-standards-alignment.md for future tool-calling
  wire-format decisions; not adopted here either. Solves agent-to-agent
  communication *across organizational/deployment boundaries*; this
  area's Agents share one harness and one owner. Revisit if/when the
  Post-POC productization idea (09-open-decisions.md #7) has this
  framework's Agents talking to another organization's existing agent
  stack.

**Build vs. Buy conclusion:** the org-specific content and process
layer — this organization's policies, taxonomies, ontologies, org
chart, risk tiers, and the planning workflow tying a request to all of
that before an Agent acts — is not a commodity and isn't sold
pre-filled by any vendor. Orchestration runtimes and agent governance
platforms are the plumbing this area sits on top of, not what this area
rebuilds.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, plus what was checked and ruled out
- [x] Modular — each standard's application scoped to exactly which term/section it grounds
- [x] Easy to update — re-run this check periodically; the "checked, not adopted" section names what to re-check first
- [x] Easy to maintain — no duplicated citation text; every other engagements/ file points back here
- [x] Easy to replace — plain markdown table, no tooling dependency
