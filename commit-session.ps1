git add -A
git commit -m @"
Build Harness domain checkpoint (Standards Alignment, Definitions, Taxonomies, Ontologies)

- 08-harness/00-standards-alignment.md: NIST AI RMF and ISO/IEC 42001 as
  primary references (both deferred to this domain back in System
  Architecture's own panel), plus reused NIST SP 800-53 families and
  OWASP Top 10 for LLM Applications.
- 08-harness/01-definitions.md: 24 terms across 5 subdomains (Agent
  Definition & Scope; Prompting & Context Management; Guardrails & Safety
  Controls; Observability & Evaluation; Escalation & Human-in-the-Loop).
  Two name-collision boundaries stated explicitly: Agent vs. Workflow/
  Process's CI Runner/Agent, and Behavioral Drift vs. Workflow/Process's
  (IaC) Drift Detection. References Roles & Departments'
  ccrole-ai-agent-harness, Cross-Cutting Sandbox (cc-sandbox), 4
  previously-pending Infrastructure AI-Specific Compute terms, and
  Data/Metadata's Data Classification.
- 08-harness/02-taxonomies.md, 03-ontologies.md: taxonomy mirrors
  Definitions exactly; 21 internal relationships plus 5 outbound
  cross-domain edges (Infrastructure x3, Data Platform x1) and 1 inbound
  edge from Workflow/Process (wf-postmortem consumes
  harness-agent-incident). Reverse pointers added to Infrastructure's,
  Data Platform's, and Workflow/Process's ontology files.
- _status.yaml and all four columns' _qa/*.qa.md updated accordingly.
- Verified: no new duplicate anchors; taxonomy leaves match Definitions
  anchors exactly.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0159kvrkXNev6gsNF338TDTr
"@
git --no-pager log -1
