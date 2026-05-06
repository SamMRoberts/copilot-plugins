---
name: refine-agentic-coding-harness
description: Refine an agentic coding harness from section-state review files, especially <section_name>.needs_update.md and <section_name>.failed.md files. Use when the user asks to improve, iterate, regenerate failed sections, or continue until every harness section is complete. Do not use for first-pass drafting unless review artifacts already exist.
---

# Refine Agentic Coding Harness

Use this skill to improve a reviewed coding harness until all required sections are complete.

## Inputs

- Harness content or path.
- Validation directory, defaulting to `.harness-validation/`.
- Target repository context.
- Optional custom section list.
- User constraints that must not change.

## Procedure

1. Load `../../references/section-refinement.md`.
2. Run the status script:

```bash
python /path/to/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

For a repository-local plugin install, the command is usually:

```bash
python .agents/plugins/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

3. Follow the next action:
   - `regenerate_from_scratch`: ignore failed prose except for review notes, rewrite the section, and rename it to the new state.
   - `create_from_scratch`: create the missing section file and set its state from the rubric.
   - `improve_existing`: preserve correct content, improve the section, and rename it to the new state.
   - `resolve_state_conflict`: merge or choose duplicate section files so exactly one state file remains.
   - `skip`: leave the section unchanged.
4. Update the main harness artifact when a section changes.
5. Re-run the status script.
6. Continue until every required section is `complete`.

## Refinement Rules

- Preserve user-approved requirements and completed sections unless a contradiction is found.
- Make each update more concrete: paths, commands, phase gates, boundaries, stop conditions, or evidence requirements.
- Prefer repository-local, versioned guidance over external context.
- Turn hard rules into scripts, tests, linters, hooks, schemas, or CI checks when the repository can support them.
- If context is missing, mark the section `needs_update` and state the specific missing input.
- Do not mark a section `complete` only because it reads well; it must be actionable.

## Output

Return:

- sections regenerated;
- sections improved;
- sections skipped;
- final status script result;
- remaining blockers;
- updated harness artifact path, if one was edited.
