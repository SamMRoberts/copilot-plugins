#!/bin/bash
# TDD Post-Tool Formatter
# Automatically formats code after edit/create operations to maintain consistent
# style during rapid TDD cycles. Detects and uses the project's existing formatter.
set -e

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
TOOL_ARGS=$(echo "$INPUT" | jq -r '.toolArgs')
RESULT_TYPE=$(echo "$INPUT" | jq -r '.toolResult.resultType')
CWD=$(echo "$INPUT" | jq -r '.cwd')

# Only format after successful edit or create operations
if [ "$RESULT_TYPE" != "success" ]; then
  exit 0
fi
if [ "$TOOL_NAME" != "edit" ] && [ "$TOOL_NAME" != "create" ]; then
  exit 0
fi

FILE_PATH=$(echo "$TOOL_ARGS" | jq -r '.path // empty')
if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Skip formatting for non-source files
case "$FILE_PATH" in
  *.md|*.json|*.yaml|*.yml|*.toml|*.lock|*.log|*.csv|*.txt|*.sh)
    exit 0 ;;
esac

# ─── Detect and run the project's formatter ───
# Check for common formatters in order of specificity

# Prettier (JavaScript/TypeScript ecosystem)
if [ -f "${CWD}/node_modules/.bin/prettier" ]; then
  "${CWD}/node_modules/.bin/prettier" --write "$FILE_PATH" 2>/dev/null || true
  exit 0
fi

# Black (Python)
if command -v black &>/dev/null && [[ "$FILE_PATH" == *.py ]]; then
  black --quiet "$FILE_PATH" 2>/dev/null || true
  exit 0
fi

# Ruff (Python)
if command -v ruff &>/dev/null && [[ "$FILE_PATH" == *.py ]]; then
  ruff format --quiet "$FILE_PATH" 2>/dev/null || true
  exit 0
fi

# gofmt (Go)
if command -v gofmt &>/dev/null && [[ "$FILE_PATH" == *.go ]]; then
  gofmt -w "$FILE_PATH" 2>/dev/null || true
  exit 0
fi

# rustfmt (Rust)
if command -v rustfmt &>/dev/null && [[ "$FILE_PATH" == *.rs ]]; then
  rustfmt "$FILE_PATH" 2>/dev/null || true
  exit 0
fi

# dotnet format (C#)
if command -v dotnet &>/dev/null && [[ "$FILE_PATH" == *.cs ]]; then
  dotnet format --include "$FILE_PATH" 2>/dev/null || true
  exit 0
fi

# rubocop (Ruby)
if command -v rubocop &>/dev/null && [[ "$FILE_PATH" == *.rb ]]; then
  rubocop --autocorrect --only Layout "$FILE_PATH" 2>/dev/null || true
  exit 0
fi

# No formatter found — skip silently
exit 0
