# NITA link discovery — 2026-11-19 (crawl baseline run B1)

Part of the Step 1 crawl baseline described in the [SEO work plan](../../../../docs/audit/02-seo/seo-audit-plan.md#crawl-baseline-method). It establishes which NITA URLs are reachable through internal links, which the free Screaming Frog version could not do within its 500-URL limit.

## Method

- **Script:** [`link_discovery.py`](link_discovery.py) (Python 3.13 standard library only).
- **Command:** `python3 -I link_discovery.py https://nita.illinois.gov/ nita-illinois-gov 0.4`
- **Run:** 2026-11-19, finished 16:54 (UTC−3). 1,730 HTML URLs requested; queue empty at the end (the crawl completed, below the 4,000-page safety cap).
- **Behavior:** starts at the homepage and follows every internal `<a href>` with no depth limit. Internal links are queued as HTTPS; the scheme used in the original link is recorded in `link_scheme`. Redirects are not followed automatically: the redirect is recorded and its internal target is queued. HTML pages are fetched with GET; internal links with document or image extensions are checked with HEAD; external links are recorded but not requested. Public `robots.txt` Disallow rules are respected. Requests are sequential with a 0.4-second delay. User agent: `Mozilla/5.0 (compatible; seo-audit-link-discovery/1.0)`.
- **Not covered:** JavaScript-generated links, `<link>`/`<script>`/`<img>` resources, forms, and external link status.

## Files

| File | Content |
| --- | --- |
| `nita-illinois-gov/pages.csv` | Every internal HTML URL requested: crawl depth, first page that linked to it, link scheme, status, content type, redirect location, canonical, and title. |
| `nita-illinois-gov/links_resources.csv` | 1,004 internal document/image links with HEAD status and redirect location. |
| `nita-illinois-gov/links_external.csv` | 2,184 unique external links and the first page linking to each (not requested). |
| `nita-illinois-gov/summary.txt` | Run parameters and totals. |

## Summary of results

These are raw observations for Step 2 analysis, not findings.

- **Status:** 1,609 pages returned 200, 63 returned 301, 6 returned 302 (external tools and partner sites), 50 returned 404, and 2 returned 403.
- **Depth:** maximum crawl depth is 66. Older blog posts and press releases are reachable only through sequential “next page” pagination; 83 URLs are 60 or more clicks from the homepage.
- **Sitemap coverage:** only 6 of the 1,286 sitemap URLs were not reached through links (`/404`, `/blog/uncategorized`, `/regsitehub`, `/ridersurvey26`, `/saveada`, `/take-action`). The large gap seen in the 2026-11-16 Screaming Frog crawl was a crawl-coverage artifact, not a website problem.
- **Linked but not in the sitemap:** 450 HTML URLs, mostly tag archives (155), blog and press-release listing pages, and legacy paths that redirect or return 404.
- **Broken internal links (404):** 50 URLs. Most are in historical blog posts and press releases (legacy `rtachicago.org` and `/index.php/...` paths, links missing `https://`, an email address used as a link, and about 20 posts whose links end in an encoded backslash `%5C`). Some are linked from current pages, for example `/riders/getaccess.org` from [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) and `/region/coalition` from `/communities/coalition`.
- **Malformed links (403):** two links that contain leftover word-processor hyperlink code (`%22%20/t%20%22_blank`, `HYPERLINK`).
- **Internal documents:** 1,004 links; 861 returned 200, 141 returned 301 (all 141 redirect to an `http://` URL), and 2 PDFs returned 404.
- **HTTP-scheme links:** two internal HTML links use `http://`.
