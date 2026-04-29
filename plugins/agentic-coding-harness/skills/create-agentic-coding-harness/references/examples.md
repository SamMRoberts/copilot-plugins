# Harness Examples

Use these examples for output shape and specificity. Adapt paths, commands, and gates to the target repository.

## Example: TypeScript Library Harness

Harness purpose:

Create a repeatable workflow for agents making scoped TypeScript library changes with test-backed verification.

Supported work:

- Bug fixes in `src/`.
- Unit test additions in `tests/`.
- Documentation updates tied to changed APIs.

Out of scope:

- Publishing packages.
- Changing package manager or build tooling.
- Rewriting public API shape without user approval.

Required context:

- `AGENTS.md`
- `README.md`
- `package.json`
- `tsconfig.json`
- Relevant `src/**` files
- Relevant `tests/**` files

Operating phases:

- Intake: restate requested behavior and likely module.
- Discovery: inspect implementation and nearby tests.
- Plan: identify changed files and validation commands.
- Implementation: make minimal edits and add tests for changed behavior.
- Verification: run `npm test` and `npm run typecheck` when available.
- Handoff: summarize changed behavior, test evidence, and residual risk.

Boundaries:

- Do not edit lockfiles unless dependency changes are explicitly required.
- Do not run network installs without approval.
- Do not overwrite dirty user changes.

## Example: iOS App Harness

Harness purpose:

Guide agents making native iOS SwiftUI changes with simulator-backed build and test evidence.

Supported work:

- SwiftUI UI updates.
- Model and persistence changes.
- Unit and UI test fixes.

Out of scope:

- App Store signing.
- Production credentials.
- Backend API contract changes unless provided by the user.

Required context:

- `AGENTS.md`
- Xcode project or package files.
- Relevant Swift source files.
- Existing test targets.
- Current simulator or destination requirements.

Verification gates:

- Build with the project scheme.
- Run targeted tests first, then broader tests when risk warrants.
- Capture simulator screenshots for meaningful UI changes.

Handoff:

- Include scheme, destination, commands run, and whether UI was visually checked.

## Example: Plugin Authoring Harness

Harness purpose:

Help agents create and update local Codex plugins with portable manifests, discoverable skills, and validation checks.

Supported work:

- Plugin scaffolding.
- Skill creation and refinement.
- Agent and prompt guidance updates.
- Manifest and marketplace metadata updates.

Out of scope:

- Publishing to external marketplaces without explicit user approval.
- Adding network-backed MCP servers without a security review.

Required context:

- Root `AGENTS.md`.
- Existing plugin manifests.
- Related skill descriptions.
- Reference files under the target skill.

Verification gates:

- `python3 -m json.tool <json-file>` for changed JSON.
- `git diff --check`.
- Skill description review for trigger clarity.
- Confirm relative paths point to files that exist.

Handoff:

- Changed plugin files.
- Manifest paths updated.
- Validation commands run.
- Remaining TODO metadata.

Section validation:

- `harness_purpose.complete.md`: purpose is specific to Codex plugin authoring.
- `supported_work.complete.md`: task classes map to plugin, skill, agent, prompt, and manifest edits.
- `boundaries.needs_update.md`: edit boundaries are correct but need explicit marketplace and MCP approval rules.
- `verification_gates.complete.md`: JSON parsing, diff check, trigger review, and path checks are explicit.
- `automation_plan.failed.md`: regenerate because it proposes unrelated CI automation instead of harness-local scripts or hooks.
