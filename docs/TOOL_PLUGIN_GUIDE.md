# Tool Plugin Guide

This guide explains how collaborators and student teams can add a new tool for `ChatClinic`.

## What to submit

Each team submits one plugin package and one Skill patch proposal.

Recommended final submission structure:

```text
team_name_submission.zip
  plugin/
    tool.json
    run.py
    README.md
    requirements.txt
  skill_update/
    skill_patch.md
    skill_rationale.md
```

## Minimal manifest

Create `tool.json`.

```json
{
  "name": "team_name_tool",
  "team": "team_name",
  "task_type": "analysis-task",
  "modality": "clinical-table",
  "approval_required": true,
  "entrypoint": "run.py",
  "description": "Short human-readable description of the tool."
}
```

## Execution contract

`ChatClinic` runs the plugin like this:

```bash
python3 run.py --input input.json --output output.json
```

Your script must:

1. read `--input`
2. write `--output`
3. exit with code `0` on success

## Skill update policy

For class submissions, do not submit a full replacement Skill.

Instead, submit:

- `skill_update/skill_patch.md`
- `skill_update/skill_rationale.md`

The instructor will merge accepted proposals into the master Skill.

## Related documents

- [Course tool contract](COURSE_TOOLS.md)
- [Skill patch template](SKILL_PATCH_TEMPLATE.md)
- [Submission site specification](SUBMISSION_SITE_SPEC.md)
- [Master Skill integration guide](MASTER_SKILL_INTEGRATION.md)
