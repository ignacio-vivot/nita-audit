# AEO Step 2 part D — structured data opportunities (2026-11-26)

Evidence for Step 2 part D of the [AEO work plan](../../../../docs/audit/03-aeo/aeo-audit-plan.md): which answer-oriented structured data types fit the visible content of the AEO sample, checked against Google's documentation as published on 2026-11-26. Validity and accuracy of the markup already on the websites are covered in SEO (`SEO-NITA-016`, `SEO-MTB-004`) and are not repeated here.

## Method

1. **Current markup.** The JSON-LD of the 20 SEO sample pages was extracted and validated on 2026-11-20 ([SEO structured data evidence](../../../public-technical/2026-11-20/structured-data/validation-results.md)). [`jsonld_types.py`](jsonld_types.py) lists the JSON-LD types on the 11 HTML pages that AEO added to the sample ([`jsonld-types-aeo-additions.csv`](jsonld-types-aeo-additions.csv)). All 11 carry the same template block as the SEO sample: `WebSite`, two `GovernmentOrganization` nodes, and `BreadcrumbList`. No page in the sample has `FAQPage`, `HowTo`, `Event`, `Article`, or `GovernmentService` markup.

   `python3 -I jsonld_types.py`

2. **Google documentation.** The pages below were read on 2026-11-26 in the built-in browser; a web-fetch agent read them first, and every statement used here was then checked directly on the page. Quotes are short extracts.

   | Page | Last updated | What it says |
   | --- | --- | --- |
   | [Search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) | 2026-10-16 | Lists Article, Breadcrumb, Dataset (“appear in Google Dataset Search”), Event, Organization, Q&A, Discussion forum, Profile page, Speakable, and others. FAQ, HowTo, Special announcement, and any government type are not listed. |
   | [Documentation updates](https://developers.google.com/search/updates) | — | May 8, 2026: FAQ rich results “will no longer appear in Google Search starting May 7, 2026.” June 15, 2026: FAQ documentation removed because the feature “is no longer shown in Google Search results”. |
   | [HowTo and FAQ changes](https://developers.google.com/search/blog/2023/08/howto-faq-changes) (blog, August 2023) | — | From August 2023, FAQ rich results were limited to “well-known, authoritative government and health websites”; since September 13, 2023, How-to rich results are no longer shown and the type “is now deprecated”. |
   | [Simplifying the search results page](https://developers.google.com/search/blog/2025/06/simplifying-search-results) (blog, June 2025) | — | Special Announcement is among the types that “will no longer be supported in Google Search results”. |
   | [Event](https://developers.google.com/search/docs/appearance/structured-data/event) | 2026-09-08 | Each event needs “a unique URL (a leaf page)”; Google “only supports pages that focus on a single event” and recommends event pages over “pages that list schedules or multiple events”. “Events must take place in a physical location.” |
   | [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) | 2025-12-10 | “There's also no special schema.org structured data that you need to add” to appear in AI Overviews or AI Mode; structured data should match the visible text. |
   | [General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | 2026-07-10 | “Don't mark up content that is not visible to readers of the page.” No rich result “for time-sensitive content that is no longer relevant.” |
   | [Organization](https://developers.google.com/search/docs/appearance/structured-data/organization) | 2026-09-08 | “There are no required properties”; Google recommends adding the relevant ones (its example includes `url`, `sameAs`, `logo`, and `name`). Markup on the homepage helps Google “disambiguate your organization in search results”. |

3. **Visible content.** Each candidate type was matched against the content recorded in the answer map and the structure inventory (Step 2 parts A and B), and the meeting and event pages were checked live on 2026-11-26.

## Results

[`structured-data-opportunities.csv`](structured-data-opportunities.csv) lists ten types with their Google status, the matching visible content, the current markup, and the AEO assessment.

| Type | Google Search status (2026-11-26) | AEO assessment |
| --- | --- | --- |
| `FAQPage` | No longer shown since May 7, 2026 | No Google feature to gain; visible question-and-answer structure matters instead |
| `HowTo` | Deprecated in 2023 | No markup; use visible numbered lists |
| `Event` | Supported, for single-event pages at a physical location | Not available with the current design (every event is on a list page); an option only if NITA publishes one page per meeting or hearing |
| `GovernmentService` | Not a Google feature | Not an AEO priority |
| `Organization` / `GovernmentOrganization` | Supported | Covered by `SEO-NITA-016` and `SEO-MTB-004`; entity naming in GEO |
| `Article` / `NewsArticle` / `BlogPosting` | Supported | Covered by `SEO-NITA-016`; dates help separate RTA-era posts from current answers |
| `BreadcrumbList` | Supported | Present and valid |
| `SpecialAnnouncement` | Phased out in 2025 | No markup |
| `Dataset` | Dataset Search only | Out of scope |
| Q&A, Discussion forum, Profile page | Supported for user content and profiles | Not applicable |

The general conclusion for Step 3: for the question types in the inventory, Google no longer offers answer-specific rich results (FAQ, HowTo), and it states that AI features need no special markup. The AEO value is in the visible content and its structure (Step 2 parts A and B) and in correcting the existing markup (SEO). `Event` is the only new type with a Google feature, and it depends on a page design change.

## Observations from the live check (2026-11-26)

These are notes for Step 3, not findings:

- **Meeting Materials sends public comments to an RTA address.** The page tells readers to “Email communications@nita.illinois.gov by noon the day prior to comment at a meeting”, but the link behind that text is `mailto:communications@rtachicago.org`. Whether the former address still receives mail cannot be verified in the public scope.
- **The calendar entry for the next board meeting is named “RTA Board Meeting”.** Both Add to Calendar links on Meeting Materials (Google Calendar and the `.ics` file) use the title “RTA Board Meeting: December 10, 2026”, with the correct time (9:00 a.m. Chicago time) and address.
- **The public meetings table lists past events as upcoming.** On 2026-11-26, “Upcoming public meetings on transit service” still lists the Pace ReVision events of November 23 (Joliet) and November 24 (Blue Island), and a note on Metra at “CTA events on 11/9, and 11/14”. The other four events are in the future.

## Files

`jsonld_types.py`, `jsonld-types-aeo-additions.csv`, `structured-data-opportunities.csv`.
