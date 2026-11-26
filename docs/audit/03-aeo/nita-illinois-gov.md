# Answer Engine Optimization (AEO) — nita.illinois.gov

## Assessment Scope

- **Website:** [nita.illinois.gov](https://nita.illinois.gov/)
- **Review date:** 2026-11-25 to 2026-11-26 (in progress)
- **Pages, templates, or journeys reviewed:** 42 inventoried questions for riders, the public, and local governments ([inventory](../../../evidence/aeo/2026-11-25/question-inventory.csv)); the approved sample of 28 pages and the rider application PDFs (see the [matrix](aeo-review-matrix.md#page-level-review-scope)), plus Moving the system and three older posts and press releases found while tracing missing answers, and the FOIA request form; Google result pages for 14 priority questions, 6 questions with missing or scattered answers, 3 FOIA searches, and 2 board meeting searches.
- **Methods and tools:** Google autocomplete and “People also ask” captures ([Step 1 evidence](../../../evidence/aeo/2026-11-25/README.md)); answer map, structure inventory, and program-name counts built from the page HTML ([Step 2 parts A and B](../../../evidence/aeo/2026-11-25/README.md#step-2-part-a--answer-map)); Google answer-feature capture ([Step 2 part C](../../../evidence/aeo/2026-11-26/answer-features/README.md)); structured data check against Google's documentation ([Step 2 part D](../../../evidence/aeo/2026-11-26/structured-data/README.md)); priority answer assessment ([Step 3 part A](../../../evidence/aeo/2026-11-26/step3a/README.md)); assessment of missing and scattered answers with nine further Google captures ([Step 3 part B](../../../evidence/aeo/2026-11-26/step3b/README.md)); structure and naming assessment with three FOIA captures ([Step 3 part C](../../../evidence/aeo/2026-11-26/step3c/README.md)); structured data assessment with two board meeting captures and one comparison ([Step 3 part D](../../../evidence/aeo/2026-11-26/step3d/README.md)). SEO evidence is reused as listed in the [work plan](aeo-audit-plan.md#what-seo-already-collected-and-how-aeo-reuses-it). The review is AI-assisted: Claude collects and analyzes the evidence, and the team reviews each part.
- **Control checklist:** [AEO review matrix](aeo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** Steps 1 and 2 of the [AEO work plan](aeo-audit-plan.md) are complete. Step 3 is complete and has produced nine findings: part A (direct answers and answer clarity), part B (question-based content and FAQ opportunities), part C (structure and semantic organization), and part D (structured data opportunities). Of the 14 priority questions, 6 have a direct, visible answer passage on the expected page. Pages built that way, such as Ride Safe, the Access Program, and People Over Parking Act, rank in the first results for their questions and are cited in the AI Overviews. NITA appears in the first results for 13 of the 14 priority searches and is a listed source in 12 AI Overviews.

The main gaps are:
- answers that sit in closed accordions or tables without a visible answer sentence (fares and ADA Paratransit applications, `AEO-NITA-001`);
- common rider questions about seniors, paratransit eligibility and trip purposes, and phone trip planning that no page answers in one place (`AEO-NITA-004`);
- rider forms that still carry the RTA name and mailing address (`AEO-NITA-002`);
- board meeting details that differ between pages (`AEO-NITA-003`), and an image label on Meeting Materials that leads Google's AI Overview to place the next board meeting in Oak Park (`AEO-NITA-009`);
- the NITA Act and the new transit sales tax, which are explained only in scattered passages, some written before the act took effect and one with a collar-county rate that differs from the Illinois Department of Revenue (`AEO-NITA-005`);
- community program pages that do not say who can apply or when (`AEO-NITA-006`);
- FOIA instructions that misname the agency and point to RTA contact details, which Google's AI Overview repeats (`AEO-NITA-007`);
- permit, program, and fare portal names that vary between rider pages (`AEO-NITA-008`).

Past events and conflicting call hours recorded in SEO (`SEO-NITA-027`) also reach the AI Overviews.

On several pages, heading levels, table header cells, and the markup of steps and FAQ questions do not match the visual layout. Google states that heading order does not matter for Google Search, and pages built this way, such as Ride Safe, are already used in AI Overviews. These patterns mainly affect screen-reader users, so they are passed to the accessibility review rather than recorded as AEO findings ([matrix](aeo-review-matrix.md#review-controls-and-current-status)).

No structured data type is recommended as a stand-alone AEO action. Google no longer shows FAQ or HowTo results and states that its AI features need no special markup. `Event` markup is an option only if each board meeting or hearing gets its own page (`AEO-NITA-009`). Corrections to the existing markup are in SEO (`SEO-NITA-016`). Step 4 (final statuses and roadmap inputs) is next.

### Findings at a glance

Findings are listed in report order: by priority, then by user impact. IDs are stable references assigned when each finding was created, so they are not consecutive. Timing will be added when the roadmap groups the findings.

| ID | Finding | Priority | Complexity | Timing |
| --- | --- | --- | --- | --- |
| [`AEO-NITA-001`](#fare-and-ada-paratransit-answers-have-no-visible-answer-passage) | Fare and ADA Paratransit answers have no visible answer passage | Medium | Low | — |
| [`AEO-NITA-004`](#common-rider-questions-about-seniors-paratransit-and-trip-planning-have-no-answer-passage) | Common rider questions about seniors, paratransit, and trip planning have no answer passage | Medium | Low | — |
| [`AEO-NITA-002`](#rider-application-forms-and-brochures-still-carry-the-rta-name-and-mailing-address) | Rider application forms and brochures still carry the RTA name and mailing address | Medium | Medium | — |
| [`AEO-NITA-003`](#board-meeting-day-time-and-comment-details-differ-between-pages) | Board meeting day, time, and comment details differ between pages | Medium | Low | — |
| [`AEO-NITA-009`](#googles-ai-overview-places-the-next-board-meeting-in-oak-park-taken-from-an-image-label-on-meeting-materials) | Google's AI Overview places the next board meeting in Oak Park, taken from an image label on Meeting Materials | Medium | Low | — |
| [`AEO-NITA-005`](#the-nita-act-and-the-new-transit-sales-tax-are-explained-only-in-scattered-partly-outdated-passages) | The NITA Act and the new transit sales tax are explained only in scattered, partly outdated passages | Medium | Low | — |
| [`AEO-NITA-007`](#foia-request-instructions-name-the-wrong-agency-and-send-requests-to-rta-contact-details) | FOIA request instructions name the wrong agency and send requests to RTA contact details | Medium | Low | — |
| [`AEO-NITA-006`](#community-program-pages-do-not-say-who-can-apply-or-when) | Community program pages do not say who can apply or when | Low | Low | — |
| [`AEO-NITA-008`](#permit-program-and-fare-portal-names-vary-between-rider-pages) | Permit, program, and fare portal names vary between rider pages | Low | Low | — |

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

  The structure review of 2026-11-26 found two more problems on Accessible transit:
  - The page's jump link “ADA Paratransit” leads to two short paragraphs and a video link.
  - The three accordions that hold the rest of the ADA Paratransit information come after the “Rideshare Access Program (RAP) and Taxi Access Program (TAP)” section, with no heading of their own: “Paratransit Certification” (application steps), “Types of Eligibility” (eligibility types and the appeal process), and “Visitors”. In the page outline they therefore sit under the taxi and rideshare heading ([`accordion-sections.csv`](../../../evidence/aeo/2026-11-26/step3c/accordion-sections.csv); [Step 3 part C evidence](../../../evidence/aeo/2026-11-26/step3c/README.md#where-answers-sit-assessed-for-aeo)).
- **Impact:** Riders who want a fare or the paratransit application number must open the right accordion to find it, and on Accessible transit the application steps are far down the page under a label that does not say “apply”. Answer systems look for a short passage that answers the question; without one on NITA's pages they tend to take the answer from operator pages, as the fare and paratransit result pages show, including a call-hours statement that differs from NITA's. Adding a passage does not guarantee that Google or an AI system will use it.
- **Recommendation:** Add a short, visible answer passage above the accordions on each page and keep the tables for detail. On Paying for your ride, state the standard CTA, Pace, and Metra fares in two or three sentences (for example “A CTA ‘L’ ride costs $2.50 and a CTA bus ride $2.25 with Ventra or a contactless card”). On Accessible transit, add an H2 such as “How to apply for ADA Paratransit” directly after the ADA Paratransit description, with the phone number, the call hours (once confirmed under `SEO-NITA-027`), and the first steps in its opening sentences. Move the “Paratransit Certification”, “Types of Eligibility”, and “Visitors” accordions under that heading, before the RAP and TAP section. Review these passages whenever fares or hours change.
- **Implementation complexity:** Low (content edits on two pages)
- **Related standard:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) (important content available in textual form; no special markup needed)

### Common rider questions about seniors, paratransit, and trip planning have no answer passage

- **Finding ID:** AEO-NITA-004
- **Page or component:** [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs), the ADA Paratransit section of [Accessible transit](https://nita.illinois.gov/riders/accessible-transit), “Plan your ride” on [How to ride](https://nita.illinois.gov/riders/how-to-ride), and the 2011 press release [Senior Ride Free FAQs](https://nita.illinois.gov/about-rta/press-releases/senior-ride-free-faqs).
- **Priority:** Medium
- **Evidence:** Answer map of 2026-11-25; the pages were fetched again on 2026-11-26 and their text had not changed ([`live-recheck.txt`](../../../evidence/aeo/2026-11-26/step3b/live-recheck.txt)). Google result pages were captured on 2026-11-26 through a US connection with a Chicago, Illinois IP address ([`question-gaps.csv`](../../../evidence/aeo/2026-11-26/step3b/question-gaps.csv)):

  | Question | What the website says | Google result page, 2026-11-26 |
  | --- | --- | --- |
  | How do seniors ride free or at a reduced fare? (`Q-NITA-13`) | Ride Free Permits: people “enrolled in the Illinois Department on Aging’s Benefit Access program are eligible to ride free”, with no age stated. The rule for age 65 and over is in the closed “Senior Reduced Fare” accordion under Reduced Fare Permits. No passage puts the two together. | “how do i get a senior cta pass in chicago”: CTA ranks first and NITA second. The AI Overview combines CTA, NITA, the 44th Ward, and CHI 311 to explain both programs |
  | Is paratransit only for medical appointments? (`Q-NITA-22`) | Not stated. The section calls ADA Paratransit “a shared ride, advanced reservation, origin-to-destination transportation service” | No NITA page in the first nine results; Pace is second. The AI Overview answers “No” from National RTAP, SMART Bus, and Ecolane |
  | Who qualifies for ADA Paratransit? (`Q-NITA-20`) | Only the service definition (“individuals who, because of their disability, are unable to use CTA or Pace fixed route transit service for some or all of their trip”) and the closed “Types of Eligibility” accordion | No NITA page in the first eight results; Pace is third. The AI Overview cites the Federal Transit Administration, DREDF, and other transit agencies |
  | How do I plan a trip, or get help by phone? (`Q-NITA-24`, `Q-NITA-25`) | How to ride: “Use the trip planner to find the best transit route for your trip.”, followed by the embedded tool. The NITA Travel Information number (312-836-7000) appears only in the Contact table, without hours | “plan a trip on cta” (Step 2 part C): How to ride is sixth and not cited. The AI Overview gives the Travel Information Center number and hours from CTA |

  Federal rules for ADA complementary paratransit state that the operator “shall not impose restrictions or priorities based on trip purpose” ([49 CFR 37.131(d)](https://www.ecfr.gov/current/title-49/subtitle-A/part-37/subpart-F/section-37.131), checked on 2026-11-26).

  The only question-and-answer page about seniors on the website is the press release “Senior Ride Free FAQs” of February 22, 2011 ([page text](../../../evidence/aeo/2026-11-26/step3b/page-text/press-senior-ride-free-faqs.md)). It describes the program as it was in 2011:
  - eligibility through the “Illinois Department on Aging Circuit Breaker Program”, with 2011 income limits (“$27,610 or less for an individual”), where the current page requires the Benefit Access Program;
  - applications “at the RTA’s Customer Service Center at 165 N. Jefferson”;
  - “200 registration sites”.

  The release is listed in the XML sitemap, is indexable, and is linked only from page 35 of the press release archive ([`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv); [`nita-page-inlinks.csv`](../../../evidence/crawls/link-discovery/2026-11-24/nita-page-inlinks.csv)). Its link for the list of registration sites (`/index.php/home`, link text “www.RTAchicago.org”) returns 404 and is part of `SEO-NITA-009`.
- **Impact:** Older adults, people with disabilities, and caregivers ask these questions before they apply or book a ride. On NITA's pages they have to combine two sections or open accordions, and nothing tells them that paratransit is not limited to medical trips. Answer systems fill the gap with operator, federal, and out-of-region sources, and an indexed 2011 FAQ with former program names, income limits, and an office address remains available to them. Adding passages does not guarantee that Google or an AI system will use them.
- **Recommendation:** Add short, visible answer passages in plain text, not in accordions:
  - On Discounted Fare and Ride Free Programs, add a two- or three-sentence passage near the top for older adults: who rides free (Benefit Access enrollment), who gets a Reduced Fare Permit (age 65 and over), and how to apply.
  - On Accessible transit, in the ADA Paratransit section and together with the “How to apply” passage in `AEO-NITA-001`, state who qualifies and that rides can be used for any trip purpose.
  - Under “Plan your ride” on How to ride, add the Travel Information Center number and its hours.
  - Add a dated note at the top of the 2011 press release that it describes a former program, with a link to the current Ride Free page.

  Confirm the wording with the fare programs and paratransit teams. Question-style headings are enough; FAQ markup is not needed, because Google stopped showing FAQ rich results on May 7, 2026 ([Step 2 part D](../../../evidence/aeo/2026-11-26/structured-data/README.md)).
- **Implementation complexity:** Low (content edits on three pages and one archive note)
- **Related standard:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features); [49 CFR 37.131(d)](https://www.ecfr.gov/current/title-49/subtitle-A/part-37/subpart-F/section-37.131) (trip purpose)

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

### Google's AI Overview places the next board meeting in Oak Park, taken from an image label on Meeting Materials

- **Finding ID:** AEO-NITA-009
- **Page or component:** “Upcoming Meetings” card on [Meeting Materials](https://nita.illinois.gov/about-nita/boards-and-committees/meeting-materials) (page template).
- **Priority:** Medium
- **Evidence:** The card was checked in the HTML fetched on 2026-11-26 and in the built-in browser ([notes](../../../evidence/aeo/2026-11-26/step3d/meeting-materials-check.txt); [screenshot](../../../evidence/aeo/2026-11-26/step3d/meeting-materials-upcoming-card-2026-11-26.png)). In order, it shows:
  - a template photo of an elevated train station (`/dist/img/rta-oakpark-meeting.jpeg`) with the alternative text “Oak Park Meeting”;
  - the headings “Upcoming: December 10, 2026: 9:00 AM” and “Board Meeting”;
  - the address “Board Room, 16th Floor, 175 W. Jackson Blvd., Chicago, IL 60604”, with no label such as “Location”.

  “Oak Park” appears nowhere else on the page. The page has no `Event` markup; its JSON-LD is the site template.

  Google result pages were captured on 2026-11-26 through a US connection with a Chicago, Illinois IP address ([captures](../../../evidence/aeo/2026-11-26/step3d/google-board-meeting-2026-11-26.jsonl); [Step 3 part D evidence](../../../evidence/aeo/2026-11-26/step3d/README.md)):
  - “nita board meeting”: Meeting Materials ranked first. The AI Overview said the next meeting is on “December 10, 2026, at 9:00 AM in Oak Park”, and then that standard meetings are held at 175 W. Jackson Blvd.
  - “when is the next nita board meeting”: Meeting Materials ranked first. The AI Overview gave the location as “Listed as an Oak Park Meeting on the NITA Meeting Materials page”, and then offered to help find “the exact Oak Park venue address”.
  - “cta board meeting”, for comparison: the AI Overview gave the Chicago Transit Board's address correctly. The CTA board page has no structured data; it states the place and usual time in a sentence of its text ([CTA check](../../../evidence/aeo/2026-11-26/step3d/cta-board-check.txt)).

  None of the three result pages showed an events panel. Google's [Event documentation](https://developers.google.com/search/docs/appearance/structured-data/event) (last updated 2026-09-08) supports event results only for pages about a single event, at a physical location and open to the public. It recommends marking up event pages rather than pages that list schedules. Every NITA meeting is listed on Meeting Materials, with no page of its own ([assessment by type](../../../evidence/aeo/2026-11-26/step3d/structured-data-assessment.csv)).
- **Impact:** The December 10 meeting includes the board's vote on the 2027 budget. Residents who ask Google where it takes place are told Oak Park, a different municipality from the Chicago address on the page. The second answer even offers to look for an Oak Park venue. Readers of the page itself see the correct address. The label that misleads the AI Overview is part of the page template, so it will appear beside every upcoming meeting until it is changed. Screen-reader users hear the same “Oak Park Meeting” label before the date.
- **Recommendation:**
  - Give the template photo an empty alternative text (`alt=""`), because it is decorative; if a description is kept, describe the photo without a place name that can be read as the venue.
  - Label the meeting details in the card's text, for example “Date and time: Thursday, December 10, 2026, 9:00 a.m. Location: Board Room, 16th Floor, 175 W. Jackson Blvd., Chicago”, followed by how to watch online and how to comment (with the corrections in `AEO-NITA-003`).
  - Optional: if NITA decides to give each board meeting and public hearing its own page (date, time, place, agenda, and how to comment), add `Event` markup to those pages that matches the visible text, and keep past meetings marked as past. On 2026-11-26 Google showed no events panel for board meeting searches, so this is a longer-term option, not a fix for the wrong location.

  Recheck the AI Overview after the change; Google may take time to recrawl the page, and the result cannot be guaranteed.
- **Implementation complexity:** Low (template alternative text and labels); Medium if single-meeting pages are added
- **Related standard:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features); [Event structured data](https://developers.google.com/search/docs/appearance/structured-data/event); WCAG 2.1 success criterion 1.1.1 (Non-text Content), for the accessibility review

### The NITA Act and the new transit sales tax are explained only in scattered, partly outdated passages

- **Finding ID:** AEO-NITA-005
- **Page or component:** [About NITA](https://nita.illinois.gov/about-nita), [Transit Funding](https://nita.illinois.gov/transit-funding), and [Moving the system](https://nita.illinois.gov/transit-funding/moving-the-system) (page title “Keeping riders moving”).
- **Priority:** Medium
- **Evidence:** Page text fetched on 2026-11-26 ([Moving the system](../../../evidence/aeo/2026-11-26/step3b/page-text/moving-the-system.md); [About NITA and Transit Funding](../../../evidence/aeo/2026-11-25/answer-map/page-text/), unchanged since 2026-11-25 per [`live-recheck.txt`](../../../evidence/aeo/2026-11-26/step3b/live-recheck.txt)):

  | Page and location | Text |
  | --- | --- |
  | About NITA, Leadership | “The Northern Illinois Transit Authority is governed by the NITA Act and by-laws”, with a link to the Public Act 104-0457 PDF. The page does not say what the act does or when NITA replaced the RTA |
  | Transit Funding, “What is operating funding?” tab | “In the early morning hours of October 31, the Illinois General Assembly passed The NITA Act” (no year), and “riders will not experience service cuts or fare increases in 2026” |
  | Moving the system, “New funding streams to support operations starting in 2026” | “Governor JB Pritzker signed the Northern Illinois Transit Authority (NITA) Act into law in December 2025.” |
  | Moving the system, closed “Sales tax” accordion | “In Cook County NITA imposes a 1.25% sales tax whereas in DuPage, Kane, Lake, McHenry, and Will Counties the rate is .50%”, followed by “*New* 2026 0.25% NITA Sales Tax: Authorized by the NITA Act in late 2025, an additional sales tax of 0.25% in all six counties” |
  | Moving the system, closed “State 5.0% Sales Tax on Gasoline” accordion | “Expected to be effective in July 2026” |
  | Moving the system, “Where does the new funding come from?” (visible) | “RTA sales tax increase of 0.25%: $478 million for RTA region, pending approval by the RTA Board after the legislation’s effective date of June 1, 2026.” The same list appears in the [blog post of November 10, 2025](https://nita.illinois.gov/blog/2025/11/10/illinois-legislators-pass-landmark-transit-funding-and-reform-bill-averting-fiscal-cliff-what-does-it-mean-for-riders) |

  Official sources give the current facts:
  - The Illinois Department of Revenue bulletin FY 2026-34 (June 2026) sets the NITA rate from August 1, 2026 at 1.25% on general merchandise and 1.50% on qualifying food, drugs, and medical appliances in Cook County, and 1.00% in the five collar counties ([bulletin text](../../../evidence/aeo/2026-11-26/step3b/nita-act-docs/idor-fy-2026-34.txt)).
  - NITA's own board summary of the act (January 2026) gives the rates before the increase as 1.00% and 1.25% in Cook County and 0.75% in the collar counties. It gives June 1, 2026 as the act's effective date and September 1, 2026 as the end of the RTA Board members' terms ([summary text](../../../evidence/aeo/2026-11-26/step3b/nita-act-docs/6a_NITA_Act_Summary_and_Timeline.txt)).

  The collar-county rate on Moving the system (.50%) matches neither the rate before nor the rate after the increase, and the page does not say whether its Cook County 1.25% includes the increase. The answer-map row for `Q-NITA-30`, which first recorded no answer, was corrected ([Step 3 part B evidence](../../../evidence/aeo/2026-11-26/step3b/README.md#correction-to-step-2-part-a)).

  Google result pages captured on 2026-11-26 through a US connection with a Chicago, Illinois IP address ([`question-gaps.csv`](../../../evidence/aeo/2026-11-26/step3b/question-gaps.csv)):
  - “what is the nita tax in illinois”: the Illinois Department of Revenue ranked first and third, and Moving the system fifth. The AI Overview listed both as sources and took the rates from the Department of Revenue.
  - “what is the nita act”: the Illinois General Assembly and the Governor's fact sheet ranked first and second, and a NITA PDF titled “NITA Act (Public Act 104-0457) Summary” third. The AI Overview cited no NITA web page; it stated that the act was signed on December 16, 2025, took effect on June 1, 2026, and that NITA began operations on September 1, 2026, which no NITA page says in one place.
- **Impact:** Residents and businesses asking what the NITA Act changed or what the NITA tax is get those answers from the State, the Department of Revenue, law firms, and news sites rather than from NITA. The NITA page that Google does show for the tax question gives a collar-county rate that differs from the official rate, and describes taxes that are already in effect as pending or expected. Answer systems that quote that page can repeat the wrong rate.
- **Recommendation:**
  - On About NITA, add a short section on the NITA Act: what it does, when it was signed, when it took effect, and when NITA replaced the RTA, with links to the Public Act and the board summary.
  - On Moving the system, replace the sales tax rates with the current rates and their effective date, linked to the Department of Revenue bulletin, and move them out of the closed accordion.
  - Rewrite the “Where does the new funding come from?” list and the gasoline tax entry in the past tense with the NITA name, and add the year to “October 31” on Transit Funding.
  - Confirm every figure and date with NITA's finance and government affairs staff before publishing.
- **Implementation complexity:** Low (content edits on three pages)
- **Related standard:** [Google Search Central: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

### FOIA request instructions name the wrong agency and send requests to RTA contact details

- **Finding ID:** AEO-NITA-007
- **Page or component:** The “How to submit a request” panel on [FOIA](https://nita.illinois.gov/about-nita/transparency/foia) and the [Freedom of Information Request form](https://nita.illinois.gov/uploads/files/general/About-RTA/FOIA-Request-Form-9-30-2015-1.docx) (Word document) that it links as “request”.
- **Priority:** Medium
- **Evidence:** The sources are:
  - the page text of 2026-11-25, unchanged on 2026-11-26 ([page text](../../../evidence/aeo/2026-11-25/answer-map/page-text/nita-illinois-gov-about-nita-transparency-foia.md); [`live-recheck.txt`](../../../evidence/aeo/2026-11-26/step3c/live-recheck.txt));
  - the request form, downloaded on 2026-11-26 ([form text](../../../evidence/aeo/2026-11-26/step3c/foia/FOIA-Request-Form-9-30-2015-1.txt)).

  | Detail | FOIA page | Linked request form |
  | --- | --- | --- |
  | Agency | “For access to the public records of the Northern Illinois Transportation Authority”, and the same name in the address block | “All FOIA requests to the RTA must be submitted in writing”, sent to the “RTA FOIA Officer” at the “Regional Transportation Authority” |
  | Mailing address | 175 W. Jackson Boulevard, Suite 1550 | 175 W. Jackson Blvd., Suite 1650 (also in the page header, with `rtachicago.org`) |
  | Email | Shown as `FOIA@nita.illinois.gov`, but the link opens `mailto:FOIA@rtachicago.org` | `FOIA@rtachicago.org` |
  | Phone | None | 312.913.3147 |

  The agency's name is Northern Illinois Transit Authority, as in the page's own title, “Freedom of Information Act | Northern Illinois Transit Authority”. The form sits in an `About-RTA` upload folder, its file name carries the date 9-30-2015, and its document properties give 2018-10-17 as the last change.

  Google result pages were captured on 2026-11-26 through a US connection with a Chicago, Illinois IP address ([captures](../../../evidence/aeo/2026-11-26/step3c/google-foia-2026-11-26.jsonl); [Step 3 part C evidence](../../../evidence/aeo/2026-11-26/step3c/README.md#names-assessed-for-aeo)):
  - “nita illinois foia request”: the FOIA page ranked first, under the title link “FOIA - Regional Transportation Authority - Illinois.gov”. The AI Overview told readers to submit requests “to the Northern Illinois Transportation Authority (NITA)” by emailing `FOIA@nita.illinois.gov` or by mail to Suite 1550, and listed the NITA FOIA page as its source.
  - “rta foia request”: the FOIA page ranked second, with the same title link. The AI Overview listed the Illinois agency next to transit authorities in Michigan and Cleveland, under the name “Regional Transportation Authority”.
  - “how to submit a foia request to nita”: Google answered for the National Telecommunications and Information Administration (NTIA), a federal agency, and showed no NITA page in the first nine results. How generative platforms identify NITA is assessed in GEO.
- **Impact:** Residents, journalists, and businesses use these instructions to address a public-records request. Two of the routes on this page point to the former agency:
  - a reader who clicks the email address writes to the former RTA mailbox;
  - a reader who uses the linked form sends it to the RTA, at a different suite, under a different phone number.

  Whether `FOIA@rtachicago.org` and Suite 1650 still reach NITA's FOIA officer cannot be verified in the public scope. The incorrect agency name is already repeated in Google's AI Overview, and Google shows the page under the former agency's name.
- **Recommendation:**
  - Confirm the FOIA email address, mailing address, and phone number with the FOIA officer.
  - Change both mentions of the agency to “Northern Illinois Transit Authority”.
  - Point the email link to the address it shows.
  - Reissue the request form with the NITA name and the confirmed contact details, as an accessible PDF or a web form, and keep the current URL or redirect it to the new file.
  - Add one sentence saying that NITA replaced the RTA on September 1, 2026, so that people who search for the RTA know they have found the right office.

  Google chooses title links from several sources and may keep the former name for some time after the page is corrected.
- **Implementation complexity:** Low (text and link edits on one page; one form reissued)
- **Related standard:** [Google Search Central: influence your title links](https://developers.google.com/search/docs/appearance/title-link); [creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

### Community program pages do not say who can apply or when

- **Finding ID:** AEO-NITA-006
- **Page or component:** [Access to Transit](https://nita.illinois.gov/communities/access-to-transit-program), [Community Planning](https://nita.illinois.gov/communities/community-planning), and [Section 5310](https://nita.illinois.gov/region/section-5310).
- **Priority:** Low
- **Evidence:** Page text of 2026-11-25, unchanged on 2026-11-26 ([page text](../../../evidence/aeo/2026-11-25/answer-map/page-text/); [`live-recheck.txt`](../../../evidence/aeo/2026-11-26/step3b/live-recheck.txt)), and Google result pages captured on 2026-11-26 through a US connection with a Chicago, Illinois IP address ([`question-gaps.csv`](../../../evidence/aeo/2026-11-26/step3b/question-gaps.csv)):
  - **Access to Transit** (`Q-NITA-40`, missing). The page explains the program's history (“launched … in 2014”, “71 projects … $34.4 million”) and lists the 2026 awards. It does not say who can apply, when the next call for projects opens, or how to apply, and it links no program guide. For “access to transit program grant illinois”, the page ranked first and a NITA PDF titled “ACCESS TO TRANSIT PROGRAM” (`nita.illinois.gov › general › ProgramGuide`) ranked fourth. The AI Overview, citing NITA, said that eligible applicants are municipalities in the six counties and that projects are selected under federal CMAQ requirements, which the program page does not state.
  - **Community Planning** (`Q-NITA-41`, partial). The page describes the program and the 10 projects for 2026. The application window and the online form are only in the blog post [“RTA Community Planning program Call for Projects open now…”](https://nita.illinois.gov/blog/2026/04/01/rta-community-planning-program-call-for-projects-open-now-includes-new-people-over-parking-implementation-category) of April 1, 2026 (“now accepting applications through April 17, 2026”; [page text](../../../evidence/aeo/2026-11-26/step3b/page-text/blog-2026-04-01-community-planning-call.md)). The program page does not link that post. For “rta community planning program”, the program page ranked first and the post second.
  - **Section 5310** (`Q-NITA-42`, partial). The page defines the federal program, lists the funded projects, and states the local match (“An operating project … must provide a 50% local funding match … Capital and mobility management projects require a 20% local match”). It does not say who can apply or when applications open; it links a Program Management Plan and a Subrecipient Guide as PDFs.
- **Impact:** Municipal and agency staff who search for these programs land on the right pages, but must find a PDF, a past blog post, or an AI summary to learn whether they are eligible and when to apply. The AI Overview for Access to Transit gives eligibility that NITA's page does not state, so NITA cannot be sure it matches the program rules.
- **Recommendation:** Add a short “Who can apply and when” section near the top of each page: eligible applicants, how often calls for projects open and when the next one is expected, how to apply, and a link to the program guide or the current call. Update it at each call for projects, and link the call announcement from the program page while the call is open.
- **Implementation complexity:** Low (content edits on three pages)
- **Related standard:** [Google Search Central: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

### Permit, program, and fare portal names vary between rider pages

- **Finding ID:** AEO-NITA-008
- **Page or component:** [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs), [Access Program](https://nita.illinois.gov/riders/access), [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride), [How to ride](https://nita.illinois.gov/riders/how-to-ride), and the blog post [“NITA expands income-based reduced fare pilot Access across Metra, CTA, and Pace”](https://nita.illinois.gov/blog/2026/10/01/nita-expanding-access-pilot-program-to-cta-and-pace-starting-october-1-offering-income-based-reduced-fare-transit-regionwide) (October 1, 2026).
- **Priority:** Low
- **Evidence:** The sources are:
  - the page text of 2026-11-25, unchanged on 2026-11-26 ([`live-recheck.txt`](../../../evidence/aeo/2026-11-26/step3c/live-recheck.txt));
  - the term counts of Step 2 part B ([`term-usage.csv`](../../../evidence/aeo/2026-11-25/structure/term-usage.csv));
  - the portal links listed in Step 3 part C ([evidence](../../../evidence/aeo/2026-11-26/step3c/README.md#names-assessed-for-aeo)).

  | Name | What the pages say |
  | --- | --- |
  | Ride Free Permit | The “How to replace your Ride Free Permit” panel begins “If your reduced fare permit is lost, stolen or damaged…”. Ride Free and Reduced Fare are separate permits with different eligibility; elsewhere the same page says “Ride Free Permit” 8 times and “Reduced Fare Permit” 9 times |
  | Fare portal, on Discounted Fare and Ride Free Programs | Linked as `getaccess.org` under “NITA Fare Programs Portal” (6 links), “Apply now”, and “new online portal”; the opening text calls it the “Fare Portal” |
  | Fare portal, on the Access page | The same address, linked as “GetAccess.org” (3 links) |
  | Fare portal, elsewhere | The blog post links `fares.nita.illinois.gov`; the rider PDFs and the RAP and TAP text on Accessible transit use `fares.rtachicago.org` (`AEO-NITA-002`, `SEO-NITA-026`) |
  | Access Program | The Access page says “Access Program” 7 times, including the H1. Its FAQ and related-article list say “Access Pilot Program” (3 times), as does the blog post (4 times, including its tag). The credential is an “Access Permit” on the Access page and an “Access card” on Paying for your ride (4 links, two of them broken, `SEO-NITA-008`); the blog post says permit holders “will be sent a new card in the mail” |
  | RTA | How to ride describes “maps for specific suburban areas in the RTA region”. Accessible transit says “Use the RTA's trip planner and maps”, which is already part of `SEO-NITA-028` |

  The three portal addresses all redirect to one portal at `fares.nita.illinois.gov`, whose page heading is “Welcome To NITA Fare Programs Online” ([redirect check](../../../evidence/aeo/2026-11-26/step3a/rta-domains-check.txt)). In the Step 2 part C captures, Google's AI Overviews used “Access Permit”, “GetAccess.org”, and “NITA Fare Programs portal (formerly RTA Fare Programs Online)” correctly, so no capture showed an error caused by these variations.
- **Impact:**
  - A rider who has lost a Ride Free Permit reads replacement instructions that name the other permit and may not be sure the steps apply to them.
  - The same portal appears as “GetAccess.org” on one page and as the “NITA Fare Programs Portal” on another, which makes it look like two different websites.
  - Answer systems quote passages as written, so a passage that names the wrong permit can be repeated. No capture showed this, so the risk is limited.
- **Recommendation:**
  - Change “reduced fare permit” to “Ride Free Permit” in the replacement panel.
  - Use one name and one address for the portal in link text on every rider page, for example “NITA Fare Programs Online (fares.nita.illinois.gov)”, and keep `getaccess.org` as a redirect for printed Access materials.
  - Use “Access Program” and “Access Permit” consistently, and say once that the program is a pilot.
  - Replace “RTA region” with “the NITA region” or “the six-county region”.
  - Keep a short list of official program, permit, and portal names for editors.
- **Implementation complexity:** Low (text edits on four pages)
- **Related standard:** [Google Search Central: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

## Positive Observations

- **Clear answer pages are used by Google.** [Ride Safe App](https://nita.illinois.gov/safety/app) opens with a short definition under the question “What is NITA Ride Safe?”, lists numbered steps, and ends with a plain-text FAQ; on 2026-11-26 it ranked first for “ride safe app chicago” and supplied every NITA statement in the AI Overview. [About NITA](https://nita.illinois.gov/about-nita), [Access Program](https://nita.illinois.gov/riders/access), and [People Over Parking Act](https://nita.illinois.gov/communities/people-over-parking-act) also answer their main question in their opening sentences, and NITA was cited in the AI Overviews for those questions.
- **NITA is a recognized source.** NITA pages appeared in the first results for 13 of the 14 priority searches, ranked first for 6, and were listed as a source in 12 of the 14 AI Overviews.
- **Fares and the budget deadline are current.** The fares on Paying for your ride match CTA, Metra, and Pace, including the Regional Day Pass prices, and the 2027 budget page gives the correct December 4 comment deadline, which the AI Overview repeated.
- **The Reduced Fare application answer is direct.** Discounted Fare and Ride Free Programs opens by saying how to apply online, in person, or by phone.
- **Program pages rank first for their names.** On 2026-11-26, Access to Transit ranked first for “access to transit program grant illinois” and Community Planning first for “rta community planning program”, and both were cited in the AI Overviews. Adding eligibility and timing (`AEO-NITA-006`) builds on pages that Google already uses.
- **Rider task headings say what each section answers.** Examples are “How much will my ride cost?” on Paying for your ride; “How to apply for a Ride Free Permit”, “How to renew Ride Free Permits”, and “How to replace your Ride Free Permit” on Discounted Fare and Ride Free Programs; and “Who is eligible?” and “How do I get Access?” on Access. The fare accordion labels also name their content (“CTA and Pace”, “Metra”, “Regional Passes”, “Children”, “Students”).

## Limitations

- Search features (“People also ask”, AI Overviews, autocomplete, result pages) were captured through a US connection with a Chicago, Illinois IP address; Google returned US results that were not localized to Chicago, and results vary by date, device, and personalization. The captures are qualitative, from single sessions, and carry no search volume.
- Search Console and analytics are outside the agreed scope, so actual queries, featured-snippet ownership over time, and clicks cannot be measured.
- Whether former RTA mailing and email addresses still receive mail cannot be verified in the public scope.
- Tax rates, the act's dates, and the federal paratransit rule were checked against the Illinois Department of Revenue, NITA's board summary, and the eCFR on 2026-11-26 only. Whether the 0.25% increase was approved by the RTA Board, as the funding list says it must be, was not checked beyond the Department of Revenue bulletin.
- The Access to Transit program guide that Google listed (`ProgramGuide`) was not reviewed, because the program page does not link it.
- Heading, table, list, and FAQ markup was assessed only for answer extraction; its effect on screen-reader users is left to the accessibility review.
- The value of `Event` markup could not be tested, because no NITA page is dedicated to a single meeting; the captures recorded only that no events panel appeared for the board meeting searches.
