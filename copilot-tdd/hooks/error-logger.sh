#!/bin/bash
# TDD Error Logger
# Logs errors that occur during agent execution to the TDD audit trail
# for debugging and post-session analysis.
set -e

INPUT=$(cat)
ERROR_MSG=$(echo "$INPUT" | jq -r '.error.message // "unknown"')
ERROR_NAME=$(echo "$INPUT" | jq -r '.error.name // "Error"')
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')
CWD=$(echo "$INPUT" | jq -r '.cwd')

LOG_DIR="${CWD}/.tdd-logs"
mkdir -p "$LOG_DIR"

jq -n -c \
  --arg ts "$TIMESTAMP" \
  --arg name "$ERROR_NAME" \
  --arg msg "$ERROR_MSG" \
  '{event: "error", timestamp: $ts, errorName: $name, errorMessage: $msg}' \
  >> "${LOG_DIR}/session.jsonl"
