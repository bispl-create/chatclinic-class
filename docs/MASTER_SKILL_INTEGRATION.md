# Master Skill Integration Guide

There should be **one master Skill** for the deployed `ChatClinic`.

Student teams propose changes, but they should not replace the shared orchestration policy directly.

## Inputs to review

For each team, review:

- `plugin/tool.json`
- `plugin/README.md`
- `skill_update/skill_patch.md`
- `skill_update/skill_rationale.md`

## Integration rule

When merging proposals into the master Skill:

- keep the Skill high level
- keep routing policy human-readable
- do not copy implementation details from `run.py`
- prefer one short rule over many scattered mentions
