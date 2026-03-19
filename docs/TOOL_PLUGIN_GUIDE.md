# Tool Plugin Guide

This guide explains how collaborators and student teams can add a new tool for `ChatClinic`.

> [!IMPORTANT]
> **Revision history**
> - **March 2026 update:** ChatClinic now supports CPU/GPU-aware tool runtime metadata and first-pass raster medical image intake for `PNG`, `JPG/JPEG`, and `TIFF` via `image_review_tool`.
> - **March 2026 update:** The expected student deliverable now includes a plugin package, Skill patch, background paper summary, and presentation slides for integration review.

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
  references/
    background_papers.md
  slides/
    team_name_chatclinic_tool_presentation.pdf
```

The expected final deliverable now includes:

- the executable plugin
- the orchestration proposal (`skill_patch.md`)
- a short background paper summary
- presentation slides for final review

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

Recommended metadata:

```json
{
  "keywords": ["cohort", "sheet", "subject"],
  "recommended_stage": "post-intake",
  "priority": 80,
  "produces": ["cohort_browser"],
  "consumes": ["table_rows"]
}
```

Recommended runtime metadata:

```json
{
  "runtime": {
    "host_compatible": ["cpu", "gpu"],
    "supported_accelerators": ["cpu"],
    "preferred_accelerator": "cpu",
    "requires_gpu": false,
    "allow_cpu_fallback": true,
    "estimated_runtime_sec": 10,
    "notes": "Explain whether the tool only needs CPU, prefers GPU, or requires GPU."
  }
}
```

These fields help the orchestration Skill choose tools with less manual hard-coding and help the shared runner decide whether a tool can run on CPU, GPU, or both.

## Execution contract

`ChatClinic` runs the plugin like this:

```bash
python3 run.py --input input.json --output output.json
```

Your script must:

1. read `--input`
2. write `--output`
3. exit with code `0` on success

## Best practices

- Keep outputs deterministic when possible.
- Return structured artifacts, not only free-form prose.
- Do not assume internet access.
- Do not assume a GPU unless your tool explicitly documents it in `tool.json`.
- Do not write outside the plugin working area unless truly needed.
- Emit helpful stderr messages when a run fails.

## Supported source families in ChatClinic

Plugins can currently be designed around source families such as:

- clinical tables (`csv`, `tsv`, `xlsx`, `xlsm`, `xls`)
- FHIR / HL7 clinical messages
- DICOM medical images
- raster medical images (`png`, `jpg`, `jpeg`, `tif`, `tiff`)
- plain-text clinical notes

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
