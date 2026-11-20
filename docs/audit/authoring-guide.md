# Audit Authoring Guide

This guide keeps the audit consistent when different people write sections or when work happens at different times. Apply it to all section files and the final report.

## 1. Writing principles

- Write in clear, professional US English. Prefer plain language over jargon.
- Use a neutral, evidence-led tone. Describe what was observed and why it matters; avoid blame, speculation, and sales language.
- Be specific and concise. Name the affected page, component, task, or user group where possible.
- Distinguish observed facts from interpretation and recommendations.
- Do not claim legal noncompliance, guaranteed ranking changes, or guaranteed AI citations. Describe the evidence and potential risk instead.
- Use consistent terms and labels as defined in this guide.

## 2. Standard section structure

Each website file within an audit section should use this structure:

```markdown
# [Audit Section] — [Website]

## Assessment Scope
- **Website:**
- **Review date:**
- **Pages, templates, or journeys reviewed:**
- **Methods and tools:**

## Summary
Briefly state the overall observation for this section and website. If the review is not complete, label this as a draft.

## Findings
Add findings using the format below, ordered by priority and then by user or business impact.

## Positive Observations
Record effective patterns worth preserving, where relevant.

## Limitations
Describe material limits on the review, such as inaccessible flows, unavailable analytics, or automated checks that could not be manually verified.
```

Remove sections that genuinely do not apply, but do not omit scope, findings, or material limitations. Use `Not assessed` when an expected area was not reviewed; do not imply it passed.

## 3. Review controls and coverage

The audit is more than a list of findings. For each area included in the agreed scope, define the topics or controls to check and record what was reviewed, what the evidence showed, and what remains open. Keep this checklist or matrix separate from the findings register: a completed check with no issue is still part of the audit record, but it is not a finding.

Use a section-specific review matrix when a workstream has several controls, evidence sources, or coverage limits. A single checklist is sufficient for a smaller review. Each review item should state, as appropriate:

- The question or control being checked.
- The agreed scope, including pages, templates, journeys, devices, or sample size.
- The method and evidence used, with the review date.
- The result and status, including a pass or no-issue result when supported.
- Any limitation, manual validation, or follow-up needed.
- Related finding IDs, if an issue or opportunity merits a finding.

Use these statuses consistently across workstreams; add a justified section-specific status only when necessary:

| Status | Meaning |
| --- | --- |
| **Not assessed** | Review has not started for this item. |
| **In progress** | Some evidence has been reviewed, but the check is incomplete. |
| **Needs manual validation** | An automated signal or incomplete evidence needs human confirmation before a conclusion. |
| **Verified — no issue observed** | The documented checks found no issue within the stated scope and limits. This is a recorded result, not a guarantee beyond that scope. |
| **Finding recorded** | A supported issue or opportunity is documented in the site report and linked by ID. |
| **Not verifiable in public scope** | Required access, evidence, or testing is outside the agreed audit scope or unavailable; state why. |
| **Not applicable** | The control does not apply; explain why. |

Do not treat an empty findings list, a tool's lack of alerts, or an untested item as a pass. Report coverage and findings separately so readers can see both what was checked and what needs action.

## 4. Finding format

Give each finding a short, descriptive title. Keep one underlying issue per finding. Use this format:

```markdown
### [Issue and affected element]

- **Finding ID:** [SECTION]-[SITE]-[NUMBER]
- **Page or component:** [Page name and URL, if available]
- **Priority:** Critical / High / Medium / Low
- **Evidence:** [What was observed, how it was checked, and a link or screenshot reference]
- **Impact:** [Who is affected and what task, understanding, or outcome is hindered]
- **Recommendation:** [A concrete action that addresses the observed issue]
- **Implementation complexity:** Low / Medium / High
- **Related standard:** [When applicable, e.g. WCAG 2.1 success criterion]
```

