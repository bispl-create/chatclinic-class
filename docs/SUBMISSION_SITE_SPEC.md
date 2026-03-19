# Submission Site Specification

This document describes how to structure a class submission site so that student plugins can be integrated into `ChatClinic` with minimal manual cleanup.

<div style="padding:12px 16px; border-radius:12px; background:#fff1f2; border:2px solid #fb7185; color:#9f1239; margin:16px 0;">
  <strong>Revision history</strong><br/>
  <strong>March 2026 update:</strong> ChatClinic now supports CPU/GPU-aware tool runtime metadata and first-pass raster medical image intake for <code>PNG</code>, <code>JPG/JPEG</code>, and <code>TIFF</code> via <code>image_review_tool</code>.<br/>
  <strong>March 2026 update:</strong> Final submissions should clearly contain the plugin package, Skill patch, background papers, and a presentation deck explaining integration into ChatClinic.
</div>

## Main design principle

The best submission format is:

- metadata in a form
- plugin code in a zip
- Skill update as a patch proposal

For **topic signup**, use a shared sheet rather than a free-form form.

## Submission and presentation timeline

The class project should support two windows:

1. **Midterm-period early submission/presentation**
   - teams may submit and present during the midterm period if they finish early
   - this is encouraged for teams that want early feedback and early integration review
   - a strong early submission should receive **bonus consideration**

2. **Final-period regular submission/presentation**
   - this is the standard path for most teams
   - teams that do not use the early track should present and submit during the final exam period

Exact dates should be announced later through **KLMS** or in-class notice.

## Team signup sheet

Use one shared sheet with:

- topic rows
- four student columns
- first-come, first-served filling

Team size policy:

- **3 students per team is strongly recommended**
- a **4th student requires prior discussion with the instructor and explicit approval**

Recommended columns:

- `Topic`
- `Description`
- `Student 1`
- `Student 2`
- `Student 3`
- `Student 4`
- `Status`
- `Notes`

See:

- [Current Google signup sheet](https://docs.google.com/spreadsheets/d/1qBiqZgEwJXho3MgaGZzxPte99jxD6xyUUIj5OkFNZIY/edit?usp=sharing)

## Topic categories and representative papers

The signup sheet should list topic categories clearly so students know what kinds of tools are expected.

Below is a recommended interpretation of each topic, along with representative papers students may use as starting points.

These papers are **representative examples only**.

Students may cite and build on other relevant papers if those papers are appropriate for the proposed tool and are clearly referenced in the final submission.

### 1. Segmentation

Typical tool ideas:

- CXR lung segmentation
- liver cancer segmentation
- brain tumor segmentation

Representative papers:

- Olaf Ronneberger, Philipp Fischer, Thomas Brox. *U-Net: Convolutional Networks for Biomedical Image Segmentation*. MICCAI 2015.
- Ozan Oktay et al. *Attention U-Net: Learning Where to Look for the Pancreas*. arXiv 2018.
- Jieneng Chen et al. *TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation*. arXiv 2021.

### 2. Classification

Typical tool ideas:

- chest X-ray diagnosis
- dementia classification from brain MRI
- retinal disease classification

Representative papers:

- Pranav Rajpurkar et al. *CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning*. arXiv 2017.
- Hoo-Chang Shin et al. *Deep Convolutional Neural Networks for Computer-Aided Detection: CNN Architectures, Dataset Characteristics and Transfer Learning*. IEEE TMI 2016.
- Yukun Zhou et al. *A foundation model for generalizable disease detection from retinal images*. Nature 2023.

### 3. Detection

Typical tool ideas:

- lung nodule detection
- GI/endoscopy lesion detection
- polyp or cancer candidate detection

Representative papers:

- Joseph Redmon et al. *You Only Look Once: Unified, Real-Time Object Detection*. CVPR 2016.
- Tsung-Yi Lin et al. *Focal Loss for Dense Object Detection*. ICCV 2017.
- Xin Yi et al. *Deep Learning for Pulmonary Nodule Detection: A Survey*. Medical Image Analysis / survey-style references are also acceptable as starting points.

### 4. Restoration

Typical tool ideas:

- low-dose CT denoising
- low-dose CXR denoising
- MR denoising or super-resolution

Representative papers:

- Karen Simonyan, Andrea Zisserman. *Very Deep Convolutional Networks for Large-Scale Image Recognition*. arXiv 2014.  (useful as a backbone reference)
- Kaiming He et al. *Deep Residual Learning for Image Recognition*. CVPR 2016.  (useful as a backbone reference)
- Several task-specific medical denoising papers may be used; students should cite the exact restoration model they implement.

### 5. Image registration

Typical tool ideas:

- mono-modal registration
- multi-modal registration
- follow-up timepoint alignment

Representative papers:

- Guha Balakrishnan et al. *VoxelMorph: A Learning Framework for Deformable Medical Image Registration*. IEEE TMI 2019.
- Hongming Li, Yefeng Zheng. *Learning deformable image registration for CT-MR or MR-MR tasks* style works are acceptable if clearly cited.

### 6. Medical VLM

Typical tool ideas:

- image-text medical QA
- report-aware visual understanding
- disease explanation with visual evidence

Representative papers:

- Chaoyi Wu et al. *PMC-VQA: Visual Instruction Tuning for Medical Visual Question Answering* style references are acceptable if clearly cited.
- Open-source medical VLM papers such as *Med-Flamingo* or *LLaVA-Med* may be used if the team clearly states the exact model.
- Harini Moor et al. *Med-Flamingo: a Multimodal Medical Few-shot Learner*. arXiv 2023.

### 7. Medical RAG

Typical tool ideas:

- retrieval from clinical guidelines
- retrieval from radiology/pathology references
- evidence-grounded Q&A

Representative papers:

- Patrick Lewis et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020.
- Microsoft / Meta / open biomedical RAG papers are acceptable if the exact system is cited.

### 8. Clinical Reasoning Model

Typical tool ideas:

- differential diagnosis assistant
- structured reasoning over multimodal artifacts
- patient-specific recommendation drafts

Representative papers:

- General clinical reasoning benchmark/model papers are acceptable if clearly cited.
- If using a recent medical reasoning model, students should cite the exact paper or model card.

### 9. Agentic model

Typical tool ideas:

- MCP-connected external tools
- agent2agent orchestration
- multi-tool planning and approval workflows

Representative references:

- MCP-related official documentation or tool-calling architecture references
- recent agent orchestration papers or engineering reports

## Recommendation for students

Students do not need to copy the exact papers above.

However, each team should:

- clearly name the model family they are building on
- cite a small set of representative references
- explain how their proposed tool differs from or extends the cited baseline

## Final submission notice

The final submission site or upload method will be announced later through **KLMS**.

Until then, students should focus on:

- selecting a topic
- forming a team
- preparing the plugin package
- preparing the Skill patch proposal

In addition, students should decide whether they aim for:

- the **midterm-period early track**, which may receive bonus consideration
- or the **final-period regular track**

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
- Presentation slides explaining:
  - the selected background model or method
  - how the tool was implemented
  - how the tool should be integrated into `ChatClinic`
  - how the Skill patch controls when the tool should be used

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
  references/
    background_papers.md
  slides/
    team01_chatclinic_tool_presentation.pdf
```
