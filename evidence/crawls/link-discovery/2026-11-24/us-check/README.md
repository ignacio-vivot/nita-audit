# External links: US check — 2026-11-24 (SEO-NITA-018)

The 2026-11-20 external link check ([README](../../2026-11-20/README.md)) left 315 URLs (480 links on 85 domains) that could not be confirmed by script or in the browser. On 2026-11-24 they were checked again through a US connection with a Chicago, Illinois IP address (`connection.txt`: ipinfo.io reports Chicago, Illinois, US; AS11878 tzulo, inc.).

## Method

1. **Script.** [`external_link_check.py`](../../2026-11-20/external_link_check.py) (same script and settings as 2026-11-20) on the 315 URLs (`us-check-input.csv`); results in `us-script-status.csv`. 200 is treated as working (after checking that redirects do not land on an unrelated homepage); 404 as not found.
2. **Browser.** The remaining URLs (403, 400, 402, 503, 999, timeouts, connection and certificate errors) were opened in the Claude desktop app's built-in browser (Chromium). Where a website's homepage loaded, its other pending URLs, including PDFs, were requested from that page (same-origin requests), which checks PDFs without downloading them. Bot challenges (Cloudflare, Akamai, paywall checks) and sign-in walls were not bypassed; those URLs stay unverified.
3. **Redirects and DNS.** TinyURL short links were resolved to their destinations, and hosts that did not respond were looked up with `dig`.
4. **Recording.** [`apply_us_check.py`](apply_us_check.py) records each observed result and writes `us-check-results.csv` and `nita-external-links-browser-check-merged.csv` (the 2026-11-20 browser check with the 315 rows updated). [`classify_external_links.py`](../../2026-11-20/classify_external_links.py) was then rerun with the merged file:

   `python3 -I ../../2026-11-20/classify_external_links.py ../../2026-11-20/nita-external-link-status.csv ../../2026-11-20/nita-external-broken-link-edges.csv nita-external-link-classification.csv nita-external-links-browser-check-merged.csv`

Team rule (2026-11-20): a link that opens normally in a browser is working; definitive failures are broken; anything that could not be confirmed stays for review.

## Results

| Result | URLs | Links |
| --- | --- | --- |
| Opens normally (`ok`, one `ok-download`) | 149 | 224 |
| Not found (404), including 37 former RTAMS paths that redirect to a 404 on `datahub.nita.illinois.gov` | 47 | 84 |
| “Access denied” page for content no longer published (28 Pace hearing pages, a NITA Data Hub dataset, a Chicago Park District event) | 30 | 31 |
| Server error or retired domain (`metrarail.com`, `www.metrarail.com`, `ridertools.metrarail.com`: CloudFront 504; `chicago.metromix.com`: 503; one 400 configuration error) | 27 | 45 |
| No response (`rtams.com`, `savetransitnow.org`, `pulse.pacebus.com`, and others) | 16 | 44 |
| Redirects to an unrelated homepage | 3 | 5 |
| 403 Forbidden with no bot challenge | 3 | 3 |
| Domain no longer resolves | 2 | 3 |
| Unverified: bot challenge or paywall check | 25 | 25 |
| Unverified: not opened in the audit browser (`nytimes.com`, `trb.org`, `ebidexchange.com`) | 8 | 10 |
| Unverified: LinkedIn sign-in wall | 4 | 4 |
| Unverified: temporary error (Sched 503) | 1 | 2 |
| **Total** | **315** | **480** |

With these results, `SEO-NITA-018` reports 937 confirmed broken links to 579 URLs on 410 pages (`nita-external-link-classification.csv` in this folder replaces the 2026-11-20 classification for reporting).

Files: `connection.txt`, `us-check-input.csv`, `us-script-status.csv`, `apply_us_check.py`, `us-check-results.csv`, `nita-external-links-browser-check-merged.csv`, `nita-external-link-classification.csv`, and the working lists `inconclusive-urls.txt`, `browser-queue.txt`, `remaining.txt`, `plain-curl.tsv` (second script pass with curl's default settings on the URLs still unresolved).
