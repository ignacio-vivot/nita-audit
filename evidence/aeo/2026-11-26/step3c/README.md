# AEO Step 3 part C — structure, hierarchy, and semantic organization (2026-11-26)

This folder holds the evidence for Step 3 part C of the [AEO work plan](../../../../docs/audit/03-aeo/aeo-audit-plan.md). The step assesses whether headings, accordions, tables, lists, and the names used for agencies and programs help or hinder answer extraction on the 31 HTML pages of the sample. It holds the checks behind findings `AEO-NITA-007` and `008` and the new evidence added to `AEO-NITA-001`.

## Method

1. **Live recheck.** The 31 pages were fetched again on 2026-11-26 between 17:27 and 17:28 UTC with curl's default settings. Two checks were run on the new HTML:
   - the Step 2 inventory ([`structure_inventory.py`](../../2026-11-25/structure/structure_inventory.py)) and this step's script both gave the same output as the HTML of 2026-11-25;
   - the page text of the nine pages cited below had not changed.

   The 2026-11-25 HTML is therefore still the evidence ([`live-recheck.txt`](live-recheck.txt)).
2. **Structure assessment.** [`structure_assessment.py`](structure_assessment.py) reads the same HTML as Step 2 part B. It starts at the first H1 and skips menus, footers, forms, and scripts. It writes five files:
   - [`heading-issues.csv`](heading-issues.csv): empty headings, repeated headings, extra H1s, skipped levels, an accordion heading at the level of its section, and heading texts used three or more times;
   - [`accordion-sections.csv`](accordion-sections.csv): the heading each accordion label falls under in the page outline;
   - [`tables.csv`](tables.csv): each table with its section, header cells, and first row;
   - [`step-blocks.csv`](step-blocks.csv): numbered steps that are not an ordered list;
   - [`question-paragraphs.csv`](question-paragraphs.csv): questions written as bold paragraphs.

   `python3 -I structure_assessment.py`
3. **Manual review.** The reviewer read each flagged element in the HTML and checked where its content sits on the page. This included the in-page links on Accessible transit, the order of the fare accordions on Paying for your ride, and the markup of a meeting card on Meeting Materials.
4. **Google's guidance.** On 2026-11-26 the reviewer read what Google says about heading markup in the [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) (page last updated 2025-12-10). Under “Number and order of headings”, the guide says that semantic order helps screen readers. It also says that out-of-order headings do not matter to Google Search, because Google “can rarely depend on semantic meanings hidden in the HTML specification”. Step 2 part D had already recorded that Google's AI features need no special markup. This step therefore assesses where content sits and how it is labeled, and leaves markup that matters mainly to assistive technology to the accessibility review.
5. **Names.** The checks started from the Step 2 term counts ([`term-usage.csv`](../../2026-11-25/structure/term-usage.csv)):
   - each variant was read in context in the page text;
   - the links behind the fare portal names were listed from the HTML;
   - their redirects were taken from the Step 3 part A check ([`rta-domains-check.txt`](../step3a/rta-domains-check.txt)).

   The FOIA request form linked from the FOIA page was downloaded and its text extracted ([`foia/`](foia/)).
6. **Google captures.** Three FOIA searches were captured on 2026-11-26 at 17:35 and 17:36 UTC, using the Step 2 part C method and settings (`hl=en&gl=us&pws=0`). They ran in the built-in browser, not signed in, through a US connection with a Chicago, Illinois IP address ([`connection.txt`](connection.txt)). The queries and the source of their wording are in [`foia-queries.tsv`](foia-queries.tsv); the captures are in [`google-foia-2026-11-26.jsonl`](google-foia-2026-11-26.jsonl). The saved file was checked against the browser's stored copy: the length of every record and every AI Overview text matches.

## Results

### Where answers sit (assessed for AEO)

