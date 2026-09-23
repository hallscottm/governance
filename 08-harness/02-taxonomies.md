# Harness Domain — Taxonomies

Status: Draft
Ratified: No
Last updated: 2026-09-23
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (24 owned terms)

Structure: strict single-parent tree, consistent with every domain's
Taxonomy column. Only terms owned by this domain are classified here —
the referenced terms (AI Agent/Harness role from Roles & Departments,
Sandbox from Cross-Cutting, CI Runner/Agent and Drift Detection from
Workflow/Process, the 4 AI-Specific Compute terms from Infrastructure,
Data Classification from Data/Metadata) are not re-classified in this
domain's tree.

---

## Harness
├── Agent Definition & Scope
│   ├── Agent (#harness-agent)
│   ├── Agent Type (#harness-agent-type)
│   ├── Capability Scope (#harness-capability-scope)
│   ├── Tool Permission Scope (#harness-tool-permission-scope)
│   └── Model Version Pin (#harness-model-version-pin)
│
├── Prompting & Context Management
│   ├── System Prompt (#harness-system-prompt)
│   ├── Prompt Template (#harness-prompt-template)
│   ├── Context Window Budget (#harness-context-window-budget)
│   ├── Retrieval Source (#harness-retrieval-source)
│   └── Memory/State Store (#harness-memory-store)
│
├── Guardrails & Safety Controls
│   ├── Guardrail (#harness-guardrail)
│   ├── Content Filter (#harness-content-filter)
│   ├── Agent Rate Limit (#harness-rate-limit)
│   ├── Action Allowlist/Denylist (#harness-action-allowlist)
│   └── Human-in-the-Loop Gate (#harness-hitl-gate)
│
├── Observability & Evaluation
│   ├── Agent Trace/Transcript (#harness-trace)
│   ├── Eval Suite (#harness-eval-suite)
│   ├── Eval Metric (#harness-eval-metric)
│   ├── Behavioral Drift (#harness-behavioral-drift)
│   └── Cost-per-Task (#harness-cost-per-task)
│
└── Escalation & Human-in-the-Loop
    ├── Escalation Path (#harness-escalation-path)
    ├── Approval Gate (Agent-Triggered) (#harness-approval-gate)
    ├── Override/Break-glass (#harness-override)
    └── Agent-Caused Incident Classification (#harness-agent-incident)

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one tree, five subdomains, matches Definitions' grouping
- [x] Modular — subdomains classify independently
- [x] Easy to update — a new guardrail/eval concept adds a leaf
- [x] Easy to maintain — mirrors 01-definitions.md's subdomain headings
      exactly, no separate structure to keep in sync by hand
- [x] Easy to replace — pure classification, no model/tooling vendor
      lock-in