Use stable IDs: `A11Y-NITA-001`, `SEO-MTB-001`, `AEO-NITA-001`, `GEO-MTB-001`, `UX-NITA-001`. Use `NITA` for `nita.illinois.gov` and `MTB` for `mytransitbenefit.com`. Number findings sequentially within each section and site. Do not reuse an ID; retain it if the finding is later edited.

### Evidence quality

- Include the observation date and the review method for results that can change over time.
- Link to the affected public URL. For screenshots or other artifacts, use a stable relative path in the repository, such as `evidence/accessibility/nita-homepage-menu.png`.
- Describe the observed behavior, not only the tool's score or alert.
- For automated results, name the tool and version when available, and manually verify the issue where practical.
- Information published on the audited websites, including staff names or email addresses that appear in public pages or their source code, may be quoted in evidence and findings when it helps locate or explain an issue (team decision, 2026-11-20; the report has limited distribution). Do not add personal data that is not publicly published, such as data from forms, accounts, or private communications.

## 5. Priority and complexity

Assign priority based on the severity and reach of the user impact, not on how easy the fix appears.

| Priority | Use when |
| --- | --- |
| **Critical** | A severe barrier or risk affects an essential task or a broad group and needs immediate attention. Explain the basis clearly. |
| **High** | A substantial barrier or defect affects an important task, key content, or a recurring experience. |
| **Medium** | A meaningful issue causes friction or reduces clarity, but users can generally complete the task. |
| **Low** | A limited improvement would refine usability, consistency, or discoverability without blocking a key task. |

Implementation complexity is a separate estimate:

- **Low:** A localized change with limited design, content, or engineering coordination.
- **Medium:** A change involving several components, templates, or coordinated review.
- **High:** A broad change involving architecture, multiple teams, significant content work, or external dependencies.

These are audit estimates, not delivery commitments. State assumptions when complexity is uncertain.

## 6. Section-specific guidance

- **Accessibility & ADA:** Cite the applicable WCAG 2.1 Level AA success criterion when confidently identified. Note the tested browser, device, assistive technology, or automated tool when relevant. Frame ADA Title II observations as potential compliance risks; this audit is not a legal determination or certification.
- **SEO:** Separate crawlability, indexability, metadata, content, structured data, and performance observations. Do not infer search ranking impact without supporting evidence.
- **AEO:** Focus on whether content gives clear, direct answers to likely user questions and is structured so answer systems can interpret it.
- **GEO:** Assess discoverability, clarity, context, and machine-readable signals. Do not promise visibility, citation, or inclusion in generative answers.
- **UX:** Describe the user goal, the steps or friction observed, and the effect on task completion or confidence. Avoid subjective design judgments without a user-centered reason.

## 7. Language and formatting

- Use sentence case for headings and labels.
- Use **website** consistently; avoid switching between “site,” “platform,” and “property” unless the distinction matters.
- Use **user** for the people using the websites. Identify a specific group only when evidence supports it.
- Spell out a term on first use, followed by its abbreviation: Search Engine Optimization (SEO), Answer Engine Optimization (AEO), and Generative Engine Optimization (GEO).
- Use US English spelling and date format `YYYY-MM-DD`.
- Use descriptive link text and Markdown links for URLs and repository evidence.
- Keep recommendations actionable: start with a verb and identify the intended change.

## 8. Review checklist

Before marking a section ready for consolidation, confirm:

- Scope, review date, methods, and limitations are recorded.
- Every in-scope area has a review-control/checklist status or an explicit reason it cannot be completed.
- Verified controls and no-issue results remain visible even when no finding is created.
- Every finding identifies the website and affected page or component.
- Evidence supports the finding and is specific enough for another reviewer to reproduce or understand it.
- Impact and recommendation are understandable without specialist knowledge.
- Priority and complexity follow the definitions above.
- Findings are distinct, IDs are unique, and no unsupported compliance or outcome claims are made.
- Spelling, terminology, heading style, and formatting are consistent with this guide.
