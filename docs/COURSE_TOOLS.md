# Course Tool Contract

`ChatClinic` can be extended by student teams without requiring each team to operate a separate server.

## Submission model

For the standard class project:

- the instructor provides `ChatClinic`
- the instructor maintains the orchestration Skill and shared runner
- each student team submits a **tool plugin**
- each student team also submits a **Skill patch proposal**

Student teams normally do **not** need to submit:

- a complete replacement Skill
- a separate MCP server
- a separate web service
- a separate frontend

In other words:

- `Master Skill` = centrally managed behavior/policy
- `Tool plugin` = primary student deliverable
- `Skill patch` = student proposal for how the new tool should be orchestrated

## When the Skill should be updated

Update the Skill when:

- a new tool adds a new workflow
- a new tool should be selected for new keywords or modalities
- a new tool requires approval
- a new tool depends on an earlier tool or artifact
- a new tool should replace an older preferred tool

In practice:

- student teams submit the plugin
- student teams submit a small `skill_patch.md` proposal
- the instructor or maintainer merges multiple proposals into one master Skill if routing policy changes

## Goal

Each team submits a tool that can be discovered and executed by the shared runner.

Examples:

- segmentation
- detection
- diagnosis draft
- image restoration
- FHIR summarization
- cohort analytics

## Grading emphasis

Basic credit comes from:

- a valid plugin
- a correct execution contract
- useful structured artifacts
- a clear Skill patch proposal

Additional credit should be given when a team goes beyond a single isolated tool.

### Recommended bonus criterion

Give extra credit when a team:

- integrates **multiple tools within the same topic**
- explains in the Skill patch **when each tool should be used**
- explains **how tool choice changes by context**
- defines **ordering or dependency rules** between tools

Example:

- a segmentation topic may include:
  - a CXR lung segmentation tool
  - a liver cancer segmentation tool
  - a brain tumor segmentation tool
- the Skill patch should then explain:
  - when the CXR tool should be selected
  - when the liver tool should be selected
  - when the brain tumor tool should be selected
  - how tool choice changes by modality or data type
  - when approval is needed

This is educationally valuable because it teaches students that Agentic AI is not only about building one model, but about designing a system in which multiple tools are orchestrated properly.

### Suggested interpretation

Higher-scoring projects usually demonstrate:

- more than one useful tool in the same topic area
- a thoughtful orchestration policy
- clear conditions for tool selection
- stronger integration with the master Skill and Studio artifacts

## Recommended submission structure

```text
team01_submission.zip
  plugin/
    tool.json
    run.py
    requirements.txt
    README.md
  skill_update/
    skill_patch.md
    skill_rationale.md
```

## Related documents

- [Tool plugin guide](TOOL_PLUGIN_GUIDE.md)
- [Skill patch template](SKILL_PATCH_TEMPLATE.md)
- [Submission site specification](SUBMISSION_SITE_SPEC.md)
- [Master Skill integration guide](MASTER_SKILL_INTEGRATION.md)
