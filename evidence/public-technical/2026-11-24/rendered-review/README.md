# Rendered review of the sample pages — 2026-11-24 (SEO Step 3, part B)

Scope: the 16 NITA and 4 My Transit Benefit sample pages listed in the [SEO review matrix](../../../../docs/audit/02-seo/seo-review-matrix.md#page-level-review-scope) (`urls.txt`).

Method:

1. **Raw HTML.** Each URL was downloaded with curl 8.7.1 (desktop Chrome user agent) at the time in `raw-html/fetched-at.txt` (about 15:30 UTC). Files are in `raw-html/`. `extract_seo.py` (Python standard library only) extracts the language, title, meta description, robots, canonical, `hreflang`, Open Graph tags, headings, JSON-LD block count, internal and external link counts, word counts, iframes, and forms into `raw-extract.jsonl`.
2. **Rendered page.** Each URL was opened in the Claude desktop app's built-in browser (Chromium) between 15:35 and 15:42 UTC. After a 4-second wait for scripts, `raw_vs_rendered.js` re-fetched the page's raw HTML in the same browser, parsed it without running scripts (`DOMParser`), extracted the same fields from both versions, and listed every field that differs. `rendered_extract.js` was used first on the homepage, Riders, and How to ride; it also records the language switcher options.
3. **Language switcher.** On one page the Weglot switcher was set to Español and the URL, `lang`, title, H1, canonical, and `hreflang` were recorded; the browser was then switched back to English. Translated URL patterns were tested with curl and dig.

Files:

- `raw-vs-rendered.csv` — one row per page: check time, rendered H1s, internal and external links, words, images, JSON-LD blocks, and the fields that differ between raw and rendered HTML. The only difference on any page is a 2–3 word increase in body text from script-inserted interface text; titles, descriptions, robots, canonicals, `hreflang` (none), headings, links, images, and JSON-LD are identical.
- `raw-extract.jsonl` — fields extracted from the raw HTML. Word counts from the Python parser and the browser differ slightly because they tokenize text differently; compare within one source only.
- `weglot-check.txt` — Weglot script and switcher, absence of `hreflang`, translated URL tests, and the Español switch result (`SEO-NITA-021`).
- `nita-multiple-h1.csv` — the 25 NITA URLs with more than one H1 in the 2026-11-19 crawl (from the read-only `h1_all.csv` batch exports), with page type, indexability, and live confirmation where checked.
- `h1-live-checks.txt` — all H1s of the NITA pages with three or more H1s (curl, 2026-11-24) and the two empty H2 elements on How to ride.

Limits: one fetch per page at one point in time; the homepage slider content changes as announcements are added. The rendered check uses a desktop-size browser window; mobile rendering is reviewed in part C.
