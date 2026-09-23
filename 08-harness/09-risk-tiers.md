# Harness Domain — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 04-metadata-standards.md, 06-policies.md, cross-cutting/risk-tiers.md

## Risk Scale

**Extends:** cross-cutting/risk-tiers.md (FIPS 199-aligned Low/Moderate/
High scale — not restated here).

## Determining Factors

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor (cross-cutting maximum rule, per cross-cutting/risk-tiers.md).

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (referenced from Infrastructure) | Dev | Staging/QA | Production |
| Agent Type (04-metadata-standards.md) | Assistant | Autonomous | Multi-Agent |
| Tool Permission Scope breadth | Read-only | Read-write, scoped to a defined resource set | Destructive operations or external communications (e.g. sending messages, spending funds, deleting data) permitted |
| Sandbox Tested Flag, for a Production-scoped grant (04-metadata-standards.md) | N/A — Sandbox testing has no Low/Moderate distinction | N/A | Not set — an untested Production-scoped grant is automatically High risk, per HPOL-1's hard block being the thing this factor would signal is about to be violated |
| Override/Break-glass used (HPROC-4's Rate Limit tightening, or HPROC-5's Guardrail override) | Not used | N/A — this factor has no Moderate value | Used — an override is automatically High risk regardless of what was overridden, per HPOL-5 |

**Note on Agent Type factor:** unlike most Determining Factors across
this framework, which score a static resource property, Agent Type
scores a *behavioral autonomy* property — how independently the Agent
can act without a human-initiated request per step. Flagged as a
distinct kind of factor from either the standard resource-property
factors (Infrastructure's, System Architecture's) or the "process, not
resource" factors Workflow/Process's 09-risk-tiers.md introduced.

**Note on Override/Break-glass factor:** this domain now has the same
"process, not resource" factor type Workflow/Process's 09-risk-tiers.md
explicitly flagged as worth watching for once Harness was built — an
Agent's own break-glass usage is exactly the kind of factor that
prediction anticipated.

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline (two-person sign-off
for High risk, via CCAR-3).

**Domain-specific additions beyond the baseline (already defined in full
in 06-policies.md/07-access-rules.md — summarized here for visibility):**

| Tier | Harness-Specific Policy Implication |
|---|---|
| **Low** | Assistant-type Agents are exempt from HPOL-3's Human-in-the-Loop Gate requirement entirely (a human already initiated the request). |
| **Moderate** | HAR-1 Production Tool Permission grant approval: Owning Team Lead alone. |
| **High** | HAR-1: Owning Team Lead + Security/Compliance. HPOL-3's Human-in-the-Loop Gate applies to Autonomous/Multi-Agent Types. HAR-3's Guardrail override always requires both roles (no Low/Moderate path exists for this specific override, since HPOL-5 fixes it at High unconditionally). HPOL-1, HPOL-2 hard blocks apply uniformly at every tier (not scaled), same treatment established across every other domain's uniform hard blocks. |

---

**Open items:**
- Agent Type and Tool Permission Scope breadth are both genuinely new
  factor shapes for this framework — behavioral-autonomy and
  action-consequence-breadth, respectively — distinct from both the
  static resource-property factors most domains use and the
  process-bypass factor Workflow/Process introduced. Worth watching for
  in any future domain that governs another kind of autonomous or
  semi-autonomous actor.
- Multi-Agent Type's High classification is a conservative default — a
  Multi-Agent configuration where each individual Agent has a narrow,
  well-scoped role may not always warrant automatic High risk; left as
  the framework's default rather than building a more granular
  sub-scoring scheme for multi-agent topologies, a genuine scope decision
  for a future pass if this factor proves too coarse in practice.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 determining factors, reusing the cross-cutting scale
- [x] Modular — domain-specific factors independent of every other domain's
- [x] Easy to update — cross-cutting scale updates once, applies here automatically
- [x] Easy to maintain — factors derived from existing Definitions/Metadata Standards
- [x] Easy to replace — standard-grounded (FIPS 199, inherited); confirms and extends the "process, not resource" factor type Workflow/Process predicted would appear here
