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
| Structured data validity and current types | SEO (`SEO-NITA-016`, `SEO-MTB-004`) | AEO covers **opportunities**: answer-oriented markup that is not present today (for example `FAQPage`, `GovernmentService`, `Event`). |
| AI crawler access, entity identity, authority signals, and how generative platforms describe NITA | GEO | AEO records Google answer features (featured snippets, “People also ask”, AI Overviews) as a symptom; GEO assesses generative platforms and their sources. |
| Readability, visual hierarchy, and task flows | UX and accessibility | AEO notes reading structure only where it affects answer extraction (question headings, lists, tables, answer placement). |

## Agreed access boundary

The audit is limited to publicly accessible pages, resources, public search results, and open testing tools, with no Search Console, analytics, CMS, source code, or server access (project decision, 2026-11-19). Actual queries, impressions, featured-snippet ownership over time, and click data cannot be measured; mark these **Not verifiable in public scope**.

Search answer features vary by location, time, device, signed-in state, and personalization. Public search checks run from Argentina with US English settings (`hl=en&gl=us&pws=0`), as in SEO Step 3, and do not represent what users in the Chicago region see. Record each query with date, settings, and the features shown; this is a qualitative sample, not rank tracking. Do not claim that a change will win a featured snippet or an AI Overview mention.

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
5. **Structured data opportunity list.** Which answer-oriented schema types fit the visible content (for example `FAQPage`, `GovernmentService`, and `Event` for hearings and board meetings), checked against Google's current documentation, because some rich results are limited or retired: Google shows FAQ rich results only for well-known government and health websites, which may include nita.illinois.gov, and retired HowTo rich results in 2023, so step-by-step instructions are assessed as plain lists.

## Tools and evidence

| Tool or source | Use | Evidence and limits |
| --- | --- | --- |
| SEO page text and raw HTML | Locate answers, headings, lists, tables, and accordions on the sample pages. | Snapshot of 2026-11-24; re-fetch pages that change before reporting. |
| Built-in Chromium browser in the Claude desktop app | Read pages as users see them, open accordions and tabs, and capture Google result pages. | Not signed in; located in Argentina; results vary by location and time. |
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
- Decide whether a sample of answer-feature checks should also be run from a US connection, as planned for the pending external links, to compare with the Argentina results.

## Current work status — 2026-11-24

- Plan drafted. Step 1 not started. SEO evidence listed above is available for reuse.
