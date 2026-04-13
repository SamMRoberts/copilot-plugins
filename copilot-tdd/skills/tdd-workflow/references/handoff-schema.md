# TDD Increment Handoff Schema

Every increment passed between agents must include these fields.

## Fields

- **incrementId**: Short kebab-case identifier (e.g., `parse-empty-input`).
- **title**: One-line description of the behavior being added.
- **acceptanceCriteria**: List of observable outcomes that define success.
- **blockingQuestions**: Unanswered questions that must be resolved before starting.
- **assumptions**: Decisions made in the absence of user input, clearly labeled.
- **targetTestCommand**: The command to run the relevant tests (e.g., `npm test`, `pytest tests/`).
- **targetTestFiles**: File paths where tests for this increment live or should be created.
- **targetProductionFiles**: File paths expected to change during Green.
- **scopeBoundary**: What this increment explicitly does NOT include.
- **doneRule**: The condition under which this increment is considered complete.

## Example

```yaml
incrementId: validate-email-format
title: Reject invalid email addresses in user registration
acceptanceCriteria:
  - Registration with "not-an-email" returns 400
  - Registration with "user@example.com" succeeds
  - Error response includes field name and reason
blockingQuestions: []
assumptions:
  - Email validation uses RFC 5322 simplified rules
  - Existing registration endpoint is POST /api/users
targetTestCommand: npm test -- --grep "email validation"
targetTestFiles:
  - tests/registration.test.ts
targetProductionFiles:
  - src/routes/users.ts
  - src/validators/email.ts
scopeBoundary: Does not add email uniqueness checking or verification emails
doneRule: All acceptance criteria pass as automated tests and production code is minimal
```
