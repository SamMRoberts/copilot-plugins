# Output Template

Use this structure when producing a skill review.

## Skill Review: [skill-name]

### Frontmatter

- `name`: [valid | invalid — reason]
- `description`: [pass | flag — reason]
- `argument-hint`: [present | missing]
- `user-invocable`: [correct | review — reason]

### Description Quality

- Trigger accuracy: [assessment]
- Phrasing: [imperative | declarative]
- Specificity: [too broad | too narrow | good]
- Near-miss exclusions: [present | missing — which adjacent skills could false-trigger]
- Suggested revision: [replacement text, or "no changes needed"]

### Context Efficiency

- Content to cut: [list items, or "none"]
- Content to move to references/: [list items with suggested filenames, or "none"]
- Content missing that the agent lacks: [list items, or "none"]

### Procedure Quality

- [finding — which step — recommended fix]

### Structure and Files

- Estimated size: [line count or token estimate]
- Scripts: [present and agentic-safe | present with issues — list | missing and recommended | not needed]
- References: [present | missing and recommended | not needed]
- Evals: [present | missing]

### Findings by Severity

#### Blocking
- [issue] — [rationale] — [fix]

#### Major
- [issue] — [rationale] — [fix]

#### Minor
- [issue] — [rationale] — [fix]

### Top 3 Improvements

1. [highest-impact change and why]
2. [second change and why]
3. [third change and why]

### Recommended Eval Cases

If evals are missing, list the 2–3 highest-value test prompts to create first:

1. Prompt: [realistic user message] — Tests: [what scenario]
2. Prompt: [realistic user message] — Tests: [what scenario]
3. Prompt: [realistic user message] — Tests: [near-miss negative]
