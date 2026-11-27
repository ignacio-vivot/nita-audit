# Accessibility Review Matrix — NITA websites

Use this matrix to track every review area committed in the [project proposal](../../project-overview.md#21-ada-compliance--digital-accessibility) and every WCAG 2.1 Level A and AA success criterion. It records checks that pass as well as issues. A matrix status is not a finding; findings are created only for evidence-backed issues that merit action. Status definitions follow the [authoring guide](../authoring-guide.md#3-review-controls-and-coverage). Method, tools, and sequence are in the [accessibility work plan](accessibility-audit-plan.md).

This matrix is the single place for coverage detail and caveats; the site reports link here instead of repeating them.

**Status on 2026-11-27:** drafted; no accessibility checks have been run. Observations handed over by the SEO, AEO, and UX reviews are listed in [Incoming observations](#incoming-observations-from-other-sections) and are not yet assessed against WCAG.

## Page-level review scope

All pages below get the automated and scripted checks (Step 2) at desktop (1280×800) and mobile (375×812) widths. The manual review (Step 3) tests each shared component once, on the page noted in [Shared components](#shared-components), and spot-checks the other pages for content-specific issues.

**My Transit Benefit — complete four-URL website (scope confirmed for SEO on 2026-11-19):**

| URL | Accessibility focus |
| --- | --- |
| [Homepage](https://www.mytransitbenefit.com/) | Header, hero, program summary, footer. |
| [Behind the benefits](https://www.mytransitbenefit.com/behind-the-benefits) | Long-form content, images, headings. |
| [Employees](https://www.mytransitbenefit.com/employees) | “Login” heading and link to the account portal (`SEO-MTB-003`). |
| [Employers](https://www.mytransitbenefit.com/employers) | Savings calculator: field labels marked as H3s (AEO), inputs, results, set-up guide PDF. |

**NITA — 18 pages: the SEO sample (16) and the two UX additions:**

| URL | Accessibility focus |
| --- | --- |
| [Homepage](https://nita.illinois.gov/) | Header, main menu, search, language switcher, carousel and its controls, Quick Links dropdown, rotating H1s, footer and contact form. |
| [Riders](https://nita.illinois.gov/riders) | Tabbed section (keyboard and screen reader behavior). |
| [How to ride](https://nita.illinois.gov/riders/how-to-ride) | Trip planner form and its empty error heading, map selectors, tabs. |
| [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) | Fare tables (header cells, reflow). |
| [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs) | Intro banner overflow, accordions, application PDFs, registration-site table. |
| [Access Program](https://nita.illinois.gov/riders/access) | Accordions used for questions. |
| [Accessible transit](https://nita.illinois.gov/riders/accessible-transit) | ADA Paratransit information, video modal and captions, skipped heading levels in the certification accordion. |
| [Communities](https://nita.illinois.gov/communities) | Audience hub; long sentences marked as headings. |
| [Community Planning](https://nita.illinois.gov/communities/community-planning) | Projects table clipped on mobile (`UX-NITA-021`); empty H2 after the table. |
| [Access to Transit](https://nita.illinois.gov/communities/access-to-transit-program) | Project tables without header cells. |
| [2027 NITA Regional Budget](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget) | Public comment form; steps typed as “1.” to “3.”; budget document. |
| [How the system is working](https://nita.illinois.gov/region/how-system-working) | Explanatory content; charts or data visuals if present. |
| [On Track blog](https://nita.illinois.gov/blog) | Listing, pagination, category labels. |
| [NITA expands the Access fare pilot](https://nita.illinois.gov/blog/2026/10/01/nita-expanding-access-pilot-program-to-cta-and-pace-starting-october-1-offering-income-based-reduced-fare-transit-regionwide) | Article template, related posts. |
| [CTA blog tag archive](https://nita.illinois.gov/blog/tags/cta) | Archive template. |
| [NITA's first regional budget proposal (press release)](https://nita.illinois.gov/about-rta/press-releases/northern-illinois-transit-authoritys-first-regional-budget-proposal-expands-service-creates-jobs-and-improves-safety-across-six-counties) | Automated and scripted checks only; for manual review the press release shares the article template (UX decision, 2026-11-26). |
| [About NITA](https://nita.illinois.gov/about-nita) | Institutional page (UX addition); long sentences marked as H3. |
| [Transparency](https://nita.illinois.gov/about-nita/transparency) | FOIA and transparency hub (UX addition); documents. |

**Proposed targeted addition (needs team confirmation):** [Meeting Materials](https://nita.illinois.gov/about-nita/boards-and-committees/meeting-materials), with 146 H2s including link labels marked as headings (AEO Step 3 part C).

**Automated sweep (proposed, axe only, desktop):** the 75 NITA pages in the 2026-11-19 baseline that are not blog posts (792), press releases (420), paginated listings (248), or tag and category archives (78), plus about 20 posts and press releases sampled across years. Source: [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv).

The sample is representative, not a page-by-page review of the 1,613 HTML pages in the crawl baseline.

## Shared components

Each component is tested once in depth, on the page listed, and its result applies wherever it appears (same approach as the [UX plan](../05-ux/ux-audit-plan.md#site-wide-vs-page-specific-findings)).

| Component | Website | Tested on | Main criteria | Status |
| --- | --- | --- | --- | --- |
| Header, main menu with dropdowns, skip link | NITA | Homepage | 2.1.1, 2.4.1, 2.4.3, 2.4.7, 1.4.13, 4.1.2 | Not assessed |
| Search (shown only at wide widths) | NITA | Homepage | 2.4.5, 3.3.2, 4.1.2 | Not assessed |
| Mobile menu | NITA | Homepage at 375 px | 2.1.1, 2.4.3, 4.1.2 | Not assessed |
| Language switcher (Weglot) | NITA | Homepage | 3.1.1, 3.1.2, 4.1.2, 1.4.10 | Not assessed |
| Homepage carousel and indicator dots | NITA | Homepage | 2.1.1, 2.2.2, 4.1.2, 1.4.3 over images | Not assessed |
| Quick Links dropdown | NITA | Homepage | 3.2.2, 4.1.2 | Not assessed |
| Tabbed sections | NITA | Riders | 2.1.1, 4.1.2, 1.3.1 | Not assessed |
| Accordions | NITA | Discounted Fare and Ride Free Programs | 2.1.1, 4.1.2, 1.3.1 | Not assessed |
| Intro banner (text and photo) | NITA | Discounted Fare and Ride Free Programs | 1.4.4, 1.4.12, 1.4.10 | Not assessed |
| Data tables | NITA | Paying for your ride; Community Planning | 1.3.1, 1.4.10 | Not assessed |
| Video modal (YouTube) | NITA | Accessible transit | 1.2.x, 2.1.1, 2.4.3, 4.1.2 | Not assessed |
| Trip planner form | NITA | How to ride | 3.3.1, 3.3.2, 1.3.5, 4.1.2 | Not assessed |
| Budget public comment form | NITA | 2027 NITA Regional Budget | 3.3.1–3.3.3, 1.3.5, 4.1.3 | Not assessed |
| Footer and footer contact form (with reCAPTCHA) | NITA | Homepage | 3.3.1, 3.3.2, 1.3.5, 1.4.3, 4.1.3 | Not assessed |
| Related posts list and pagination | NITA | Blog article; On Track blog | 2.4.4, 1.3.1 | Not assessed |
| Header, navigation, footer | My Transit Benefit | Homepage | 2.1.1, 2.4.1, 2.4.7, 4.1.2 | Not assessed |
| Savings calculator | My Transit Benefit | Employers | 1.3.1, 3.3.2, 4.1.2, 4.1.3 | Not assessed |
| Login link to the account portal | My Transit Benefit | Employees | 2.4.4, 2.4.6 | Not assessed |

## Key journeys

Keyboard (Step 2 part D and Step 3 part A) and screen reader (Step 3 part E) testing follows these journeys end to end on the websites; linked third-party services are noted but not audited.

| # | Website | Journey | Pages | Status |
| --- | --- | --- | --- | --- |
| J1 | NITA | Find the fare for a trip | Homepage → Riders → Paying for your ride | Not assessed |
| J2 | NITA | Learn about Reduced Fare and Ride Free and open the application | Riders → Discounted Fare and Ride Free Programs → application PDF | Not assessed |
| J3 | NITA | Find ADA Paratransit eligibility and how to apply | Homepage → Accessible transit (accordions, video) | Not assessed |
| J4 | NITA | Plan a trip | How to ride → trip planner (up to the handoff to Google Maps) | Not assessed |
| J5 | NITA | Prepare a public comment on the 2027 budget | 2027 NITA Regional Budget → comment form (empty and invalid values only) | Not assessed |
| J6 | NITA | Change the language and navigate on a phone | Homepage at 375 px → language switcher → mobile menu | Not assessed |
| J7 | My Transit Benefit | Understand the benefit and reach Login | Homepage → Employees → Login | Not assessed |
| J8 | My Transit Benefit | Estimate employer savings | Employers → savings calculator → set-up guide PDF | Not assessed |

## Documents

Proposed scope, pending team confirmation. Already saved files are reused in place.

| Document | Website | Why | Saved copy | Status |
| --- | --- | --- | --- | --- |
| Ride Free application | NITA | Application form in active use | [PDF](../../../evidence/aeo/2026-11-25/answer-map/RTA-Ride-Free-Application-240117-v11.pdf) | Not assessed (tagged per 2026-11-27 triage) |
| Reduced Fare application | NITA | Application form in active use | [PDF](../../../evidence/aeo/2026-11-25/answer-map/Reduced-Fare-Application-240301-mk-v12.pdf) | Not assessed (tagged) |
| Permit replacement application | NITA | Application form in active use | [PDF](../../../evidence/aeo/2026-11-26/step3a/rider-pdfs/RTA-FP-0056-Permit-Replacement-Application-Pad-24_v4-1.pdf) | Not assessed (**untagged**) |
| Reduced Fare brochure (English, Spanish) | NITA | Program information | [English](../../../evidence/aeo/2026-11-26/step3a/rider-pdfs/Reduced-Fare-Brochure-240301-mk-v7.pdf), [Spanish](../../../evidence/aeo/2026-11-26/step3a/rider-pdfs/Reduced-Fare-Brochure-Spanish_v1.pdf) | Not assessed (English tagged; **Spanish untagged**) |
| Ride Free brochure (English, Spanish) | NITA | Program information | [English](../../../evidence/aeo/2026-11-26/step3a/rider-pdfs/Ride-Free-Brochure-240201-mk-v17.pdf), [Spanish](../../../evidence/aeo/2026-11-26/step3a/rider-pdfs/Ride-Free-Brochure-Spanish_v1.pdf) | Not assessed (English tagged; **Spanish untagged**) |
| FOIA request form | NITA | Request form in active use | [DOCX](../../../evidence/aeo/2026-11-26/step3c/foia/FOIA-Request-Form-9-30-2015-1.docx) | Not assessed |
| NITA Act summary and timeline | NITA | Public information | [PDF](../../../evidence/aeo/2026-11-26/step3b/nita-act-docs/6a_NITA_Act_Summary_and_Timeline.pdf) | Not assessed (tagged) |
| Current budget document | NITA | Public comment period | To be downloaded in Step 2 part E | Not assessed |
| Transit benefit set-up guide | My Transit Benefit | Employer enrollment | [PDF](../../../evidence/aeo/2026-11-26/step3b/mtb-docs/NITA-TBP-Set-Up-Guide-mk-v2.pdf) | Not assessed (**untagged**) |

The tagged/untagged notes come from a `pdfinfo` 24.11.0 check on 2026-11-27 and are an early signal only; a tagged PDF can still have reading-order, alternative-text, or table problems. Optional triage: the 836 internal PDFs (and 16 DOCX files) linked from NITA pages in the [2026-11-19 link discovery](../../../evidence/crawls/link-discovery/2026-11-19/README.md).

## Review controls and current status

| Proposal area / control | What to verify | Primary method and evidence | NITA status | My Transit Benefit status |
| --- | --- | --- | --- | --- |
| Evaluation against WCAG 2.1 Level AA | Every Level A and AA criterion has a supported result within the sample. | [Per-criterion table](#wcag-21-level-aa-coverage); Steps 2 and 3. | **Not assessed.** | **Not assessed.** |
| Navigation and keyboard accessibility | All functions work with a keyboard; focus order is logical; focus is visible; no traps; skip link and landmarks; menus open and close with the keyboard. | Scripted Tab traversal with focus screenshots (Step 2 part D); component operation (Step 3 part A). | **Not assessed.** UX found buttons without hover feedback (`UX-NITA-013`); focus visibility is checked separately. | **Not assessed.** |
| Screen reader compatibility | Names, roles, states, reading order, headings, and announcements make the key journeys understandable. | Accessibility-tree snapshots (Step 3 part A); VoiceOver session on the key journeys (Step 3 part E). | **Not assessed.** AEO passed on heading and table markup observations. | **Not assessed.** AEO noted calculator labels marked as H3s. |
| Color contrast, typography, and visual accessibility | Text and non-text contrast, text over images, resize to 200%, text spacing, reflow at 320 px, use of color, images of text. | Axe contrast rules; scripted visual-adaptation checks with screenshots (Step 2 part C). | **Not assessed.** SEO measured 11.2 px reCAPTCHA text; UX found the intro banner hides overflowing text (`UX-NITA-018`) and tables overflow on mobile (`UX-NITA-019`, `UX-NITA-021`, `SEO-NITA-022`). | **Not assessed.** |
| Images and alternative text | Meaningful images have equivalent text; decorative images are hidden; functional images in links name the destination. | Axe image rules; SEO [`image-alt-review.csv`](../../../evidence/public-technical/2026-11-20/image-alt-review.csv); manual review (Step 3 part C). | **Not assessed.** SEO recorded file-name alt text and a footer logo labeled “RTA” (`SEO-NITA-017`). | **Not assessed.** Same pattern recorded in `SEO-MTB-005`. |
| Links | Link purpose from text or context; no empty links; links that open new windows or files are identified where needed. | SEO link graph anchors ([README](../../../evidence/crawls/link-discovery/2026-11-24/README.md)); axe link rules; manual review. | **Not assessed.** AEO found link labels marked as H2s on Meeting Materials. | **Not assessed.** |
| Forms | Labels and instructions, required fields, input purpose (`autocomplete`), error identification and suggestions, status messages. | Axe form rules; field inventory; empty and invalid input tests (Step 3 part B). No valid submissions. | **Not assessed.** UX found misaligned footer form fields (`UX-NITA-016`). | **Not assessed.** |
| Interactive elements | Carousel, tabs, accordions, dropdowns, mobile menu, language switcher, video modal, calculator: keyboard operation, name, role, state, and content on hover or focus. | Step 3 part A. | **Not assessed.** UX verified no carousel autoplay and captions on the accessible-features video. | **Not assessed.** |
| Semantic HTML and accessibility attributes | Landmarks, headings, lists, tables, page language, ARIA used correctly, accessible name matches visible label. | Axe; structure scripts reusing AEO and SEO data (Step 2 part B). | **Not assessed.** Incoming: extra H1s, empty and skipped headings, tables without header cells, steps not in lists. | **Not assessed.** Incoming: H3 slogan subtitles, calculator labels as H3s. |
| Desktop and mobile experiences | Same checks at desktop and mobile widths; reflow, orientation, zoom; mobile menu; optional VoiceOver on iPhone. | Chromium device emulation (Step 2 part C); optional physical device. | **Not assessed.** | **Not assessed.** |
| Documents (PDF and DOCX) | Tags, title, language, reading order, headings, alternative text, tables, form fields of documents used to apply for or understand services. | `pdfinfo`, DOCX script, optional veraPDF (Step 2 part E); manual review (Step 3 part D). | **Not assessed.** Early signal: 3 of the 8 NITA PDFs already saved are untagged. | **Not assessed.** Early signal: the set-up guide is untagged. |
| Potential ADA Title II compliance risks | Which barriers affect essential services and are most likely to matter for the 2027 and 2028 compliance dates; facts relevant to the rule's exceptions. No legal conclusion. | Synthesis in Step 4 part D; [Title II context](accessibility-audit-plan.md#ada-title-ii-context-and-how-the-audit-frames-it). | **Not assessed.** | **Not assessed.** |
| Severity classification | Every finding has a priority under the authoring guide; Critical only for barriers to essential tasks, with the basis stated. | Step 4 part B. | **Not assessed.** | **Not assessed.** |
| Testing with users with disabilities; CMS authoring controls | Real-user task success; whether the CMS enforces alternative text or accessible tables. | Outside the [access boundary](accessibility-audit-plan.md#agreed-access-boundary). | **Not verifiable in public scope.** No user research or CMS access. | **Not verifiable in public scope.** Same reason. |

## WCAG 2.1 Level AA coverage

Method classes (explained in the [work plan](accessibility-audit-plan.md#can-the-checks-be-automated-as-in-seo)):
- **Automated:** a rule engine or script detects failures; the reviewer confirms a sample.
- **Scripted + review:** scripts collect the evidence across pages; the reviewer judges it.
- **Manual:** the reviewer operates the page in a browser and judges the result.

**AT** marks criteria where the VoiceOver session (Step 3 part E) confirms the result. No criterion is marked verified on a clean automated result alone.

| SC | Level | Criterion | Method class | Planned method | NITA status | MTB status | Related |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1.1 | A | Non-text Content | Scripted + review | Axe image rules; SEO alt inventory; screenshot review of each image's role (content, decorative, functional). | Not assessed | Not assessed | `SEO-NITA-017`, `SEO-MTB-005` |
| 1.2.1 | A | Audio-only and Video-only (Prerecorded) | Manual | Script inventories audio, video, and embeds; reviewer checks alternatives. | Not assessed | Not assessed | — |
| 1.2.2 | A | Captions (Prerecorded) | Manual | Check caption tracks on each embedded video and whether they are automatic or edited. | Not assessed | Not assessed | UX: accessible-features video has captions |
| 1.2.3 | A | Audio Description or Media Alternative (Prerecorded) | Manual | Check whether visual-only information in videos is described. | Not assessed | Not assessed | — |
| 1.2.4 | AA | Captions (Live) | Manual | Check whether the websites host live streams (for example board meetings) or only link to them. | Not assessed | Not assessed | — |
| 1.2.5 | AA | Audio Description (Prerecorded) | Manual | As 1.2.3. | Not assessed | Not assessed | — |
| 1.3.1 | A | Info and Relationships | Scripted + review; AT | Axe table, list, label, and ARIA rules; heading and table outlines from AEO; review. | Not assessed | Not assessed | AEO Step 3 part C observations |
| 1.3.2 | A | Meaningful Sequence | Scripted + review | Compare DOM order with visual order (CSS order, positioning); review at both widths. | Not assessed | Not assessed | — |
| 1.3.3 | A | Sensory Characteristics | Manual | Text search for shape, color, and position instructions; review. | Not assessed | Not assessed | — |
| 1.3.4 | AA | Orientation | Automated | Portrait and landscape emulation; detect orientation locks. | Not assessed | Not assessed | — |
| 1.3.5 | AA | Identify Input Purpose | Automated | Axe `autocomplete-valid`; inventory of personal-data fields without `autocomplete`. | Not assessed | Not assessed | — |
| 1.4.1 | A | Use of Color | Scripted + review | Axe `link-in-text-block`; review of maps, charts, status labels, required-field markers. | Not assessed | Not assessed | — |
| 1.4.2 | A | Audio Control | Automated | Detect autoplaying media and embed parameters. | Not assessed | Not assessed | — |
| 1.4.3 | AA | Contrast (Minimum) | Automated; Scripted + review over images | Axe `color-contrast` for solid backgrounds; pixel sampling and screenshots for text over images and gradients (carousel, banners). | Not assessed | Not assessed | — |
| 1.4.4 | AA | Resize Text | Scripted + review | 200% zoom; detect clipped or overlapping text; screenshots. | Not assessed | Not assessed | `UX-NITA-018` |
| 1.4.5 | AA | Images of Text | Scripted + review | Image inventory plus visual review for text in images (graphics, flyers, charts). | Not assessed | Not assessed | — |
| 1.4.10 | AA | Reflow | Scripted + review | 320 CSS px width; detect horizontal scrolling and clipped content; apply the data-table exception. | Not assessed | Not assessed | `SEO-NITA-022`, `UX-NITA-017`, `UX-NITA-019`, `UX-NITA-021` |
| 1.4.11 | AA | Non-text Contrast | Scripted + review | Computed colors of input borders, icons, focus indicators, carousel dots; review. | Not assessed | Not assessed | — |
| 1.4.12 | AA | Text Spacing | Scripted + review | Inject the WCAG spacing values; detect clipped or overlapping text. | Not assessed | Not assessed | `UX-NITA-018` |
| 1.4.13 | AA | Content on Hover or Focus | Manual | Menus, dropdowns, tooltips, language switcher: dismissible, hoverable, persistent. | Not assessed | Not assessed | — |
| 2.1.1 | A | Keyboard | Scripted + review | Tab traversal: reachable versus interactive elements; operate widgets with keys. | Not assessed | Not assessed | — |
| 2.1.2 | A | No Keyboard Trap | Scripted + review | Tab and Shift+Tab traversal detects stuck focus; confirm in modals and embeds. | Not assessed | Not assessed | — |
| 2.1.4 | A | Character Key Shortcuts | Manual | Check for single-key shortcuts in page scripts; likely not applicable. | Not assessed | Not assessed | — |
| 2.2.1 | A | Timing Adjustable | Manual | Check forms and sessions for time limits; likely not applicable. | Not assessed | Not assessed | — |
| 2.2.2 | A | Pause, Stop, Hide | Scripted + review | Detect moving or auto-updating content; UX verified no carousel autoplay. | Not assessed | Not assessed | UX homepage row 4 |
| 2.3.1 | A | Three Flashes or Below Threshold | Manual | Visual check of animations and videos. | Not assessed | Not assessed | — |
| 2.4.1 | A | Bypass Blocks | Automated | Axe `bypass` and landmark rules; confirm the skip link works with the keyboard. | Not assessed | Not assessed | — |
| 2.4.2 | A | Page Titled | Automated | Titles from the SEO crawl; review whether each describes the page. | Not assessed | Not assessed | `SEO-NITA-010`, `SEO-NITA-011` |
| 2.4.3 | A | Focus Order | Scripted + review; AT | Focus sequence with screenshots; menus, modals, and mobile menu. | Not assessed | Not assessed | — |
| 2.4.4 | A | Link Purpose (In Context) | Scripted + review | Anchor texts from the SEO link graph; axe `link-name`; review of generic or repeated texts. | Not assessed | Not assessed | — |
| 2.4.5 | AA | Multiple Ways | Manual | Navigation, search (hidden below the wide-screen breakpoint), sitemap, related links. | Not assessed | Not assessed | — |
| 2.4.6 | AA | Headings and Labels | Scripted + review; AT | Heading outlines and form labels; review whether they describe topic or purpose. | Not assessed | Not assessed | `SEO-MTB-003`; AEO Step 3 part C |
| 2.4.7 | AA | Focus Visible | Scripted + review | Screenshot and style comparison at every focus stop. | Not assessed | Not assessed | `UX-NITA-013` (hover only) |
| 2.5.1 | A | Pointer Gestures | Manual | Check carousel, maps, and sliders for path or multipoint gestures without a single-pointer alternative. | Not assessed | Not assessed | — |
| 2.5.2 | A | Pointer Cancellation | Manual | Check custom controls that act on pointer down. | Not assessed | Not assessed | — |
| 2.5.3 | A | Label in Name | Scripted + review | Compare visible label text with the accessible name of buttons, links, and fields. | Not assessed | Not assessed | — |
| 2.5.4 | A | Motion Actuation | Manual | Likely not applicable; confirm no motion-triggered functions. | Not assessed | Not assessed | — |
| 3.1.1 | A | Language of Page | Automated | Axe `html-has-lang` and `html-lang-valid`; check `lang` after a Weglot language change. | Not assessed | Not assessed | `UX-NITA-006`, `SEO-NITA-021` |
| 3.1.2 | A | Language of Parts | Scripted + review | Detect passages and links in other languages (for example Spanish brochure links) without `lang`. | Not assessed | Not assessed | — |
| 3.2.1 | A | On Focus | Scripted + review | Tab traversal detects navigation, pop-ups, or focus moves triggered by focus alone. | Not assessed | Not assessed | — |
| 3.2.2 | A | On Input | Manual | Quick Links dropdown, map selectors, language switcher, form fields: changes of context without warning. | Not assessed | Not assessed | `UX-NITA-012` (automatic translation) |
| 3.2.3 | AA | Consistent Navigation | Automated | Compare header, menu, and footer link order across the sample pages. | Not assessed | Not assessed | — |
| 3.2.4 | AA | Consistent Identification | Scripted + review | Compare names of repeated controls and icons across pages. | Not assessed | Not assessed | — |
| 3.3.1 | A | Error Identification | Manual | Empty and invalid values in each form; no valid submission. | Not assessed | Not assessed | — |
| 3.3.2 | A | Labels or Instructions | Automated | Axe label rules; review required-field and format instructions. | Not assessed | Not assessed | `UX-NITA-016` |
| 3.3.3 | AA | Error Suggestion | Manual | As 3.3.1: whether errors explain how to correct the input. | Not assessed | Not assessed | — |
| 3.3.4 | AA | Error Prevention (Legal, Financial, Data) | Manual | Confirm whether any form creates a legal or financial commitment; likely not applicable. | Not assessed | Not assessed | — |
| 4.1.1 | A | Parsing | — | Not applicable for HTML content per the W3C note in WCAG 2.1; markup problems that affect users are assessed under 1.3.1 and 4.1.2. | Not applicable | Not applicable | — |
| 4.1.2 | A | Name, Role, Value | Scripted + review; AT | Axe ARIA and name rules; accessibility-tree snapshots of each custom widget; VoiceOver confirmation. | Not assessed | Not assessed | — |
| 4.1.3 | AA | Status Messages | Manual; AT | Form errors and confirmations, calculator results, search results: announced without moving focus. | Not assessed | Not assessed | — |

Totals: 9 Automated, 21 Scripted + review, 19 Manual, 1 Not applicable.

## Incoming observations from other sections

Observations recorded elsewhere that this review must assess against WCAG. Each is resolved by citing the existing finding, recording an accessibility finding for the part not covered, or recording a no-issue result.

| Source | Observation | Criteria to assess | Status |
| --- | --- | --- | --- |
| [AEO Step 3 part C](../../../evidence/aeo/2026-11-26/step3c/README.md) | 16 extra H1s on 10 pages; 5 empty headings on 3 pages; 7 skipped levels on 5 pages; 146 H2s on Meeting Materials (84 are link labels); ADA Paratransit content under the taxi heading | 1.3.1, 2.4.6 | Not assessed |
| AEO Step 3 part C | 4 fare tables and 3 Program of Projects tables use ordinary cells for the header row; 6 tables used for layout | 1.3.1 | Not assessed |
| AEO Step 3 part C | Steps as numbered blocks or typed numbers, not lists; FAQ questions as bold paragraphs | 1.3.1 | Not assessed |
| AEO Step 3 part C | My Transit Benefit: H3 slogan subtitles; calculator field labels marked as H3s | 1.3.1, 2.4.6, 3.3.2 | Not assessed |
| [SEO image alt review](../../../evidence/public-technical/2026-11-20/image-alt-review.csv) | File-name alt text, footer logo and social links labeled “RTA”, menu icons with text alternatives next to visible labels | 1.1.1, 2.4.4 | Not assessed |
| [SEO multiple H1s](../../../evidence/public-technical/2026-11-24/rendered-review/nita-multiple-h1.csv) | 18 core pages use an H1 for a secondary block | 1.3.1, 2.4.6 | Not assessed |
| [SEO mobile review](../../../evidence/public-technical/2026-11-24/mobile-review/README.md) | 11.2 px reCAPTCHA text; breadcrumb and category links 21–22 px tall; 16×16 px checkboxes; language switcher covers text while scrolling | 1.4.4, 1.4.10; target size as a WCAG 2.2 observation | Not assessed |
| SEO, UX | Tables wider than the phone screen; projects table clipped with no scroll (`SEO-NITA-022`, `UX-NITA-019`, `UX-NITA-021`); footer overflow at tablet widths (`UX-NITA-017`) | 1.4.10 | Not assessed |
| UX | Intro banner hides overflowing text (`UX-NITA-018`) | 1.4.4, 1.4.12 | Not assessed |
| UX | Buttons have no hover feedback (`UX-NITA-013`) | 2.4.7 (focus), 1.4.11 | Not assessed |
| UX, SEO | Right-to-left layout not mirrored, `dir` empty (`UX-NITA-006`); automatic translation (`UX-NITA-012`); translations only in the browser (`SEO-NITA-021`) | 3.1.1, 3.1.2, 3.2.2 | Not assessed |
| UX | Trip planner opens Google Maps in the same tab without warning (`UX-NITA-008`) | 3.2.2 (submission is an expected change; confirm), 2.4.4 | Not assessed |
| AEO | Rider PDFs to be reissued with the NITA name (`AEO-NITA-002`) | Document accessibility | Not assessed |

## Evidence and review log

| Date | Website | Control(s) reviewed | Method / evidence | Reviewer notes or follow-up |
| --- | --- | --- | --- | --- |
| 2026-11-27 | Both websites | Plan and matrix | [Work plan](accessibility-audit-plan.md); this matrix | Drafted the plan, page and component scope, journeys, document scope, and the per-criterion method classes. Checked local tools: Chrome 158, Node.js 24, Java 17, and `pdfinfo` 24.11.0 installed; axe-core, Playwright, and veraPDF not installed at that point. Confirmed the 2026-04-20 extension of the Title II compliance dates in the Federal Register. |
| 2026-11-27 | Both websites | Tooling (Step 1 item 2) | [`tools/accessibility/`](../../../tools/accessibility/README.md) | Team approved the install. axe-core 4.14.1, @axe-core/playwright 4.14.1, and Playwright 1.65.1 installed, using Chrome 158.0.8127.88. Smoke test of `axe-scan.mjs` on both homepages ran without errors; results are not used as evidence (Step 2 part A reruns them). |
| 2026-11-27 | Both websites | Documents (early signal) | `pdfinfo` 24.11.0 on the nine PDFs saved in the AEO evidence | Four untagged: permit replacement application, Spanish Reduced Fare and Ride Free brochures, transit benefit set-up guide. Not a finding until Step 2 part E. |

## Related reports

- [NITA accessibility report](nita-illinois-gov.md)
- [My Transit Benefit accessibility report](mytransitbenefit-com.md)
- [Accessibility work plan](accessibility-audit-plan.md)
