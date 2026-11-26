# AEO Step 3 part B — question-based content and FAQ opportunities (2026-11-26)

Evidence for Step 3 part B of the [AEO work plan](../../../../docs/audit/03-aeo/aeo-audit-plan.md): an assessment of the inventory questions whose answer is missing, scattered, partial, or link-only. For each one, it records where the answer is today and where a direct answer belongs. It also holds the checks behind findings `AEO-NITA-004` to `006` and `AEO-MTB-003`.

## Method

1. **Live recheck.** The 13 answer pages involved were fetched again on 2026-11-26 with curl's default settings and converted with the Step 2 extractor ([`structured_text.py`](../../2026-11-25/answer-map/structured_text.py)). Their text matched the 2026-11-25 page text line for line ([`live-recheck.txt`](live-recheck.txt)), so the Step 2 page text remains the evidence for those pages.
2. **Answers elsewhere on the domain.** For each gap, the reviewer looked for the answer on other NITA pages, in posts, press releases, and linked documents, using the SEO crawl exports (titles and headings of all 1,613 NITA pages) and the links on the answer pages. The pages and documents found were fetched with curl and kept as evidence:
   - [`page-text/`](page-text/): Moving the system, Riders, the NITA Act blog post of November 10, 2025, the Community Planning call for projects of April 1, 2026, and two RTA press releases (Senior Ride Free FAQs, 2011; Transit Benefit Prepaid MasterCard, 2013);
   - [`nita-act-docs/`](nita-act-docs/): NITA's board summary of the NITA Act (January 2026, PDF and text), the text of Illinois Department of Revenue bulletin FY 2026-34, and 49 CFR 37.131 from the eCFR API;
   - [`mtb-docs/`](mtb-docs/): the My Transit Benefit Account Setup Guide for employers (PDF and text).
3. **Google captures.** Nine more questions were searched on 2026-11-26 between 15:07 and 15:08 UTC with the Step 2 part C method and settings (`hl=en&gl=us&pws=0`). The captures ran in the built-in browser, not signed in, through a US connection with a Chicago, Illinois IP address ([`connection.txt`](connection.txt)). The queries use the wording of an autocomplete suggestion, a “People also ask” question, or the SEO search sample ([`gap-queries.tsv`](gap-queries.tsv)). The capture file [`google-gap-questions-2026-11-26.jsonl`](google-gap-questions-2026-11-26.jsonl) was checked against the browser's stored copy: the length of every record and every overview text matches.
4. **Assessment.** [`question_gaps.py`](question_gaps.py) joins the answer map, both capture files, and the reviewer's notes for 19 gap questions and writes [`question-gaps.csv`](question-gaps.csv). For each question, the file gives where the answer is today, the recommended location, and the Google result. A NITA or My Transit Benefit page counts as a cited source only when the AI Overview's source label names the website or one of its pages; labels that only mention the agency or the act (for example “FACT SHEET: Northern Illinois Transit Authority Act”) do not count. The same rule applied to the Step 2 part C capture gives the same results as before.

   `python3 -I question_gaps.py`

## Results

| Question | Status | Where the answer is today | Recommended location | Finding |
| --- | --- | --- | --- | --- |
| Seniors (`Q-NITA-13`) | scattered | Ride Free section without an age; age 65 rule in a closed accordion; a 2011 RTA FAQ | Short passage at the top of Discounted Fare and Ride Free Programs | `AEO-NITA-004` |
| Who qualifies for paratransit (`Q-NITA-20`) | partial | Service definition; closed “Types of Eligibility” accordion | ADA Paratransit section | `AEO-NITA-004` |
| Paratransit trip purposes (`Q-NITA-22`) | missing | Not stated | One sentence in the ADA Paratransit section | `AEO-NITA-004` |
| Trip planning and the Travel Information Center (`Q-NITA-24`, `25`) | partial, scattered | Embedded tool; number only on Contact, no hours | “Plan your ride” on How to ride | `AEO-NITA-004` |
| The NITA Act (`Q-NITA-29`), the NITA tax (`Q-NITA-30`), new funding (`Q-NITA-37`) | scattered, conflicting, partial | Leadership link on About NITA; Transit Funding tab; Moving the system accordions and list in pre-2026 wording | Section on About NITA; current rates on Moving the system | `AEO-NITA-005` |
| Access to Transit, Community Planning, Section 5310 (`Q-NITA-40` to `42`) | missing, partial, partial | Program history and awards; call dates only in a blog post; eligibility only in PDFs | “Who can apply and when” section on each page | `AEO-NITA-006` |
| Employee enrollment, services, unused funds, card, employer sign-up, fees (`Q-MTB-06`, `08`, `09`, `10`, `13`, `15`) | missing, partial, link-only | Empty product sections; employer Account Setup Guide (PDF) | Product sections on Behind the Benefits; common questions on Employees and Employers | `AEO-MTB-003` |
| What the program is (`Q-MTB-01`) | partial | No opening passage | Opening passage under the H1 | `AEO-MTB-002` |
| Registration sites (`Q-NITA-14`) | link-only | Menu link to an ArcGIS locator that works | One sentence near the locator link | Not a finding |

