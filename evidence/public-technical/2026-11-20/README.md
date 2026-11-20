# Public technical checks — 2026-11-20

`step2a-live-checks.txt` records raw status lines, redirect locations, headers, and short HTML extracts captured with curl 8.7.1 on 2026-11-20 (12:25 UTC) for SEO Step 2, part A (crawlability and indexability). It covers:

- HTTP-scheme responses on ten NITA URLs across templates (all returned 200 without redirecting) and the `www.` host (redirects to `https://nita.illinois.gov/`).
- The six-hop coalition redirect chain ending in 404.
- Soft 404 candidates: `/404` (200, indexable), out-of-range pagination (200 with canonical to page 1), and a nonexistent URL (404, `robots: none`).
- Status of sitemap-only URLs, trailing-slash variants, and the robots-blocked `/cpresources/` files referenced on a page with a form.
- My Transit Benefit HTTP and non-www redirects on inner pages.

Each check is a single dated fetch; results can change.

`step2b-live-checks.txt` (13:59 UTC) records the raw anchors of broken links on two current pages (`/region` and Paying for your ride), the 404 status of representative broken targets, and candidate destinations for redirects, for SEO Step 2, part B.

`step2c-live-checks.txt` (14:13 UTC) records the `<title>`, meta description, and H1 elements from the raw HTML of representative NITA and My Transit Benefit pages for SEO Step 2, part C. `nita-metadata-review.csv` is derived from the 2026-11-19 NITA crawl baseline (List-mode `internal_all.csv` batches): one row per indexable HTML page (1,358) with page type, title, title pixel width, description, H1s, and flags for ellipsis truncation and duplicate counts.

`sitemaps/` contains raw copies of the NITA sitemap index and its five child sitemaps and the My Transit Benefit sitemap index and child, downloaded on 2026-11-20 (about 15:00 UTC) without editing. `step2d-live-checks.txt` (15:01 UTC) records the status, redirect target, title, robots, canonical, and H1 of sitemap entries not reached through links, and checks for an RTA-period notice on a historical press release and on the blog and press-release indexes, for SEO Step 2, part D.
