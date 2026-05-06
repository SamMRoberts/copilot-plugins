# Software Engineering Workflow

Software Engineering Workflow is a Copilot plugin for structured software work. It uses a controller-first workflow with three user-facing controller agents and narrow specialist phase agents for discovery, requirements, strategy, scope control, runtime selection, authentication, data modeling, CI/CD, Git, code comments, planning, review, documentation, implementation, and verification.

The machine-readable routing source of truth is [`workflow-routes.json`](./workflow-routes.json), validated by [`workflow-routes.schema.json`](./workflow-routes.schema.json). Agent frontmatter mirrors only the controls that VS Code custom agents understand, such as `user-invocable`, `agents`, and `handoffs`.

## Required VS Code Setting

Controller agents can invoke phase agents as subagents. If nested subagent invocation is not already enabled, set:

```json
{
	"chat.subagents.allowInvocationsFromSubagents": true
}
```

## User-Facing Routes

Start with `software-workflow-entry` for every request. It classifies the prompt as new work, resumed work, or ambiguous work.

Default user-facing agents:

- `software-workflow-entry`: initial classifier for new, resumed, ambiguous, and explicit phase-targeted requests.
- `software-workflow-orchestrator`: new-work conversation owner and fan-out/fan-in coordinator.
- `work-resumption`: resumed-work state reconstructor and continuation recommender.

All other agents are specialist phase agents. They are subagent-first and hidden from broad direct picker use, but they remain reachable through controller handoffs and explicit phase override requests.

## Companion Skills

The [`skills`](./skills) folder contains one companion `SKILL.md` for every workflow agent. These skills are discovery and routing wrappers: they describe when a phase should load, point back to the matching agent, and summarize the route contract from [`workflow-routes.json`](./workflow-routes.json).

Only the three default controller skills are slash-invocable by default:

- `software-workflow-entry`
- `software-workflow-orchestrator`
- `work-resumption`

Specialist phase skills set `user-invocable: false` so they can support automatic model routing without crowding the slash-command picker. When agent roles, prerequisites, handoffs, or approval gates change, update [`workflow-routes.json`](./workflow-routes.json), the matching agent frontmatter, and the companion skill together.

## New Work Flow

For new work, `software-workflow-entry` hands off to `software-workflow-orchestrator`. The orchestrator owns the user conversation and runs only the phases that are useful for the task:

1. `context-discovery`: gather facts about the request, repository, relevant files, constraints, and risks.
2. `requirements-synthesis`: define goals, non-goals, assumptions, acceptance criteria, and unresolved questions.
3. `strategy-evaluation`: compare short-term and long-term strategies when the task has meaningful tradeoffs.
4. `follow-up-work-items`: record future obligations when a short-term strategy is accepted.
5. `scope-creep-review`: check plans or changes against the original ask when drift is possible.
6. `runtime-options-assessment`: evaluate language, runtime, framework, platform, or execution model choices.
7. `runtime-decision-review`: review a proposed runtime choice before implementation.
8. `authentication-planning`: choose authentication and identity strategy.
9. `authentication-review`: review authentication plans for security, maintainability, and complexity.
10. `data-model-planning`: choose data representations, schemas, validation boundaries, and evolution strategy.
11. `ci-cd-pipeline-planning`: choose automation platform, triggers, stages, gates, permissions, and validation.
12. `git-workflow-planning`: choose branch, commit, history, review, release, or collaboration strategy.
13. `git-troubleshooting`: diagnose Git failures or confusing repository state.
14. `code-comment-audit`: identify where comments add maintainability value before implementation when useful.
15. `solution-planning`: produce the scoped implementation plan.
16. `plan-review`: critique the plan before implementation.
17. `documentation`: prepare required documentation work.
18. `ci-cd-pipeline-creation`: create or update pipeline files from an approved CI/CD plan.
19. `code-comment-authoring`: edit comments from an approved comment plan.
20. `git-conflict-resolution`: resolve merge, rebase, cherry-pick, revert, or concurrent edit conflicts.
21. `git-advanced-operations`: execute approved advanced Git operations.
22. `implementation`: perform scoped code or documentation changes.
23. `code-comment-audit`: always inspect completed code changes to determine whether comments are needed before final verification.
24. `code-comment-authoring`: edit comments when the post-change audit finds required additions, revisions, or removals.
25. `verification`: validate behavior and decide whether the work is complete or needs another phase.

## Resumed Work Flow

For resumed work, `software-workflow-entry` routes through `work-resumption` unless the user explicitly names a phase. `work-resumption` reconstructs current state and recommends one best continuation point plus reasonable alternatives.

After resumption, the user can accept the recommended continuation or choose any specialist phase that has enough context and prerequisites. The normal phase progression resumes from that point.

## Caller Rules

Only controller agents invoke other agents automatically:

- `software-workflow-entry` may hand off to `software-workflow-orchestrator`, `work-resumption`, or a specialist phase when the user explicitly names that phase.
- `software-workflow-orchestrator` may call any specialist phase needed for the approved new-work path, then gathers the results before making decisions.
- `work-resumption` may recommend or hand off to the best continuation phase, but it does not perform downstream work itself.

Specialists return artifacts, missing prerequisites, findings, questions, or recommended next phases to the controller. They should not invoke further specialists directly.

## Parallel Work Policy

Default to sequential execution. Parallel subagents are allowed only when every task is read-only, independent, and does not depend on another result.

Good parallel candidates:

