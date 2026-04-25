"use strict";

const mode = process.argv[2] || "context";
const contextKind = process.argv[3] || "session-start";

let stdin = "";
if (process.stdin.isTTY) {
    writeOutput("");
} else {
    let completed = false;
    const fallback = setTimeout(finish, 100);

    process.stdin.setEncoding("utf8");
    process.stdin.on("data", (chunk) => {
        stdin += chunk;
    });
    process.stdin.on("end", finish);

    function finish() {
        if (completed) {
            return;
        }

        completed = true;
        clearTimeout(fallback);
        writeOutput(stdin);
    }
}

function writeOutput(rawInput) {
    const input = parseInput(rawInput);
    const output = mode === "pre-tool-use" ? preToolUseOutput(input) : contextOutput(contextKind);

    if (output) {
        process.stdout.write(`${JSON.stringify(output)}\n`);
    }
}

function parseInput(rawInput) {
    if (!rawInput.trim()) {
        return {};
    }

    try {
        return JSON.parse(rawInput);
    } catch {
        return {};
    }
}

function contextOutput(kind) {
    const controllerContext = [
        "Software Engineering Workflow context:",
        "- Use software-engineering-workflow/workflow-routes.json as the routing source of truth.",
        "- Start broad software work through software-workflow-entry; new work flows to software-workflow-orchestrator, resumed work flows to work-resumption.",
        "- Controllers own the user-facing thread; specialist agents return artifacts, missing prerequisites, questions, findings, or recommended next phases.",
        "- Run writers sequentially. Parallelize only independent read-only investigations whose outputs fan back into a controller.",
        "- After code changes, run code-comment-audit before verification, then code-comment-authoring only when the audit finds useful comment work.",
        "- Ask for approval before destructive commands, history rewrites, force pushes, discarding user changes, broad rewrites, out-of-scope dependency changes, secrets, permissions, branch protection, or cloud provisioning."
    ];

    const subagentContext = [
        "Software Engineering Workflow subagent context:",
        "- Keep the phase boundary narrow and return control to the controller instead of chaining to another specialist.",
        "- Return concise artifacts, prerequisites, findings, questions, and recommended next phases.",
        "- Do not write files unless this phase is an execution or recovery phase whose route explicitly allows mutation.",
        "- Follow workflow-routes.json for prerequisites, handoffs, approval gates, and parallel policy."
    ];

    return {
        continue: true,
        systemMessage: (kind === "subagent-start" ? subagentContext : controllerContext).join("\n")
    };
}

function preToolUseOutput(input) {
    const toolName = getToolName(input);
    const command = getCommandText(input);

    if (!command || !isTerminalTool(toolName)) {
        return { continue: true };
    }

    const risk = riskyCommandReason(command);
    if (!risk) {
        return { continue: true };
    }

    return {
        continue: true,
        systemMessage: "Software Engineering Workflow approval gate: risky shell and Git operations need explicit user confirmation before continuing.",
        hookSpecificOutput: {
            hookEventName: "PreToolUse",
            permissionDecision: "ask",
            permissionDecisionReason: risk
        }
    };
}

function getToolName(input) {
    return String(input.tool_name || input.toolName || input.name || input.tool?.name || "");
}

function getCommandText(input) {
    const toolInput = input.tool_input || input.toolInput || input.input || input.tool?.input || input.arguments || {};

    if (typeof toolInput === "string") {
        return toolInput;
    }

    if (!toolInput || typeof toolInput !== "object") {
        return "";
    }

    const candidates = [
        toolInput.command,
        toolInput.cmd,
        toolInput.script,
        Array.isArray(toolInput.args) ? toolInput.args.join(" ") : ""
    ].filter(Boolean);

    return candidates.join(" ");
}

function isTerminalTool(toolName) {
    if (!toolName) {
        return true;
    }

    return /terminal|shell|bash|zsh|run_in_terminal|runCommands|runTasks/i.test(toolName);
}

function riskyCommandReason(command) {
    const risks = [
        [/\bgit\s+reset\s+--hard\b/i, "`git reset --hard` can discard local work and requires explicit approval."],
        [/\bgit\s+clean\b(?=.*-[^\s]*f)(?=.*-[^\s]*d)/i, "`git clean` with force and directory deletion can remove untracked files and requires explicit approval."],
        [/\bgit\s+checkout\s+(--|\.)/i, "`git checkout` against paths can discard file changes and requires explicit approval."],
        [/\bgit\s+restore\b/i, "`git restore` can discard or rewrite local file state and requires explicit approval."],
        [/\bgit\s+push\b(?=.*(--force|-f\b|--force-with-lease))/i, "Force-pushing can publish rewritten history and requires explicit approval."],
        [/\bgit\s+(branch|tag)\s+-D\b/i, "Deleting Git branches or tags requires explicit approval."],
        [/\brm\s+-[^\s]*r[^\s]*f|\brm\s+-[^\s]*f[^\s]*r/i, "Recursive forced deletion requires explicit approval."],
        [/\bsudo\b/i, "Privileged shell commands require explicit approval."],
        [/\bchmod\s+-R\s+777\b/i, "Broad world-writable permission changes require explicit approval."]
    ];

    const match = risks.find(([pattern]) => pattern.test(command));
    return match ? match[1] : "";
}
