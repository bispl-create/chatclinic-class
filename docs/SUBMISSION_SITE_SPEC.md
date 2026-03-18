# Submission Site Specification

This document describes how to structure a class submission site so that student plugins can be integrated into `ChatClinic` with minimal manual cleanup.

## Main design principle

The best submission format is:

- metadata in a form
- plugin code in a zip
- Skill update as a patch proposal

## Final submission fields

- Team name
- Tool name
- Tool description
- Task type
- Modality
- Approval required
- Plugin zip upload
- `skill_patch.md` upload
- `skill_rationale.md` upload
- Optional demo video
- Optional sample input/output bundle

## Recommended zip structure

```text
team01_submission.zip
  plugin/
    tool.json
    run.py
    README.md
  skill_update/
    skill_patch.md
    skill_rationale.md
```
