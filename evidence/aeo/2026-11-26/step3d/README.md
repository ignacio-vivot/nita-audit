# AEO Step 3 part D — structured data opportunities (2026-11-26)

Evidence for Step 3 part D of the [AEO work plan](../../../../docs/audit/03-aeo/aeo-audit-plan.md). The step decides which answer-oriented structured data, if any, to recommend for each website. It builds on the opportunity list of [Step 2 part D](../structured-data/README.md), and it holds the checks behind finding `AEO-NITA-009`. The validity and accuracy of the markup already on the websites are covered in SEO (`SEO-NITA-016`, `SEO-MTB-004`).

## Method

1. **Current markup.** The JSON-LD types were listed again on the 31 sample pages fetched on 2026-11-26 at 17:27 UTC (Step 3 part C):
   - the 27 NITA pages carry only the site template (`WebSite`, `GovernmentOrganization`, `BreadcrumbList`);
   - the 4 My Transit Benefit pages carry `WebSite`, `LocalBusiness`, and `BreadcrumbList`.

   This is unchanged from Step 2 part D, and no page has answer-oriented markup.
2. **Google documentation.** The pages used in Step 2 part D were fetched again with curl on 2026-11-26 at 18:14 UTC: Event, the search gallery, AI features and your website, the general structured data guidelines, Organization, Article, and the documentation updates. The “last updated” dates of the pages read in Step 2 part D were unchanged: Event and Organization 2026-09-08, search gallery 2026-10-16, AI features 2025-12-10, and general guidelines 2026-07-10. The Article page was last updated on 2026-09-08. The Event page lists the United States (English) among the regions where events are shown. Its requirements are:
   - one page per event;
   - a physical location;
   - events open to the general public.

   It recommends marking up event pages rather than pages that list schedules.
3. **Google captures.** Three searches were captured on 2026-11-26 at 18:15 UTC, using the Step 2 part C method and settings (`hl=en&gl=us&pws=0`). They ran in the built-in browser, not signed in, through a US connection with a Chicago, Illinois IP address ([`connection.txt`](connection.txt)). Two were for the board meeting question (`Q-NITA-32`), and one was the same search for the Chicago Transit Board, for comparison ([`board-meeting-queries.tsv`](board-meeting-queries.tsv)). The capture also records any “Events” panel on the result page. The saved file [`google-board-meeting-2026-11-26.jsonl`](google-board-meeting-2026-11-26.jsonl) was checked against the browser's stored copy: the length of every record and every AI Overview text matches.
4. **Meeting Materials.** The markup of the “Upcoming Meetings” card was read in the HTML fetched at 17:27 and 18:17 UTC, and the card was captured in the built-in browser. The notes are in [`meeting-materials-check.txt`](meeting-materials-check.txt) and the capture is [`meeting-materials-upcoming-card-2026-11-26.png`](meeting-materials-upcoming-card-2026-11-26.png).
5. **Comparison.** The Chicago Transit Board page was fetched with curl to see how it states its meeting details ([`cta-board-check.txt`](cta-board-check.txt)).

## Results

### Board meeting location in Google's AI Overviews

| Query | First NITA result | AI Overview on the location of the December 10 meeting |
| --- | --- | --- |
| nita board meeting | 1, Meeting Materials | “December 10, 2026, at 9:00 AM in Oak Park”; it adds that standard meetings take place at 175 W. Jackson Blvd. |
| when is the next nita board meeting | 1, Meeting Materials | “Location: Listed as an Oak Park Meeting on the NITA Meeting Materials page”; it then offers to help find “the exact Oak Park venue address” |
| cta board meeting (comparison) | — | “567 W. Lake St.”, the address stated in the CTA board page text |

In the “Upcoming Meetings” card on Meeting Materials, the only place the words “Oak Park” appear is a template photo of an elevated train station, `/dist/img/rta-oakpark-meeting.jpeg`, whose alternative text is “Oak Park Meeting”. The photo is placed before the date. The visible text gives the right place (“Board Room, 16th Floor, 175 W. Jackson Blvd., Chicago, IL 60604”) but no label such as “Location”. The second AI Overview names the page as the source of “Oak Park Meeting”.

None of the three result pages showed an “Events” panel. The CTA board page has no JSON-LD, but it states the place and usual time in a sentence of its text, and Google's AI Overview repeated them correctly. Neither board's answer depended on Event markup. The NITA answer was wrong because of an image label.

Recorded as `AEO-NITA-009`. The day, time, comment address, and calendar title of the same meetings are in `AEO-NITA-003`.

### Assessment by type

[`structured-data-assessment.csv`](structured-data-assessment.csv) gives the decision for each type and website:

| Type | NITA | My Transit Benefit |
| --- | --- | --- |
| `FAQPage`, `HowTo` | Not recommended: no Google feature. Visible question-and-answer passages instead (`AEO-NITA-001`, `004`) | Not recommended; visible common questions instead (`AEO-MTB-003`) |
| `Event` | Optional, only with one page per board meeting or public hearing (`AEO-NITA-009`); no events panel seen for board meeting searches | Not applicable |
| `GovernmentService` | Not recommended: no Google feature, and Google says AI features need no special markup | Not recommended |
| `Organization` / `GovernmentOrganization`, `Article`, `BreadcrumbList` | Covered by `SEO-NITA-016`; entity naming in GEO | Covered by `SEO-MTB-004`; entity naming in GEO |
| `SpecialAnnouncement`, `Speakable`, `Dataset`, Q&A, Discussion forum, Profile page | Not applicable or retired | Not applicable |

Conclusion: no structured data type is recommended as a stand-alone AEO action. What answer systems use from these websites is the visible text, its labels, and the text attached to images and links. The board meeting result shows that a misleading image label can change an answer. `Event` markup is worth adding only if NITA decides to publish one page per meeting for its own reasons.

## Not findings

- **No answer-oriented markup on either website.** This is not a gap in itself; Google offers no FAQ or HowTo results and needs no markup for AI features.
- **The NITA template's `GovernmentOrganization` nodes and the My Transit Benefit `LocalBusiness` node** are already covered by `SEO-NITA-016` and `SEO-MTB-004`.

## Files

`connection.txt`, `board-meeting-queries.tsv`, `google-board-meeting-2026-11-26.jsonl`, `meeting-materials-check.txt`, `meeting-materials-upcoming-card-2026-11-26.png`, `cta-board-check.txt`, `structured-data-assessment.csv`.
