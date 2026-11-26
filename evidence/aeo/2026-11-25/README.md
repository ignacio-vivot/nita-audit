# AEO Steps 1 and 2 — question inventory, sample, answer map, and content structure (2026-11-25)

Evidence for Step 1 and Step 2 parts A and B of the [AEO work plan](../../../docs/audit/03-aeo/aeo-audit-plan.md): the question inventory, the sources behind it, and the proposed page sample. All search captures ran through a US connection with a Chicago, Illinois IP address (`connection.txt`) and US English settings; Google returned US results that were not localized to Chicago. Qualitative only: no search volume, no rank tracking.

## Step 1 — method

1. **Autocomplete.** [`autocomplete_questions.py`](autocomplete_questions.py) requested Google autocomplete suggestions (`hl=en&gl=us`) for 48 question-style seed phrases grouped by audience ([`question-seeds.tsv`](question-seeds.tsv)); results in `autocomplete-questions-2026-11-25.csv` (250 suggestions). The SEO capture of 2026-11-24 ([`autocomplete-2026-11-24.txt`](../../public-technical/2026-11-24/content-review/autocomplete-2026-11-24.txt)) was also used.
2. **“People also ask”.** Seventeen Google result pages (`hl=en&gl=us&pws=0`) were opened in the Claude desktop app's built-in browser (Chromium, not signed in) on 2026-11-25 (see `connection.txt` for the start time); a browser script recorded whether an AI Overview was shown, the “People also ask” questions, and the site and title of the first results (`google-paa-2026-11-25.jsonl`; 60 questions). The seven result pages captured for SEO on 2026-11-24 ([`search-sample-2026-11-24.md`](../../public-technical/2026-11-24/content-review/search-sample-2026-11-24.md)) were also used.
3. **Questions already on the websites.** [`question_headings.py`](question_headings.py) fetched the 60 NITA core pages and the 4 My Transit Benefit pages listed in `core-urls.txt` (raw HTML kept in `html/`) and recorded every H1–H4 heading and accordion label (`<summary>`), flagging question-style text (`page-headings.csv`; 652 elements, 52 question-style: 48 on NITA, 4 on My Transit Benefit). Question-style H2s on all 1,613 NITA HTML pages were taken from the 2026-11-19 crawl's `h2_all.csv` exports (`crawl-question-h2.csv`; 71, mostly blog posts; the free crawler exports only the first two H2s per page).
4. **Inventory.** The questions were consolidated into [`question-inventory.csv`](question-inventory.csv): 42 for NITA and 15 for My Transit Benefit, grouped by audience and topic, each with its sources and the page expected to answer it. Twenty are marked for the answer-feature sample in Step 2 part C (14 NITA, 6 My Transit Benefit).
5. **Sample.** [`proposed-sample.csv`](proposed-sample.csv) lists the 20 SEO sample pages plus 12 NITA pages and 2 application PDFs that are expected to answer inventory questions but were not in the SEO sample.

## Step 1 — observations for later steps

These are notes for Step 2, not findings:

- **Google features are common.** An AI Overview appeared on 16 of the 17 result pages; “People also ask” appeared on 15.
- **Riders search with the RTA name.** Suggestions include “how to apply for rta reduced fare permit”, “how do i renew my rta reduced fare permit”, and “rta transit benefit card”. This matches `SEO-NITA-028`.
- **Some questions lack local suggestions.** Several riders' questions return no autocomplete suggestions specific to the Chicago region (“can veterans ride cta free”, “how to get senior bus pass chicago”). The questions themselves still appear in “People also ask” (“How do I get a senior CTA pass in Chicago?”).
- **Retired domains still appear in results.** Google still lists `ridertools.metrarail.com` for “metra fares”, although that domain no longer responds (`SEO-NITA-018`).
- **The NITA core pages already contain some question-style sections.** Examples are “Who is eligible?” and “How do I get Access?” on Access, “How to renew Ride Free Permits”, and “What is NITA Ride Safe?”. They also include accordion FAQs on Access and the Privacy Policy.

## Step 2 part A — answer map

Folder [`answer-map/`](answer-map/). For each of the 57 inventory questions, the answer map records whether and where the websites answer it.

