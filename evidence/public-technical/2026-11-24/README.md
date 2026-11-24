# Public technical checks — 2026-11-24 (SEO Step 3, part A: performance)

PageSpeed Insights (PSI) was run on 2026-11-24 between 8:40 and 9:08 AM (GMT-3) through its web interface at [pagespeed.web.dev](https://pagespeed.web.dev/), opened in the Claude desktop app's built-in browser (Chromium). The keyless PSI API returned "Quota exceeded" that morning, so each URL was analyzed one at a time. PSI runs Lighthouse 13.6.0 on Google's servers (mobile: emulated Moto G Power, Slow 4G throttling; desktop: custom throttling) and shows Chrome UX Report field data for the latest 28 days when Google has enough real-user samples.

Scope: 7 NITA templates (homepage, Riders landing page, Paying for your ride, 2027 regional transit budget, On Track blog index, a 2026 blog post, and the 2026 budget press release) and the 4 My Transit Benefit pages, each in mobile and desktop. Unusual results were repeated: the NITA homepage (both devices) and the My Transit Benefit homepage (mobile).

Files:

- `psi-results.jsonl` — one record per page, device, and run: report link (`href`), field-data scope (`This URL`, `Origin` when the URL has too few samples, or `none`), field metrics (Core Web Vitals assessment, LCP, INP, CLS, FCP, TTFB), lab metrics (performance score, FCP, LCP, TBT, CLS, Speed Index, capture time, emulated device), and the list of Lighthouse insights and diagnostics shown. Values were read from the PSI page text with a script in the browser.
- `psi-details.txt` — expanded audit details for the cases analyzed in the findings: layout-shift culprits, LCP element and breakdown, render-blocking requests, unused JavaScript, image delivery, cache lifetimes, network payloads, and third parties; plus a code inspection of the NITA homepage slider that explains its layout shift.
- `step3a-header-checks.txt` — `curl -sI` response headers for representative static files on both websites (caching headers) and the scripts and iframes in the My Transit Benefit Employers page.

Test location: PSI runs Lighthouse on Google's own servers (Google chooses the region; the report does not show it), not in the requesting browser. On mobile, Lighthouse simulates a slow 4G connection (about 150 ms round-trip time and 1.6 Mbps) and a 4× slower CPU, so the requester's location and connection have little effect on lab results. Field data comes from real Chrome users who visited the pages and is not affected by these tests. The curl header checks and code inspection are not location-dependent. Lighthouse always measures a first visit with an empty cache, so missing cache headers do not change lab scores; they affect repeat and multi-page visits.

PSI report links are kept in each record; Google may expire them. Lab results vary between runs and depend on Google's test location and throttling; field data reflects Chrome users who visited the pages in the previous 28 days.

`rendered-review/` contains the Step 3 part B evidence (raw HTML compared with the rendered page on the 20 sample pages, the Weglot translation check, and heading checks); see its [README](rendered-review/README.md).

`mobile-review/` contains the Step 3 part C evidence (device parity, mobile layout checks at 375 px, accordion tables, and mobile navigation); see its [README](mobile-review/README.md).

`content-review/` contains the Step 3 part E evidence (page text of the 20 sample pages, fare comparison, time-sensitive content, Outlook Safe Links URLs, and the public search-feature sample); see its [README](content-review/README.md).
