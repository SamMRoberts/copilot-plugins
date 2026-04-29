# Scripts

Place helper scripts here when the harness needs repeatable local checks, context capture, or report generation.

Prefer scripts for behavior that must be deterministic and easy for agents to run before final handoff.

## Scripts

- `harness_section_status.py`: inspects `<section_name>.<state>.md` validation files and reports the next section to regenerate, improve, or skip. Default sections include purpose, scope, knowledge system, operating phases, boundaries, agent legibility, mechanical enforcement, verification, evidence, handoff, automation, feedback loops, and open questions.