### Method

1. **Page text with structure markers.** [`structured_text.py`](answer-map/structured_text.py) converted the raw HTML of the 23 answer pages listed in `answer-pages.txt` (19 NITA, 4 My Transit Benefit; HTML from Step 1 in `html/`) to text in `answer-map/page-text/`. Menus, footers, scripts, and forms are skipped. Accordion content is wrapped as `[ACCORDION: label]`, tables as `[TABLE]`, and content hidden until a click (tab panels, `hidden` classes) as `[HIDDEN-PANEL]`. Each heading carries `{w=N}`, the number of content words between the H1 and that heading, so the position of an answer can be read.

   `python3 -I structured_text.py ../html page-text $(sed 's/$/.html/' answer-pages.txt)`

2. **Application PDFs.** The Reduced Fare and Ride Free application PDFs (`/uploads/files/general/Riders/…`, shown by Google for permit searches) were saved and converted with `pdftotext -layout` (`*.pdf`, `*.txt`).
3. **Reading and recording.** Each question was looked up in the page text and PDFs. The result is recorded in [`build_answer_map.py`](answer-map/build_answer_map.py), which joins it with the inventory and writes [`answer-map.csv`](answer-map/answer-map.csv): status, page, location (open text, section, table, accordion, tab panel, external tool), heading above the answer, words from the H1, a short quoted excerpt, and notes on currency and consistency.

   `python3 -I build_answer_map.py`

