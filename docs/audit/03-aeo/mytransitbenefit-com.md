# Answer Engine Optimization (AEO) — mytransitbenefit.com

## Assessment Scope

- **Website:** [mytransitbenefit.com](https://www.mytransitbenefit.com/)
- **Review date:** 2026-11-25 to 2026-11-26 (in progress)
- **Pages, templates, or journeys reviewed:** 15 inventoried questions for employees and employers ([inventory](../../../evidence/aeo/2026-11-25/question-inventory.csv)); all four pages ([homepage](https://www.mytransitbenefit.com/), [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), [Employers](https://www.mytransitbenefit.com/employers)); the employer Account Setup Guide (PDF); Google result pages for 6 priority questions and 3 questions with missing answers.
- **Methods and tools:** Google autocomplete and “People also ask” captures ([Step 1 evidence](../../../evidence/aeo/2026-11-25/README.md)); answer map, structure inventory, and program-name counts built from the page HTML ([Step 2 parts A and B](../../../evidence/aeo/2026-11-25/README.md#step-2-part-a--answer-map)); Google answer-feature capture ([Step 2 part C](../../../evidence/aeo/2026-11-26/answer-features/README.md)); structured data check against Google's documentation ([Step 2 part D](../../../evidence/aeo/2026-11-26/structured-data/README.md)); priority answer assessment ([Step 3 part A](../../../evidence/aeo/2026-11-26/step3a/README.md)); assessment of missing answers with three further Google captures ([Step 3 part B](../../../evidence/aeo/2026-11-26/step3b/README.md)). SEO evidence is reused as listed in the [work plan](aeo-audit-plan.md#what-seo-already-collected-and-how-aeo-reuses-it). The review is AI-assisted: Claude collects and analyzes the evidence, and the team reviews each part.
- **Control checklist:** [AEO review matrix](aeo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** Steps 1 and 2 of the [AEO work plan](aeo-audit-plan.md) are complete. Step 3 part A (direct answers and answer clarity) and part B (question-based content and FAQ opportunities) have produced three findings. The website has a direct answer passage for three of the six priority questions (the 2026 limits, parking, and whether employers must offer the benefit, although the last is outdated, `SEO-MTB-008`). The gaps are:
- it states the monthly limit and the savings figures differently from page to page (`AEO-MTB-001`);
- practical questions about enrolling, the card and Ventra loads, unused funds, and fees are answered only in an employer PDF or not at all, and the three product sections are empty (`AEO-MTB-003`);
- no page opens with a short statement of what the program is and who runs it (`AEO-MTB-002`).

In Google on 2026-11-26, My Transit Benefit appeared for enrollment, the employer law, and the “rta transit benefit card” search, and was a listed source in three of nine AI Overviews checked; national benefit providers and federal sources answered the general benefit questions. The outdated description of the employer law is recorded in SEO (`SEO-MTB-008`). Steps 3C and 3D (structure, structured data) are pending.

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

### Enrollment, card, unused-fund, and fee questions are answered only in an employer PDF or not at all

- **Finding ID:** AEO-MTB-003
- **Page or component:** The product sections of [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), [Employers](https://www.mytransitbenefit.com/employers), and the [Account Setup Guide](https://www.mytransitbenefit.com/uploads/files/general/NITA-TBP-Set-Up-Guide-mk-v2.pdf) (PDF) linked from Employers.
- **Priority:** Medium
- **Evidence:** Page text of 2026-11-25, unchanged on 2026-11-26 ([page text](../../../evidence/aeo/2026-11-25/answer-map/page-text/); [`live-recheck.txt`](../../../evidence/aeo/2026-11-26/step3b/live-recheck.txt)), and the Account Setup Guide fetched on 2026-11-26 ([PDF and text](../../../evidence/aeo/2026-11-26/step3b/mtb-docs/)):
  - Behind the Benefits has three H2 headings, “The RTA/NITA Transit Benefit Prepaid Mastercard®”, “Ventra® Direct Loads”, and “Pace Vanpool”, each followed by an empty panel with no text in the HTML.
  - Employees says only “If your employer doesn’t offer a transit benefit fare program, encourage them to enroll today.” and “Log into your Transit Fare Benefit account to check your balance, order a new card, add more money, and more.” No page says how an employee enrolls, where the card or a Ventra load can be used, when funds become available, or what happens to unused funds or when an employee leaves the job.
  - Employers gives no fees and no sign-up steps; it links the Account Setup Guide.
  - The six-page guide, written for employer administrators, answers most of these questions:
    - the three products and where they work: the card “can only be used to purchase transit fares from qualified transit agencies where Debit Mastercard®, Maestro® cards and NYCE® cards are accepted”, and Ventra Direct Load funds are “for use on the CTA, Pace and Metra”;
    - when funds arrive: “the funds are available for use on the 20th of each month”;
    - balance limits: a $2,000 maximum card balance and a $500 limit for Ventra;
    - fees: “$0.00 per month/order” by ACH debit and “4% of the total order” by credit card;
    - credit-adjustment options for unused funds, including “Not Returned - Returned only upon employee termination”;
    - the sign-up steps.
  - The guide gives the phone number 312-913-5523; the four web pages give 888-782-1008.

  Google result pages captured on 2026-11-26 through a US connection with a Chicago, Illinois IP address ([`question-gaps.csv`](../../../evidence/aeo/2026-11-26/step3b/question-gaps.csv)):

  | Question | Google result page, 2026-11-26 |
  | --- | --- |
  | Do pre-tax transit benefit funds expire? (`Q-MTB-09`, “do pre-tax transit benefits expire”) | No My Transit Benefit page in the first nine results. The AI Overview answers from HealthEquity, ADP, NYC.gov, and a Reddit thread, and says unused funds generally roll over but may be forfeited after leaving a job, depending on the plan |
  | Which transit services can I use it on? (`Q-MTB-08`, “what can you use transit benefits for”) | No My Transit Benefit page in the first seven results; sources are Optum, TRI-AD, Wikipedia, and Reddit |
  | How do I use the card? (`Q-MTB-10`, “rta transit benefit card”) | The homepage ranks first and is cited. The overview's statement on where the card works (“such as CTA, Pace, Metra, South Shore, and Amtrak where supported”) is attributed to NITA. The NITA result is the RTA press release [“RTA to Offer Regional RTA Transit Benefit Prepaid MasterCard®”](https://nita.illinois.gov/about-rta/press-releases/rta-to-offer-regional-rta-transit-benefit-prepaid-mastercard) of November 14, 2013 (rank 4), which lists “CTA, Pace, Metra, South Shore, Amtrak, and Chicago Water Taxi” ([page text](../../../evidence/aeo/2026-11-26/step3b/page-text/press-rta-transit-benefit-prepaid-mastercard.md)) |
  | How do I enroll? (`Q-MTB-06`, “how to enroll in transit benefits chicago”, Step 2 part C) | The homepage ranks fifth and is cited; the overview explains enrollment from CTA, City of Chicago, and Loyola University Chicago sources |
- **Impact:** Employees deciding whether to enroll, and participants with a card or balance question, find empty sections and a login button. The answers they get from search come from national benefit providers, whose rules vary by plan, and from a 2013 press release whose list of agencies may no longer be current. The program's own rules, which are already written in the guide, are not on any web page. Two different support numbers add doubt about whom to call.
- **Recommendation:** Fill the three product sections on Behind the Benefits with short descriptions based on the guide. Add a short block of common questions in plain text:
  - on Employees: how to enroll (check whether your employer participates, then order through the employer or the Employee Login), where the card and Ventra loads work, when funds are available each month, what happens to unused funds and when leaving a job, and how to get help;
  - on Employers: a three- or four-step sign-up summary with the guide as detail, and the fees.

  Confirm every answer and one support phone number with the program team. Add a dated note to the 2013 press release that links to My Transit Benefit. FAQ markup is not needed, because Google stopped showing FAQ rich results on May 7, 2026.
- **Implementation complexity:** Low (content edits on three pages; the content already exists in the guide)
- **Related standard:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)

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
