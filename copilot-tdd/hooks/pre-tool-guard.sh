#!/bin/bash
# TDD Pre-Tool Use Guard
# Enforces TDD methodology discipline by:
# 1. Protecting TDD methodology definition files from accidental modification
# 2. Blocking edits to lock files and generated artifacts
# 3. Logging all tool invocations for the TDD audit trail
set -e

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
TOOL_ARGS=$(echo "$INPUT" | jq -r '.toolArgs')
CWD=$(echo "$INPUT" | jq -r '.cwd')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')

LOG_DIR="${CWD}/.tdd-logs"
mkdir -p "$LOG_DIR"

# Log the tool invocation
jq -n -c \
  --arg ts "$TIMESTAMP" \
  --arg tool "$TOOL_NAME" \
  --arg args "$TOOL_ARGS" \
  '{event: "tool_invoked", timestamp: $ts, tool: $tool, args: $args}' \
  >> "${LOG_DIR}/session.jsonl"

# Only guard edit and create operations
if [ "$TOOL_NAME" != "edit" ] && [ "$TOOL_NAME" != "create" ]; then
  exit 0
fi

# Extract the file path from tool args
FILE_PATH=$(echo "$TOOL_ARGS" | jq -r '.path // empty')
if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# ─── Guard 1: Protect TDD methodology files ───
# These files define the TDD workflow and should not be modified during TDD execution.
PROTECTED_PATTERNS=(
  "*/agents/*.agent.md"
  "*/skills/*/SKILL.md"
  "*/skills/*/references/*.md"
  "*/prompts/*.prompt.md"
  "*/instructions/copilot-instructions.md"
  "*/hooks.json"
  "*/hooks/*.sh"
  "*/plugin.json"
)

for PATTERN in "${PROTECTED_PATTERNS[@]}"; do
  # shellcheck disable=SC2254
  case "$FILE_PATH" in
    $PATTERN)
      jq -n -c \
        --arg reason "Protected TDD methodology file: $FILE_PATH. These files define the TDD workflow and must not be modified during TDD execution." \
        '{permissionDecision: "deny", permissionDecisionReason: $reason}'
      exit 0
      ;;
  esac
done

# ─── Guard 2: Protect lock files and generated artifacts ───
LOCKED_PATTERNS=(
  "*/package-lock.json"
  "*/yarn.lock"
  "*/pnpm-lock.yaml"
  "*/Pipfile.lock"
  "*/poetry.lock"
  "*/Gemfile.lock"
  "*/go.sum"
  "*/Cargo.lock"
  "*/.tdd-logs/*"
)

for PATTERN in "${LOCKED_PATTERNS[@]}"; do
  # shellcheck disable=SC2254
  case "$FILE_PATH" in
    $PATTERN)
      jq -n -c \
        --arg reason "Lock/generated file: $FILE_PATH. Use the package manager to update lock files instead of editing directly." \
        '{permissionDecision: "deny", permissionDecisionReason: $reason}'
      exit 0
      ;;
  esac
done

# Allow all other edits
exit 0