4. **Partner check.** Fares and program facts were compared with the SEO fare check of 2026-11-24 and, for the Regional Day Pass, with [metra.com/rdp](https://metra.com/rdp), read in the built-in browser on 2026-11-25 through the US connection with a Chicago, Illinois IP address.

Status values: **direct** (answered in one or two sentences on the expected page), **partial** (incomplete or indirect), **scattered** (parts on different sections or pages), **conflicting** (the website gives different answers, or differs from the operator's source), **outdated** (past dates presented as current), **link-only** (answer only in a linked tool or PDF), **missing** (no answer found).

### Results

| Website | Questions | Direct | Partial | Scattered | Conflicting | Outdated | Link-only | Missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nita.illinois.gov | 42 | 24 | 6 | 3 | 3 | 2 | 1 | 3 |
| mytransitbenefit.com | 15 | 4 | 5 | 0 | 0 | 1 | 1 | 4 |
| **Total** | **57** | **28** | **11** | **3** | **3** | **3** | **2** | **7** |

Of the 20 priority questions, 13 have a direct answer. The other seven are `Q-NITA-13` (seniors, scattered), `Q-NITA-21` (ADA Paratransit call hours, conflicting), `Q-NITA-24` (trip planning, partial), `Q-NITA-31` (2027 budget comments, outdated), `Q-MTB-06` (employee enrollment, missing), `Q-MTB-11` (employer requirement, outdated), and `Q-MTB-12` (covered employers, partial).

### Observations for later steps

These are notes for Steps 2B to 3, not findings:

- **Answers often sit in closed accordions or tab panels.** Of the 45 answers found on a page (direct, partial, conflicting, or outdated), 16 are wholly or partly inside accordions or tab panels. Some are far down the page: the ADA Paratransit application steps are about 1,100 words below the H1 in an accordion with no “How to apply” heading.
- **Strong answer pages exist.** Ride Safe and People Over Parking Act answer questions in plain-text FAQs, and Access has an accordion FAQ and question-style headings (“Who is eligible?”, “How do I get Access?”).
- **Several answers conflict or are out of date.** Examples are the board meeting day (Board of Directors says the third Thursday; the listed meetings fall on second Thursdays), the 2027 budget page that still invites readers to the November 12 hearing, and the closed Riders Advisory Council application period. Several overlap SEO findings (`SEO-NITA-027`, `SEO-MTB-008`).
- **Some questions have no answer.** NITA does not explain the NITA tax or revenue sources created by the NITA Act, whether ADA Paratransit can be used for any trip purpose, or how to apply to Access to Transit. My Transit Benefit does not explain employee enrollment, whether funds expire, the prepaid card, or fees, and three product headings on Behind the Benefits have no text.
- **Numbers differ within My Transit Benefit.** The homepage says “Up to 7.65% in savings” and the Employers calculator uses 8.45%. The homepage and Employers say “up to $340 each month” for transit and parking, while Behind the Benefits says $340 for each.
- **The application PDFs still carry the RTA name.** Both PDFs say “Questions? Call 312-913-3110 or visit rtachicago.org” and “Apply online now at fares.rtachicago.org”. The Reduced Fare application is mailed to “Regional Transportation Authority, PO Box 301150, Chicago, IL 60630” and refers to the “RTA Reduced Fare Permit Program”.

## Step 2 part B — content structure and semantic organization

Folder [`structure/`](structure/). It records how the sample pages are built (headings, accordions, tabs, lists, tables) and which names they use for the same programs.

### Method

1. **Pages.** The 31 HTML pages of the approved sample (27 NITA, 4 My Transit Benefit; `structure-pages.tsv`). The Registration Sites URL is left out because it redirects to an ArcGIS map. HTML comes from `html/` (fetched 2026-11-25) or, for the blog, blog post, CTA tag, and press release pages, from the SEO snapshot of 2026-11-24 ([`rendered-review/raw-html/`](../../public-technical/2026-11-24/rendered-review/raw-html/)), used in place.
2. **Structure inventory.** [`structure_inventory.py`](structure/structure_inventory.py) counts headings by level, empty headings, skipped levels, repeated heading text, question-style headings and accordion labels, accordions, panels hidden until a click, lists, tables, and definition lists. It also records the words between the H1 and the next heading (the opening passage). Output: [`structure-inventory.csv`](structure/structure-inventory.csv) and [`heading-outlines.md`](structure/heading-outlines.md), the outline of every page with word positions and marks for accordions and hidden panels.

   `python3 -I structure_inventory.py structure-pages.tsv`

3. **Text not visible on load.** The 31 pages were opened in the built-in browser at 1280 × 900 px on 2026-11-25. A script counted the words after the H1, outside menus, footers, and forms, and how many of them were not visible when the page loaded (closed accordions, inactive tabs, lightboxes), using the browser's `checkVisibility()` ([`browser-hidden-content.csv`](structure/browser-hidden-content.csv)). This measure is more reliable than the HTML markers in step 2, which flag the visible first tab and miss the board biographies (they open in a lightbox).
4. **Names and terms.** [`term_usage.py`](structure/term_usage.py) counts 32 names and terms in [`terms.tsv`](structure/terms.tsv) (agency names, permit and program names, the fare portal, ADA Paratransit, the Travel Information number, the transit benefit program and law) in the content of the 31 pages, from the H1 down, and in the two application PDFs ([`term-usage.csv`](structure/term-usage.csv)).

   `python3 -I term_usage.py structure-pages.tsv terms.tsv`

5. **Site-wide question headings.** Taken from Step 1 (`crawl-question-h2.csv`): 71 question-style H2s on the 1,613 crawled NITA pages, 51 on blog posts, 4 on press releases, and 16 on 12 other pages. The crawl exports only the first two H2s per page and no H3s, so this is a lower bound.

### Results

| Measure | NITA (27 pages) | My Transit Benefit (4 pages) |
| --- | --- | --- |
| Pages with question-style headings or accordion labels | 13 (24 headings, 3 accordion labels) | 4 (one each: “How the Program Works”, “How you save”) |
| Accordions (`<details>`) | 21 on 4 pages | None |
| Pages where 25% or more of the text is not visible on load | 9 | None |
| Tables | 17 (4 with header cells, none with a caption) | None |
| Numbered lists (`<ol>`) | None (steps are styled blocks or typed numbers) | None |
| Pages with more than one H1 | 10 | 1 |
| Pages with skipped heading levels | 5 | 3 |
| Pages with empty headings | 3 (5 headings) | None |

Text not visible on load, by page (25% or more): Paying for your ride 87%, Board of Directors 72% (biographies), FOIA 71%, Discounted Fare and Ride Free Programs 61%, Contact 57%, How to ride 53%, Accessible transit 49%, Access 45%, Funding 26%. The text is present in the HTML on all of them.

### Observations for later steps

These are notes for Step 3, not findings:

- **Rider answers sit behind clicks.** On the five main rider pages, 45% to 87% of the text is hidden on load. Fares are only in tables inside closed accordions; Ride Free steps are in tabs; the FOIA request steps and copying fees are in panels opened by buttons; on Contact, five of seven sections are panels.
- **Headings do not always describe the content.** Paying for your ride has an H2 “Metra Passes” inside an accordion under an H3. Accessible transit repeats the H2s “ADA Paratransit” and “Rideshare Access Program (RAP) and Taxi Access Program (TAP)”, and its Paratransit Certification accordion has H4s under an H2. Meeting Materials uses 146 H2s, including “Agenda” 29 times, “Minutes” 20, “Slides” 19, and “Watch” 16, so the meeting dates and types are at the same level as their links.
- **Good patterns exist.** Ride Safe has a 16-word opening passage, question-style H2s, with “What is NITA Ride Safe?” answered in its first sentence, numbered steps, and a plain-text FAQ. Access uses question headings and an accordion FAQ. These are models for the other program pages.
- **FAQs are not marked as questions.** Ride Safe and People Over Parking Act write questions as plain paragraphs, not headings or accordion labels.
- **Answers are split by topic.** Seniors' options are split between the Ride Free and Reduced Fare sections; the Travel Information number is only on Contact; the NITA Act and funding appear on About NITA, Funding, and blog posts.
- **Program names vary.** The Access Program is called “Access Program”, “Access Pilot Program”, “Access Permit”, and, on Paying for your ride only, “Access card” (4 times). The reduced fare credential is “Reduced Fare Permit” 24 times and “Reduced Fare cards” twice (in the opening text and the accordion label “Replace Lost, Stolen or Damaged Reduced Fare Cards”). FOIA uses “Northern Illinois Transportation Authority” twice. The fare portal is “NITA Fare Programs Portal”, “Fare Portal”, and “online portal”, while both application PDFs send readers to `fares.rtachicago.org`.
- **The RTA name remains in current text.** Most of the 46 “RTA” mentions on 12 NITA pages are historical (“NITA's predecessor, the RTA”) or titles of older blog posts shown as related articles on program pages (for example “RTA begins exploring reduced fares for riders with low incomes” on Access). Two are written as current: “the RTA region” (How to ride) and “Use the RTA's trip planner” (Accessible transit).
- **My Transit Benefit uses five names for the program:** “NITA Transit Benefit Fare Program” (11), “Transit Benefit Program” (5), “Transit Fare Benefit” (3, for the account), “RTA/NITA Transit Benefit” (1, the card), and “My Transit Benefit” (the domain; used once, on NITA's Riders page). The law is called the “Transit Benefits Program Act”; the official name, Transportation Benefits Program Act, does not appear (`SEO-MTB-008`). Every page goes from the H1 straight to another heading with no opening passage.

Step 2 part C (answer-feature capture, 2026-11-26) is in [`../2026-11-26/answer-features/`](../2026-11-26/answer-features/README.md). It corrected the answer-map row for `Q-NITA-29` (About NITA names the NITA Act in its Leadership section). Step 3 part A (2026-11-26) corrected `Q-NITA-04`: the Regional Passes table does list zones 1-3 and 1-4, at the prices Metra gives, so the answer is direct, not conflicting; the counts above include this correction.

## Files

`connection.txt`, `question-seeds.tsv`, `autocomplete_questions.py`, `autocomplete-questions-2026-11-25.csv`, `google-paa-2026-11-25.jsonl`, `core-urls.txt`, `question_headings.py`, `page-headings.csv`, `html/`, `crawl-question-h2.csv`, `question-inventory.csv`, `proposed-sample.csv`; `answer-map/` (`structured_text.py`, `answer-pages.txt`, `page-text/`, the two application PDFs and their text, `build_answer_map.py`, `answer-map.csv`); `structure/` (`structure-pages.tsv`, `structure_inventory.py`, `structure-inventory.csv`, `heading-outlines.md`, `browser-hidden-content.csv`, `terms.tsv`, `term_usage.py`, `term-usage.csv`).
