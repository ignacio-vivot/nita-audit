# Content and keyword review — 2026-11-24 (SEO Step 3, part E)

Scope: the 16 NITA and 4 My Transit Benefit sample pages, the content observations listed in the [SEO review matrix](../../../../docs/audit/02-seo/seo-review-matrix.md#public-content-inventory-and-review-priorities), and a small public search-feature sample.

Method:

1. **Page text.** [`extract_text.py`](extract_text.py) converted the raw HTML fetched on 2026-11-24 (`../rendered-review/raw-html/`) to readable text without menus, footer, scripts, and forms, with headings marked and each link written as its text in brackets followed by its address in parentheses (`page-text/`). The text was read in full and every date, deadline, phone schedule, fare, statistic, and program name was noted.
2. **Fares.** Fare tables on Paying for your ride were compared with the operators' pages the same day ([`fare-check.txt`](fare-check.txt)): CTA and Pace read with WebFetch, Metra's fare table read in the built-in browser because metra.com refused the automated request.
3. **Time-sensitive content.** Results in [`time-sensitive-content.txt`](time-sensitive-content.txt).
4. **Safe Links.** The HTML of all 1,609 NITA pages, cached during the internal link crawl ([`../../../crawls/link-discovery/2026-11-24/`](../../../crawls/link-discovery/2026-11-24/README.md)), was searched for Microsoft Outlook Safe Links URLs in any attribute with [`safelinks_scan.py`](safelinks_scan.py); each was decoded to its destination and the mailbox embedded in its `data` parameter ([`safelinks-urls.csv`](safelinks-urls.csv)). The Safe Links URLs on Accessible transit and Ethics & OEIG were requested with curl to confirm they still redirect.
5. **Search language.** Google autocomplete suggestions for 22 seed phrases ([`autocomplete-2026-11-24.txt`](autocomplete-2026-11-24.txt)) and seven Google result pages ([`search-sample-2026-11-24.md`](search-sample-2026-11-24.md)), captured through a US connection with a Chicago, Illinois IP address (ipinfo.io: Chicago, Illinois, US) and US English settings; Google returned US results that were not localized to Chicago. Qualitative only: no search volume, no rank tracking.

Findings: `SEO-NITA-026`, `SEO-NITA-027`, `SEO-NITA-028`, and `SEO-MTB-008`; additional evidence for `SEO-NITA-010`.

Other observations:

- **Program naming:** “Access Program” (reduced fares) and “Access to Transit” (infrastructure grants) are not mixed on each other's pages; the reduced-fare card is called “Access card”, “Access permit”, and “Access Permit” in different places, and Metra calls it the “NITA-issued Access Permit”.
- **Editorial transition:** the On Track blog states that posts before September 1, 2026 were written by the RTA, and current core pages describe older work as done “under its predecessor the RTA”. Related-article excerpts on core pages still show RTA-era posts (`SEO-NITA-025`).
- **Content depth:** of the 71 pages under 200 words in the 2026-11-19 crawl, the core pages are the homepage (178), `/region` (173), `/communities/toolkits-and-education/funding-guide` (133), `/about-nita/transparency` (115), `/about-nita/boards-and-committees/nita-committees` (112), `/investor-relations-sub` (68), and `/404` (40); the rest are posts, press releases, and listings.

Limits: one fetch per page; search results depend on location, time, and personalization; they were captured on one date from a US connection and are not localized to Chicago; partner-site facts (fares, phone hours) were checked on 2026-11-24 only.
