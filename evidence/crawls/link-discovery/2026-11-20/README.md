# NITA internal links to non-200 URLs — 2026-11-20 (SEO Step 2, part B)

The 2026-11-19 link-discovery run recorded only the first page linking to each URL. This run records **every** internal link that points to a URL returning a non-200 status, so broken links can be counted and traced to their pages.

- **Script:** [`link_edges.py`](link_edges.py) (Python 3.13 standard library only).
- **Command:** `python3 -I link_edges.py ../2026-11-19/nita-illinois-gov/pages.csv nita-broken-link-edges.csv 0.3`
- **Input:** the 1,609 HTML pages that returned 200 in the 2026-11-19 run; targets are the URLs that returned 404, 403, 301, or 302 in that run.
- **Run:** 2026-11-20, sequential requests with a 0.3-second delay; no fetch errors.
- **Output:** `nita-broken-link-edges.csv` — source page, raw `href`, resolved target, target status, and anchor text. 8,471 links: 8,096 to internal 302 redirects (mostly global navigation shortcuts to external tools and partner websites), 203 to 301 redirects, 170 to 404 URLs, and 2 to 403 URLs.

Link status reflects the 2026-11-19 run; spot checks on 2026-11-20 are in [`step2b-live-checks.txt`](../../../public-technical/2026-11-20/step2b-live-checks.txt).

## External links — SEO Step 2, part F

- **Status script:** [`external_link_check.py`](external_link_check.py) (Python 3 standard library). Command: `python3 -I external_link_check.py ../2026-11-19/nita-illinois-gov/links_external.csv nita-external-link-status.csv 0.2`. Each of the 2,184 unique external URLs found in the 2026-11-19 run is requested with HEAD and, if HEAD fails or returns 4xx/5xx, again with GET; redirects are followed; browser-like user agent with the suffix `seo-audit-link-check`; 20-second timeout; 0.2-second delay. Run on 2026-11-20 from Buenos Aires, Argentina.
- **Status output:** `nita-external-link-status.csv` — URL, first NITA page linking to it, final status (0 = no HTTP response), final URL after redirects, method, and error. Result: 1,337 returned 200, 13 returned 202, and 7 ended in a 3xx; 335 returned 403, 219 returned 404, 3 returned 410, 12 returned 400, 4 returned LinkedIn's 999, 6 returned other 4xx/5xx (402, 429, 503, 520), and 248 gave no HTTP response (99 DNS failures, 67 certificate errors, 76 timeouts, 6 refused or TLS errors).
- **Edges script:** [`external_link_edges.py`](external_link_edges.py). Command: `python3 -I external_link_edges.py ../2026-11-19/nita-illinois-gov/pages.csv nita-external-link-status.csv nita-external-broken-link-edges.csv 0.2`. Re-reads the 1,609 HTML pages that returned 200 in B1 and records every `<a href>` whose resolved URL had status 0 or ≥ 400 in the status file, with anchor text.
- **Edges output:** `nita-external-broken-link-edges.csv` — source page, raw `href`, target URL, target status, error, and anchor text.

Automated status codes are not conclusive for external websites: many return 403, 400, 999, or time out for scripts while working in a browser, and some block requests by country. Representative results were checked in a browser on 2026-11-20; see the SEO review matrix log and `SEO-NITA-018`.
