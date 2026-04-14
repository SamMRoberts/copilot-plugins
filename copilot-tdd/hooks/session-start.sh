#!/bin/bash
# TDD Session Start Hook
# Initializes the TDD audit log for tracking cycle progress, file changes,
# and test results throughout the session.
set -e

INPUT=$(cat)
SOURCE=$(echo "$INPUT" | jq -r '.source')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')
CWD=$(echo "$INPUT" | jq -r '.cwd')
PROMPT=$(echo "$INPUT" | jq -r '.initialPrompt // "N/A"')

# Create the TDD audit log directory
LOG_DIR="${CWD}/.tdd-logs"
mkdir -p "$LOG_DIR"

# Initialize the session log with metadata
SESSION_ID="tdd-$(date +%Y%m%d-%H%M%S)"
SESSION_FILE="${LOG_DIR}/session.jsonl"

jq -n -c \
  --arg id "$SESSION_ID" \
  --arg source "$SOURCE" \
  --arg ts "$TIMESTAMP" \
  --arg prompt "$PROMPT" \
  --arg cwd "$CWD" \
  '{
    event: "session_start",
    sessionId: $id,
    source: $source,
    timestamp: $ts,
    initialPrompt: $prompt,
    cwd: $cwd
  }' >> "$SESSION_FILE"

# Initialize cycle counter
echo '{"cycle": 0, "phase": "init", "testsRun": 0, "testsPassed": 0, "testsFailed": 0, "filesEdited": [], "filesCreated": []}' \
  > "${LOG_DIR}/cycle-state.json"