- **ADA Paratransit application (`Q-NITA-19`, `20`).** On Accessible transit, the page's jump links name three sections: “Transit Accessibility”, “ADA Paratransit”, and “Rideshare Access Program (RAP) and Taxi Access Program (TAP)”. The “ADA Paratransit” anchor leads to two short paragraphs and a video link. Three accordions come after the RAP and TAP text, with no heading of their own: “Paratransit Certification” (the phone number, the application steps, and the decision letter), “Types of Eligibility” (which includes the appeal process), and “Visitors”. In the page outline all three sit under the RAP and TAP heading ([`accordion-sections.csv`](accordion-sections.csv)). Each of the two section headings is also written twice as an H2 with the same text, once in the section title and once in the text block. This adds to `AEO-NITA-001`, which already records that the application steps have no visible “How to apply” passage; its evidence and recommendation were extended.
- **Fares (`Q-NITA-01`, `02`, `06`).**
  - On Paying for your ride, the six fare accordions sit together under “How much will my ride cost?”. Each accordion label (“CTA and Pace”, “Metra”, “Regional Passes”, “Children”, “Students”, “NICTD (South Shore Line)”) names its content, and the first sentences of the Metra accordion explain the zone tables.
  - The heading markup does not match this layout. The Metra accordion has no heading over its one-way fare table, unlike the CTA and Pace accordion (H3 “CTA and Pace”). It then opens an H2 “Metra Passes”, so the outline places the Regional, Children, Students, and South Shore accordions under “Metra Passes”.
  - The four Metra and Regional Day Pass price tables have no header cells: their first row (“Zone | 1 – 2 | 1 – 3 | 1 – 4 | 2 – 4”) is coded as ordinary cells. The four CTA, Pace, children, and student tables use header cells ([`tables.csv`](tables.csv)).
  - Because the labels and text next to each table name the content, and Google states that heading order does not matter to it, these are recorded as observations for the accessibility review, not as an AEO finding. The missing visible fare passage is `AEO-NITA-001`.
- **Seniors, the NITA Act, the Travel Information number, and community program eligibility** are split across sections or pages; this was assessed in Step 3 part B (`AEO-NITA-004`, `005`, `006`).
- **Other pages where much of the text is hidden on load** (FOIA 71%, Contact 57%, Board of Directors 72%) answer their inventory questions directly under descriptive labels (`Q-NITA-33`, `34`, `36`). The text is in the HTML. No further finding.

### Heading, table, list, and question markup (observations for the accessibility review)

| Pattern | NITA (27 pages) | My Transit Benefit (4 pages) |
| --- | --- | --- |
| H1s after the first, for secondary blocks or document links | 16 on 10 pages; for example “Recent Blog Posts”, “Related Articles”, “Newsletter”, “Disclaimer”, and, on Section 5310, “Program Management Plan”, “Human Services Transportation Plan (HSTP)”, and “Section 5310 Subrecipient Guide”; the homepage's three extra H1s are in `SEO-NITA-010` | “Login” on Employees (`SEO-MTB-003`) |
| Empty headings | 5 on 3 pages: the trip planner's error placeholder (`<h2 id="error">`) on How to ride and Getting to the Obama Presidential Center, section titles left blank on both pages, and a blank H2 after the Community Planning table | None |
| Skipped levels | 7 on 5 pages, for example H2 to H5 on Contact (“NITA Administrative Offices”), H2 to H4 in the Paratransit Certification accordion, and long sentences marked as H3 under an H1 on About NITA and Communities | 3: the slogan subtitle under each H1 is an H3 |
| Same heading twice in a row; heading repeating the H1 | Accessible transit (two section headings); How to ride (“How to ride”) | None |
| Heading texts used three or more times | Meeting Materials: 146 H2s, made up of 30 meeting dates, 30 meeting types, 84 link labels (“Agenda” 29, “Minutes” 20, “Slides” 19, “Watch” 16), and the two section headings. Each link label is an H2 inside its link | None |
| Tables | 17: 4 with header cells (CTA and Pace fares, CTA and Pace passes, children, students); 4 fare tables and 3 Program of Projects tables use ordinary cells for their header row; 6 tables lay out addresses, contacts, hearing dates, budget highlights, and the Ride Safe report types | None |
| Numbered steps | No ordered list on any page. Ride Safe shows four steps as numbered blocks (`<span>1</span>`); the 2027 budget page types “1.” to “3.”; ADA Paratransit, FOIA, Ride Free, and Access describe their steps in paragraphs | None |
| Questions | Ride Safe (9) and People Over Parking Act (11) write their FAQ questions as bold paragraphs; Access uses accordion labels; 24 question-style headings across the sample (Step 2 part B) | Calculator field labels (“Number of employees”, “Average Annual Salary Range”, “Savings Estimate”) are marked as H3s |

These patterns are not AEO findings, for three reasons:
- Google states that heading order does not matter for Google Search.
- Ride Safe ranked first for its question and supplied every NITA statement in the AI Overview on 2026-11-26 (Step 2 part C), even though its steps are numbered blocks and its FAQ is bold paragraphs.
- Google no longer shows FAQ or HowTo rich results (Step 2 part D).

