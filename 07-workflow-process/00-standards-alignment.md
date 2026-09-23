# Workflow/Process Domain — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Reference panel for this domain, consulted before drafting Definitions —
this domain is being built fresh (no terms migrated in from elsewhere),
so this panel comes first, same order Infrastructure and Networking used.
Scope per 00-framework/domain-axis-definition.md: Git, CI/CD, SOPs,
directory conventions — six subdomains this pass covers: Source Control,
CI/CD Pipelines, Data Pipeline Orchestration, Infrastructure as Code,
Operational SOPs, and Release Management.

| Standard | Body | Covers |
|---|---|---|
| **NIST SP 800-218 (Secure Software Development Framework, SSDF)** | NIST | Security practices for the software development lifecycle — directly grounds this domain's CI/CD security gates (build integrity, dependency/secret scanning triggers), the closest formal standard to what this domain's Pipeline concept actually governs. |
| **NIST SP 800-53 (CM family — Configuration Management)** | NIST | Change/configuration management controls — grounds this domain's Change Request and Infrastructure-as-Code (drift detection, plan/apply review) concepts. |
| **ISO/IEC 20000 (IT Service Management)** | ISO/IEC | Service management framework — grounds this domain's Operational SOPs subdomain (incident, change, and problem management processes). |
| **ITIL (IT Infrastructure Library)** | AXELOS (now PeopleCert) | The dominant industry practice framework for incident/change/problem management processes — cited as the practical source for Runbook, Incident, and Post-Incident Review vocabulary, distinct in authority from the ISO/NIST citations (a framework, not a certifiable standard in the ISO/NIST sense). |
| **Semantic Versioning 2.0.0 (SemVer)** | semver.org | Already cited by System Architecture (`sysarch-semver`); reused here since this domain's Release Candidate/Changelog concepts are versioned against it. |

**Noted but not cited as a formal standard:**
- **Conventional Commits** — a widely-adopted community specification for
  structuring commit messages to drive automated changelog/version
  generation; not issued by a standards body, flagged the same way
  System Architecture flagged the Twelve-Factor App.
- **DORA metrics (DevOps Research and Assessment: deployment frequency,
  lead time for changes, change failure rate, mean time to restore)** —
  originated from the DORA research program (Google-affiliated), now a
  widely-cited industry benchmark for CI/CD pipeline health; candidate
  source of vocabulary for a future Metadata Standards/Risk Tiers
  refinement if pipeline health measurement is ever formalized further.
- **GitOps principles (OpenGitOps, CNCF)** — a community-originated set
  of principles (declarative, versioned, pulled automatically,
  continuously reconciled) informing this domain's Infrastructure as Code
  and Environment Promotion concepts; not a certifiable standard.
- **Keep a Changelog (keepachangelog.com)** — a community convention for
  structuring a Changelog; informs this domain's Conventions column
  (05-conventions.md, not yet drafted) rather than Definitions itself.

**Not yet consulted, candidate for future passes:**
- **SLSA (Supply-chain Levels for Software Artifacts)** — a supply-chain
  integrity framework (OpenSSF-originated) directly relevant to Build
  Artifact provenance (System Architecture's `sysarch-build-artifact`) and
  this domain's Pipeline concept; flagged rather than cited now since
  adopting it is a genuine scope decision, not assumed here for a
  generalized framework.

**Note on citation confidence:** NIST SP 800-218/800-53 and ISO/IEC 20000
are formal standards. ITIL is a widely-adopted practitioner framework, not
an ISO/NIST standard — cited distinctly in authority, same treatment
FAIR Data Principles and the Twelve-Factor App received elsewhere.
Conventional Commits, DORA metrics, GitOps, and Keep a Changelog are all
community-originated, cited as de facto industry references.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, scoped to what this domain actually covers
- [x] Modular — independent of every other domain's panel, no forced overlap beyond the genuine SemVer reuse
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — drafted proactively, before Definitions, same order used for Infrastructure/Networking; will be reconciled against actual Definitions citations once column 1 is drafted
- [x] Easy to replace — no single standard is load-bearing for the whole domain
