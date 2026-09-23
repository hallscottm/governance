# Data/Metadata Domain — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Same posture as all three prior domains: capability categories only, no
specific product/vendor recommendations — deferred entirely per explicit
choice, confirmed again for this domain. Notably, this is the category the
original framing conversation named directly ("standardize and update
metadata... using tools like OpenMetadata or other as recommended") —
still deferred here for consistency with the rest of the framework, with
that context preserved for whoever picks a tool later.

## Capability Categories

### Data Catalog / Metadata Registry Platform
Implements the Data Catalog and Metadata Registry (Definitions), making
Data Assets discoverable with their Business/Technical/Operational
Metadata. The category this framework's originating conversation
specifically named (e.g., OpenMetadata-class platforms), still deferred
to no-specific-product per this domain's confirmed posture.

### Data Classification & Sensitivity Tagging
Applies and verifies Sensitivity Level and Contains PII tags (DPROC-1),
ideally with automated PII/sensitive-data detection rather than
manual-only tagging.

### Data Quality Monitoring & Profiling
Runs Data Profiling and evaluates Data Quality Rules against the six
quality dimensions, producing the Data Quality Score field
(04-metadata-standards.md).

### Data Lineage Tracking
Captures and maintains Data Lineage records — Source System, Data
Transformation steps, Downstream Consumer — feeding the Lineage
Reference field and DPROC-4's erasure-fulfillment step, which depends on
knowing every downstream consumer of a given dataset.

### Master Data Management (MDM) Platform
Implements Data Deduplication and Survivorship Rules to produce Golden
Records for Master Data domains.

### Retention & Disposal Management
Enforces DPOL-2's retention-period tracking and expiry-triggered
disposal, including Legal Hold suspension logic.

### Privacy Request Management
Handles DPOL-4's Right to Erasure workflow — intake, SLA tracking,
cross-system disposal coordination, and completion logging.

---

**Cross-category dependency notes:**
- Data Catalog/Metadata Registry Platform is the natural integration
  point for most other categories here (lineage, quality scores,
  classification tags typically surface through the catalog UI) — likely
  one platform covering several categories rather than one tool per
  category, though not assumed here.
- Retention & Disposal Management should coordinate with Infrastructure's
  Decommissioning tooling (01-infrastructure/10-tooling.md) where
  disposal involves destroying the underlying storage resource, not just
  the logical data.

**Open items:** none for this pass.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 7 capability categories, no product lock-in
- [x] Modular — each category maps to a specific Policy/Procedure/Definitions concept
- [x] Easy to update — a category can be filled in with a specific product later
- [x] Easy to maintain — cross-category dependencies documented explicitly
- [x] Easy to replace — no product named, so no migration cost baked into the framework itself
