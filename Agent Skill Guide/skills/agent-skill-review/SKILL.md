---
name: agent-skill-review
description: 'Review a SKILL.md against agent skill best practices. Use when auditing a skill for description quality, context efficiency, structure, procedure clarity, script design, or eval readiness. Use for: skill quality review, best practice analysis, SKILL.md audit, description optimization, progressive loading check, improving an existing skill, checking if a skill will trigger reliably.'
argument-hint: 'Provide the path to the SKILL.md to review, or paste its contents.'
user-invocable: true
---

# Agent Skill Review

## What This Skill Produces

A structured quality review of one SKILL.md, covering:

1. Frontmatter validity and description effectiveness.
2. Context efficiency — what to keep, cut, or move to references.
3. Procedure quality — concrete steps, good defaults, calibrated specificity.
4. Structure — progressive loading compliance and file organization.
5. Script design — where scripts would help and whether existing ones are agentic-safe.
6. Eval readiness — test coverage and recommendations for the highest-value cases.
7. Prioritized improvements by severity.

## When to Use

- You have a SKILL.md and want to know how it measures up against best practices.
- A skill is not triggering reliably or produces inconsistent outputs.
- You want a structured review before sharing or publishing a skill.

## Required Inputs

- The SKILL.md to review (path or pasted content).
- Optional: the skill's folder structure (to verify file organization).
- Optional: example prompts the skill should and should not trigger on.

## Procedure

1. Read the target SKILL.md and note its folder structure.

2. Review frontmatter.
   Check each field against [review-checklist.md](./references/review-checklist.md#frontmatter).

3. Evaluate description quality.
   Apply the criteria in [description-criteria.md](./references/description-criteria.md) to assess trigger accuracy, phrasing, and specificity. Flag any revision needed and provide a concrete suggested replacement.

4. Audit context efficiency.
   - Flag instructions the agent already knows without being told (general programming knowledge, common tools, what standard formats are).
   - Flag content that only matters at specific steps and belongs in a references/ file with a conditional load instruction.
   - Flag content that can be cut entirely without reducing skill quality.

5. Assess procedure quality.
   Load [review-checklist.md](./references/review-checklist.md#procedure-quality) and check:
   - Steps describe how to approach the task, not just what to produce.
   - A clear default is given when multiple approaches are valid.
   - Gotchas are concrete corrections, not generic advice.
   - Prescriptiveness is calibrated to fragility — tight where sequence matters, flexible where it doesn't.

6. Check structure and file organization.
   - Verify the skill body is under 500 lines / 5000 tokens.
   - Check that output format templates are referenced from assets/ or references/, not inlined if long.
   - If reusable processing logic appears in the instructions, recommend bundling it in scripts/.
   - If scripts exist, verify they follow agentic design rules from [review-checklist.md](./references/review-checklist.md#script-design).

7. Assess eval readiness.
   Check whether evals/evals.json exists with test prompts, expected outputs, and assertions.
   If not, note the 2–3 highest-value test cases to create first based on the skill's most failure-prone scenarios.

8. Compile findings.
   Group issues by severity using [output-template.md](./references/output-template.md).
   Prioritize the top 3 improvements by impact.
