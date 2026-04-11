# Agent Routing Notes

## Default-Routed Agents

The following model-specific runner agents are assigned as default routes for named personas in the persona index (`skills/team-shared-task-perspectives/references/personas/index.json`):

| Agent | Assigned Persona |
|---|---|
| `persona-proposal-runner-gpt-5-mini` | Software Engineer (Junior) |
| `persona-proposal-runner-gpt-5-2` | Software Engineer (Mid-level) |
| `persona-proposal-runner-gpt-5-4` | Software Engineer (Senior) |
| `persona-proposal-runner-claude-haiku-4-5` | Site Reliability Engineer (Junior) |
| `persona-proposal-runner-gpt-4-1` | Site Reliability Engineer (Mid-level) |
| `persona-proposal-runner-gemini-3-1-pro` | Site Reliability Engineer (Senior) |
| `persona-proposal-runner-gemini-2-5-pro` | Engineering Manager |
| `persona-proposal-runner-claude-sonnet-4-5` | Program Manager |
| `persona-proposal-runner-claude-sonnet-4-6` | Product Manager |

## Override-Only Agents

The following agents exist for routing override use and are not assigned to any persona as a default in the index. They can be specified via the `routed metadata` field when invoking `run-team-perspectives` to substitute a different model for any persona at runtime.

| Agent | Model |
|---|---|
| `persona-proposal-runner-gemini-3-flash` | Gemini 3 Flash (copilot) |
| `persona-proposal-runner-gpt-4o` | GPT-4o (copilot) |
| `persona-proposal-runner-gpt-5-3-codex` | GPT-5.3-Codex (copilot) |
| `persona-proposal-runner-gpt-5-4-mini` | GPT-5.4 mini (copilot) |
| `persona-proposal-runner` | Generic fallback (no specific model) |

## Fallback Chain

For any persona invocation, the routing resolution order is:

1. Routed metadata override (caller-supplied at runtime)
2. `preferredModel` + `runnerAgent` from `index.json`
3. Generic fallback: `persona-proposal-runner`
