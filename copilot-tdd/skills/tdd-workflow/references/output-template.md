# TDD Cycle Output Template

Use this structure when reporting the result of each TDD cycle.

## Cycle Summary

- Increment: `{incrementId}`
- Title: {title}
- Phase completed: {Red | Green | Refactor | Acceptance Gate}

## Plan Phase

- Behavior increments identified: {count}
- Blocking questions asked: {count}
- Assumptions made: {list}

## Outcomes Discovery

- Outcome categories evaluated: {count} ({count} applicable, {count} N/A)
- Total outcomes discovered: {count} ({count} must, {count} should, {count} could)
- Outcomes covered by increments: {count}/{total must}
- Test infrastructure needed: {list or "none"}

## Red Phase

- Test file(s) changed: {paths}
- Test(s) added: {names}
- Expected failure reason: {description}
- Actual failure output: {summary or "execution not available"}

## Green Phase

- Production file(s) changed: {paths}
- Behavior added: {description}
- Tests run: {command}
- Result: {pass | fail with reason}

## Refactor Phase

- File(s) changed: {paths}
- Refactors performed: {description}
- Tests run: {command}
- Result: {pass | fail with reason}
- Residual tech debt: {notes or "none"}

## Acceptance Gate

- Acceptance criteria met: {yes | partial | no}
- Criteria status:
  - Criterion 1: {met | not met | untestable}
- Next increment ready: {yes | no — reason}
- Re-plan needed: {yes — reason | no}

## Cycle Status

- Overall: {complete | blocked | needs re-plan}
- Next action: {description}
