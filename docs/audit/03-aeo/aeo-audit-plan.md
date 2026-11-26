# AEO Audit Work Plan — NITA websites

## Purpose and governing scope

This work plan operationalizes the Answer Engine Optimization (AEO) scope in [`docs/project-overview.md`](../../project-overview.md#23-answer-engine-optimization-aeo). That proposal is the source of truth for what the client was told would be reviewed. The AEO assessment covers both [nita.illinois.gov](https://nita.illinois.gov/) and [mytransitbenefit.com](https://www.mytransitbenefit.com/) and asks how effectively their content is structured to appear in direct-answer search experiences. It includes:

1. Content structure and information hierarchy.
2. Opportunities for featured snippets and direct answers.
3. Question-based content and FAQ opportunities.
4. Semantic content organization.
5. Structured data opportunities.
6. Content clarity and relevance for answer-oriented search queries.

The proposal calls for automated analysis plus expert manual review of representative pages, templates, and key journeys, with recommendations focused on helping search engines and answer platforms identify and present relevant information from the websites. Like the other sections, the result is a set of evidence-based findings with priority, implementation complexity, and inputs to the action plan.

The AEO work is organized in four **steps** (Step 1–4), mirroring the [SEO work plan](../02-seo/seo-audit-plan.md). They are internal to this workstream and are distinct from the three project phases in the proposal.

## Boundaries with SEO and GEO

AEO asks a narrower question than SEO: for the questions people actually ask, does the website contain a clear, current answer that a search engine or answer feature can find, extract, and show? To avoid duplicate findings:

| Topic | Covered in | AEO use |
| --- | --- | --- |
| Crawlability, indexability, redirects, sitemaps, titles, descriptions, Core Web Vitals | SEO (complete) | Cite the SEO finding when it limits an answer (for example `SEO-NITA-010`, the homepage title “Home”); do not re-report it. |
| Structured data validity and current types | SEO (`SEO-NITA-016`, `SEO-MTB-004`) | AEO covers **opportunities**: answer-oriented markup that is not present today (for example `Event`; Step 2 part D found that `FAQPage` and `HowTo` no longer produce Google rich results and that `GovernmentService` is not a Google feature). |
| AI crawler access, entity identity, authority signals, and how generative platforms describe NITA | GEO | AEO records Google answer features (featured snippets, “People also ask”, AI Overviews) as a symptom; GEO assesses generative platforms and their sources. |
| Readability, visual hierarchy, and task flows | UX and accessibility | AEO notes reading structure only where it affects answer extraction (question headings, lists, tables, answer placement). |

## Agreed access boundary

The audit is limited to publicly accessible pages, resources, public search results, and open testing tools, with no Search Console, analytics, CMS, source code, or server access (project decision, 2026-11-19). Actual queries, impressions, featured-snippet ownership over time, and click data cannot be measured; mark these **Not verifiable in public scope**.

Search answer features vary by location, time, device, signed-in state, and personalization. Public search checks run through a US connection with a Chicago, Illinois IP address and US English settings (`hl=en&gl=us&pws=0`), as in SEO Step 3; record the connection with each capture. Google may return US results that are not localized to Chicago, so the sample does not represent exactly what every user in the region sees. Record each query with date, settings, and the features shown; this is a qualitative sample, not rank tracking. Do not claim that a change will win a featured snippet or an AI Overview mention.

## How to record the audit

Create an AEO review matrix (`aeo-review-matrix.md`) with one row per proposal area for each website, following the [review controls and coverage method](../authoring-guide.md#3-review-controls-and-coverage) and the status definitions in the authoring guide. Findings use the IDs `AEO-NITA-###` and `AEO-MTB-###` and the finding format in the [authoring guide](../authoring-guide.md#4-finding-format), including the “Findings at a glance” table when a file has more than five findings. Update the two AEO site reports to the guide's section structure before the first finding is recorded (they still contain an older template without the Finding ID field).

Store new evidence in dated folders under `evidence/aeo/` (for example `evidence/aeo/2026-11-25/`), each with a README that states method, date, settings, and limits. Reference SEO evidence in place; do not copy it.

## What SEO already collected and how AEO reuses it

| SEO evidence | Location | AEO use |
| --- | --- | --- |
| Agreed page-level sample: 16 NITA and 4 My Transit Benefit URLs | [SEO review matrix](../02-seo/seo-review-matrix.md#page-level-review-scope) | Starting sample for answer and structure review; extended in Step 1 with pages that answer priority questions. |
| Raw HTML of the 20 sample pages (2026-11-24) | [`rendered-review/raw-html/`](../../../evidence/public-technical/2026-11-24/rendered-review/raw-html/) | Heading outlines, lists, tables, accordions, and answer placement, without re-fetching. Raw and rendered HTML match, so answer content does not depend on JavaScript. |
| Readable page text with headings and links (2026-11-24) | [`content-review/page-text/`](../../../evidence/public-technical/2026-11-24/content-review/page-text/) | Primary input for locating answers and measuring answer length and position. |
| Google autocomplete for 22 seed phrases and seven result pages, including “People also ask”, related searches, and two AI Overviews | [`content-review/`](../../../evidence/public-technical/2026-11-24/content-review/README.md) | Seed list for the question inventory; first observations of which pages Google shows as answers (for example the NITA homepage snippet showing hidden form text). |
| Fare check against CTA, Pace, and Metra; time-sensitive and conflicting facts | [`fare-check.txt`, `time-sensitive-content.txt`](../../../evidence/public-technical/2026-11-24/content-review/README.md) | Ground truth for checking whether answers are correct and current (fares match; paratransit call hours conflict, `SEO-NITA-027`). |
| JSON-LD extracted from the 20 sample pages and validator results | [`structured-data/`](../../../evidence/public-technical/2026-11-20/structured-data/) | Baseline of current markup for structured data opportunities. |
| Titles, descriptions, and H1/H2 exports for all 1,613 NITA pages; multiple-H1 list | [B2 crawl exports](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/), [`nita-multiple-h1.csv`](../../../evidence/public-technical/2026-11-24/rendered-review/nita-multiple-h1.csv) | Site-wide scan for question-style headings and FAQ-like sections beyond the sample. |
| Internal link graph of all 1,609 NITA pages with anchor text | [`link-discovery/2026-11-24/`](../../../evidence/crawls/link-discovery/2026-11-24/README.md) | Which pages are linked as the place to answer a topic (anchor text and inlinks to answer pages). The full-page HTML cache used in SEO was temporary; re-fetch with `internal_link_graph.py` and a cache folder if site-wide text is needed. |
| Mobile review at 375 px, including accordions and fare tables | [`mobile-review/`](../../../evidence/public-technical/2026-11-24/mobile-review/README.md) | Whether answers inside accordions and tables are readable on phones (`SEO-NITA-022`). |
| SEO findings on titles, search language, stale content, and translations | [NITA SEO report](../02-seo/nita-illinois-gov.md), [My Transit Benefit SEO report](../02-seo/mytransitbenefit-com.md) | Cross-references; AEO adds the answer perspective only (`SEO-NITA-010`, `011`, `021`, `027`, `028`; `SEO-MTB-003`, `008`). |

## What AEO needs to collect

1. **Question inventory.** About 40 questions for NITA and 15 for My Transit Benefit, grouped by audience: riders (fares, passes, trip planning, reduced fare and Ride Free permits, Access, ADA Paratransit, safety), local governments (Community Planning, Access to Transit, People Over Parking Act), the public (budget, board meetings, public comment, what NITA is), employers, and employees (pre-tax limits, enrollment, the Transportation Benefits Program Act). Sources: the SEO autocomplete and “People also ask” data, new “People also ask” and autocomplete captures for question seeds, questions already answered on the websites, and partner pages (CTA, Metra, Pace, Ventra). Record each question's source; the inventory is qualitative and carries no volume data. The team approves the inventory before Step 2.
2. **Answer map.** For each question: the page and passage that answers it (or “no answer”), the heading above it, the answer length, whether the answer appears in the first screen or inside an accordion or table, whether it is current, and whether two pages give different answers.
3. **Answer-feature capture.** For a subset of about 20 priority questions: the Google result page with featured snippet, “People also ask”, and AI Overview, noting which website supplies the answer and how NITA or My Transit Benefit content is shown. Saved as dated page text, as in SEO Step 3.
4. **Content structure inventory.** For the sample pages: the heading outline, question-style headings, lists, tables, accordions, definitions, and summary or “key facts” blocks; site-wide, the count and location of question-style H2 and H3 headings from the crawl exports.
5. **Structured data opportunity list.** Which answer-oriented schema types fit the visible content (for example `FAQPage`, `GovernmentService`, and `Event` for hearings and board meetings), checked against Google's current documentation, because some rich results are limited or retired. As checked on 2026-11-26, Google stopped showing FAQ rich results on May 7, 2026 (they had been limited to well-known government and health websites since 2023) and retired HowTo rich results in 2023, so questions and step-by-step instructions are assessed as visible content (question headings, numbered lists) rather than as markup.

## Tools and evidence

| Tool or source | Use | Evidence and limits |
| --- | --- | --- |
| SEO page text and raw HTML | Locate answers, headings, lists, tables, and accordions on the sample pages. | Snapshot of 2026-11-24; re-fetch pages that change before reporting. |
| Built-in Chromium browser in the Claude desktop app | Read pages as users see them, open accordions and tabs, and capture Google result pages. | Not signed in; US connection with a Chicago, Illinois IP address; results vary by location and time. |
| Google autocomplete endpoint and result pages (`hl=en&gl=us&pws=0`) | Question discovery and answer-feature capture. | Qualitative; no volume or rank tracking; record date and settings. |
| Partner and official sources (CTA, Metra, Pace, Ventra, ilga.gov) | Ground truth for checking that answers are correct and current. | Checked on the review date only. |
| Google Rich Results Test, Schema.org Validator, Google Search Central documentation | Confirm which structured data types are supported and how. | Valid markup does not guarantee a search feature. |
| Scripts in the evidence folders (Python standard library) | Heading and question extraction across pages, answer length, and consistency checks. | Saved with the evidence so results can be reproduced. |

## Work sequence

Method (team decision, 2026-11-24, same as SEO Step 3): the AEO review is AI-assisted. The reviewer (Claude) collects and analyzes the evidence with the browser and scripts; the team approves the question inventory and the extended sample, and reviews each part before the next.

### Step 1 — Scope, question inventory, and sample

1. Create the AEO review matrix and update the two site reports to the authoring guide structure.
2. Build the question inventory (see “What AEO needs to collect”, item 1) from the existing SEO data plus new autocomplete and “People also ask” captures.
3. Map each question to the page that should answer it, using the internal link graph and the site search, and extend the 20-page sample with answer pages that are not in it (for example the ADA Paratransit section, Ride Free and Reduced Fare application steps, Contact, About NITA, Ride Safe, board meetings, and public meetings). Agree the extended sample with the team.
4. Record the scope, sources, and limits in the matrix.

**Output:** AEO matrix, approved question inventory, extended page sample.

### Step 2 — Collect answer and structure evidence

Work in parts and review each with the team before the next: (A) answer map for the question inventory, items 2 and 6; (B) content structure and semantic organization, items 1 and 4; (C) answer-feature capture for priority questions, item 2; (D) structured data opportunities, item 5.

1. Build the answer map: answer present or missing, location, length, heading, currency, and conflicts between pages.
2. Capture featured snippets, “People also ask”, and AI Overviews for about 20 priority questions; note which source answers and whether the NITA or My Transit Benefit answer is current.
3. Extract heading outlines and content patterns from the sample and question-style headings site-wide.
4. List structured data opportunities that match visible content, checked against current Google documentation.

**Output:** dated evidence folders, answer map, answer-feature sample, structure inventory, and structured data opportunity list.

### Step 3 — Assess answer quality and opportunities

Work in parts: (A) direct-answer and featured-snippet opportunities, items 2 and 6; (B) question-based content and FAQ opportunities, item 3; (C) structure, hierarchy, and semantic organization, items 1 and 4; (D) structured data opportunities, item 5.

1. Judge each priority answer for directness (does the passage answer the question in its first sentence or two?), completeness, currency, and consistency with partner sources.
2. Identify questions with no answer or a scattered answer, and recommend where the answer belongs (an existing page section, a short FAQ block on the program page, or a new page) without proposing new pages where a section would do.
3. Assess whether heading hierarchy, lists, tables, and accordions help or hinder answer extraction on the templates reviewed.
4. Recommend answer-oriented structured data only where it matches visible content and Google supports it.

**Output:** AEO findings for both websites with evidence, priority, and complexity; matrix statuses.

### Step 4 — Close controls and report recommendations

Same as SEO Step 4: (A) give every matrix row a final status; (B) validate the findings against the authoring guide and order them by priority; (C) classify recommendations as technical, editorial, or requiring client confirmation, noting that new FAQ content and answer wording need NITA's approval; (D) add AEO inputs to the [roadmap](../06-recommendations-and-roadmap.md), grouped with related SEO actions where the same page change serves both, and add the “Findings at a glance” table.

**Output:** completed AEO matrix, site reports, evidence links, and roadmap inputs.

## Completion criteria

The AEO workstream is ready for consolidation when:

- All six proposal areas are represented in the matrix for both websites, each with a final status and evidence or a documented limitation.
- The question inventory, its sources, and the answer map are saved with dates, and every priority question has a recorded answer location or “no answer”.
- Answer-feature observations state the date, settings, and location, and no finding promises a featured snippet, AI Overview mention, or ranking.
- Findings cross-reference related SEO and GEO findings instead of repeating them.
- Site reports, the matrix, and the roadmap are consistent with each other and with the authoring guide.

## Open decisions for the team

- Approve the question inventory and the extended page sample (Step 1).

## Current work status — 2026-11-25

- Step 1 completed 2026-11-25 and approved by the team: [AEO review matrix](aeo-review-matrix.md) created; both site reports updated to the authoring guide structure; question inventory of 57 questions (42 NITA, 15 My Transit Benefit; 20 marked for the answer-feature sample) built from autocomplete, “People also ask” on 17 result pages, question-style headings on the websites, and the SEO search sample; proposed sample of 32 pages and 2 documents ([Step 1 evidence](../../../evidence/aeo/2026-11-25/README.md)).
- Step 2 part A completed 2026-11-25: answer map for all 57 questions ([evidence](../../../evidence/aeo/2026-11-25/README.md#step-2-part-a--answer-map); summary in the [matrix](aeo-review-matrix.md#answer-map)). NITA: 24 direct, 6 partial, 3 scattered, 4 conflicting, 2 outdated, 1 link-only, 2 missing (after the corrections of `Q-NITA-04` and `Q-NITA-30`). My Transit Benefit: 4 direct, 5 partial, 1 outdated, 1 link-only, 4 missing. Reviewed by the team.
- Step 2 part B completed 2026-11-25: structure inventory, heading outlines, text not visible on load, and program-name counts for the 31 HTML pages of the sample ([evidence](../../../evidence/aeo/2026-11-25/README.md#step-2-part-b--content-structure-and-semantic-organization); summary in the [matrix](aeo-review-matrix.md#content-structure-inventory)). Reviewed by the team.
- Step 2 part C completed 2026-11-26: Google answer features for the 20 priority questions, captured through a US connection with a Chicago, Illinois IP address ([evidence](../../../evidence/aeo/2026-11-26/answer-features/README.md); summary in the [matrix](aeo-review-matrix.md#answer-feature-sample)). AI Overviews on all 20, no featured snippets. One answer-map row (`Q-NITA-29`) was corrected. Reviewed by the team.
- Step 2 part D completed 2026-11-26: structured data opportunity list for ten types, checked against Google's documentation on the same day ([evidence](../../../evidence/aeo/2026-11-26/structured-data/README.md)). FAQ and HowTo rich results are no longer shown, and Google states that AI features need no special markup; `Event` is the only new type with a Google feature and requires one page per event. Reviewed by the team.
- Step 2 is complete.
- Step 3 part A completed 2026-11-26: the 20 priority answers were assessed for directness, completeness, currency, and consistency ([evidence](../../../evidence/aeo/2026-11-26/step3a/README.md)), and five findings were recorded: `AEO-NITA-001` to `003` in the [NITA report](nita-illinois-gov.md) and `AEO-MTB-001` and `002` in the [My Transit Benefit report](mytransitbenefit-com.md). The answer-map row for `Q-NITA-04` was corrected. Reviewed by the team.
- Step 3 part B completed 2026-11-26: the 19 inventory questions with missing, scattered, partial, or link-only answers were traced on the websites and in linked documents, nine more questions were captured in Google through a US connection with a Chicago, Illinois IP address, and tax rates, the NITA Act dates, and the federal paratransit rule were checked against official sources ([evidence](../../../evidence/aeo/2026-11-26/step3b/README.md)). Four findings were recorded: `AEO-NITA-004` to `006` in the [NITA report](nita-illinois-gov.md) and `AEO-MTB-003` in the [My Transit Benefit report](mytransitbenefit-com.md). The answer-map row for `Q-NITA-30` was corrected (missing to conflicting). Reviewed by the team.
- Step 3 part C completed 2026-11-26 ([evidence](../../../evidence/aeo/2026-11-26/step3c/README.md)). Work done:
  - the 31 sample pages were fetched again (structure unchanged);
  - headings, accordions, tables, numbered steps, and question markup were assessed against Google's guidance on heading order;
  - agency, permit, program, and portal names were reviewed;
  - three FOIA searches were captured through a US connection with a Chicago, Illinois IP address.

  Two findings were recorded in the [NITA report](nita-illinois-gov.md): `AEO-NITA-007` and `008`. The evidence and recommendation of `AEO-NITA-001` were extended. Markup patterns that mainly affect screen-reader users were passed to the accessibility review. There is no new My Transit Benefit finding. Reviewed by the team.
- Step 3 part D completed 2026-11-26 ([evidence](../../../evidence/aeo/2026-11-26/step3d/README.md)). Work done:
  - the current markup and Google's structured data documentation were rechecked;
  - two board meeting searches and one CTA comparison were captured through a US connection with a Chicago, Illinois IP address;
  - each schema type received a decision for both websites.

  One finding was recorded in the [NITA report](nita-illinois-gov.md): `AEO-NITA-009`, Google's AI Overview places the next board meeting in Oak Park because of an image label. No stand-alone structured data is recommended; `Event` markup is optional with single-meeting pages. There is no new My Transit Benefit finding. Reviewed by the team.
- Step 3 is complete.
- Step 4 part A completed 2026-11-26: every control in the [matrix](aeo-review-matrix.md#review-controls-and-current-status) has a final status for both websites. Two rows were added: “Answer performance in search” (not verifiable in public scope) and a synthesis row that lists the findings by priority and the themes that link them. Reviewed by the team.
- Step 4 part B completed 2026-11-26: the 12 findings were checked against the authoring guide's format, evidence, wording, and priority definitions. Recommendation wording, date format, list formatting, and four cross-references to SEO and UX findings were corrected. Priorities and order are unchanged ([review log](aeo-review-matrix.md#evidence-and-review-log)). Reviewed by the team.
- Step 4 part C completed 2026-11-26: both site reports have a “Recommendation types and confirmations” table. Each of the 12 recommendations is classified as editorial (9) or technical and editorial (3), with the owner who should confirm facts or wording before publication. Awaiting team review.
- Next: Step 4 part D (add AEO inputs to the [roadmap](../06-recommendations-and-roadmap.md), grouped with related SEO actions, and add timing to the “Findings at a glance” table).
