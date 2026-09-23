---
task_id: factory-run-dq-dummy-data-generator
parent_project: dq-metrics-dashboard
engagement_type: Request / Ad Hoc
status: complete
assigned_agent:
  role_name: Factory Agent
  capability_scope: draft Skill candidates only
attempt_count: 1
dependencies: []
approval_required: true
approved_by: user (hallscottm@gmail.com), direct chat confirmation, 2026-09-23
result:
  output_location: skill-lib/dq-metrics-dummy-data-generator-v1 (engagements/10-skill-library.md)
  completed_date: 2026-09-23
  outcome_summary: >
    Registered after 1 scope-compliance failure (reverted), isolated
    retry, 5/5 independent Eval cases passed, human approval.
---

## Description

dq-metrics-dashboard's build task (dq-dash-t2-build-report) needs real
data-quality-metrics input, and no real data-quality-checks source is
connected yet (implementation/pilots/dq-metrics-dashboard/pilot-log.md
did not resolve this - it's a real, separate gap). Rather than block on
that, or hand-fabricate one-off sample data, build a Skill that
generates realistic synthetic weekly data-quality-metrics data - reusable
for this pilot's eval AND for evaluating any future Skill/Agent that
needs data-quality-shaped test input, not just this one case.

## Inputs / Outputs

Input: parameters (number of weeks, number of checks/tables to
simulate, a random seed for reproducibility). Output: a CSV shaped like
a real weekly data-quality-metrics export - one row per (check, table,
week): check_name, table_name, week_ending, pass_count, fail_count,
pass_rate.

## Reasoning

Second real Factory Run, deliberately: the csv-to-markdown-summary Factory Run proved the loop
works once. This proves it's repeatable, and unblocks the actual BI
report pilot without needing a live production data source yet
(consistent with implementation/03-new-deployment-bootstrap.md item #5
- domain-specific systems are handled per-Engagement, not assumed).
