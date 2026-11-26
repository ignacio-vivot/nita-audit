# Answer Engine Optimization (AEO) — mytransitbenefit.com

## Assessment Scope

- **Website:** [mytransitbenefit.com](https://www.mytransitbenefit.com/)
- **Review date:** 2026-11-25 to 2026-11-26 (in progress)
- **Pages, templates, or journeys reviewed:** 15 inventoried questions for employees and employers ([inventory](../../../evidence/aeo/2026-11-25/question-inventory.csv)); all four pages ([homepage](https://www.mytransitbenefit.com/), [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), [Employers](https://www.mytransitbenefit.com/employers)); Google result pages for 6 priority questions.
- **Methods and tools:** Google autocomplete and “People also ask” captures ([Step 1 evidence](../../../evidence/aeo/2026-11-25/README.md)); answer map, structure inventory, and program-name counts built from the page HTML ([Step 2 parts A and B](../../../evidence/aeo/2026-11-25/README.md#step-2-part-a--answer-map)); Google answer-feature capture ([Step 2 part C](../../../evidence/aeo/2026-11-26/answer-features/README.md)); structured data check against Google's documentation ([Step 2 part D](../../../evidence/aeo/2026-11-26/structured-data/README.md)); priority answer assessment ([Step 3 part A](../../../evidence/aeo/2026-11-26/step3a/README.md)). SEO evidence is reused as listed in the [work plan](aeo-audit-plan.md#what-seo-already-collected-and-how-aeo-reuses-it). The review is AI-assisted: Claude collects and analyzes the evidence, and the team reviews each part.
- **Control checklist:** [AEO review matrix](aeo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** Steps 1 and 2 of the [AEO work plan](aeo-audit-plan.md) are complete, and Step 3 part A (direct answers and answer clarity) has produced two findings. The website has a direct answer passage for three of the six priority questions (the 2026 limits, parking, and whether employers must offer the benefit, although the last is outdated, `SEO-MTB-008`), but it states the monthly limit and the savings figures differently from page to page (`AEO-MTB-001`), and no page opens with a short statement of what the program is and who runs it (`AEO-MTB-002`). In Google on 2026-11-26, My Transit Benefit appeared only for enrollment and the employer law (ranks 5, 6, and 8) and was a listed source in two of six AI Overviews; national and federal sources answered the general benefit questions. The outdated description of the employer law is recorded in SEO (`SEO-MTB-008`). Steps 3B to 3D (missing answers and FAQ content, structure, structured data) are pending.

## Findings

### The monthly limit and the savings figures are stated differently across pages

- **Finding ID:** AEO-MTB-001
- **Page or component:** Benefit figures on the [homepage](https://www.mytransitbenefit.com/), [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), and [Employers](https://www.mytransitbenefit.com/employers).
- **Priority:** Medium
- **Evidence:** Page text of 2026-11-25 ([page text](../../../evidence/aeo/2026-11-25/answer-map/page-text/); [answer map](../../../evidence/aeo/2026-11-25/answer-map/answer-map.csv), `Q-MTB-03`, `Q-MTB-04`, `Q-MTB-14`):

  | Figure | Behind the Benefits and Employees | Homepage and Employers |
  | --- | --- | --- |
  | Monthly limit | “for 2026, the monthly amount is $340 for transit and $340 for parking” (Behind the Benefits); “You can set aside up to $340 for transit and $340 for parking, per month” (Employees) | “set aside pre-tax income, up to $340 each month” (homepage, employer box); “set aside pre-tax income, up to $340 each month, for parking and transit fares on CTA, Metra, and Pace” (Employers) |
  | Savings | “save up to 40% annually on their commuting costs” (Behind the Benefits); “save up to 40 percent through reduced taxes” (Employees) | “Up to 7.65% in savings.” (homepage, employer box); “Estimated Total Tax Rate: 8.45%” in the Employers savings calculator; “Save 40% with pre-tax deductions.” (homepage, employee box) |

  No page explains what the 7.65% and 8.45% rates represent or how the “up to 40%” figure is reached. On 2026-11-26 the AI Overview for “transit benefit limit 2026” gave $340 a month for transit and a separate $340 for parking, citing federal and HR sources; no My Transit Benefit page appeared in the results ([answer-feature capture](../../../evidence/aeo/2026-11-26/answer-features/answer-features-summary.csv)).
- **Impact:** The limit is the first fact employees and employers look for. The homepage and Employers wording reads as one combined $340 limit for transit and parking, half of what an employee can set aside when both benefits are used, while two other pages give the separate limits. Unexplained percentages (7.65%, 8.45%, 40%) make the savings claim harder to trust and harder for answer systems to quote correctly.
- **Recommendation:** Use one sentence for the limit on every page, for example “In 2026 you can set aside up to $340 a month for transit and a separate $340 a month for parking”, and update it each January. Explain the savings figures where they appear: label the 7.65% as the employer's payroll tax savings, explain the calculator's tax rate, and support “up to 40%” with a short worked example or replace it with the calculator result. Confirm the figures with the program team before publishing.
- **Implementation complexity:** Low (content edits on four pages)
- **Related standard:** [Google Search Central: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

### No page opens by saying what the program is and who runs it

- **Finding ID:** AEO-MTB-002
- **Page or component:** Opening content of the [homepage](https://www.mytransitbenefit.com/), [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), and [Employees](https://www.mytransitbenefit.com/employees).
- **Priority:** Low
- **Evidence:** On 2026-11-25 ([heading outlines](../../../evidence/aeo/2026-11-25/structure/heading-outlines.md); [structure inventory](../../../evidence/aeo/2026-11-25/structure/structure-inventory.csv)) every page went from the H1 straight to another heading, with no opening passage:
  - Homepage: H1 “NITA Pre-Tax Transit Benefits Program. Enroll Now and Save.”, H3 “Discover the Future of Commuting in Chicagoland!”, then “How the Program Works”, which explains Section 132(f) of federal tax law rather than the program.
  - Behind the Benefits: H1 “A Deep Dive into The Heart of Our Program.”, then “About Transit Benefits”, the same Section 132(f) paragraph.
  - Employees: H1 “Your Tax Savings Starts Here!”, H3 “Simplify Your Commute and Save Big!”.
  Only Employers opens with a description, written for employers. No page says in one passage that the program is run by the Northern Illinois Transit Authority for employers and employees in the six-county region. The pages also name the program four different ways (“NITA Transit Benefit Fare Program”, “Transit Benefit Program”, “Transit Fare Benefit”, and “RTA/NITA Transit Benefit”), none of which matches the domain name, My Transit Benefit ([term counts](../../../evidence/aeo/2026-11-25/structure/term-usage.csv)). On 2026-11-26 Google showed no My Transit Benefit page for the general questions “how does pre tax transit benefit work”, “transit benefit limit 2026”, and “can you use transit benefits for parking”. For “how to enroll in transit benefits chicago”, CTA's “Transit Benefit Fare Program” page ranked first and the homepage fifth, and the AI Overview named both a “CTA Transit Benefit Fare Program” and a “NITA Transit Benefit Program” ([answer-feature capture](../../../evidence/aeo/2026-11-26/answer-features/answer-features-summary.csv)).
- **Impact:** Employees who arrive from search, and answer systems that summarize the website, find slogans and a general description of federal tax law instead of a short identification of the program. With a similarly named CTA program in the same results, it is harder to tell which program this is and whether it applies to a given employer.
- **Recommendation:** Add a two- or three-sentence opening under the H1 of the homepage and Employees page that says what the program is, who runs it (NITA, formerly the RTA), and who can use it, using one program name consistently. Confirm the wording with the program team and align it with the entity description reviewed in GEO and the organization markup in `SEO-MTB-004`.
- **Implementation complexity:** Low (content edits)
- **Related standard:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)

## Positive Observations

- **The 2026 limits are correct where they are stated in full.** Behind the Benefits and Employees give the separate $340 monthly limits for transit and parking, which match the federal limit cited in Google's AI Overview on 2026-11-26.
- **Employees answers the parking question directly.** The “How you save” section states in its first sentences that employees can set aside money for transit and for parking.

## Limitations

- Search features (“People also ask”, AI Overviews, autocomplete, result pages) were captured through a US connection with a Chicago, Illinois IP address; Google returned US results that were not localized to Chicago, and results vary by date, device, and personalization. The captures are qualitative, from single sessions, and carry no search volume.
- Search Console and analytics are outside the agreed scope, so actual queries, featured-snippet ownership over time, and clicks cannot be measured.
- The savings calculators run in JavaScript; only their labels and default values in the HTML were reviewed.
