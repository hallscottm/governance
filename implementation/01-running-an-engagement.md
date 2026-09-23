# Implementation — Running an Engagement Yourself

Status: Draft — pilot, not ratified
Ratified: No
Last updated: 2026-09-23

The mechanism behind implementation/pilots/dq-metrics-dashboard, written
up as a repeatable runbook. No hidden infrastructure - this is "hand a
fresh agent a compiled spec file and an input, in order." Written so you
(or anyone else) can run this without needing me in the loop.

## The pattern, in general

For each step, open a session (this one, a fresh Claude Code session, or
any agent-capable Claude surface) pointed at this repo, and give it two
things: (1) which compiled agent to act as, (2) the actual input for
that step. Each step's real output is a **file written to this repo**,
not just a chat reply - that file is what the next step reads.

```
Step N prompt shape:
  "Read implementation/agents/<agent>.md and act as that agent on/with:
   <the actual input for this step - a raw request, or the previous
   step's output file path>."
```

## Step by step, idea to completion

1. **Vetting.** Give it your raw idea, however rough. Prompt:
   > Read implementation/agents/vetting-agent.md and act as that agent
   > on this request: "<your idea, verbatim>". Write the Intake Brief
   > to implementation/pilots/<slug>/intake-brief.yaml.

   Output: a completed (or partially-gapped) Intake Brief file.

2. **Planning.** Hand it the Intake Brief. Prompt:
   > Read implementation/agents/planning-agent.md and act as that
   > agent using implementation/pilots/<slug>/intake-brief.yaml. Write
   > the Project Document and Task Documents into
   > implementation/pilots/<slug>/.

   Output: a Project Document + Task Documents, `status: proposed`
   everywhere. It will read the real Anchor layer and Library, and it
   will draft Factory Run Tasks instead of inventing an Agent/Skill
   that doesn't exist yet.

3. **Human approval (CCAR-1/CCAR-2/CCAR-4) - genuinely yours, not an
   agent's.** Open the Project Document. Decide: approve, send back for
   revision, or reject. If approved, you (or whoever holds
   `ccrole-approver`) edit the file directly: set `status: approved`,
   fill `approved_by`. This is the one step in the whole pipeline that
   is never delegated to an agent - CCAR-1/CCAR-2 forbid the Planning
   Agent from doing this to its own plan, and CCAR-4 (cross-cutting/
   access-rules.md) requires this to trace back to a real authenticated
   identity, not just a name typed into a file. In this pilot substrate
   that authentication is *you, personally, editing the file* - a real
   deployment would gate this through actual IAM/SSO instead.

4. **Per Task, in dependency order.** For a Task whose `skills_invoked`
   already names a real, registered Library entry: spin up that Agent
   with the Task's Capability/Tool Scope as its brief, same pattern as
   steps 1-2. For a Task that is itself a Factory Run (`skills_invoked:
   [FACTORY]`, or a `task_id: factory-run-*`): see the Factory loop
   below - it's the same pattern, one more agent.
   > Read implementation/agents/<assigned agent>.md and act as that
   > agent on implementation/pilots/<slug>/task-<id>.md.

5. **Register and close out.** Once a Task's work is approved, its
   result gets recorded (`result.output_location`,
   `completed_date`, `outcome_summary`), status flips to `complete`,
   and if it was a Factory Run, the built Skill/Agent's Library entry
   flips from `draft` to `approved` - now every future Engagement can
   just reference it (the efficiency payoff 08-worked-example.md
   describes).

## The Factory loop specifically

Same step-by-step shape, five stages (13-factory.md), each a real agent
run or a real human decision - no stage is skipped or simulated:

1. **Draft** - Factory Agent (once compiled - not yet, see
   implementation/pilots/skill-pilot-1/ for the first real run) drafts
   the candidate Skill/Agent entry, `status: draft`.
2. **Sandbox** - the candidate is exercised somewhere that isn't
   Production before anything trusts it. In this pilot substrate: a
   throwaway subdirectory or an isolated agent run, not the real Library
   path, until Eval passes.
3. **Eval** - an actual test of the candidate against sample input, not
   just "it ran without erroring."
4. **Approve** - a real human, same rule as step 3 above: never the
   Factory Agent itself.
5. **Register** - the Library entry flips `draft` -> `approved`, the
   Factory Run Task closes out.

## What this pilot substrate does NOT give you yet

- Mechanical Tool Permission Scope enforcement (00-overview.md's
  "Honest limits" section) - every boundary above is currently held by
  instruction, not by a hard technical block.
- A real Sandbox environment distinct from Production - this pilot
  approximates it, doesn't build it.
- Real IAM/SSO-backed approval (CCAR-4) - approval here is you editing
  a file, which is honest but not what CCAR-4 actually requires at
  scale.
- Automatic Task sequencing - you (or whoever's running it) still
  decide when to move to the next step. Nothing here is wired to run
  unattended yet.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one pattern (agent file + input -> file output), repeated per step
- [x] Modular — each step is independently runnable; nothing here assumes a prior step ran in the same session
- [x] Easy to update — new compiled agents just slot into the same pattern
- [x] Easy to maintain — the honest-limits list keeps this from overclaiming what's actually enforced
- [x] Easy to replace — plain markdown runbook, no tooling dependency
