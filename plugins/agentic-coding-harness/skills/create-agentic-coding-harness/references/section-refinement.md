# Section Refinement Reference

Use this reference when validating and refining a generated coding harness section by section.

## Section Files

Each section must be represented by exactly one markdown file:

```text
<section_name>.<state>.md
```

Use snake_case section names. Valid states:

- `complete`: no more work is needed for this section.
- `needs_update`: the section is directionally right, but another refinement pass should improve specificity, coverage, or clarity.
- `failed`: the section is so incomplete, generic, contradictory, or mis-scoped that it should be regenerated from scratch.

Default section names:

- `harness_purpose`
- `supported_work`
- `out_of_scope`
- `required_context`
- `operating_phases`
- `boundaries`
- `verification_gates`
- `evidence_requirements`
- `handoff_format`
- `automation_plan`
- `open_questions`

## Section File Content

Each section file should contain:

- Section title.
- Current state.
- Section draft content.
- Evaluation notes.
- Specific missing details or defects.
- Next action recommendation.

Keep the content focused on that one section. Do not duplicate the entire harness into every section file.

## Evaluation Rubric

Mark a section `complete` when:

- It is specific to the target repository or target workflow.
- It uses concrete file paths, commands, phase gates, or decision points where applicable.
- Another agent could follow it without hidden context.
- It does not conflict with other completed sections.
- It has no meaningful TODOs except explicitly accepted future work.

Mark a section `needs_update` when:

- It is mostly correct but too generic in places.
- It is missing some paths, commands, examples, or edge cases.
- It needs clearer wording, stronger boundaries, or better sequencing.
- It has minor inconsistencies with another section.

Mark a section `failed` when:

- It describes the wrong repository, technology, workflow, or audience.
- It is mostly boilerplate and cannot guide real agent behavior.
- It contradicts hard user requirements.
- It omits the section's core purpose.
- It would be faster and safer to rewrite than repair.

## Refinement Loop

1. Draft the harness sections.
2. Create or update one section-state file per section.
3. Run `scripts/harness_section_status.py --dir <validation-dir>`.
4. Follow the reported next action:
   - `regenerate_from_scratch`: replace the section content and rename the file to the new state.
   - `improve_existing`: use the current file content as input, improve it, and rename the file to the new state.
   - `skip`: leave the section unchanged.
   - `resolve_state_conflict`: delete or merge duplicate state files so exactly one remains.
5. Repeat until the script reports that all sections are complete.

## Regeneration Guidance

When regenerating a failed section:

- Re-read the user request and the target repository facts.
- Ignore the failed prose except for evaluation notes that explain why it failed.
- Recreate the section from the output contract in `SKILL.md` and the template in `harness-spec-template.md`.
- Rename the resulting file to `section_name.complete.md` only when it satisfies the rubric.

## Improvement Guidance

When improving a `needs_update` section:

- Preserve correct content.
- Replace vague phrases with concrete paths, commands, gates, or stop conditions.
- Add missing edge cases and escalation rules.
- Remove advice that belongs in another section.
- Check whether the update creates conflicts with already complete sections.

## Completion Check

The validation phase is done only when every required section has exactly one `section_name.complete.md` file and the status script exits successfully.
