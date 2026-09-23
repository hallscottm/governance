# Business Intelligence / Reporting Domain — Definitions

Status: Draft
Ratified: No
Last updated: 2026-09-22

Scope: reports, dashboards, and the report-level data models built to
produce them — the layer where data becomes a decision-facing artifact.
Split out as its own domain on 2026-09-22 (see
00-framework/ea-framework-alignment.md) because data flow from Data
Platform/Data-Metadata into a report is not 1:1: a report builder can
create a second, parallel model (calculated fields, blended sources,
extracts) inside the reporting tool itself, which can silently diverge
from the official Semantic Layer/Metric definitions. This domain exists
to make that divergence a visible, governed choice rather than a silent
default.

Anchor convention: `bi-<term-slug>`. See
00-framework/term-linking-convention.md for the DRY/anti-drift rules this
file follows.

---

## Referenced Terms (owned elsewhere)

- **Semantic Layer** — owned by Data Platform →
  [04-data-platform/01-definitions.md#dp-semantic-layer](../04-data-platform/01-definitions.md#dp-semantic-layer)
- **Metric** — owned by Data/Metadata →
  [05-data-metadata/01-definitions.md#data-metric](../05-data-metadata/01-definitions.md#data-metric)
- **Data Lineage** — owned by Data/Metadata →
  [05-data-metadata/01-definitions.md#data-lineage](../05-data-metadata/01-definitions.md#data-lineage)
- **Data Warehouse, Data Lakehouse** — owned by Data Platform →
  [04-data-platform/01-definitions.md#dp-data-warehouse](../04-data-platform/01-definitions.md#dp-data-warehouse)

---

## Delivered Artifacts

### Report {#bi-report}
A structured presentation of data intended to answer a specific business
question, typically static or scheduled. Source: Common industry
practice.

### Dashboard {#bi-dashboard}
A collection of Reports/visualizations presented together, typically
interactive and refreshed on a shorter cycle than a single Report.
Source: Common industry practice.

### Visualization {#bi-visualization}
A single chart, table, or graphic within a Report or Dashboard. Source:
Common industry practice.

---

## Report-Level Models

### Report Data Model {#bi-report-data-model}
A data model built inside a reporting tool itself (e.g., a Power BI
dataset, Tableau workbook data source, or spreadsheet pivot model) —
relationships, aggregations, and structure defined by the report's
builder, separately from any upstream Semantic Layer (`dp-semantic-
layer`). This is the central term this domain exists to govern: a
Report Data Model can be built entirely from Certified upstream sources
(low risk) or can blend/reshape data in ways that diverge from official
definitions (the risk this domain's eventual Policies column will gate
on). Source: Common industry practice.

### Calculated Field / Measure {#bi-calculated-field}
A formula defined within a Report Data Model — a report-level
computation. Distinct from Data/Metadata's Metric (`data-metric`), which
is the *official* definition a Calculated Field should trace back to,
if one exists for the same business concept; a Calculated Field with no
matching Metric is not automatically wrong, but it is exactly the case
that needs a documented Source-to-Target Mapping (below) so the
divergence — intentional or not — is visible. Source: Common industry
practice.

### Data Extract {#bi-data-extract}
A cached or snapshotted subset of data pulled into a reporting tool,
as opposed to a live connection to the source. Introduces its own
staleness/refresh-cadence concern distinct from the source data's own
freshness. Source: Common industry practice.

### Report Refresh Schedule {#bi-refresh-schedule}
The defined cadence at which a Report/Dashboard's underlying Data
Extract or live connection is refreshed. Source: Common industry
practice.

---

## Documentation & Governance

### Source-to-Target Mapping {#bi-source-to-target-mapping}
Extends: data-lineage
Adds: the specific mapping, at report grain, from a Calculated Field or
Report Data Model element back to its upstream source field(s)/table(s)/
Metric, including any transformation applied along the way. Typically
tool-derived (a metadata registry such as OpenMetadata auto-extracts
this from the reporting tool's own API/metadata, per 04-data-platform's
and 05-data-metadata's Tooling posture) rather than hand-authored —
required for Certified status, not for a Report/Dashboard to exist at
all. Source: Common industry practice; extends the framework's own
lineage concept one hop further than Data/Metadata models it.

### Certified Dataset/Report {#bi-certified}
A lifecycle status on a Report Data Model or Report indicating it has
been reviewed, its Source-to-Target Mapping is complete, and it uses
official Metric/Semantic Layer definitions where those exist rather than
reinventing them — as opposed to Draft/Uncertified, which is allowed to
exist (self-service modeling is not prohibited) but is scoped away from
broad distribution until certified. Typically promoted by a BI Analyst/
Developer reviewing a Business Analyst/Report Builder's self-service
work (cross-cutting/roles-and-departments/01-definitions.md). Source:
Common industry practice (BI governance tooling, e.g. certification
tiers in Power BI/Tableau/Looker).

### Row-Level Security (Report-Level) {#bi-row-level-security}
Access filtering applied within the reporting tool itself, restricting
which rows of a Report Data Model a given viewer can see — distinct
from Data Platform's own database-level access controls and Data/
Metadata's Data Handling Requirements; this is a report-tool-native
filter layered on top of, not a replacement for, either. Source: Common
industry practice.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 10 owned terms, three subdomains
- [x] Modular — each term owned once; Semantic Layer/Metric/Lineage
      referenced, not restated
- [x] Easy to update — a new BI concept (e.g., a specific tool's native
      feature) adds a term without touching existing ones
- [x] Easy to maintain — Source-to-Target Mapping's `extends` relationship
      keeps it tied to Data/Metadata's lineage concept rather than
      drifting into its own definition over time
- [x] Easy to replace — no BI vendor/product named as the definition of
      a concept (Power BI, Tableau, Looker appear only as examples)
