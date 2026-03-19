# KAIST AI619 (Spring 2026)

Course companion repository for the **KAIST AI619** class offered in **Spring 2026**.

<div style="padding:12px 16px; border-radius:12px; background:#fff1f2; border:2px solid #fb7185; color:#9f1239; margin:16px 0;">
  <strong>Revision history</strong><br/>
  <strong>March 2026 update:</strong> ChatClinic now supports CPU/GPU-aware tool runtime metadata and first-pass raster medical image intake for <code>PNG</code>, <code>JPG/JPEG</code>, and <code>TIFF</code> via <code>image_review_tool</code>.<br/>
  <strong>March 2026 update:</strong> Final submissions must now clearly include the plugin package, Skill patch, background papers for the tool, and presentation slides explaining implementation and ChatClinic integration.
</div>

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

The official final submission site or upload method will be announced later through **KLMS**.

## Final submission package

Every team should prepare:

- one plugin package
- one Skill patch proposal
- one short background paper list for the tool
- one slide deck explaining implementation and ChatClinic integration

Recommended package structure:

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
  references/
    background_papers.md
  slides/
    team01_chatclinic_tool_presentation.pdf
```

Use the detailed submission rules in [docs/SUBMISSION_SITE_SPEC.md](/Users/jongcye/Documents/Codex/workspace/chatclinic-class/docs/SUBMISSION_SITE_SPEC.md).

## Submission timeline

There are two recommended submission/presentation windows for the class project:

1. **Midterm-period early track**
   - teams that finish early may submit and present during the midterm period
   - this early track is intended for teams that want feedback sooner
   - **bonus consideration** should be given to teams that complete a strong, integrable project by this earlier window

2. **Final-period regular track**
   - the default submission and presentation window is the final exam period
   - teams that do not use the early track should follow the final-period schedule

Exact calendar dates will be announced separately in class or through **KLMS**.

## Current signup sheet

Current team signup sheet:

- [Google signup sheet](https://docs.google.com/spreadsheets/d/1qBiqZgEwJXho3MgaGZzxPte99jxD6xyUUIj5OkFNZIY/edit?usp=sharing)

Note:

- the link is reachable
- Google may require sign-in depending on sharing settings

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

Additional bonus consideration may also be given to teams that complete a strong submission in the **midterm-period early track** rather than waiting until the final-period deadline.

## Reference policy

The papers listed in the course documents are representative examples, not a fixed mandatory list.

Students may use other appropriate papers as long as they:

- clearly cite them
- explain why they are relevant
- explain how their tool relates to the cited baseline

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
