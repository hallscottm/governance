# Infrastructure Domain — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Per the artifact-axis-definition.md rule, Tooling is filled last and is
allowed to stay TBD. Per explicit choice, this column names required
capabilities per category and what each must satisfy — it does not
recommend or rank specific products. Selecting an actual tool is an
implementation decision left to whoever applies this framework, informed
by their existing stack, cloud provider, and budget (none of which this
generalized template presumes).

---

## Category 1 — Metadata Catalog / Registry

**Must satisfy:** the field registry and entity-type applicability matrix
in 04-metadata-standards.md; must support tagging/describing real
infrastructure instances against the taxonomy (02-taxonomies.md) and
ontology (03-ontologies.md) already defined.
**Capability needed:** ingestion from cloud/infra APIs, a schema/field
registry mechanism, searchable/queryable interface (ideally one an AI
harness can query directly).
**Status:** Not selected. (Note: OpenMetadata was raised earlier in this
project as an example of this category — named here for context only,
not evaluated or recommended.)

## Category 2 — Infrastructure-as-Code (IaC) Platform

**Must satisfy:** the resource naming convention and tag-key rules in
05-conventions.md; must be able to enforce required fields at
provisioning time (feeds Category 3).
**Capability needed:** declarative resource definition, state management,
plan/apply workflow compatible with an approval gate (PROC-1).
**Status:** Not selected.

## Category 3 — Policy Enforcement / Policy-as-Code

**Must satisfy:** the hard-block policies in 06-policies.md (POL-1
metadata completeness, POL-2 Availability Tier minimum, POL-6 cost tag)
and the break-glass override path in AR-2/PROC-5.
**Capability needed:** pre-provisioning validation gate, integration with
whatever IaC platform is chosen (Category 2), auditable override/exception
logging.
**Status:** Not selected.

## Category 4 — Provisioning Workflow / Approval

**Must satisfy:** PROC-1 (Production provisioning request & approval),
including the deferred SLA and notification mechanism
(08-procedures.md open items — intentionally left to this category).
**Capability needed:** request submission, routing to a designated
Approver (distinct from Requester per AR-3), approval/rejection recording,
notification delivery.
**Status:** Not selected.

## Category 5 — Cost / FinOps Management

**Must satisfy:** POL-6 (Cost Center Tag enforcement) and the Chargeback
Unit concept (`infra-chargeback-unit`).
**Capability needed:** cost allocation by tag, reporting/chargeback
generation, ideally integrated with Category 3's enforcement gate so
untagged resources are caught before Category 2 provisions them.
**Status:** Not selected.

---

**Cross-category dependency note:** Categories 2, 3, and 4 are tightly
coupled — the IaC platform, the policy enforcement gate, and the approval
workflow tool need to integrate with each other for PROC-1 to actually
function as a single flow rather than three disconnected tools. Selecting
these together (or ensuring compatibility) matters more than optimizing
any one category in isolation.

**Open items:**
- No tools selected in any category — entirely deferred per explicit
  choice. This is the expected/acceptable state per
  00-framework/artifact-axis-definition.md (Tooling may legitimately stay
  TBD).
- When tool selection does happen, it should be logged in this same file
  (updating Status per category) plus a Q&A entry recording why each was
  chosen — same provenance discipline as every other column.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — capability requirements only, no premature tool lock-in
- [x] Modular — each category can be filled independently as tools are chosen
- [x] Easy to update — "Status: Not selected" becomes a tool name with no
      structural change needed
- [x] Easy to maintain — every category traces to specific columns/policies
      it must satisfy, so a future tool evaluation has clear requirements
- [x] Easy to replace — no product named/endorsed, so no lock-in exists
      even at the documentation level
