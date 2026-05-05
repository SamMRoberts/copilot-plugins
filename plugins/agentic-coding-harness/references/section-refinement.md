# Section Refinement

Use this reference for section-level review and refinement loops.

## Required Sections

- `harness_purpose`
- `supported_work`
- `out_of_scope`
- `required_context`
- `knowledge_system`
- `operating_phases`
- `boundaries`
- `agent_legibility`
- `mechanical_enforcement`
- `verification_gates`
- `evidence_requirements`
- `handoff_format`
- `automation_plan`
- `feedback_loops`
- `open_questions`

## File Naming

Each section state file must use:

```text
<section_name>.<state>.md
```

Allowed states:

- `complete`
- `needs_update`
- `failed`

Use snake_case section names. There must be exactly one state file per section.

## State Rubric

Use `complete` when the section:

- is specific to the repository or workflow;
- names concrete files, commands, boundaries, or evidence where relevant;
- is internally consistent with the rest of the harness;
- can be followed by another agent without hidden chat context.

Use `needs_update` when the section:

- is mostly correct;
- has useful content worth preserving;
- needs clearer paths, commands, scope boundaries, sequencing, examples, or acceptance criteria.

Use `failed` when the section:

- is generic, wrong, contradictory, unsafe, or misleading;
- conflicts with user-approved constraints;
- should be regenerated from scratch instead of patched.

## Status Actions

The section status script reports one of:

- `regenerate_from_scratch`: rewrite a failed section.
- `create_from_scratch`: create a missing required section.
- `improve_existing`: improve a needs-update section.
- `resolve_state_conflict`: consolidate duplicate state files for the same section.
- `skip`: all required sections are complete.
