# Answer Engine Optimization (AEO) — nita.illinois.gov

## Assessment Scope

- **Website:** [nita.illinois.gov](https://nita.illinois.gov/)
- **Review date:** 2026-11-25 to 2026-11-26 (in progress)
- **Pages, templates, or journeys reviewed:** 42 inventoried questions for riders, the public, and local governments ([inventory](../../../evidence/aeo/2026-11-25/question-inventory.csv)); the approved sample of 28 pages and the rider application PDFs (see the [matrix](aeo-review-matrix.md#page-level-review-scope)); Google result pages for 14 priority questions.
- **Methods and tools:** Google autocomplete and “People also ask” captures ([Step 1 evidence](../../../evidence/aeo/2026-11-25/README.md)); answer map, structure inventory, and program-name counts built from the page HTML ([Step 2 parts A and B](../../../evidence/aeo/2026-11-25/README.md#step-2-part-a--answer-map)); Google answer-feature capture ([Step 2 part C](../../../evidence/aeo/2026-11-26/answer-features/README.md)); structured data check against Google's documentation ([Step 2 part D](../../../evidence/aeo/2026-11-26/structured-data/README.md)); priority answer assessment ([Step 3 part A](../../../evidence/aeo/2026-11-26/step3a/README.md)). SEO evidence is reused as listed in the [work plan](aeo-audit-plan.md#what-seo-already-collected-and-how-aeo-reuses-it). The review is AI-assisted: Claude collects and analyzes the evidence, and the team reviews each part.
- **Control checklist:** [AEO review matrix](aeo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** Steps 1 and 2 of the [AEO work plan](aeo-audit-plan.md) are complete, and Step 3 part A (direct answers and answer clarity) has produced the first three findings. Of the 14 priority questions, 6 have a direct, visible answer passage on the expected page. Pages built that way, such as Ride Safe, the Access Program, and People Over Parking Act, rank in the first results for their questions and are cited in the AI Overviews. NITA appears in the first results for 13 of the 14 priority searches and is a listed source in 12 AI Overviews. The main gaps are answers that sit in closed accordions or tables without a visible answer sentence (fares and ADA Paratransit applications, `AEO-NITA-001`), rider forms that still carry the RTA name and mailing address (`AEO-NITA-002`), and board meeting details that differ between pages (`AEO-NITA-003`). Past events and conflicting call hours recorded in SEO (`SEO-NITA-027`) also reach the AI Overviews. Steps 3B to 3D (missing answers and FAQ content, structure, structured data) are pending.

## Findings

### Fare and ADA Paratransit answers have no visible answer passage

- **Finding ID:** AEO-NITA-001
- **Page or component:** [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) and the “Paratransit Certification” accordion on [Accessible transit](https://nita.illinois.gov/riders/accessible-transit).
- **Priority:** Medium
- **Evidence:** In the answer map of 2026-11-25 ([`answer-map.csv`](../../../evidence/aeo/2026-11-25/answer-map/answer-map.csv)) and the priority answer assessment of 2026-11-26 ([`priority-answer-assessment.csv`](../../../evidence/aeo/2026-11-26/step3a/priority-answer-assessment.csv)), four priority questions are answered on these two pages only in closed accordions or tables, with no sentence under a matching heading that states the answer:

  | Question | Where the answer is | Google result page, 2026-11-26 |
  | --- | --- | --- |
  | How much is a CTA bus or train fare? (`Q-NITA-01`) | Only in a table (“CTA 'L' train fare \| $2.50*”, “CTA Bus fare \| $2.25”) inside the closed “CTA and Pace” accordion, 226 words below the H1 | CTA ranks first; NITA third. The AI Overview answers from CTA and lists NITA as one source |
  | How much does Metra cost? (`Q-NITA-02`) | The zone system is explained in visible text; prices only in tables inside the closed “Metra” accordion | Metra pages hold six of the first eight results; NITA is not among them |
  | How do I apply for ADA Paratransit? (`Q-NITA-19`) | First sentence of the closed “Paratransit Certification” accordion (“To apply for ADA Paratransit, call NITA's ADA Paratransit Certification program at 312-663-HELP (4357)”), about 1,100 words below the H1, with no “How to apply” heading | NITA ranks second and is cited, but the call hours in the AI Overview (8:30 AM to 5:00 PM) are attributed to Pace |
  | What is the ADA Paratransit phone number and when can I call? (`Q-NITA-21`) | Same accordion (“between 8:00 a.m. and 5:00 p.m., Monday through Friday”) | Pace holds the first three results; NITA is fifth |

  Measured in the built-in browser at 1280 × 900 px on 2026-11-25, 87% of the text after the H1 on Paying for your ride and 49% on Accessible transit is not visible until a reader opens an accordion or tab ([`browser-hidden-content.csv`](../../../evidence/aeo/2026-11-25/structure/browser-hidden-content.csv)). The text is in the HTML, so it can be indexed. The fares match CTA, Metra, and Pace (SEO fare check of 2026-11-24 and Regional Day Pass check of 2026-11-25). The two Google result pages for paratransit gave different call hours in the same session (8:30 and 8:00), which reflects the conflict already recorded in `SEO-NITA-027` ([answer-feature evidence](../../../evidence/aeo/2026-11-26/answer-features/README.md)).
- **Impact:** Riders who want a fare or the paratransit application number must open the right accordion to find it, and on Accessible transit the application steps are far down the page under a label that does not say “apply”. Answer systems look for a short passage that answers the question; without one on NITA's pages they tend to take the answer from operator pages, as the fare and paratransit result pages show, including a call-hours statement that differs from NITA's. Adding a passage does not guarantee that Google or an AI system will use it.
- **Recommendation:** Add a short, visible answer passage above the accordions on each page and keep the tables for detail. On Paying for your ride, state the standard CTA, Pace, and Metra fares in two or three sentences (for example “A CTA ‘L’ ride costs $2.50 and a CTA bus ride $2.25 with Ventra or a contactless card”). On Accessible transit, add an H2 such as “How to apply for ADA Paratransit” directly after the ADA Paratransit description, with the phone number, the call hours (once confirmed under `SEO-NITA-027`), and the first steps in its opening sentences. Review these passages whenever fares or hours change.
- **Implementation complexity:** Low (content edits on two pages)
- **Related standard:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) (important content available in textual form; no special markup needed)

### Rider application forms and brochures still carry the RTA name and mailing address

- **Finding ID:** AEO-NITA-002
- **Page or component:** The seven PDFs linked from [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs): [Reduced Fare Application](https://nita.illinois.gov/uploads/files/general/Riders/Reduced-Fare-Application-240301-mk-v12.pdf), [Ride Free Application](https://nita.illinois.gov/uploads/files/general/Riders/RTA-Ride-Free-Application-240117-v11.pdf), [Permit Replacement Application](https://nita.illinois.gov/uploads/files/general/Riders/RTA-FP-0056-Permit-Replacement-Application-Pad-24_v4-1.pdf), and the Reduced Fare and Ride Free brochures in English and Spanish ([Reduced Fare](https://nita.illinois.gov/uploads/files/general/Riders/Reduced-Fare-Brochure-240301-mk-v7.pdf), [Reduced Fare, Spanish](https://nita.illinois.gov/uploads/files/general/Riders/Reduced-Fare-Brochure-Spanish_v1.pdf), [Ride Free](https://nita.illinois.gov/uploads/files/general/Riders/Ride-Free-Brochure-240201-mk-v17.pdf), [Ride Free, Spanish](https://nita.illinois.gov/uploads/files/general/Riders/Ride-Free-Brochure-Spanish_v1.pdf)).
- **Priority:** Medium
- **Evidence:** The PDFs were fetched on 2026-11-25 and 2026-11-26 and their text was extracted with `pdftotext` ([`pdf-branding.csv`](../../../evidence/aeo/2026-11-26/step3a/pdf-branding.csv)):
  - None of the seven mentions NITA or the Northern Illinois Transit Authority. All use “RTA” (3 to 7 times each), for example “RTA Reduced Fare Permit Program” and “RTA Ride Free Permit”.
  - The six applications and brochures other than the replacement form send readers to `rtachicago.org` and `fares.rtachicago.org` (“Questions? Call 312-913-3110 or visit rtachicago.org”; “Apply online now at fares.rtachicago.org”). On 2026-11-26 these addresses redirected to the NITA homepage and to the NITA Fare Programs portal, so the links still work ([`rta-domains-check.txt`](../../../evidence/aeo/2026-11-26/step3a/rta-domains-check.txt)).
  - The three applications ask readers to mail them to “Regional Transportation Authority, PO Box 301150, Chicago, IL 60630”. The web page itself gives no mailing address.
  - Two file names start with “RTA”.
  On 2026-11-26, for “how to apply for rta reduced fare permit”, the Reduced Fare Application ranked third, and the AI Overview named the “Regional Transportation Authority (RTA/NITA) Reduced Fare Permit” and told readers to send applications “to the Regional Transportation Authority, PO Box 301150” ([capture](../../../evidence/aeo/2026-11-26/answer-features/google-answer-features-2026-11-26.jsonl)). The NITA Fare Programs portal, by contrast, states that NITA “replaced the RTA as of September 1, 2026”.
- **Impact:** Older adults and people with disabilities who apply by mail use these forms. A form that names a different agency and an RTA mailing address can make applicants unsure whether it is still valid, and answer systems already repeat the RTA address as the current instruction. Whether the PO Box still receives NITA's mail cannot be verified in the public scope.
- **Recommendation:** Confirm the current mailing address with the fare programs team, then reissue the seven PDFs with the NITA name and logo, `nita.illinois.gov` and `fares.nita.illinois.gov` addresses, and the confirmed mailing address, with a line such as “NITA replaced the RTA on September 1, 2026” for readers who know the program by its former name (`SEO-NITA-028`). Keep the current PDF URLs or redirect them to the new files so existing links and search results keep working, and add the mailing address to the program page text.
- **Implementation complexity:** Medium (form and brochure redesign in two languages, coordinated with print materials)
- **Related standard:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)

### Board meeting day, time, and comment details differ between pages

- **Finding ID:** AEO-NITA-003
- **Page or component:** [Board of Directors](https://nita.illinois.gov/about-nita/boards-and-committees/board-of-directors), [Meeting Materials](https://nita.illinois.gov/about-nita/boards-and-committees/meeting-materials), and the [2027 NITA Regional Budget](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget) page.
- **Priority:** Medium
- **Evidence:** Page text of 2026-11-25 ([page text](../../../evidence/aeo/2026-11-25/answer-map/page-text/)), with the Meeting Materials links checked live on 2026-11-26 ([structured data evidence](../../../evidence/aeo/2026-11-26/structured-data/README.md#observations-from-the-live-check-2026-11-26)):
  - Board of Directors: the board “meets on the third Thursday of each month”. Meeting Materials lists the next board meeting on Thursday, December 10, 2026, and a board meeting on November 12, 2026; both are second Thursdays. The October 15, 2026 meeting was a third Thursday.
  - Meeting Materials: “All NITA Board meetings take place at 9:00 a.m.” The 2027 budget page says the November 12 board meeting “will begin at 1 p.m.”
  - Meeting Materials tells readers to “Email communications@nita.illinois.gov by noon the day prior to comment at a meeting”, but the link behind that address is `mailto:communications@rtachicago.org`.
  - Both Add to Calendar links for December 10 (Google Calendar and `.ics`) are titled “RTA Board Meeting: December 10, 2026”; the time and address are correct.
  The budget page's invitation to the past November 12 hearing is recorded in `SEO-NITA-027`.
- **Impact:** Residents who want to attend a board meeting or comment on it, including the December 10 vote on the 2027 budget, get a meeting pattern that does not match the schedule, two different start times, and an email link that opens a message to the former RTA address. A comment sent through that link may not reach NITA, which cannot be verified in the public scope. Answer systems asked when the board meets can repeat any of these versions.
- **Recommendation:** Confirm the meeting schedule with the board office and replace “third Thursday of each month” with the correct pattern or a link to the meeting list; publish the year's adopted meeting dates on Meeting Materials; state each meeting's start time in its listing instead of a single time for all meetings; change the `mailto` link to `communications@nita.illinois.gov`; and rename the calendar entry “NITA Board Meeting”.
- **Implementation complexity:** Low (content and link edits; calendar title in the template)
- **Related standard:** [Google Search Central: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

## Positive Observations

- **Clear answer pages are used by Google.** [Ride Safe App](https://nita.illinois.gov/safety/app) opens with a short definition under the question “What is NITA Ride Safe?”, lists numbered steps, and ends with a plain-text FAQ; on 2026-11-26 it ranked first for “ride safe app chicago” and supplied every NITA statement in the AI Overview. [About NITA](https://nita.illinois.gov/about-nita), [Access Program](https://nita.illinois.gov/riders/access), and [People Over Parking Act](https://nita.illinois.gov/communities/people-over-parking-act) also answer their main question in their opening sentences, and NITA was cited in the AI Overviews for those questions.
- **NITA is a recognized source.** NITA pages appeared in the first results for 13 of the 14 priority searches, ranked first for 6, and were listed as a source in 12 of the 14 AI Overviews.
- **Fares and the budget deadline are current.** The fares on Paying for your ride match CTA, Metra, and Pace, including the Regional Day Pass prices, and the 2027 budget page gives the correct December 4 comment deadline, which the AI Overview repeated.
- **The Reduced Fare application answer is direct.** Discounted Fare and Ride Free Programs opens by saying how to apply online, in person, or by phone.

## Limitations

- Search features (“People also ask”, AI Overviews, autocomplete, result pages) were captured through a US connection with a Chicago, Illinois IP address; Google returned US results that were not localized to Chicago, and results vary by date, device, and personalization. The captures are qualitative, from single sessions, and carry no search volume.
- Search Console and analytics are outside the agreed scope, so actual queries, featured-snippet ownership over time, and clicks cannot be measured.
- Whether former RTA mailing and email addresses still receive mail cannot be verified in the public scope.
