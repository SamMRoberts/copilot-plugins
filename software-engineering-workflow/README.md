# Software Engineering Workflow

Software Engineering Workflow is a Copilot plugin for structured software work. It provides a standalone entry agent plus narrow phase agents that separate intake, resumption, discovery, requirements, strategy evaluation, scope control, authentication, data modeling, CI/CD planning, Git workflow management, code commenting, planning, review, documentation, implementation, and verification.

Start with `software-workflow-entry` for every request. The entry agent decides whether the prompt is resumed work, new work, or ambiguous work that needs a short clarification.

## Workflow

For resumed work, the entry agent routes through `work-resumption` to reconstruct the current state and offer a continuation point. The user can continue with any phase agent:

- `context-discovery`
- `requirements-synthesis`
- `strategy-evaluation`
- `follow-up-work-items`
- `scope-creep-review`
- `authentication-planning`
- `authentication-review`
- `data-model-planning`
- `ci-cd-pipeline-planning`
- `ci-cd-pipeline-creation`
- `git-workflow-planning`
- `git-troubleshooting`
- `git-conflict-resolution`
- `git-advanced-operations`
- `code-comment-audit`
- `code-comment-authoring`
- `solution-planning`
- `plan-review`
- `documentation`
- `implementation`
- `verification`

For new work, the entry agent hands off to `software-workflow-orchestrator`. The orchestrator owns the user conversation and moves through these phases:

1. Information gathering with `context-discovery`
2. Requirements and acceptance criteria with `requirements-synthesis`
3. Strategy evaluation with `strategy-evaluation` when the work needs short-term versus long-term tradeoff analysis or multiple possible ways forward
4. Follow-up work definition with `follow-up-work-items` when an expedited short-term strategy creates future obligations
5. Scope creep review with `scope-creep-review` when the current plan or work needs comparison against the original ask to prevent overreach
6. Authentication planning with `authentication-planning` when the work involves local, managed, cloud, Microsoft Entra ID, Azure, OAuth, OIDC, SAML, MFA, Conditional Access, service-to-service, or API authentication choices
7. Authentication review with `authentication-review` when an auth plan needs security, maintainability, or over-complexity review before implementation
8. Data model planning with `data-model-planning` when the work involves databases, structured files, API contracts, events, or configuration schemas
9. CI/CD planning with `ci-cd-pipeline-planning` when the work involves GitHub Actions, Azure DevOps Pipelines, release automation, deployment gates, or pipeline templates
10. Git workflow planning with `git-workflow-planning` when the work involves branch strategy, commit structure, history policy, release branching, or advanced Git choices
11. Git troubleshooting with `git-troubleshooting` when repository state or Git command failures block progress
12. Code comment audit with `code-comment-audit` when key code areas need comments explaining what, why, how, pitfalls, assumptions, TODOs, or known problems
13. Implementation planning with `solution-planning`
14. Plan critique with `plan-review`
15. Documentation preparation with `documentation`
16. Pipeline creation with `ci-cd-pipeline-creation` when the approved scope is CI/CD automation
17. Code comment authoring with `code-comment-authoring` when the approved scope is adding, updating, or removing comments
18. Git conflict resolution with `git-conflict-resolution` when merge, rebase, cherry-pick, or concurrent edit conflicts must be deconflicted
19. Advanced Git operations with `git-advanced-operations` when an approved workflow requires rebase, cherry-pick, reflog recovery, bisect, worktree, stash, tag, submodule, sparse checkout, patch, or safe force-with-lease work
20. Scoped code changes with `implementation`
21. Validation and completion assessment with `verification`

## Subagent Policy

Use subagents when they improve focus or speed. Run subagents in parallel only for independent read-only work, such as inspecting separate areas of a codebase, comparing documentation, reviewing a plan, or checking test coverage assumptions. Do not parallelize file edits, commits, migrations, dependency changes, or decisions that must be sequenced.

The orchestrator remains the user-facing owner for new work. Phase agents return findings, plans, questions, or completion signals to the orchestrator unless the user explicitly resumes at that phase.

## Agent Boundaries

Each agent owns a narrow part of the software engineering workflow:

- `software-workflow-entry` classifies and routes work.
- `work-resumption` reconstructs current state and recommends a continuation point.
- `software-workflow-orchestrator` coordinates new work end to end.
- `context-discovery` gathers facts without editing files.
- `requirements-synthesis` turns facts into scoped requirements.
- `strategy-evaluation` compares short-term and long-term ways forward and checks for over-engineering.
- `follow-up-work-items` turns expedited short-term decisions into concrete future work items.
- `scope-creep-review` compares current plans or changes against the original ask and flags overreach.
- `authentication-planning` selects local, managed, cloud, Microsoft Entra ID, Azure, and third-party authentication strategies.
- `authentication-review` reviews authentication plans for security, maintainability, and over-complexity risk.
- `data-model-planning` selects data representations and schemas.
- `ci-cd-pipeline-planning` selects CI/CD platforms, triggers, stages, gates, artifacts, and security models.
- `ci-cd-pipeline-creation` creates or updates workflow and pipeline files from an approved plan.
- `git-workflow-planning` selects branch, commit, collaboration, history, and repository workflow strategies.
- `git-troubleshooting` diagnoses Git failures and confusing repository states with non-destructive checks.
- `git-conflict-resolution` resolves merge, rebase, cherry-pick, revert, and concurrent edit conflicts.
- `git-advanced-operations` plans and executes advanced Git operations with explicit safety gates.
- `code-comment-audit` identifies where comments should explain what, why, how, pitfalls, assumptions, TODOs, or known problems.
- `code-comment-authoring` adds, updates, or removes comments from an approved commenting plan.
- `solution-planning` creates the implementation approach.
- `plan-review` finds risks before implementation.
- `documentation` prepares and updates docs.
- `implementation` performs scoped code changes.
- `verification` validates behavior and decides whether the work is complete.
