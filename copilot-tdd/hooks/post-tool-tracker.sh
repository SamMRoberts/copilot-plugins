#!/bin/bash
# TDD Post-Tool Tracker
# Tracks file modifications and test execution results to build an audit trail
# of TDD cycle progress. Detects test commands and logs pass/fail outcomes
# to help monitor Red → Green → Refactor transitions.
set -e

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')
TOOL_ARGS=$(echo "$INPUT" | jq -r '.toolArgs')
RESULT_TYPE=$(echo "$INPUT" | jq -r '.toolResult.resultType')
RESULT_TEXT=$(echo "$INPUT" | jq -r '.toolResult.textResultForLlm // ""')
CWD=$(echo "$INPUT" | jq -r '.cwd')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')

LOG_DIR="${CWD}/.tdd-logs"
mkdir -p "$LOG_DIR"
SESSION_FILE="${LOG_DIR}/session.jsonl"
STATE_FILE="${LOG_DIR}/cycle-state.json"

# ─── Track file edits and creations ───
if [ "$TOOL_NAME" = "edit" ] || [ "$TOOL_NAME" = "create" ]; then
  FILE_PATH=$(echo "$TOOL_ARGS" | jq -r '.path // empty')
  if [ -n "$FILE_PATH" ]; then
    jq -n -c \
      --arg ts "$TIMESTAMP" \
      --arg tool "$TOOL_NAME" \
      --arg file "$FILE_PATH" \
      --arg result "$RESULT_TYPE" \
      '{event: "file_modified", timestamp: $ts, action: $tool, file: $file, result: $result}' \
      >> "$SESSION_FILE"

    # Update cycle state with modified files (use a lock file to prevent races)
    if [ -f "$STATE_FILE" ]; then
      LOCK_FILE="${STATE_FILE}.lock"
      FIELD="filesEdited"
      if [ "$TOOL_NAME" = "create" ]; then
        FIELD="filesCreated"
      fi
      (
        flock -w 5 200 || exit 0
        UPDATED=$(jq --arg file "$FILE_PATH" --arg field "$FIELD" \
          'if (.[$field] | index($file)) == null then .[$field] += [$file] else . end' \
          "$STATE_FILE")
        echo "$UPDATED" > "$STATE_FILE"
      ) 200>"$LOCK_FILE"
    fi
  fi
fi

# ─── Track test executions ───
if [ "$TOOL_NAME" = "bash" ] || [ "$TOOL_NAME" = "execute" ]; then
  COMMAND=$(echo "$TOOL_ARGS" | jq -r '.command // empty')

  # Detect test commands by common patterns
  IS_TEST="false"
  case "$COMMAND" in
    *"npm test"*|*"npm run test"*|*"npx jest"*|*"npx vitest"*|*"npx mocha"*)
      IS_TEST="true" ;;
    *"pytest"*|*"python -m pytest"*|*"python -m unittest"*)
      IS_TEST="true" ;;
    *"go test"*)
      IS_TEST="true" ;;
    *"dotnet test"*|*"dotnet xunit"*)
      IS_TEST="true" ;;
    *"cargo test"*)
      IS_TEST="true" ;;
    *"bundle exec rspec"*|*"rake test"*|*"rails test"*)
      IS_TEST="true" ;;
    *"mvn test"*|*"gradle test"*)
      IS_TEST="true" ;;
    *"mix test"*)
      IS_TEST="true" ;;
  esac

  if [ "$IS_TEST" = "true" ]; then
    # Determine if tests passed or failed
    TEST_OUTCOME="unknown"
    if [ "$RESULT_TYPE" = "success" ]; then
      TEST_OUTCOME="pass"
    elif [ "$RESULT_TYPE" = "failure" ]; then
      TEST_OUTCOME="fail"
    fi

    jq -n -c \
      --arg ts "$TIMESTAMP" \
      --arg cmd "$COMMAND" \
      --arg outcome "$TEST_OUTCOME" \
      --arg result "$RESULT_TYPE" \
      '{event: "test_execution", timestamp: $ts, command: $cmd, outcome: $outcome, resultType: $result}' \
      >> "$SESSION_FILE"

    # Update cycle state counters (use a lock file to prevent races)
    if [ -f "$STATE_FILE" ]; then
      LOCK_FILE="${STATE_FILE}.lock"
      (
        flock -w 5 200 || exit 0
        if [ "$TEST_OUTCOME" = "pass" ]; then
          UPDATED=$(jq '.testsRun += 1 | .testsPassed += 1' "$STATE_FILE")
        elif [ "$TEST_OUTCOME" = "fail" ]; then
          UPDATED=$(jq '.testsRun += 1 | .testsFailed += 1' "$STATE_FILE")
        else
          UPDATED=$(jq '.testsRun += 1' "$STATE_FILE")
        fi
        echo "$UPDATED" > "$STATE_FILE"
      ) 200>"$LOCK_FILE"
    fi
  fi
fi
