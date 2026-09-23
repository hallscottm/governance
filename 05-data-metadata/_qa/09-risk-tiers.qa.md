# Q&A Log — Risk Tiers (Data/Metadata)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q9.1: Determining factors, and resolving the cross-domain Data-sensitivity factor

**Context:** This is the domain three prior domains have been carrying a
placeholder/provisional Data-sensitivity factor in anticipation of.
Drafted the real definitions here, then retrofitted all three prior
domains in the same session (Infrastructure, Networking, System
Architecture) to source their Data-sensitivity factor from this domain's
Sensitivity Level field — resolved in one pass, exactly as anticipated
when the open item was first carried forward.

**Bucket:** [Standard]/AI-draftable for the factor definitions;
[Org-decision]/Human-only implicitly already resolved via DPOL-1/DPOL-3's
enforcement levels (06-policies.md), not re-litigated here.

**Drafted:** 4 determining factors (Environment, Sensitivity Level,
Contains PII, Data volume/scale). Contains PII treated as automatically
High when true, consistent with how public exposure was treated
categorically in Networking and System Architecture. Data volume/scale
deliberately left qualitative, not a hard numeric threshold.

**Retrofits applied this session:**
- 01-infrastructure/09-risk-tiers.md: Data sensitivity row populated,
  provisional note resolved.
- 02-networking/09-risk-tiers.md: new Data sensitivity row added (this
  domain previously excluded the factor entirely, relying on network
  exposure/trust boundary as proxies).
- 03-system-architecture/09-risk-tiers.md: Data handled row populated,
  provisional note resolved.

**Status:** Pending explicit review.
