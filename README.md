# ChatClinic Class

Classroom companion repository for `ChatClinic`.

This repository is meant for:

- student team signup
- tool plugin submission rules
- Skill patch proposal templates
- instructor review and integration workflow

The main application code stays in the `ChatClinic` platform repository.

## Why this repository is separate

It is useful to keep two repositories:

1. **ChatClinic platform repo**
   - application code
   - production or demo-ready tools
   - master Skill
   - shared runner

2. **ChatClinic class repo**
   - course instructions
   - signup sheet specification
   - plugin submission templates
   - Skill patch proposal templates
   - instructor integration workflow

This prevents the platform repository from becoming overloaded with course administration documents.

## Read first

- [Course tool contract](docs/COURSE_TOOLS.md)
- [Tool plugin guide](docs/TOOL_PLUGIN_GUIDE.md)
- [Skill patch template](docs/SKILL_PATCH_TEMPLATE.md)
- [Submission site specification](docs/SUBMISSION_SITE_SPEC.md)
- [Master Skill integration guide](docs/MASTER_SKILL_INTEGRATION.md)

## Recommended class workflow

1. Students sign up as teams.
2. Each team proposes a tool project.
3. Each team submits:
   - one plugin package
   - one Skill patch proposal
4. The instructor reviews the tool and the proposed orchestration rule.
5. Accepted tools are integrated into the main `ChatClinic` repository.
6. Accepted Skill patches are merged into one master `SKILL.md`.

## Submission package structure

```text
team01_submission.zip
  plugin/
    tool.json
    run.py
    README.md
    requirements.txt
  skill_update/
    skill_patch.md
    skill_rationale.md
```

## Included template

This repository includes a starter submission template under:

- `submission_template/`
