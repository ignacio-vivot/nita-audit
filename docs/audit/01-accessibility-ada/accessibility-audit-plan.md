# Accessibility & ADA Audit Work Plan — NITA websites

## Purpose and governing scope

This work plan operationalizes the accessibility scope in [`docs/project-overview.md`](../../project-overview.md#21-ada-compliance--digital-accessibility). That proposal is the source of truth for what the client was told would be reviewed. The accessibility assessment covers both [nita.illinois.gov](https://nita.illinois.gov/) and [mytransitbenefit.com](https://www.mytransitbenefit.com/) and includes:

1. Evaluation against WCAG 2.1 Level AA.
2. Navigation, keyboard accessibility, and screen reader compatibility.
3. Color contrast, typography, and visual accessibility.
4. Images, alternative text, links, forms, and interactive elements.
5. Semantic HTML structure and accessibility attributes.
6. Accessibility issues across desktop and mobile experiences.
7. Potential compliance risks related to ADA Title II requirements, with special attention to critical issues that may need immediate remediation.

The proposal calls for automated tools plus manual review of representative pages, templates, and interactions. It excludes a complete page-by-page certification and exhaustive testing of every interaction, and it is not a legal certification or a guarantee of ADA compliance. Findings are classified by severity and impact so that DHD and NITA can prioritize corrective actions.

The work is organized in four **steps** (Step 1–4), mirroring the [SEO](../02-seo/seo-audit-plan.md), [AEO](../03-aeo/aeo-audit-plan.md), and [GEO](../04-geo/geo-audit-plan.md) work plans. They are internal to this workstream and are distinct from the three project phases in the proposal.

## ADA Title II context and how the audit frames it

The Department of Justice's 2024 rule on web and mobile app accessibility for state and local governments (28 CFR part 35, subpart H) adopts WCAG 2.1 Level AA as the technical standard. An interim final rule published on 2026-04-20 extended the compliance dates: to 2027-04-26 for public entities with a total population of 50,000 or more, and to 2028-04-26 for smaller entities and special district governments ([Federal Register, 2026-04-20](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web)). The technical standard did not change. Re-check the rule's status at Step 4, because the extension was open to public comment.

How the audit uses this context:

- **Which date applies to NITA, and whether a rule exception applies to any content, are legal determinations outside this audit.** The plan records both dates and does not choose one.
- The rule lists exceptions, for example archived web content, preexisting conventional electronic documents that are not currently used to apply for or access a service, and some third-party content. The audit records the facts that matter for those questions (for example, whether RTA-era posts sit in a clearly identified archive, and whether a PDF is an application form currently in use) and leaves the conclusion to NITA's counsel.
- Findings report WCAG 2.1 AA evidence and describe **potential compliance risk**; they never state that a page is or is not compliant ([authoring guide, sections 1 and 6](../authoring-guide.md#6-section-specific-guidance)).
- WCAG 2.2 criteria are not part of the agreed standard. Where a WCAG 2.2 criterion (for example 2.5.8 Target Size, Minimum) helps explain a usability barrier, record it as an observation or best practice, not as a WCAG 2.1 AA failure.

## Boundaries with the other sections

Accessibility owns the WCAG success criteria. Other sections have already recorded observations that touch them; this section assesses each against WCAG and cross-references, instead of duplicating, the existing finding:

| Topic | Already recorded in | Accessibility use |
| --- | --- | --- |
| Alternative text that repeats file names; footer logo labeled “RTA” | SEO (`SEO-NITA-017`, `SEO-MTB-005`), from [`image-alt-review.csv`](../../../evidence/public-technical/2026-11-20/image-alt-review.csv) | Assess against 1.1.1 for screen-reader users. Record an accessibility finding only for what SEO does not cover (for example, functional images in links, decorative images that are announced); otherwise cite the SEO ID. |
| Page titles (“Home”, slogans) and multiple H1s | SEO (`SEO-NITA-010`, `SEO-NITA-011`, `SEO-MTB-003`; [`nita-multiple-h1.csv`](../../../evidence/public-technical/2026-11-24/rendered-review/nita-multiple-h1.csv)) | Assess against 2.4.2 and 2.4.6. |
| Heading levels, empty headings, table header cells, numbered steps, FAQ markup | AEO Step 3 part C, explicitly passed to accessibility ([`step3c/README.md`](../../../evidence/aeo/2026-11-26/step3c/README.md)) | Assess against 1.3.1 and 2.4.6; for example the 146 H2s on Meeting Materials and the five H1s on Section 5310. |
| Text size, link and checkbox target size, language switcher covering text | SEO mobile review ([`mobile-review/README.md`](../../../evidence/public-technical/2026-11-24/mobile-review/README.md)) | Assess against 1.4.4 and 1.4.10; target size is a WCAG 2.2 observation only. |
| Fare tables and projects table wider than a phone screen, clipped content | SEO (`SEO-NITA-022`), UX (`UX-NITA-019`, `UX-NITA-021`) | Assess against 1.4.10, applying the exception for content that needs two-dimensional layout, such as data tables. Clipped content with no way to scroll to it is not covered by that exception. |
| Intro banner that hides overflowing text | UX (`UX-NITA-018`) | Assess against 1.4.4 and 1.4.12. |
| Buttons without hover feedback | UX (`UX-NITA-013`) | Check focus visibility separately (2.4.7); hover alone is not a WCAG 2.1 AA criterion. |
| Translations: right-to-left layout, automatic switching, untranslated slide | UX (`UX-NITA-002`, `UX-NITA-006`, `UX-NITA-012`), SEO (`SEO-NITA-021`) | Check whether the page `lang` changes with the language (3.1.1) and whether parts in another language are marked (3.1.2). |
| Accessible-features video has captions | UX matrix (Accessible transit, row 2) | Reuse as 1.2.2 evidence for that video; other media still need checking. |
| Rider PDFs to be reissued with the NITA name | AEO (`AEO-NITA-002`) | Assess the same PDFs for document accessibility so a reissue can fix both. |

Usability effects that go beyond a WCAG criterion stay in UX ([UX work plan](../05-ux/ux-audit-plan.md#relationship-to-other-sections)).

## Agreed access boundary

The audit uses publicly accessible pages, documents, and open tools, with no CMS, source code, hosting, analytics, or user research (project decision, 2026-11-19). Consequences:

- Accessibility features that exist only in the CMS (for example a required alternative-text field) can be recommended but not verified.
- Forms are tested only up to client-side validation, with empty or clearly invalid values. **No form is submitted with valid data**, because that would send a real message or public comment to NITA. Server-side error messages and confirmation messages are **Not verifiable in public scope** unless they appear without sending.
- Testing with people with disabilities is outside scope. Screen reader checks by the team show how the content behaves with one assistive technology on one date; they do not represent every user or assistive technology.
- Services that the websites link to but do not host (Ventra, Google Maps, ArcGIS, YouTube, the transit benefit account portal) are noted when a journey depends on them, but not audited.

## Can the checks be automated as in SEO?

Short answer: **about three-fifths of the WCAG 2.1 AA criteria can be checked mostly by scripts, as in SEO; the rest need someone to operate the pages, which Claude can do in a browser in the same AI-assisted way as SEO Step 3 and UX. Only screen reader behavior needs a person with an assistive technology. No paid tool is needed.**

The per-criterion classification is in the [review matrix](accessibility-review-matrix.md#wcag-21-level-aa-coverage). Summary of the 50 Level A and AA criteria:

| Method class | Meaning | Criteria |
| --- | --- | --- |
| **Automated** | A rule engine or script detects failures reliably across many pages; the reviewer confirms a sample. | 9 (for example 1.4.3 contrast on solid backgrounds, 2.4.1 bypass blocks, 3.1.1 page language, 3.3.2 labels) |
| **Scripted + review** | Scripts collect the evidence across pages (measurements, screenshots, inventories, focus order); the reviewer judges it. | 21 (for example 1.1.1 alternative text quality, 1.4.10 reflow, 1.4.12 text spacing, 2.1.1 keyboard, 2.4.7 focus visible, 4.1.2 name, role, value) |
| **Manual (browser)** | The reviewer operates the page and judges the result: media, forms and errors, menus on hover, changes of context. Claude can do this with the browser tools; the team reviews conclusions. | 19 (for example the five media criteria, 1.4.13, 3.2.2, 3.3.1, 4.1.3) |
| **Not applicable** | 4.1.1 Parsing: W3C notes that it should be considered always satisfied for HTML content; duplicate-ID and markup problems that affect users are assessed under 1.3.1 and 4.1.2. | 1 |

Three limits apply whatever the class:

1. **A clean automated result is not a pass.** Rule engines check only part of each criterion. A criterion is marked **Verified — no issue observed** only after the review step for its class, within the stated sample.
2. **Screen reader behavior.** Scripts can read the browser's accessibility tree, which is what screen readers receive, and that catches most naming and role problems. How a screen reader actually announces menus, accordions, tabs, live messages, and the language switcher still needs a person listening. The proposal names screen reader compatibility explicitly, so the plan includes a short human session with VoiceOver, which is built into macOS and iOS (Step 3 part E).
3. **Mobile.** Reflow, orientation, and zoom can be scripted in Chromium device emulation, as in the SEO and UX mobile reviews. Touch screen readers (VoiceOver on iPhone, TalkBack) and physical devices are optional human checks; without them, the report states that mobile results come from emulation.

## Tools and evidence

| Tool or source | Use | Status, evidence, and limits |
| --- | --- | --- |
| [axe-core](https://github.com/dequelabs/axe-core) (open source, MPL-2.0) run through [Playwright](https://playwright.dev/) (open source, Apache-2.0) with the installed Google Chrome | Rule-based WCAG 2.1 A/AA checks on the rendered page at desktop (1280×800) and mobile (375×812) widths; save violations and “needs review” items as JSON and CSV. | **Installed 2026-11-27** (team approval): axe-core 4.14.1, @axe-core/playwright 4.14.1, Playwright 1.65.1, in [`tools/accessibility/`](../../../tools/accessibility/README.md), driving the installed Chrome 158 (no Playwright browser downloaded). Each run records its versions. Axe reports only what its rules cover. |
| Playwright scripts written for this audit (Node.js 24, installed) | Keyboard traversal (Tab order, focus screenshots, focus style changes, traps, context changes on focus); reflow at 320 CSS px; 200% zoom; text-spacing override; orientation; accessible-name versus visible-label comparison; accessibility-tree snapshots of custom widgets; contrast sampling of text over images. | Same install as above. Shared scripts live in [`tools/accessibility/`](../../../tools/accessibility/README.md); one-off scripts are saved with their evidence, as in SEO. Keyboard events are sent by the browser automation, not a physical keyboard. |
| Built-in Chromium browser in the Claude desktop app | Manual operation of menus, tabs, accordions, carousel, forms, video, language switcher; screenshots. | Already used in SEO, GEO, and UX. Desktop and emulated mobile only. |
| poppler `pdfinfo` 24.11.0 (installed) | Document triage: tagged or not, title, form fields, structure tree (`-struct`). | No language or PDF/UA rule check. A tagged PDF is not necessarily accessible; key documents also need manual review. |
| [veraPDF](https://verapdf.org/) (open source; Java 17 is installed) | Optional: PDF/UA-1 machine checks on key rider documents. | **Not installed.** Optional; decide in Step 1. Machine checks cover only part of PDF/UA. |
| Python standard library scripts | DOCX checks (headings, alternative text in the XML), result tables, joining axe output with the SEO inventories. | No install. |
| Existing evidence from SEO, AEO, and UX | Image alt inventory, heading outlines, multiple-H1 list, link-text graph, mobile measurements, rendered-versus-raw comparison, PDFs already downloaded. | Snapshots from their review dates; re-check live before citing a changed page. |
| VoiceOver (macOS Safari; optionally iOS) | Human screen reader session on the key journeys (Step 3 part E). | A team member runs it; Claude prepares the script and records results. One assistive technology, one date. |
| WebAIM WAVE (web interface) | Optional cross-check of two or three pages if an axe result is disputed. | Free one page at a time; the WAVE API is paid and is not used. |

Alternatives considered and not used: Screaming Frog's accessibility tab (needs JavaScript rendering, which the free version lacks; see the [SEO plan](../02-seo/seo-audit-plan.md#crawl-baseline-method)); Lighthouse's accessibility score (a subset of axe, already shown in PageSpeed Insights); Pa11y (wraps the same engines); paid platforms such as Siteimprove or the axe DevTools Pro tier (paid subscriptions are excluded by the proposal unless agreed).

Store new evidence in dated folders under `evidence/accessibility/`, each with a README stating method, tool versions, viewport, date, and limits. Keep scripts with their outputs. Reference SEO, AEO, and UX evidence in place; do not copy it. Keep `evidence/crawls/screaming-frog/**` read-only.

## Page, component, and journey scope

Details and per-page reasons are in the [review matrix](accessibility-review-matrix.md#page-level-review-scope).

- **Representative pages:** the 16 NITA pages of the SEO sample plus the two UX additions (About NITA and Transparency), and the four My Transit Benefit pages: 18 NITA and 4 My Transit Benefit pages, 22 in all. All 22 get the automated and scripted checks at desktop and mobile widths. The manual review follows the UX approach: test each shared component once, on the page where it is most complete, then spot-check the other pages for content-specific issues (headings, tables, links, images, documents).
- **Proposed targeted addition:** [Meeting Materials](https://nita.illinois.gov/about-nita/boards-and-committees/meeting-materials), because AEO passed on its 146 headings and it is the main page for public participation in board meetings. Needs team confirmation.
- **Automated sweep beyond the sample (proposed):** the 75 NITA pages that are not blog posts, press releases, tag archives, or paginated listings in the 2026-11-19 baseline, plus a stratified sample of about 20 blog posts and press releases across years. Axe only, desktop width, about one page per second. This shows which issues recur across templates without manual review of every page. A full sweep of all 1,613 pages is possible with the same script if the team wants site-wide counts.
- **Shared components:** header and main menu, search, mobile menu, language switcher, homepage carousel, Quick Links dropdown, tabbed sections, accordions, intro banner, data tables, related-posts list, embedded video, footer and footer contact form, trip planner, budget comment form, and, on My Transit Benefit, the header, savings calculator, and Login link.
- **Key journeys** for keyboard and screen reader testing: find a fare; learn about Reduced Fare and Ride Free and open the application; find ADA Paratransit eligibility and how to apply; plan a trip; prepare a public comment on the 2027 budget (up to validation); change the language and use the mobile menu; and, on My Transit Benefit, understand the benefit as an employee, estimate savings as an employer, and reach Login.
- **Documents:** the PDFs and DOCX files that riders use to apply for or understand programs (the rider applications and brochures in English and Spanish, the permit replacement application, the FOIA request form, the transit benefit set-up guide, and the current budget document), about 10 files with manual review. Optionally, `pdfinfo` triage of all 836 internal PDFs linked from NITA pages in the 2026-11-19 link discovery, keeping only the result table, not the files. Documents are not listed separately in the proposal; they are included because they are part of the pages' content and the Title II rule covers conventional electronic documents. Needs team confirmation.

## Work sequence

Method (team decision for SEO Step 3, 2026-11-24, proposed here for the whole section): the review is AI-assisted. The reviewer (Claude) writes and runs the scripts, operates the pages in the browser, and drafts the findings; the team approves the tooling and scope, runs the VoiceOver session, and reviews each part before the next.

### Step 1 — Scope, tooling, and matrix

1. Agree the open decisions below: tool installation, Meeting Materials, the automated sweep, documents, and who runs the VoiceOver session.
2. Install the approved tools in a project tools folder, record versions, and run a smoke test on one page.
3. Update the two site reports to the [authoring guide structure](../authoring-guide.md#2-standard-section-structure).
4. Keep the [review matrix](accessibility-review-matrix.md) current: page scope, components, journeys, proposal-area controls, and the per-criterion table.

**Output:** approved scope and tools, working scripts, updated site reports.

### Step 2 — Automated and scripted checks

Work in parts and review each with the team before the next:

- **(A) Rule-based scan.** Axe on the 22 sample pages at desktop and mobile widths, plus the agreed sweep. Group results by rule, component, and template; separate violations from “needs review” items; confirm each grouped violation on at least one live page.
- **(B) Structure and semantics.** Landmarks, skip link, page language before and after a Weglot language change, titles, heading outlines (reusing AEO and SEO data), lists and tables, link text (reusing the SEO link graph), form labels and `autocomplete`, accessible name versus visible label, and consistency of navigation across pages.
- **(C) Visual adaptation.** Reflow at 320 CSS px, 200% zoom, the WCAG text-spacing override, portrait and landscape, contrast of text over images and of non-text elements (borders, icons, focus indicators), and images of text. Screenshots for every page and condition with a detected problem.
- **(D) Keyboard traversal.** Scripted Tab and Shift+Tab through each sample page: reachable elements compared with interactive elements, focus order, a screenshot and style comparison for every focus stop, traps, and context changes on focus.
- **(E) Documents.** `pdfinfo` and DOCX checks on the key documents (and on the 836 PDFs if agreed); optional veraPDF on the key PDFs.

**Output:** dated evidence folders, grouped results per criterion, matrix statuses, and candidate findings.

### Step 3 — Manual and assistive-technology review

Work in parts:

- **(A) Interactive components.** Operate each shared component with the keyboard and check its role, name, state, and behavior in the accessibility tree: menus and dropdowns (including content shown on hover or focus), mobile menu, tabs, accordions, carousel, language switcher, video modal, search, trip planner, calculator.
- **(B) Forms and errors.** Footer contact form, budget comment form, trip planner, savings calculator, and search: labels and instructions, required fields, error identification and suggestions with empty or invalid values, status messages. No valid submission.
- **(C) Content.** Alternative text quality and decorative images (with SEO's inventory), media captions and alternatives, sensory instructions, link purpose, language of parts, use of color, and the facts relevant to Title II exceptions (archive labeling, documents in active use).
- **(D) Key documents.** Reading order, headings, alternative text, tables, form fields, language, and title of the agreed documents.
- **(E) Screen reader session.** A team member runs the key journeys with VoiceOver on macOS Safari (optionally on an iPhone), following a script Claude prepares, and notes what is announced; Claude records the results and links them to criteria.

**Output:** accessibility findings for both websites with WCAG references, evidence, priority, and complexity; matrix statuses.

### Step 4 — Close controls and report recommendations

Same structure as the other sections:

- **(A)** Give every matrix row and every criterion a final status for both websites.
- **(B)** Validate findings against the authoring guide, merge findings with one root cause in a shared component, and order them by priority. Assign **Critical** only where a barrier blocks an essential task (for example, a rider cannot reach ADA Paratransit or reduced-fare application information with a keyboard or a screen reader), and state the basis.
- **(C)** Classify recommendations as template or component fixes, content fixes, document fixes, or items needing a decision from NITA; note dependencies on third parties (Weglot, YouTube, reCAPTCHA, linked services).
- **(D)** Write the Title II risk summary for each website (which barriers are most likely to matter for the 2027 and 2028 compliance dates, without a legal conclusion), re-check the status of the rule, add inputs to the [roadmap](../06-recommendations-and-roadmap.md), and add the “Findings at a glance” table.

**Output:** completed accessibility matrix, site reports, evidence links, Title II risk summary, and roadmap inputs.

## Completion criteria

The accessibility workstream is ready for consolidation when:

- All seven proposal areas and all 50 WCAG 2.1 Level A and AA criteria have a final status for both websites, with evidence or a documented limitation.
- Every automated result used in a finding was confirmed on a live page, and no criterion is marked verified on the basis of a clean tool result alone.
- Desktop and mobile (emulated) are both covered for the sample, and the screen reader session is recorded or its absence is stated as a limitation.
- Findings cite WCAG 2.1 success criteria, frame ADA Title II as potential risk, and make no compliance claim.
- Findings cross-reference related SEO, AEO, and UX findings instead of repeating them, and the site reports, matrix, and roadmap are consistent with the authoring guide.

## Open decisions for the team

1. ~~Install axe-core and Playwright.~~ **Decided 2026-11-27: installed** in [`tools/accessibility/`](../../../tools/accessibility/README.md).
2. **veraPDF** for PDF/UA machine checks on the key PDFs. Recommended: optional; `pdfinfo` plus manual review is enough for the report.
3. **Meeting Materials** as a targeted addition to the page scope. Recommended: yes.
4. **Automated sweep:** the 75 core pages plus about 20 posts and press releases (recommended), or all 1,613 pages.
5. **Documents:** manual review of about 10 key documents (recommended), plus optional `pdfinfo` triage of the 836 linked PDFs.
6. **Screen reader session:** who runs VoiceOver, and whether an iPhone check is added.

## Current work status — 2026-11-27

- Plan and [review matrix](accessibility-review-matrix.md) drafted 2026-11-27. No checks have been run; every control is **Not assessed** except the observations already handed over by SEO, AEO, and UX, which are listed in the matrix.
- Tooling checked on 2026-11-27: Google Chrome 158, Node.js 24, Java 17, and poppler `pdfinfo` 24.11.0 are installed. After team approval, axe-core 4.14.1 and Playwright 1.65.1 were installed the same day in [`tools/accessibility/`](../../../tools/accessibility/README.md), and a smoke test of [`axe-scan.mjs`](../../../tools/accessibility/axe-scan.mjs) ran on both homepages (desktop) and the NITA homepage (mobile). Smoke-test output was not kept as evidence; Step 2 part A reruns the scan on the full sample. veraPDF is not installed (decision 2 open).
- Early signal, not yet a finding: a `pdfinfo` check on 2026-11-27 of the nine rider and program PDFs already saved in the AEO evidence shows four without tags (the permit replacement application, both Spanish brochures, and the transit benefit set-up guide). To be confirmed in Step 2 part E.
- Step 1 progress: item 2 (tools and smoke test) done. Next: remaining decisions 2–6, then Step 1 item 3 (site reports to the guide structure).
