# Copilot Persona Skills Bundle

This bundle contains GitHub Copilot-style skill folders for role personas and personality modifiers.

## Included

### Base role skills
- senior-engineer-systems-thinker
- mid-engineer-pragmatic-builder
- junior-engineer-careful-implementer
- staff-engineer-technical-strategist
- project-manager-delivery-driver
- product-manager-outcome-focused
- engineering-manager-team-optimizer
- people-manager-supportive-operator

### Personality modifier skills
- detail-oriented
- adhd-style
- average-baseline

## Folder structure

Each skill folder contains:
- `SKILL.md`
- `persona.md`

## Usage pattern

A simple pattern is:

1. Pick one base role skill
2. Optionally add one personality modifier
3. In your orchestration, read the base role `persona.md` first
4. Then apply the modifier `persona.md`

Example combinations:
- senior-engineer-systems-thinker + detail-oriented
- mid-engineer-pragmatic-builder + adhd-style
- project-manager-delivery-driver + average-baseline

## Note

These files use explicit references from `SKILL.md` to `persona.md`. They do not rely on undocumented frontmatter imports.
