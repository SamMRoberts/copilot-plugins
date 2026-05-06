# Examples

Use this reference when the user asks what inputs or outputs should look like.

## Answers File

```json
{
  "project_name": "Example App",
  "purpose": "A local tool for managing example workflows.",
  "users": "Developers and maintainers",
  "agent_scope": "Documentation, tests, small fixes, scoped feature work",
  "out_of_scope": "Production credentials, destructive data changes, unapproved rewrites",
  "approval_required": "Public APIs, migrations, dependencies, deployment",
  "domains": "CLI, service layer, persistence, docs",
  "architecture": "CLI -> service -> repository -> storage",
  "tech_stack": "Go, Cobra, Bubble Tea, SQLite",
  "commands": "go test ./...; go build ./...",
  "observability": "CLI output, logs, fixture-based smoke tests",
  "constraints": "No secrets in logs; preserve existing data files",
  "doc_locations": "Use the default docs/ layout",
  "plan_process": "Active plans in docs/exec-plans/active/",
  "quality": "Small packages, explicit errors, fixture-backed tests"
}
```

## Section Review File

```markdown
# verification_gates

State: needs_update

## Current Content

The harness says to run tests.

## Review Notes

The section is directionally correct but does not name commands, expected artifacts, or skipped-check reporting.

## Missing Details

- Exact format/lint/test/build commands.
- When UI or runtime evidence is required.
- Required final-response validation summary.

## Recommended Next Action

Improve this section and rename the file to `verification_gates.complete.md` only after exact commands are captured.
```
