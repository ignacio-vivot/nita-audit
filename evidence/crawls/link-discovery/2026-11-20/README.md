# NITA internal links to non-200 URLs — 2026-11-20 (SEO Step 2, part B)

The 2026-11-19 link-discovery run recorded only the first page linking to each URL. This run records **every** internal link that points to a URL returning a non-200 status, so broken links can be counted and traced to their pages.

- **Script:** [`link_edges.py`](link_edges.py) (Python 3.13 standard library only).
- **Command:** `python3 -I link_edges.py ../2026-11-19/nita-illinois-gov/pages.csv nita-broken-link-edges.csv 0.3`
- **Input:** the 1,609 HTML pages that returned 200 in the 2026-11-19 run; targets are the URLs that returned 404, 403, 301, or 302 in that run.
- **Run:** 2026-11-20, sequential requests with a 0.3-second delay; no fetch errors.
- **Output:** `nita-broken-link-edges.csv` — source page, raw `href`, resolved target, target status, and anchor text. 8,471 links: 8,096 to internal 302 redirects (mostly global navigation shortcuts to external tools and partner websites), 203 to 301 redirects, 170 to 404 URLs, and 2 to 403 URLs.

Link status reflects the 2026-11-19 run; spot checks on 2026-11-20 are in [`step2b-live-checks.txt`](../../../public-technical/2026-11-20/step2b-live-checks.txt).
