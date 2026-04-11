---
name: run-team-perspectives-end-to-end
description: "Run the full team perspectives workflow: generate task-ready brief, orchestrate isolated persona proposals, then score and rank options."
argument-hint: "Provide the task, context, constraints, risks, success metrics, and any hard constraints."
agent: "run-team-perspectives"
---
Run this workflow in order and do not skip steps.

## Step 1: Build Task-Ready Brief
Create a task-ready brief using the same structure as `create-task-ready-brief`.

Required sections:
- Canonical task statement
- Problem context
- In scope
- Out of scope
- Constraints
- Dependencies
- Risks
- Success metrics
- Assumptions
- Open questions

If required inputs are missing, make explicit assumptions and continue.

## Step 2: Run Isolated Persona Proposals
Use isolated persona runs from `persona-proposal-runner` in parallel for all personas in the index:
- `./.github/skills/team-shared-task-perspectives/references/personas/index.json`

Each subagent call must receive:
- The same canonical task statement
- The same constraints
- The same risks
- The same success metrics

Collect all per-persona outputs into the synthesis format used by `team-shared-task-perspectives`.
Do not block the full run if one persona call fails; continue with completed outputs and report missing personas.

## Step 3: Score And Rank Proposals
Apply `compare-persona-options` to the collected persona proposals.

Scoring dimensions:
- Risk
- Effort
- Impact
- Reversibility

Default weights:
- Risk: 0.40
- Impact: 0.30
- Reversibility: 0.20
- Effort: 0.10

If the user explicitly requests speed-first, switch to speed-first weights.
Honor hard constraints before ranking.

## Final Output Format
Use exactly this structure:

### Task-Ready Brief
- Canonical task statement:
- Problem context:
- In scope:
- Out of scope:
- Constraints:
- Dependencies:
- Risks:
- Success metrics:
- Assumptions:
- Open questions:

### Team Perspectives Synthesis
- Areas of agreement:
- Areas of disagreement:
- Recommended path:
- Alternatives:
- Rationale:

### Scorecard
- Persona name | Risk | Effort | Impact | Reversibility | Weighted total | Rank

### Final Recommendation
- Selected proposal:
- Why selected:
- Runner-up:
- Tradeoff summary:
- Sensitivity notes:
