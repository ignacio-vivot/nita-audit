# Search Engine Optimization (SEO) — nita.illinois.gov

## Assessment Scope

- **Website:** [nita.illinois.gov](https://nita.illinois.gov/)
- **Review date:** 2026-11-19
- **Pages, templates, or journeys reviewed:** Crawl-level review of 1,736 URLs (1,613 HTML pages returning 200), combining the 1,286-URL public sitemap with every HTML URL reachable through internal links; dated live header and HTML checks on 2026-11-19; navigation and spot checks across the agreed 15-URL sample listed in the [SEO review matrix](seo-review-matrix.md#page-level-review-scope). Detailed manual evaluation of the sample is in progress.
- **Methods and tools:** link-discovery script with no depth limit ([B1 README](../../../evidence/crawls/link-discovery/2026-11-19/README.md)); Screaming Frog SEO Spider 25.1 free version, List mode, Text Only ([B2 README](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/README.md)); curl 8.7.1 ([`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)); public browser review; Google Search Central guidance.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** The most consequential observation so far is protocol handling: the website serves pages over unencrypted HTTP without redirecting to HTTPS, and 141 internal links to legacy documents redirect to HTTP destinations. Canonical tags point to HTTPS, which limits but does not remove the risk of split signals and unencrypted visits. Paginated listings declare their first page as canonical. Metadata observations are lower priority: 155 tag archive URLs share a brand-only title, and 292 pages share one generic meta description.

The 2026-11-19 crawl baseline replaces the 2026-11-16 crawl, which stopped short of deep pagination ([method](seo-audit-plan.md#crawl-baseline-method)). With complete link discovery, only 6 of the 1,286 sitemap URLs are not reached through internal links; the earlier gap of 1,203 URLs was a crawl artifact. The new baseline also surfaces items for Step 2: 50 internal links returning 404, content up to 66 clicks from the homepage, and malformed links in older posts. This review does not establish rankings, clicks, or Google index status.

## Findings

### HTTP pages load without redirecting to HTTPS

- **Finding ID:** SEO-NITA-003
- **Page or component:** Website-wide protocol handling; observed on the [homepage](http://nita.illinois.gov/) and [Riders](http://nita.illinois.gov/riders) over HTTP.
- **Priority:** Medium
- **Evidence:** On 2026-11-19, `curl -sI` requests to `http://nita.illinois.gov/` and `http://nita.illinois.gov/riders` returned `HTTP/1.1 200 OK` with no `Location` header. The HTTPS homepage returned no `Strict-Transport-Security` header. The HTTP homepage declares `https://nita.illinois.gov/` as canonical. The 2026-11-19 crawl baseline also found two internal links that use `http://` (to a press release and to `/popa`) and two tag archives whose canonical uses `http://` (`/blog/tags/chicago`, `/blog/tags/moving-you`). See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt), [`pages.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/pages.csv), and [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv). By contrast, My Transit Benefit redirects HTTP to HTTPS.
- **Impact:** Every page is available at two protocol versions. Search engines must rely on canonical tags to consolidate them, and links or bookmarks to HTTP URLs keep users on an unencrypted connection. Google's canonicalization guidance states a preference for HTTPS pages as canonical and lists redirects as a strong signal for consolidating duplicate URLs.
- **Recommendation:** Add a website-wide, server-level 301 redirect from HTTP to the equivalent HTTPS URL, then consider adding an HSTS header after the redirects are verified. Update internal links and canonicals that still use `http://`.
- **Implementation complexity:** Low (assumes a server or CDN configuration change; confirm with the hosting team)
- **Related standard:** [Google Search Central: consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) and [redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Legacy document redirects point to HTTP destinations

- **Finding ID:** SEO-NITA-004
- **Page or component:** 141 internal links to legacy document URLs under `/sites/default/files/...` (previous Drupal paths), mainly on [Financial documents](https://nita.illinois.gov/transit-funding/financial-documents) (54) and historical press releases (49); full list in the evidence file.
- **Priority:** Low
- **Evidence:** On 2026-11-19, link discovery checked 1,004 internal document and image links with HEAD requests. All 141 that returned 301 redirect to an `http://nita.illinois.gov/uploads/files/general/Drupal-Old/...` destination. One example (`Spanish-Title-VI-Notice-to-Public.pdf`) was followed: the HTTP destination returned 200. Two other linked PDFs return 404 (`TransitIstheAnswer.pdf`, `Travel-Information-Action-Plan.pdf`). See [`links_resources.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/links_resources.csv) and [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt).
- **Impact:** Users and crawlers following these links pass through a redirect and land on an unencrypted document URL. Once `SEO-NITA-003` is fixed, each would become a two-step redirect chain. The documents include Title VI notices and financial reports that users may need.
- **Recommendation:** Update the internal links to point directly to the current HTTPS document URLs, and change the redirect targets to HTTPS so external links to the old paths resolve in one step. Restore or remove the links to the two missing PDFs.
- **Implementation complexity:** Low to Medium (depends on whether redirects are managed in the CMS or server configuration)
- **Related standard:** [Google Search Central: redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Paginated listings declare the first page as canonical

- **Finding ID:** SEO-NITA-005
- **Page or component:** Paginated listings: [On Track blog](https://nita.illinois.gov/blog) (65 pages), blog categories such as `/blog/plan` (15), [press releases](https://nita.illinois.gov/news/press-releases) (34), and paginated tag archives (77).
- **Priority:** Low
- **Evidence:** On 2026-11-19, `/blog/p2` and `/blog/p3` returned 200, linked to the next page with standard anchors, and declared `https://nita.illinois.gov/blog` as canonical. The 2026-11-19 crawl baseline shows the same pattern on every paginated listing: each page canonicalizes to the first page of its listing. Older posts and press releases are reachable only through these sequential pages, up to 66 clicks from the homepage. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt) and [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv).
- **Impact:** Later listing pages contain different items from the first page, so the canonical signal is inaccurate. Search engines may give less weight to these pages and the links on them, which are the only internal crawl path to older posts and press releases. The XML sitemap partly offsets this because it lists individual posts.
- **Recommendation:** Give each paginated listing page a self-referencing canonical URL. Keep sequential links between pages.
- **Implementation complexity:** Low (template change)
- **Related standard:** [Google Search Central: pagination best practices](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)

### Blog tag archive titles do not identify their topics

- **Finding ID:** SEO-NITA-001
- **Page or component:** Blog tag archive template: 155 `/blog/tags/` URLs (78 tag pages and 77 paginated tag pages), for example [CTA](https://nita.illinois.gov/blog/tags/cta) and [Metra](https://nita.illinois.gov/blog/tags/metra).
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, all 155 tag archive URLs have the title “NITA | Northern Illinois Transit Authority.” Of the 78 tag pages, 76 are indexable with self-referencing canonicals and 2 canonicalize to their `http://` version (see `SEO-NITA-003`). On 2026-11-18, a public spot check of the [CTA archive](https://nita.illinois.gov/blog/tags/cta) confirmed that it lists CTA-related posts while its title does not identify the topic. The tag list also contains a misspelled duplicate, `/blog/tags/acces-to-transit`, alongside `/blog/tags/access-to-transit`. See [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv) and the batch `page_titles_all.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/).
- **Impact:** In a search result or browser tab, these pages are difficult to distinguish by subject. Google may generate title links from other page signals, so the exported title alone does not predict the exact result shown.
- **Recommendation:** Update the tag archive template so each title names the tag topic and NITA. Confirm which of the 78 tags should remain indexable, and merge the misspelled duplicate tag.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#influence-your-title-links)

### Archive and listing pages share a generic meta description

- **Finding ID:** SEO-NITA-002
- **Page or component:** 292 pages: the homepage, all 155 tag archive URLs, blog archive and pagination pages, and the blog category pages `/blog/plan`, `/blog/invest`, and `/blog/move`.
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, all 1,613 HTML pages have a meta description; 292 use the same description beginning “Committed to achieving a vision of safe, reliable, accessible public transportation…”. See the batch `meta_description_all.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/).
- **Impact:** The repeated description does not summarize the distinct purpose of these pages when used as a search snippet. Google may instead create a snippet from page content.
- **Recommendation:** Write concise descriptions for the homepage and any priority blog landing/archive pages intended for search. Confirm the indexability and editorial purpose of archive and pagination pages before producing copy for all of them.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: control your snippets](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#control-your-snippets)

## Content observations under review

Manual review priorities (rider decision content, program naming, time-sensitive budget and fare content, and the RTA-to-NITA editorial transition) are listed in the [matrix](seo-review-matrix.md#public-content-inventory-and-review-priorities). They are validation priorities, not findings at this stage.

## Positive Observations

- All 1,613 HTML pages in the 2026-11-19 crawl baseline have a title, meta description, and H1, and none has a `noindex` directive. This does not assess whether their content is effective.
- The website publishes an XML sitemap index with five child sitemaps, referenced from `robots.txt`. 1,280 of its 1,286 URLs are also reachable through internal links.
- The homepage includes a JSON-LD `WebSite` graph, providing a base for further structured data. Its content has not yet been validated.

## Limitations

- The crawl baseline uses raw HTML only (no JavaScript rendering). Links generated only by JavaScript are not covered.
- The free Screaming Frog version does not extract structured data, and List mode does not crawl images, so structured data and image alternative text are reviewed on the page-level sample instead.
- Live checks are single dated fetches of the listed URLs; protocol behavior was confirmed on two pages and is presumed website-wide.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- Performance/Core Web Vitals, mobile, internal linking quality, broken internal links, blocked-resource rendering impact, and external links have not yet been assessed (Step 2 and Step 3).
