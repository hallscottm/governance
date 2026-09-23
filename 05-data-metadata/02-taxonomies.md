# Data/Metadata Domain — Taxonomies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (67 owned terms)

Structure: strict single-parent tree, consistent with all three prior
domains. Only terms owned by this domain are classified here — the 4
referenced terms (Database, Database Schema from System Architecture;
Archive, Environment lifecycle from Infrastructure) are not re-classified.

---

## Data/Metadata
├── Data Governance Roles & Structures
│   ├── Data Governance (#data-governance)
│   ├── Data Domain (#data-domain)
│   ├── Data Owner (#data-owner)
│   ├── Data Steward (#data-steward)
│   ├── Data Custodian (#data-custodian)
│   └── Data Governance Council (#data-governance-council)
│
├── Data Classification & Sensitivity
│   ├── Data Classification (#data-classification)
│   ├── Sensitivity Level (#data-sensitivity-level)
│   ├── Public (#data-classification-public)
│   ├── Internal (#data-classification-internal)
│   ├── Confidential (#data-classification-confidential)
│   ├── Restricted (#data-classification-restricted)
│   ├── PII (#data-pii)
│   ├── PHI (#data-phi)
│   └── Data Handling Requirement (#data-handling-requirement)
│
├── Data Quality
│   ├── Data Quality (#data-quality)
│   ├── Accuracy (#data-quality-accuracy)
│   ├── Completeness (#data-quality-completeness)
│   ├── Consistency (#data-quality-consistency)
│   ├── Timeliness (#data-quality-timeliness)
│   ├── Validity (#data-quality-validity)
│   ├── Uniqueness (#data-quality-uniqueness)
│   ├── Data Quality Rule (#data-quality-rule)
│   └── Data Profiling (#data-profiling)
│
├── Metadata Types
│   ├── Metadata (#data-metadata)
│   ├── Business Metadata (#data-business-metadata)
│   ├── Technical Metadata (#data-technical-metadata)
│   ├── Operational Metadata (#data-operational-metadata)
│   ├── Metadata Registry (#data-metadata-registry)
│   └── Metadata Repository (#data-metadata-repository)
│
├── Data Catalog & Discovery
│   ├── Data Catalog (#data-catalog)
│   ├── Data Asset (#data-asset)
│   ├── Dataset (#data-dataset)
│   ├── Business Glossary (#data-business-glossary)
│   ├── Glossary Term (#data-glossary-term)
│   ├── Data Dictionary (#data-dictionary)
│   ├── Semantic Domain (#data-semantic-domain)
│   └── Metric (#data-metric)
│
├── Data Modeling Concepts
│   ├── Conceptual Data Model (#data-conceptual-model)
│   ├── Logical Data Model (#data-logical-model)
│   ├── Physical Data Model (#data-physical-model)
│   ├── Entity (Data Modeling) (#data-entity)
│   ├── Attribute (Data Modeling) (#data-attribute)
│   └── Relationship (Data Modeling) (#data-relationship)
│
├── Master & Reference Data
│   ├── Master Data (#data-master-data)
│   ├── Reference Data (#data-reference-data)
│   ├── Golden Record (#data-golden-record)
│   ├── System of Record (#data-system-of-record)
│   ├── Data Deduplication (#data-deduplication)
│   └── Survivorship Rule (#data-survivorship-rule)
│
├── Data Lineage & Provenance
│   ├── Data Lineage (#data-lineage)
│   ├── Data Provenance (#data-provenance)
│   ├── Data Transformation (#data-transformation)
│   ├── Source System (#data-source-system)
│   └── Downstream Consumer (#data-downstream-consumer)
│
├── Data Lifecycle & Retention
│   ├── Data Retention Period (#data-retention-period)
│   ├── Data Lifecycle Stage (#data-lifecycle-stage)
│   ├── Data Archival (#data-archival)
│   ├── Data Disposal (#data-disposal)
│   └── Legal Hold (#data-legal-hold)
│
└── Data Privacy & Regulatory
    ├── Personal Data (#data-personal-data)
    ├── Data Subject (#data-subject)
    ├── Consent (#data-consent)
    ├── Right to Erasure (#data-right-to-erasure)
    ├── Data Processing Purpose (#data-processing-purpose)
    ├── Data Minimization (#data-minimization)
    └── Cross-Border Data Transfer (#data-cross-border-transfer)

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one tree, mirrors the 10 Definitions subdomains 1:1
- [x] Modular — referenced (not owned) terms excluded
- [x] Easy to update — a new term appends under its existing subdomain
- [x] Easy to maintain — single-parent, no cross-branch duplication
- [x] Easy to replace — plain tree structure, no tooling dependency
