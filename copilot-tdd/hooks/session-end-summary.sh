#!/bin/bash
# TDD Session End Summary
# Generates a summary of the TDD session including files changed, tests run,
# and cycle statistics. Writes to the audit log for review.
set -e

INPUT=$(cat)
REASON=$(echo "$INPUT" | jq -r '.reason')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')
CWD=$(echo "$INPUT" | jq -r '.cwd')

LOG_DIR="${CWD}/.tdd-logs"
SESSION_FILE="${LOG_DIR}/session.jsonl"
STATE_FILE="${LOG_DIR}/cycle-state.json"

# Skip if no log directory exists (session-start may not have run)
if [ ! -d "$LOG_DIR" ]; then
  exit 0
fi

# Read cycle state
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0
FILES_EDITED="[]"
FILES_CREATED="[]"

if [ -f "$STATE_FILE" ]; then
  TESTS_RUN=$(jq -r '.testsRun // 0' "$STATE_FILE")
  TESTS_PASSED=$(jq -r '.testsPassed // 0' "$STATE_FILE")
  TESTS_FAILED=$(jq -r '.testsFailed // 0' "$STATE_FILE")
  FILES_EDITED=$(jq -c '.filesEdited // []' "$STATE_FILE")
  FILES_CREATED=$(jq -c '.filesCreated // []' "$STATE_FILE")
fi

# Count events from the session log
TOOL_INVOCATIONS=0
FILE_MODIFICATIONS=0
TEST_EXECUTIONS=0

if [ -f "$SESSION_FILE" ]; then
  TOOL_INVOCATIONS=$(grep -c '"event":"tool_invoked"' "$SESSION_FILE" 2>/dev/null || echo "0")
  FILE_MODIFICATIONS=$(grep -c '"event":"file_modified"' "$SESSION_FILE" 2>/dev/null || echo "0")
  TEST_EXECUTIONS=$(grep -c '"event":"test_execution"' "$SESSION_FILE" 2>/dev/null || echo "0")
fi

# Write the session summary
jq -n -c \
  --arg ts "$TIMESTAMP" \
  --arg reason "$REASON" \
  --argjson tests_run "$TESTS_RUN" \
  --argjson tests_passed "$TESTS_PASSED" \
  --argjson tests_failed "$TESTS_FAILED" \
  --argjson files_edited "$FILES_EDITED" \
  --argjson files_created "$FILES_CREATED" \
  --argjson tool_invocations "$TOOL_INVOCATIONS" \
  --argjson file_modifications "$FILE_MODIFICATIONS" \
  --argjson test_executions "$TEST_EXECUTIONS" \
  '{
    event: "session_end",
    timestamp: $ts,
    reason: $reason,
    summary: {
      toolInvocations: $tool_invocations,
      fileModifications: $file_modifications,
      testExecutions: $test_executions,
      testsRun: $tests_run,
      testsPassed: $tests_passed,
      testsFailed: $tests_failed,
      filesEdited: $files_edited,
      filesCreated: $files_created
    }
  }' >> "$SESSION_FILE"
