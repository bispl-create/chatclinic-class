# KAIST AI619 (Spring 2026)

Course companion repository for the **KAIST AI619** class offered in **Spring 2026**.

This repository supports the `ChatClinic` project workflow used in the course.

Main platform repository:

- [ChatClinic](https://github.com/bispl-create/chatclinic)

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
   - GitHub: [https://github.com/bispl-create/chatclinic](https://github.com/bispl-create/chatclinic)

2. **KAIST AI619 course repo**
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

## Grading note

Projects that only submit a single standalone tool can still receive good credit.

However, higher credit should be given to teams that:

- build multiple related tools within the same topic
- design a Skill patch that explains when each tool should be used
- specify how tool choice depends on context
- define ordering or dependency rules clearly

For example, in a segmentation topic, a team that proposes:

- a CXR lung segmentation tool
- a liver cancer segmentation tool
- a brain tumor segmentation tool

with a clear Skill patch describing **which tool should be selected for which modality or clinical context**, should receive bonus consideration.

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