The patterns do affect people who navigate by headings with a screen reader. Examples are 146 headings on Meeting Materials, five H1s on Section 5310, and ADA Paratransit content under the taxi heading. They are passed to the accessibility review, which should assess them against WCAG 2.1 success criteria 1.3.1 (Info and Relationships) and 2.4.6 (Headings and Labels). The SEO review recorded the extra H1s as an observation without a finding ([`nita-multiple-h1.csv`](../../../public-technical/2026-11-24/rendered-review/nita-multiple-h1.csv)). Step 3 part D will use the Meeting Materials markup when it assesses `Event` markup.

### Names (assessed for AEO)

| Name | Where | Observation |
| --- | --- | --- |
| Agency | FOIA, “How to submit a request” | “Northern Illinois Transportation Authority” twice; the email shown as `FOIA@nita.illinois.gov` links to `mailto:FOIA@rtachicago.org`; the linked request form (`FOIA-Request-Form-9-30-2015-1.docx`) is addressed to the “Regional Transportation Authority”, Suite 1650, `FOIA@rtachicago.org`, 312.913.3147. Recorded as `AEO-NITA-007` |
| Ride Free Permit | Discounted Fare and Ride Free Programs, “How to replace your Ride Free Permit” | “If your reduced fare permit is lost, stolen or damaged…” |
| Fare portal | Discounted Fare and Ride Free Programs; Access; the Access blog post of 2026-10-01; rider PDFs; Accessible transit | One portal at `fares.nita.illinois.gov` (page heading “Welcome To NITA Fare Programs Online”) is linked as `getaccess.org` from the fare programs page under “NITA Fare Programs Portal” (6 links), “Apply now”, and “new online portal”. The Access page links the same address as “GetAccess.org” (3 links) and Paying for your ride as “NITA-issued Access card” (4 links, two of them broken, `SEO-NITA-008`). The blog links `fares.nita.illinois.gov`; the PDFs and the RAP and TAP text use `fares.rtachicago.org` (`AEO-NITA-002`, `SEO-NITA-026`). All three addresses lead to the same portal. |
| Access Program | Access; Paying for your ride; the blog post; the 2027 budget page | The H1 says “Access Program”; the FAQ and the blog say “Access Pilot Program”. The credential is an “Access Permit” on Access, “Access permits” sent as “a new card” in the blog, and an “Access card” on Paying for your ride. |
| RTA | How to ride; Accessible transit | “maps for specific suburban areas in the RTA region”; “Use the RTA's trip planner and maps” (already in `SEO-NITA-028`) |

Recorded as `AEO-NITA-008`, except the agency name, which is part of `AEO-NITA-007`. My Transit Benefit's program names are covered by `AEO-MTB-002`.

Google captures of 2026-11-26 (details in `google-foia-2026-11-26.jsonl`):

| Query | NITA FOIA page in first results | AI Overview |
| --- | --- | --- |
| how to submit a foia request to nita | none | About the National Telecommunications and Information Administration (NTIA), a federal agency |
| nita illinois foia request | 1, with the title link “FOIA - Regional Transportation Authority - Illinois.gov” | Opens “Submit a Freedom of Information Act (FOIA) request to the Northern Illinois Transportation Authority (NITA) by emailing FOIA@nita.illinois.gov…”; lists the NITA FOIA page as a source |
| rta foia request | 2, same title link | Lists Illinois among several RTAs: “contact FOIA@nita.illinois.gov via the Regional Transportation Authority FOIA page” |

The page's own title is “Freedom of Information Act | Northern Illinois Transit Authority”. Google built a title link with the former agency name instead.

## Changes to earlier findings

`AEO-NITA-001` (Step 3 part A) gained one evidence paragraph and one recommendation clause: the ADA Paratransit accordions sit after the taxi and rideshare section, and they should be moved into the ADA Paratransit section with the new “How to apply” passage. Its priority and complexity are unchanged.

## Not findings

- **Heading levels, table header cells, numbered steps, and FAQ markup** are observations for the accessibility review (see above).
- **The secondary H1s** were already recorded by SEO as an observation; this step adds the document links on Section 5310.
- **My Transit Benefit structure.** The pages have no accordions, hidden text, tables, or lists. Their gaps are recorded in `AEO-MTB-002` (no opening passage, program names), `AEO-MTB-003` (empty product sections), and `SEO-MTB-003` (slogan H1s).
- **“Access card” and “Reduced Fare cards”** describe the physical card on which the permit is issued. They are recorded only as part of the naming pattern in `AEO-NITA-008`.

## Files

`live-recheck.txt`, `structure_assessment.py`, `heading-issues.csv`, `accordion-sections.csv`, `tables.csv`, `step-blocks.csv`, `question-paragraphs.csv`, `foia/` (request form and its text), `connection.txt`, `foia-queries.tsv`, `google-foia-2026-11-26.jsonl`.