Google captures for the nine new queries (details in `question-gaps.csv`):

| Query | NITA or My Transit Benefit in first results | Cited in AI Overview | Other main sources |
| --- | --- | --- | --- |
| is paratransit only for medical appointments | none (Pace second) | no | National RTAP, SMART Bus, Ecolane |
| how do you qualify for paratransit | none (Pace third) | no | FTA, DREDF, Westchester County |
| what is the nita act | 3 (NITA Act summary PDF), 8 (press release) | no | Illinois General Assembly, State of Illinois Newsroom, Tressler LLP |
| what is the nita tax in illinois | 5 (Moving the system) | yes | Illinois Department of Revenue, VitalLaw.com |
| access to transit program grant illinois | 1 (Access to Transit), 4 (program guide PDF) | yes | AASHTO Journal |
| rta community planning program | 1 (Community Planning), 2 and 6 (blog posts) | yes | ArcGIS StoryMaps |
| do pre-tax transit benefits expire | none | no | HealthEquity, ADP, NYC.gov |
| rta transit benefit card | 1 (My Transit Benefit homepage); NITA's 2013 press release 4 | yes | CTA, Edenred |
| what can you use transit benefits for | none | no | Optum, TRI-AD, Wikipedia |

### Facts checked against official sources (2026-11-26)

- **NITA sales tax.** Illinois Department of Revenue bulletin FY 2026-34: from August 1, 2026, 1.25% (general merchandise) and 1.50% (qualifying food, drugs, and medical appliances) in Cook County, and 1.00% in DuPage, Kane, Lake, McHenry, and Will counties. NITA's board summary gives the rates before the increase as 1.00% and 1.25% in Cook County and 0.75% in the collar counties. Moving the system says 1.25% in Cook County and .50% in the collar counties, plus a “New 2026 0.25%”.
- **NITA Act dates.** The board summary gives June 1, 2026 as the effective date and September 1, 2026 as the end of the RTA Board members' terms; Moving the system says the Governor signed the act in December 2025.
- **Paratransit trip purpose.** 49 CFR 37.131(d): the operator “shall not impose restrictions or priorities based on trip purpose.”

## Correction to Step 2 part A

The answer-map row for `Q-NITA-30` (the NITA tax) recorded no answer, because Moving the system was not among the answer pages read in Step 2. That page does answer the question, in closed accordions, with rates that differ from the Department of Revenue's. The row was changed from “missing” to “conflicting” in [`build_answer_map.py`](../../2026-11-25/answer-map/build_answer_map.py) and [`answer-map.csv`](../../2026-11-25/answer-map/answer-map.csv). NITA's counts are now 24 direct, 6 partial, 3 scattered, 4 conflicting, 2 outdated, 1 link-only, and 2 missing, and 17 of the 46 answers found on a page sit wholly or partly in accordions or tab panels. The Step 2 README, the Step 2 part C note for `Q-NITA-28`, the matrix, and the work plan were updated.

## Not findings

- **Registration Sites** redirects to an ArcGIS locator that works; one sentence on the page would help, but the gap is small.
- **The blog link on Transit Funding** first appeared broken in the extracted text, because the extractor shortens long link addresses; the full `href` in the HTML works (200).
- **Rider press releases from the RTA period** are numerous; only the two that Google used, or that are the only answer to an inventory question, are cited in findings.

## Files

`live-recheck.txt`, `page-text/` (6 pages), `nita-act-docs/` (board summary PDF and text, Department of Revenue bulletin text, eCFR extract), `mtb-docs/` (Account Setup Guide PDF and text), `connection.txt`, `gap-queries.tsv`, `google-gap-questions-2026-11-26.jsonl`, `question_gaps.py`, `question-gaps.csv`.
