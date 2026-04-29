---
name: refine-agentic-coding-harness
description: "Use when improving an agentic coding harness from section-state review files, especially files named <section_name>.needs_update.md or <section_name>.failed.md. Iterates with the harness section status script until every required section is complete. Do not use for first-pass harness drafting unless review artifacts already exist or the user asks for review-driven refinement."
argument-hint: "Provide the harness content or path, validation directory containing section-state files, target repository context, and required section list if custom."
---

# Refine Agentic Coding Harness

Use this skill to improve a reviewed coding harness until all required sections are complete.

Read `../create-agentic-coding-harness/references/section-refinement.md` before changing section content.
Read `../create-agentic-coding-harness/references/agent-first-harness-principles.md` before deciding whether a refined section is complete.

## Inputs

- Harness content or path.
- Validation directory, defaulting to `.harness-validation/`.
- Target repository or workflow context.
- Required section list, defaulting to the standard harness sections.
- User constraints that must not change.

## Refinement Procedure

1. Run the status script:

```bash
python3 plugins/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

2. Follow the next action:
   - `regenerate_from_scratch`: ignore the failed prose except for review notes, rewrite that section, and rename the file to the new state.
   - `create_from_scratch`: create the missing section file and set its state from the rubric.
   - `improve_existing`: preserve correct content, improve the section, and rename the file to the new state.
   - `resolve_state_conflict`: merge or choose duplicate section files so exactly one state file remains.
   - `skip`: leave the section unchanged.
3. Update the main harness artifact when a section changes.
4. Re-run the status script.
5. Continue until all sections are `complete`.

## Refinement Rules

- Preserve user-approved requirements and completed sections unless a contradiction is discovered.
- Make each update more concrete: paths, commands, phase gates, boundaries, stop conditions, or evidence requirements.
- Prefer repository-local, versioned guidance over external context.
- Turn hard rules into scripts, tests, linters, hooks, schemas, CI checks, or other mechanical enforcement when possible.
- Add agent-legibility requirements for runtime state, logs, metrics, traces, screenshots, videos, schemas, or generated artifacts when relevant.
- Add feedback loops that convert failed runs, review comments, bugs, drift, and stale docs into durable repo updates.
- Keep each section focused on its own responsibility.
- If a section cannot be completed because context is missing, mark it `needs_update` and state the specific missing input.
- Do not mark a section `complete` only because it is polished prose; it must be actionable by another agent.

## Output

Return:

- Sections regenerated.
- Sections improved.
- Sections skipped.
- Final status script result.
- Remaining blockers, if any.
- Updated harness artifact path if one was edited.
