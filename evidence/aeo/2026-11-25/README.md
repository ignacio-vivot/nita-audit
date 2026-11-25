# AEO Step 1 — question inventory and sample (2026-11-25)

Evidence for Step 1 of the [AEO work plan](../../../docs/audit/03-aeo/aeo-audit-plan.md): the question inventory, the sources behind it, and the proposed page sample. All search captures ran through a US connection with a Chicago, Illinois IP address (`connection.txt`) and US English settings; Google returned US results that were not localized to Chicago. Qualitative only: no search volume, no rank tracking.

## Method

1. **Autocomplete.** [`autocomplete_questions.py`](autocomplete_questions.py) requested Google autocomplete suggestions (`hl=en&gl=us`) for 48 question-style seed phrases grouped by audience ([`question-seeds.tsv`](question-seeds.tsv)); results in `autocomplete-questions-2026-11-25.csv` (250 suggestions). The SEO capture of 2026-11-24 ([`autocomplete-2026-11-24.txt`](../../public-technical/2026-11-24/content-review/autocomplete-2026-11-24.txt)) was also used.
2. **“People also ask”.** Seventeen Google result pages (`hl=en&gl=us&pws=0`) were opened in the Claude desktop app's built-in browser (Chromium, not signed in) on 2026-11-25 (see `connection.txt` for the start time); a browser script recorded whether an AI Overview was shown, the “People also ask” questions, and the site and title of the first results (`google-paa-2026-11-25.jsonl`; 60 questions). The seven result pages captured for SEO on 2026-11-24 ([`search-sample-2026-11-24.md`](../../public-technical/2026-11-24/content-review/search-sample-2026-11-24.md)) were also used.
3. **Questions already on the websites.** [`question_headings.py`](question_headings.py) fetched the 60 NITA core pages and the 4 My Transit Benefit pages listed in `core-urls.txt` (raw HTML kept in `html/`) and recorded every H1–H4 heading and accordion label (`<summary>`), flagging question-style text (`page-headings.csv`; 652 elements, 52 question-style: 48 on NITA, 4 on My Transit Benefit). Question-style H2s on all 1,613 NITA HTML pages were taken from the 2026-11-19 crawl's `h2_all.csv` exports (`crawl-question-h2.csv`; 71, mostly blog posts; the free crawler exports only the first two H2s per page).
4. **Inventory.** The questions were consolidated into [`question-inventory.csv`](question-inventory.csv): 42 for NITA and 15 for My Transit Benefit, grouped by audience and topic, each with its sources and the page expected to answer it. Twenty are marked for the answer-feature sample in Step 2 part C (14 NITA, 6 My Transit Benefit).
5. **Sample.** [`proposed-sample.csv`](proposed-sample.csv) lists the 20 SEO sample pages plus 12 NITA pages and 2 application PDFs that are expected to answer inventory questions but were not in the SEO sample.

## Observations for later steps

These are notes for Step 2, not findings:

- **Google features are common.** An AI Overview appeared on 16 of the 17 result pages; “People also ask” appeared on 15.
- **Riders search with the RTA name.** Suggestions include “how to apply for rta reduced fare permit”, “how do i renew my rta reduced fare permit”, and “rta transit benefit card”. This matches `SEO-NITA-028`.
- **Some questions lack local suggestions.** Several riders' questions return no autocomplete suggestions specific to the Chicago region (“can veterans ride cta free”, “how to get senior bus pass chicago”). The questions themselves still appear in “People also ask” (“How do I get a senior CTA pass in Chicago?”).
- **Retired domains still appear in results.** Google still lists `ridertools.metrarail.com` for “metra fares”, although that domain no longer responds (`SEO-NITA-018`).
- **The NITA core pages already contain some question-style sections.** Examples are “Who is eligible?” and “How do I get Access?” on Access, “How to renew Ride Free Permits”, and “What is NITA Ride Safe?”. They also include accordion FAQs on Access and the Privacy Policy.

## Files

`connection.txt`, `question-seeds.tsv`, `autocomplete_questions.py`, `autocomplete-questions-2026-11-25.csv`, `google-paa-2026-11-25.jsonl`, `core-urls.txt`, `question_headings.py`, `page-headings.csv`, `html/`, `crawl-question-h2.csv`, `question-inventory.csv`, `proposed-sample.csv`.
