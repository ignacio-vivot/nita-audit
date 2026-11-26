# AEO Step 2 part C — answer-feature capture (2026-11-26)

Evidence for Step 2 part C of the [AEO work plan](../../../../docs/audit/03-aeo/aeo-audit-plan.md): what Google shows for the 20 priority questions of the [question inventory](../../2026-11-25/question-inventory.csv), which sources it uses, and how that compares with the websites' own answers in the [answer map](../../2026-11-25/answer-map/answer-map.csv).

All captures ran through a US connection with a Chicago, Illinois IP address (`connection.txt`: ipinfo.io reports Chicago, Illinois, US; AS11878 tzulo, inc.) with US English settings (`hl=en&gl=us&pws=0`). Google returned US results that were not localized to Chicago. The captures are a qualitative sample from one session on 2026-11-26 between 11:40 and 11:41 UTC. They are not rank tracking, and AI Overviews and results change between searches.

## Method

1. **Queries.** One query per priority question, using the wording people search with: an autocomplete suggestion from Step 1 or the SEO capture of 2026-11-24, or a “People also ask” question, with “chicago” added where the suggestion had no place ([`queries.tsv`](queries.tsv)).
2. **Capture.** Each query was opened in the Claude desktop app's built-in browser (Chromium, not signed in). A browser script waited up to six seconds for an AI Overview, clicked “Show more” when present, and recorded the overview text (first 2,200 characters), the source labels Google shows for it, any featured snippet (detected by Google's “About featured snippets” label), the “People also ask” questions, and the title and displayed URL of the first organic results ([`google-answer-features-2026-11-26.jsonl`](google-answer-features-2026-11-26.jsonl)). The saved file was checked against the browser's stored copy: the length of every record and every overview text matches.
3. **Summary.** [`summarize_answer_features.py`](summarize_answer_features.py) joins the capture with the queries and the answer map and writes [`answer-features-summary.csv`](answer-features-summary.csv): whether an AI Overview or featured snippet appeared, where NITA or My Transit Benefit pages rank (matched on the displayed URL), whether the AI Overview lists them as a source (matched on the source labels), the other sources, the answer-map status, and a reviewer note comparing the overview with the website.

   `python3 -I summarize_answer_features.py`

Limits: the organic list skips results without a standard title link (videos, forum carousels), so ranks are positions among standard results. Source labels are the names Google displays, not resolved URLs. Overview text longer than 2,200 characters is cut.

## Results

| Measure | NITA (14 questions) | My Transit Benefit (6 questions) |
| --- | --- | --- |
| AI Overview shown | 14 | 6 |
| Featured snippet shown | 0 | 0 |
| “People also ask” shown | 12 | 6 |
| Own website among the first organic results | 13 (first on 6) | 3 (ranks 5, 6, and 8) |
| Own website listed as an AI Overview source | 12 | 2 |

NITA ranks first for the Reduced Fare application and renewal, Ride Free renewal, Ride Safe, “what is NITA”, and the 2027 budget. It is not in the first results for Metra fares, where Metra's pages hold six of the first eight results. My Transit Benefit does not appear for the three general employee questions (how the benefit works, the 2026 limit, parking), which national and federal sources answer.

## Observations for Step 3

These are notes, not findings:

- **AI Overviews replace featured snippets.** Every query showed an AI Overview and none showed a featured snippet. Answer extraction for these questions now happens mainly in AI Overviews, which combine several sources.
- **Where NITA has a clear page, Google uses it.** Ride Safe (a definition, steps, and a plain-text FAQ) ranks first and supplies every NITA statement in its overview. The 2027 budget page ranks first and the overview gives the correct comment deadline and board date.
- **Where NITA's answer is weak, other sources fill the gap.** For seniors (scattered on NITA), the overview combines CTA, NITA, the 44th Ward, and CHI 311. For trip planning, it cites only CTA and gives the NITA Travel Information Center hours from CTA's site. For employee enrollment (missing on My Transit Benefit), it uses employer and university pages.
- **Conflicting website facts reach the overviews.** Two overviews captured in the same session give different hours for the ADA Paratransit certification line: 8:30 AM to 5:00 PM (for “how to apply for ada paratransit chicago”) and 8:00 AM to 5:00 PM (for “paratransit chicago phone number”). NITA's pages give both times (`SEO-NITA-027`).
- **The RTA name and RTA-era documents shape the answers.** For the Reduced Fare application, the overview names the “Regional Transportation Authority (RTA/NITA) Reduced Fare Permit”, gives the mailing address “Regional Transportation Authority, PO Box 301150” from the RTA-branded application PDF, and asks whether the user meant another agency's RTA (Greater Dayton or Riverside). For renewals, the results include the RTA-era press release and the 2022 RTA blog post on the online portal, and the overview cites a 2018 CHI 311 page.
- **“People also ask” is not local for RTA queries.** For both Reduced Fare queries, three of the four questions are about New York or New Jersey (OMNY, NJ Transit).
- **Unanswered questions surface in Google.** For “what is nita in illinois”, “People also ask” shows “What is the Nita tax in Illinois?” and “What is the Nita Act?”, which the answer map recorded as missing and scattered on NITA. (Step 3 part B later found the tax question answered, with outdated rates, on Moving the system and changed it to conflicting.)
- **My Transit Benefit is named inconsistently in answers.** The enrollment overview cites it as “NITA Transit Benefit Program” next to a “CTA Transit Benefit Fare Program”. For the employer law, the overview uses the name “Transportation Benefits Program Act”, “50 or more covered employees”, and says it took effect on January 1, 2024, while the Employers page says “Transit Benefits Program Act”, “more than 50”, and that it “goes into effect on January 1, 2024” (`SEO-MTB-008`).

## Correction to Step 2 part A

While reviewing the “what is nita in illinois” capture, the answer-map row for `Q-NITA-29` was found to be wrong: About NITA does name the NITA Act, as a link to the Public Act 104-0457 PDF in its Leadership section. The row was corrected on 2026-11-26 in [`build_answer_map.py`](../../2026-11-25/answer-map/build_answer_map.py) and [`answer-map.csv`](../../2026-11-25/answer-map/answer-map.csv). The status (scattered) does not change, because the page still does not say what the act does or when the RTA became NITA.

## Files

`connection.txt`, `queries.tsv`, `google-answer-features-2026-11-26.jsonl`, `summarize_answer_features.py`, `answer-features-summary.csv`.
