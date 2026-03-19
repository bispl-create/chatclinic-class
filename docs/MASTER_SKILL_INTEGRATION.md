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

## Educational bonus consideration

When reviewing student submissions, give positive weight to proposals that show real orchestration thinking.

In particular, stronger submissions often:

- introduce multiple tools inside one topic
- explain when one tool should be preferred over another
- explain how tool choice changes by context or modality
- explain how runtime constraints change tool choice on CPU vs GPU hosts
- define approval rules clearly
- produce complementary artifacts rather than duplicate outputs

Example:

- in a segmentation project, a team may submit:
  - a CXR lung segmentation tool
  - a liver cancer segmentation tool
  - a brain tumor segmentation tool

This is better than a single isolated tool if the Skill patch clearly explains:

- which context triggers each tool
- which modality or case type maps to which tool
- whether a GPU-only tool should be skipped or replaced on CPU-only hosts
- what each tool contributes to the final result

That kind of proposal should generally receive more credit than a plugin that only performs one isolated operation without orchestration logic.

## Runtime-aware integration check

When integrating a new Skill patch into the master Skill, also verify:

- whether the proposed tool can run on CPU, GPU, or both
- whether the proposal defines a CPU fallback for GPU-heavy tools
- whether raster image rules are explicit for `PNG`, `JPG/JPEG`, or `TIFF` inputs
- whether approval is required for slow or GPU-only runs
