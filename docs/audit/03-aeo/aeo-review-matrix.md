# AEO Review Matrix — NITA websites

Use this matrix to track every review area committed in the [project proposal](../../project-overview.md#23-answer-engine-optimization-aeo). It records checks that pass as well as issues. A matrix status is not a finding; findings are created only for evidence-backed issues or opportunities that merit action. Status definitions follow the [authoring guide](../authoring-guide.md#3-review-controls-and-coverage). Method and sequence are in the [AEO work plan](aeo-audit-plan.md).

This matrix is the single place for coverage detail and caveats; the site reports link here instead of repeating them.

## Question inventory

The AEO review starts from the questions people ask, not from page templates. The inventory built in Step 1 has 57 questions: 42 for nita.illinois.gov (riders, the public, and local governments) and 15 for mytransitbenefit.com (employees and employers), each with its sources and the page expected to answer it ([`question-inventory.csv`](../../../evidence/aeo/2026-11-25/question-inventory.csv); method in the [Step 1 README](../../../evidence/aeo/2026-11-25/README.md)). Sources are Google autocomplete for 48 question-style seeds, “People also ask” on 17 Google result pages, question-style headings already on the websites, and the SEO search sample. All search captures ran through a US connection with a Chicago, Illinois IP address; they are qualitative and carry no search volume.

| Audience | Topics | Questions |
| --- | --- | --- |
| Riders (NITA) | Fares and payment, Reduced Fare and Ride Free permits, seniors, Access Program, ADA Paratransit, accessibility, trip planning, safety | 27 |
| Public (NITA) | What NITA is, the NITA Act and tax, the 2027 budget, board meetings, contact, Riders Advisory Council, FOIA, funding | 10 |
| Local governments (NITA) | People Over Parking Act, Access to Transit, Community Planning, Section 5310 | 5 |
| Employees (My Transit Benefit) | How the benefit works, 2026 limits, parking, savings, enrollment, account, coverage, expiry, card | 10 |
| Employers (My Transit Benefit) | Transportation Benefits Program Act, covered employers, sign-up, savings, cost | 5 |

Twenty priority questions (14 NITA, 6 My Transit Benefit) are marked for the answer-feature capture in Step 2 part C.

## Answer map

Step 2 part A recorded, for every inventory question, whether the websites answer it, where, under which heading, how far below the H1, and whether the answer is current and consistent ([`answer-map.csv`](../../../evidence/aeo/2026-11-25/answer-map/answer-map.csv); method and status definitions in the [evidence README](../../../evidence/aeo/2026-11-25/README.md#step-2-part-a--answer-map)). The map reads the page text of 23 answer pages and the two application PDFs.

| Website | Questions | Direct | Partial | Scattered | Conflicting | Outdated | Link-only | Missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nita.illinois.gov | 42 | 23 | 6 | 3 | 4 | 2 | 1 | 3 |
| mytransitbenefit.com | 15 | 4 | 5 | 0 | 0 | 1 | 1 | 4 |

Thirteen of the 20 priority questions have a direct answer (10 of 14 on NITA, 3 of 6 on My Transit Benefit). The answer map is evidence for Step 3; it does not create findings by itself.

## Page-level review scope

**Status: approved by the team on 2026-11-25.** The AEO sample is the 20-page SEO sample ([SEO matrix](../02-seo/seo-review-matrix.md#page-level-review-scope)) plus the pages expected to answer inventory questions that the SEO sample did not include ([`proposed-sample.csv`](../../../evidence/aeo/2026-11-25/proposed-sample.csv)):

| Proposed addition | Questions it should answer |
| --- | --- |
| [Registration Sites](https://nita.illinois.gov/riders/free-and-reduced-fare-programs/registration-sites) (redirects to an ArcGIS map) | Where to apply in person (`Q-NITA-14`) |
| [Ride Safe App](https://nita.illinois.gov/safety/app) | How to report a safety problem (`Q-NITA-26`) |
| [Getting to the Obama Presidential Center](https://nita.illinois.gov/riders/how-to-ride/getting-to-the-obama-presidential-center) | Trip to the Obama Presidential Center (`Q-NITA-27`) |
| [About NITA](https://nita.illinois.gov/about-nita) | What NITA is, the NITA Act, the RTA transition, the NITA tax (`Q-NITA-28` to `30`) |
| [Meeting Materials](https://nita.illinois.gov/about-nita/boards-and-committees/meeting-materials) | Board meeting schedule and public comment (`Q-NITA-32`) |
| [Board of Directors](https://nita.illinois.gov/about-nita/boards-and-committees/board-of-directors) | Board members (`Q-NITA-33`) |
| [Contact](https://nita.illinois.gov/contact) | NITA phone numbers (`Q-NITA-34`) |
| [NITA Riders Advisory Council](https://nita.illinois.gov/nita-rider-advisory-council) | Joining the council (`Q-NITA-35`) |
| [FOIA](https://nita.illinois.gov/about-nita/transparency/foia) | FOIA requests (`Q-NITA-36`) |
| [Funding](https://nita.illinois.gov/transit-funding) | How transit is funded, the fiscal cliff (`Q-NITA-37`) |
| [People Over Parking Act](https://nita.illinois.gov/communities/people-over-parking-act) | The act and municipal assistance (`Q-NITA-38`, `39`) |
| [Section 5310](https://nita.illinois.gov/region/section-5310) | Section 5310 program (`Q-NITA-42`) |
| Reduced Fare and Ride Free application PDFs (`/uploads/files/general/Riders/…`) | Shown by Google for permit searches; checked as answer documents |

With these additions the sample has 32 pages (28 NITA, 4 My Transit Benefit) and 2 documents.

## Review controls and current status

| Proposal area / control | What to verify | Primary method and evidence | NITA status | My Transit Benefit status |
| --- | --- | --- | --- | --- |
| Content structure and information hierarchy | Whether page structure (headings, lists, tables, accordions, answer placement) lets answer systems find and extract the answer to each inventory question. | Heading and accordion inventory of the core pages ([`page-headings.csv`](../../../evidence/aeo/2026-11-25/page-headings.csv)); SEO raw HTML and page text; Step 2 part B. | **In progress.** Step 1 recorded 622 headings and accordion labels on 60 core pages. The answer map shows that 16 of the 45 answers found on a page sit wholly or partly in closed accordions or tab panels; the ADA Paratransit application steps are about 1,100 words below the H1. Part B pending. | **In progress.** 30 headings on the four pages recorded; three product headings on Behind the Benefits have no text. Part B pending. |
| Featured snippet and direct-answer opportunities | Whether each priority question has a concise, direct answer near the top of the right page, and which source Google shows today. | Answer map (Step 2 part A); answer-feature capture for 20 priority questions (Step 2 part C). | **In progress.** 23 of 42 questions have a direct answer, including 10 of 14 priority questions. Answer-feature capture (part C) pending. | **In progress.** 4 of 15 questions have a direct answer, including 3 of 6 priority questions. Answer-feature capture (part C) pending. |
| Question-based content and FAQ opportunities | Which inventory questions are answered, scattered, or missing; where FAQ blocks would help. | Question inventory and answer map. | **In progress.** 42 questions inventoried; 48 question-style headings and accordion labels found on core pages (for example on Access, Ride Free, Ride Safe, FOIA). Answer map: 3 questions missing (the NITA tax, ADA Paratransit trip purposes, how to apply to Access to Transit), 3 scattered, 1 link-only. Ride Safe and People Over Parking Act have plain-text FAQs; Access has an accordion FAQ. | **In progress.** 15 questions inventoried; the only question-style headings are “How the Program Works” and “How you save”. Answer map: 4 questions missing (employee enrollment, fund expiry, the prepaid card, fees), 1 link-only (employer sign-up in a PDF guide). |
| Semantic content organization | Whether related answers are grouped on the page people expect, and whether program names and terms are consistent. | Answer map; content structure inventory; SEO page text. | **In progress.** Answers for seniors, the NITA Act, and the Travel Information number are spread across sections or pages. Names vary: “Access Permit” and “Access card”; FOIA says “Northern Illinois Transportation Authority”; the Ride Free replacement text says “reduced fare permit”. Part B pending. | **In progress.** What the program is and who runs it is not stated in one place; product information is in empty headings. Part B pending. |
| Structured data opportunities | Answer-oriented markup that fits visible content and that Google supports (`FAQPage`, `GovernmentService`, `Event`), beyond the current markup reviewed in SEO. | SEO JSON-LD extraction; Google Search Central documentation; Step 2 part D. | **Not assessed.** | **Not assessed.** |
| Content clarity and relevance for answer-oriented queries | Whether answers are current, consistent between pages and with partner sources, and written in the terms people use. | Answer map; SEO fare and time-sensitive checks; partner sources. | **In progress.** Inventory records the terms people use (including “RTA” permit names). Answer map: 4 conflicting answers (Regional Day Pass prices, ADA Paratransit call hours, CTA station accessibility, board meeting day and time) and 2 outdated (2027 budget hearing, Riders Advisory Council applications). The application PDFs still name the RTA and `rtachicago.org`. | **In progress.** Inventory records the terms people use. Answer map: the employer law section is outdated; savings rates (7.65% and 8.45%) and the $340 limit are stated differently on different pages. |

## Evidence and review log

| Date | Website | Control(s) reviewed | Method / evidence | Reviewer notes or follow-up |
| --- | --- | --- | --- | --- |
| 2026-11-25 | Both websites | Step 1: scope, question inventory, and sample | [Step 1 evidence](../../../evidence/aeo/2026-11-25/README.md) | Autocomplete for 48 question-style seeds (250 suggestions) and “People also ask” on 17 Google result pages (60 questions), through a US connection with a Chicago, Illinois IP address; AI Overviews on 16 of 17 pages. Heading and accordion inventory of 60 NITA core pages and the 4 My Transit Benefit pages. Built a 57-question inventory and proposed 12 pages and 2 documents to add to the SEO sample. The team approved the inventory and the sample the same day. |
| 2026-11-25 | Both websites | Step 2 part A: answer map (structure, snippets, FAQ, semantic, clarity) | [Answer map evidence](../../../evidence/aeo/2026-11-25/README.md#step-2-part-a--answer-map) | Page text with accordion, table, and tab-panel markers for 23 answer pages, plus the two application PDFs. All 57 questions mapped: NITA 23 direct, 6 partial, 3 scattered, 4 conflicting, 2 outdated, 1 link-only, 3 missing; My Transit Benefit 4 direct, 5 partial, 1 outdated, 1 link-only, 4 missing. Regional Day Pass prices compared with metra.com/rdp through the US connection with a Chicago, Illinois IP address. |

## Related reports

- [NITA AEO report](nita-illinois-gov.md)
- [My Transit Benefit AEO report](mytransitbenefit-com.md)
- [AEO work plan](aeo-audit-plan.md)
