# GEO Step 1 — fact sheet, prompt set, and platform plan (2026-11-26)

This folder holds the evidence for Step 1 of the [GEO work plan](../../../docs/audit/04-geo/geo-audit-plan.md):
- the official facts that generative answers will be scored against;
- the prompts to send to the platforms;
- which platforms can be tested, and how.

The fact sheet and the prompt set need the team's approval before Step 2 part C (the platform answer sample).

## Fact sheet

[`fact-sheet.csv`](fact-sheet.csv) lists 33 facts: 25 for nita.illinois.gov and 8 for mytransitbenefit.com. Each fact gives:
- the official URL that states it;
- the repository evidence it was checked against;
- the related AEO inventory questions;
- any conflict found on the websites.

Every fact was already checked during the SEO and AEO reviews on 2026-11-24 to 2026-11-26, as follows:
- **Fares:** checked against CTA, Pace, and Metra ([`fare-check.txt`](../../public-technical/2026-11-24/content-review/fare-check.txt)) and against metra.com/rdp for the Regional Day Pass.
- **NITA sales tax:** checked against the Illinois Department of Revenue bulletin FY 2026-34.
- **NITA Act dates:** checked against NITA's board summary of the act.
- **Paratransit trip purpose:** checked against 49 CFR 37.131(d).
- **Program rules on My Transit Benefit:** checked against the employer Account Setup Guide.
- **Everything else:** checked against the page text of 2026-11-25. The pages cited were fetched again on 2026-11-26 with no change ([AEO Step 3 part C recheck](../../aeo/2026-11-26/step3c/live-recheck.txt)).

Where the websites disagree with each other or with an official source, the conflict is recorded in the `conflict_or_note` column and not resolved by the reviewer. Examples are the ADA Paratransit call hours, the collar-county tax rate, the board meeting pattern, the FOIA contact details, the transit benefit limit wording, and the employer law threshold. An AI answer that repeats either side of such a conflict will be scored as “conflicting source”, not as wrong.

## Prompt set

[`prompt-set.csv`](prompt-set.csv) lists 40 prompts: 29 for NITA and 11 for My Transit Benefit. Each is linked to the facts it tests and to the AEO question it comes from.

| Type | NITA | My Transit Benefit |
| --- | --- | --- |
| Entity (what the agency or program is, the RTA transition) | 3 | 1 |
| Task (fares, permits, paratransit, safety, budget, meetings, FOIA, enrollment, employer law) | 20 | 8 |
| Comparison (programs or agencies people confuse) | 2 | 1 |
| Spanish and Polish | 4 | 1 |

Rules for the prompts:
- Prompts are worded as people ask AI assistants. Five keep the former name “RTA”, because people still search with it (`SEO-NITA-028`).
- No prompt contains personal or client data.
- Eleven prompts are marked to be run a second time to show how much answers vary.
- Three facts are not asked about directly: the Pace fare, children's fares, and the board size. They are used only to score answers that mention them.

## Platform plan

The start pages were loaded on 2026-11-26 in the built-in browser, not signed in, through a US connection with a Chicago, Illinois IP address ([`platform-access.txt`](platform-access.txt)). No prompt was sent.

| Platform | Available signed out | Mode to use | Notes |
| --- | --- | --- | --- |
| ChatGPT | Yes | Default model with the “Web search” tool on | Deep research needs an account; not used |
| Perplexity | Yes, after an automatic Cloudflare check | “Search” mode | Decline optional cookies when the banner is answered |
| Gemini | Yes | Default (“Auto”) | Signed out, so no Google account history |
| Google AI Mode | Yes | AI Mode, `hl=en&gl=us&pws=0` | AI Overviews already captured in AEO for 35 searches |

Each prompt is run once per platform, in a new conversation, and recorded with:
- the date and time;
- the platform, mode, and any model name shown;
- the answer text and the cited URLs.

The 11 marked prompts are run a second time in a later session. Answers are scored against the fact sheet on four points:
- accuracy: correct, partly correct, wrong, or conflicting source;
- whether a NITA or My Transit Benefit URL is cited;
- whether the cited URL is current;
- whether the answer presents the RTA as the current agency.

With 40 prompts on four platforms, the first pass is 160 answers. The answer sample can therefore be split into parts by platform.

## Limits

- Generative answers change with the model, mode, date, and location. Signed-out sessions see no personal history. The sample shows what these platforms answered on the test dates; it does not measure visibility, share of answers, or traffic.
- Using these platforms means accepting their terms of use; the sample starts only with the team's agreement.

## Files

`fact-sheet.csv`, `prompt-set.csv`, `platform-access.txt`.