- Multiple `context-discovery` runs scoped to independent code areas, docs, tests, or configuration.
- Independent read-only specialty planning after requirements stabilize.
- Independent read-only research supporting one phase, with the orchestrator making the final decision after fan-in.

Never parallelize:

- File writers with any other writer: `documentation`, `implementation`, `ci-cd-pipeline-creation`, `code-comment-authoring`, and `git-conflict-resolution`.
- Git state mutation or recovery with any other active phase: `git-troubleshooting`, `git-conflict-resolution`, and `git-advanced-operations`.
- Verification while mutation is still active or before post-change code comment audit is complete.
- Dependent phase pairs such as `runtime-options-assessment` -> `runtime-decision-review`, `authentication-planning` -> `authentication-review`, `solution-planning` -> `plan-review`, and `implementation` -> `verification`.
- Final phase decisions, including entry classification, resumption continuation, strategy selection, review gate outcomes, and verification completion decisions.

## Handoff Ownership

Use user-choice handoffs when:

- The prompt is ambiguous between new and resumed work.
- The user explicitly names a phase or chooses a resumption continuation.
- Strategy, runtime, authentication, data, CI/CD, cost, security, migration, or product behavior tradeoffs are material.
- Plan review exposes risk the user may accept or reject.
- Documentation obligations are unclear.
- Git work requires destructive operations, history rewriting, branch or tag deletion, remote mutation, force-with-lease, or discard strategies.
- Verification finds failures outside the approved scope.

Use agent-determined handoffs when:

- Entry clearly identifies new work or resumed work.
- The orchestrator selects relevant optional specialty phases from accepted scope.
- Resumption identifies a precise continuation point.
- A specialist detects missing prerequisites and returns to the prerequisite phase.
- A review gate returns to its planning phase or approves onward progress.
- Verification decides complete, needs implementation, needs planning, or needs user input.

## Prerequisite Map

| Agent | Prerequisite |
| --- | --- |
| `context-discovery` | User prompt or resumed-work state |
| `requirements-synthesis` | Prompt plus discovery findings or enough user-provided context |
| `strategy-evaluation` | Requirements plus multiple viable paths or short-term/long-term tension |
| `follow-up-work-items` | Selected short-term workaround, deferred improvement, TODO, known limitation, or accepted debt |
| `scope-creep-review` | Original ask plus requirements, plan, changed files, or proposed next steps |
| `runtime-options-assessment` | Objectives and requirements involving language, runtime, framework, platform, or execution model |
| `runtime-decision-review` | Proposed runtime choice plus rationale and requirements |
| `authentication-planning` | Authentication requirements, threat context, identity provider constraints, and environment constraints |
| `authentication-review` | Authentication plan |
| `data-model-planning` | Data, schema, API contract, event, file, or configuration requirements |
| `ci-cd-pipeline-planning` | Build, test, release, or deploy automation requirements and repository constraints |
| `ci-cd-pipeline-creation` | Approved CI/CD plan with platform, permissions, secrets model, triggers, stages, and validation gates |
| `git-workflow-planning` | Repository collaboration, branch, commit, history, release, or review objective |
| `git-troubleshooting` | Failed Git command, confusing repository state, visible divergence, lock, remote/auth issue, or unexpected diff |
| `git-conflict-resolution` | Actual conflict state or approved conflict-resolution workflow |
| `git-advanced-operations` | Approved command plan and safety gates |
| `code-comment-audit` | Target code or scope plus maintainability/commenting objective, or completed code changes requiring post-change audit |
| `code-comment-authoring` | Comment audit or approved comment plan |
| `solution-planning` | Accepted requirements plus relevant specialty plans, reviews, and constraints |
| `plan-review` | Concrete implementation plan |
| `documentation` | Requirements and plan plus a decision on documentation impact |
| `implementation` | Requirements, approved plan, review outcome, and documentation decision |
| `verification` | Implemented changes, pipeline/comment/Git changes, or resumed work needing completion assessment after any required post-change code comment audit |

## Workflow Cycles

- New work: `entry -> orchestrator -> discovery -> requirements -> optional specialty phases -> solution planning -> plan review -> documentation preparation -> execution -> post-change comment audit -> verification`.
- Resumed work: `entry -> work-resumption -> recommended continuation -> normal phase progression`.
- Strategy loop: `strategy-evaluation -> follow-up-work-items -> solution-planning` or user decision.
- Runtime loop: `runtime-options-assessment -> runtime-decision-review`, returning to assessment when evidence is missing or the choice is disproportionate.
- Authentication loop: `authentication-planning -> authentication-review`, returning to planning for security or complexity blockers.
- Planning loop: `solution-planning -> plan-review`, returning to planning or targeted specialty review when gaps are found.
- Comment loop: `implementation -> code-comment-audit -> code-comment-authoring when needed -> verification`, returning to audit if intent is unclear.
- CI/CD loop: `ci-cd-pipeline-planning -> ci-cd-pipeline-creation -> verification`, returning to planning if platform, security, or gates are missing.
- Git recovery loop: `git-troubleshooting -> git-conflict-resolution` or `git-advanced-operations -> verification`.
- Verification loop: `verification -> complete`, `implementation`, `solution-planning`, or user input.

## Agent Boundaries

Each agent owns one narrow part of the workflow. The boundaries and route metadata are maintained in [`workflow-routes.json`](./workflow-routes.json). When changing an agent role, update both the route table and the matching `.agent.md` frontmatter so picker visibility, allowed callers, and handoff behavior stay aligned.
