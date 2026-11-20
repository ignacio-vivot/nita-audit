# Public technical checks — 2026-11-20

`step2a-live-checks.txt` records raw status lines, redirect locations, headers, and short HTML extracts captured with curl 8.7.1 on 2026-11-20 (12:25 UTC) for SEO Step 2, part A (crawlability and indexability). It covers:

- HTTP-scheme responses on ten NITA URLs across templates (all returned 200 without redirecting) and the `www.` host (redirects to `https://nita.illinois.gov/`).
- The six-hop coalition redirect chain ending in 404.
- Soft 404 candidates: `/404` (200, indexable), out-of-range pagination (200 with canonical to page 1), and a nonexistent URL (404, `robots: none`).
- Status of sitemap-only URLs, trailing-slash variants, and the robots-blocked `/cpresources/` files referenced on a page with a form.
- My Transit Benefit HTTP and non-www redirects on inner pages.

Each check is a single dated fetch; results can change.

`step2b-live-checks.txt` (13:59 UTC) records the raw anchors of broken links on two current pages (`/region` and Paying for your ride), the 404 status of representative broken targets, and candidate destinations for redirects, for SEO Step 2, part B.
