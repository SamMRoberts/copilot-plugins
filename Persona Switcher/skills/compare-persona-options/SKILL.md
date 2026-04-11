---
name: compare-persona-options
description: "Score and rank persona proposals by risk, effort, impact, and reversibility. Use for comparing outputs from team-shared-task-perspectives and selecting a recommended path."
argument-hint: "Provide the persona proposals and optional weighting preferences."
user-invocable: true
---

# Persona Proposal Scoring

## What This Skill Produces

This skill evaluates persona proposals using a consistent rubric and returns:

1. Normalized scoring per proposal.
2. Weighted total score and ranked order.
3. Recommendation with rationale and runner-up options.
4. Sensitivity notes if ranking is close.

## When To Use

- You have multiple persona proposals and need a structured comparison.
- The team disagrees on direction and needs explicit tradeoff scoring.
- You want a repeatable selection method that can be audited.

## Required Inputs

- Proposal set with one entry per persona.
- Optional scoring weights.
- Optional hard constraints that must override scoring.

If weights are not provided, use defaults from [Scoring Rubric](./references/scoring-rubric.md).

## Scoring Dimensions

Score each dimension on 1-5, where 5 is best for selection:

- Risk: Lower delivery and operational risk receives higher score.
- Effort: Lower effort for equivalent value receives higher score.
- Impact: Higher expected user or business impact receives higher score.
- Reversibility: Easier rollback or change receives higher score.

## Procedure

1. Normalize proposals to comparable granularity.
2. Apply hard constraints to remove disqualified options.
3. Score all four dimensions using the rubric.
4. Apply weights and compute weighted total.
5. Rank proposals from highest to lowest score.
6. Resolve ties by this order:
- Higher risk score
- Higher impact score
- Higher reversibility score
- Lower effort (higher effort score)
7. Provide recommendation and sensitivity analysis.

## Decision Rules

- Default weights:
- Risk: 0.40
- Impact: 0.30
- Reversibility: 0.20
- Effort: 0.10

- If the user requests speed-first:
- Effort: 0.35
- Impact: 0.30
- Risk: 0.20
- Reversibility: 0.15

- If a hard constraint is violated, the proposal cannot be ranked first regardless of score.

## Output Format

### Inputs
- Proposals scored:
- Weights used:
- Hard constraints:

### Scorecard
- Persona name | Risk | Effort | Impact | Reversibility | Weighted total | Rank

### Recommendation
- Recommended proposal:
- Why it ranked first:
- Runner-up:
- Tradeoff summary:

### Sensitivity Check
- What would change the ranking:
- Close-call notes:

### Assumptions
- Assumption 1

### Open Questions
- Question 1

## Authoring Guidance

- Keep scoring explanations concise and evidence-based.
- Do not hide uncertainty; include confidence notes.
- If data is missing, score conservatively and mark assumptions.
