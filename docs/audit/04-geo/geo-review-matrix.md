# GEO Review Matrix — NITA websites

Use this matrix to track every review area committed in the [project proposal](../../project-overview.md#24-generative-engine-optimization-geo). It records checks that pass as well as issues. A matrix status is not a finding; findings are created only for evidence-backed issues or opportunities that merit action. Status definitions follow the [authoring guide](../authoring-guide.md#3-review-controls-and-coverage). Method and sequence are in the [GEO work plan](geo-audit-plan.md).

This matrix is the single place for coverage detail and caveats; the site reports link here instead of repeating them.

## Fact sheet

Generative answers are scored against 33 official facts: 25 for nita.illinois.gov and 8 for mytransitbenefit.com ([`fact-sheet.csv`](../../../evidence/geo/2026-11-26/fact-sheet.csv); method in the [Step 1 README](../../../evidence/geo/2026-11-26/README.md)). Each fact cites the official URL that states it and the evidence it was checked against in the SEO and AEO reviews.

Eight facts carry a conflict found on the websites:
- the ADA Paratransit call hours;
- the collar-county sales tax rate;
- the board meeting pattern and location;
- the FOIA contact details;
- the transit benefit limit wording and the savings figures;
- the employer law name and threshold;
- the program support phone number.

These conflicts are recorded, not resolved by the reviewer, and an answer that repeats either side is scored as “conflicting source”. Six more facts are stated only in a PDF, only in an official source outside the website, or without key details on the website: the date NITA replaced the RTA, the paratransit trip-purpose rule, the Travel Information hours, and three program rules in the employer guide.

| Topic | NITA facts | My Transit Benefit facts |
| --- | --- | --- |
| Agency, NITA Act, and tax | 4 | — |
| Fares and passes | 5 | — |
| Reduced Fare, Ride Free, and Access | 5 | — |
| ADA Paratransit, trip planning, and safety | 5 | — |
| Budget, board, contact, FOIA, and People Over Parking Act | 6 | — |
| Program, limits, savings, products, funds, fees, employer law, and contact | — | 8 |

## Prompt set

**Status: proposed on 2026-11-26; awaiting team approval.** The prompts come from the AEO question inventory and are worded as people ask AI assistants ([`prompt-set.csv`](../../../evidence/geo/2026-11-26/prompt-set.csv)):

| Type | NITA | My Transit Benefit |
| --- | --- | --- |
| Entity | 3 | 1 |
| Task | 20 | 8 |
| Comparison | 2 | 1 |
| Spanish and Polish | 4 | 1 |
| **Total** | **29** | **11** |

Eleven prompts are marked to be run twice to show variability. Five keep the former name “RTA”, as people still search with it.

## Platform plan

**Status: proposed on 2026-11-26; awaiting team confirmation.** The platforms are ChatGPT (with web search), Perplexity (Search mode), Gemini, and Google AI Mode. Each is tested signed out in the built-in browser, through a US connection with a Chicago, Illinois IP address, in a new conversation for each prompt. All four were available signed out on 2026-11-26 ([`platform-access.txt`](../../../evidence/geo/2026-11-26/platform-access.txt)). Google AI Overviews are reused from the AEO captures. Using the platforms means accepting their terms of use, so testing starts only with the team's agreement.

## Review controls and current status

| Proposal area / control | What to verify | Primary method and evidence | NITA status | My Transit Benefit status |
| --- | --- | --- | --- | --- |
| Content accessibility for AI-powered search systems | Whether AI crawlers and retrieval systems can reach the content: `robots.txt` rules for AI user agents, server or firewall responses, content only in PDFs or images, translations only in the browser. | Live `robots.txt`; curl with AI crawler user agents; SEO rendering and translation evidence (Step 2 part A). | **Not assessed.** SEO found no `robots.txt` rules for AI crawlers on 2026-11-19, identical raw and rendered HTML, and translations visible only in the browser (`SEO-NITA-021`). | **Not assessed.** SEO found no `robots.txt` rules for AI crawlers on 2026-11-19. |
| Semantic structure and content organization | Whether page structure lets platforms identify services, eligibility rules, and contacts as distinct facts. | AEO structure inventory and answer map; platform answers (Step 3 part B). | **Not assessed.** AEO Step 3 part C assessed headings and names for answer extraction (`AEO-NITA-001`, `008`). | **Not assessed.** AEO recorded the missing opening passage and program names (`AEO-MTB-002`). |
| Structured data and machine-readable information | Whether markup, sitemaps, feeds, and documents describe NITA and the program consistently and in a form machines can read. | SEO JSON-LD; sitemaps; feeds; PDF text extraction; entity sources (Step 2 parts A and B). | **Not assessed.** Existing markup is covered by `SEO-NITA-016`; AEO found no answer-oriented markup to recommend. | **Not assessed.** Existing markup is covered by `SEO-MTB-004`. |
| Content clarity, authority, and contextual relevance | Official status, dates, sources, consistency between pages and with partner sources, and separation of RTA-era content from current guidance. | Fact sheet; entity and source review (Step 2 part B); AEO clarity findings. | **In progress.** Fact sheet built; 4 of its 25 NITA facts carry a conflict already recorded in SEO or AEO findings. | **In progress.** Fact sheet built; conflicts on the limit wording, savings figures, employer law, and support phone are recorded. |
| Opportunities to improve content visibility in AI-generated answers | Topics where platforms cite other sources instead of NITA, or no source. | Platform answer sample (Step 2 part C). | **Not assessed.** Prompt set proposed. | **Not assessed.** Prompt set proposed. |
| Accurate retrieval, summary, and reference by generative platforms | Whether answers are accurate against the fact sheet, cite current official URLs, and treat NITA, not the RTA, as the current agency. | Platform answer sample scored against the fact sheet (Step 2 part C, Step 3 part D). | **Not assessed.** | **Not assessed.** |
| AI crawler visits and citations over time | Which AI crawlers visit, how often, what they receive, and how often answers cite the websites. | Requires server logs and analytics ([access boundary](geo-audit-plan.md#agreed-access-boundary)). | **Not verifiable in public scope.** No server logs or analytics access; public tests show only what a borrowed user agent or a single session receives. | **Not verifiable in public scope.** Same reason. |

## Evidence and review log

| Date | Website | Control(s) reviewed | Method / evidence | Reviewer notes or follow-up |
| --- | --- | --- | --- | --- |
| 2026-11-26 | Both websites | Step 1: fact sheet, prompt set, and platform plan | [Step 1 evidence](../../../evidence/geo/2026-11-26/README.md) | Built a fact sheet of 33 official facts from evidence already checked in SEO and AEO, with 8 recorded conflicts. Drafted 40 prompts from the AEO question inventory, 5 of them in Spanish or Polish. Checked that ChatGPT, Perplexity, Gemini, and Google AI Mode open signed out through a US connection with a Chicago, Illinois IP address; no prompt was sent. Awaiting team approval of the prompt set and the platform plan. |

## Related reports

- [NITA GEO report](nita-illinois-gov.md)
- [My Transit Benefit GEO report](mytransitbenefit-com.md)
- [GEO work plan](geo-audit-plan.md)
