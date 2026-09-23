# Enterprise Architecture Framework Alignment

Status: Draft
Ratified: No
Last updated: 2026-09-22

Why this file exists: the domain axis (00-framework/domain-axis-definition.md)
was built bottom-up, from real infrastructure-to-human concerns, not derived
from an existing EA framework. This note maps it onto two established ones
after the fact — not to replace either, but to show the framework isn't
reinventing structure that already has a name, and to borrow vocabulary
where it helps (e.g. "Domain" itself, over the original "Domain").
Cross-referenced from domain-axis-definition.md.

## TOGAF (BDAT)

TOGAF's Architecture Development Method organizes everything under four
architecture domains — Business, Data, Application, Technology (BDAT).
Rough mapping:

| TOGAF domain | This framework |
|---|---|
| Technology Architecture | Domain 1 (Infrastructure) + Domain 2 (Networking) |
| Data Architecture | Domain 4 (Data Platform) + Domain 5 (Data/Metadata) |
| Application Architecture | Domain 3 (System Architecture) |
| Business Architecture | Domain 9 (Interface/Human) + the Roles & Departments cross-cutting pillar (org structure, reporting lines) |

Three domains fall outside classical BDAT, by design:

- **Domain 6 (Business Intelligence / Reporting)** is the clearest case of
  something TOGAF's four domains don't separate out. TOGAF would fold
  reporting into Application Architecture (a BI tool is just another
  application) or Data Architecture (a report is just another data
  consumer). Neither captures the actual risk: a report tool lets its
  builder create a second, parallel data model (calculated fields,
  extracts, blended sources) that can silently diverge from the official
  Data Platform/Data-Metadata model. That divergence is a governance
  problem BDAT has no domain positioned to catch, because BDAT assumes
  data flow is architecturally intentional all the way to consumption —
  this framework doesn't.
- **Domain 7 (Workflow/Process)** doesn't map to a BDAT domain either —
  it's closer to TOGAF's Architecture Governance and the operational/
  change-management disciplines TOGAF treats as process wrapping the four
  domains, not a domain itself. This framework makes it a first-class
  domain because CI/CD, repo scaffolding, and SOPs are exactly the kind
  of thing that drifts without one.
- **Domain 8 (Harness)** has no TOGAF equivalent at all — TOGAF predates
  AI agents as architectural actors. It's this framework's own extension,
  positioned where it is because it depends on Workflow/Process (an agent
  needs something to plug into) and precedes Interface/Human (a human
  ultimately supervises it).

TOGAF's own architecture-governance discipline (not a BDAT domain) is the
closest analog to this framework's Governance/Security/Roles & Departments
cross-cutting pillars — expressed through every domain's Policies/Access
Rules/Risk Tiers columns rather than as a row of its own, same as TOGAF
treats governance as wrapping all four domains rather than sitting beside
them.

## Zachman Framework

Zachman is an enterprise ontology, not a process — a 6x6 grid of
perspectives (Scope, Business, System, Technology, Component, Operations)
against interrogatives (What, How, Where, Who, When, Why). This framework's
domains don't line up with Zachman's rows (those are stakeholder
perspectives — planner vs. builder vs. subcontractor — this framework
doesn't split by viewpoint), but its columns map cleanly onto this
framework's concerns:

| Zachman column | This framework |
|---|---|
| What (Data) | Domain 4 (Data Platform), Domain 5 (Data/Metadata) |
| How (Function/Process) | Domain 3 (System Architecture), Domain 7 (Workflow/Process) |
| Where (Network) | Domain 1 (Infrastructure), Domain 2 (Networking) |
| Who (People) | Roles & Departments cross-cutting pillar, Domain 9 (Interface/Human) |
| When (Time) | Domain 7 (Workflow/Process) — lifecycle states, release sequencing; also each domain's own has-lifecycle-state ontology relations |
| Why (Motivation) | Governance cross-cutting pillar (Policies columns) |

Domain 6 (Business Intelligence / Reporting) doesn't sit cleanly in one
Zachman column either — it's "What" (report-level data models) crossed
with "Why" (a report exists to answer a business question), which is
consistent with Zachman's own observation that presentation/decision
artifacts are typically a composite view across columns, not a column of
their own.

Takeaway: this framework's Definitions/Taxonomies/Ontologies columns are,
in effect, a lightweight instantiation of "What" for every domain (Zachman
treats data modeling as universal across columns, not just its own column —
same instinct behind this framework's per-domain Definitions column).

## 3-Tier / N-Tier Architecture

Already correctly positioned — not a separate domain. It's a Definitions
entry owned by System Architecture: `### N-Tier Architecture
{#sysarch-n-tier-architecture}` in 03-system-architecture/01-definitions.md.
Presentation and logic/application tiers map to Domain 3 (System
Architecture); the data tier is what motivated splitting out Domain 4
(Data Platform) rather than leaving database internals folded into System
Architecture indefinitely.

## Cloud Reference Models (NIST SP 500-292, IaaS/PaaS/SaaS)

Added as a cited standard in Domain 1 (Infrastructure)'s Standards
Alignment column — IaaS/PaaS/SaaS service-model boundaries are exactly the
kind of vocabulary Infrastructure's Definitions column already needs for
describing what a given Compute Unit or environment actually is.

## Why "Domain" and not "Domain"

"Domain" implies a strict dependency stack (each domain rests on the one
below). That was true for Domains 1-5 but broke down once Workflow/Process,
Harness, and the Roles & Departments pillar entered the picture — those
are cross-department surfaces referenced from everywhere, not strata. TOGAF
and Zachman both use "domain"/column for this kind of grouping-by-concern
rather than grouping-by-dependency-order, which is the better fit here.
Fill order (00-framework/traversal-order.md) is unchanged — domains are
still filled in ascending # order for the same dependency reasons the old
name described — only the name changed.
