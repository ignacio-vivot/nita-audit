# Search Engine Optimization (SEO) — nita.illinois.gov

## Assessment Scope

- **Website:** [nita.illinois.gov](https://nita.illinois.gov/)
- **Review date:** 2026-11-19
- **Pages, templates, or journeys reviewed:** Crawl-level review of the 87 HTML page records from the 2026-11-16 crawl; public sitemap inventory (1,286 unique URLs) captured on 2026-11-19; dated live header and HTML checks on 2026-11-19; navigation and spot checks across the agreed 15-URL sample listed in the [SEO review matrix](seo-review-matrix.md#page-level-review-scope). Detailed manual evaluation of the sample is in progress.
- **Methods and tools:** Screaming Frog SEO Spider 25.1, Text Only ([exports](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/)); curl 8.7.1 ([`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)); public browser review; Google Search Central guidance.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** The most consequential observation so far is protocol handling: the website serves pages over unencrypted HTTP without redirecting to HTTPS, and 61 legacy document URLs redirect to HTTP destinations. Canonical tags point to HTTPS, which limits but does not remove the risk of split signals and unencrypted visits. Blog pagination pages all declare the first listing page as canonical. Metadata observations are lower priority: seven tag archives share a brand-only title, and 13 pages share one generic meta description.

Coverage is not yet sufficient for conclusions about the 1,203 sitemap URLs the crawl did not discover. The 2026-11-16 crawl probably used a crawl depth limit, and its structured-data export did not detect markup that is present on the website. A re-crawl with documented settings is planned; see the [work plan](seo-audit-plan.md#step-2--re-crawl-and-complete-automated-technical-checks). This review does not establish rankings, clicks, or Google index status.

## Findings

### HTTP pages load without redirecting to HTTPS

- **Finding ID:** SEO-NITA-003
- **Page or component:** Website-wide protocol handling; observed on the [homepage](http://nita.illinois.gov/) and [Riders](http://nita.illinois.gov/riders) over HTTP.
- **Priority:** Medium
- **Evidence:** On 2026-11-19, `curl -sI` requests to `http://nita.illinois.gov/` and `http://nita.illinois.gov/riders` returned `HTTP/1.1 200 OK` with no `Location` header. The HTTPS homepage returned no `Strict-Transport-Security` header. The HTTP homepage declares `https://nita.illinois.gov/` as canonical. The 2026-11-16 crawl also recorded one internally linked HTTP press-release URL (seven inlinks) that loaded with 200 and canonicalized to its HTTPS version. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt) and [`internal_all.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/internal_all.csv). By contrast, My Transit Benefit redirects HTTP to HTTPS.
- **Impact:** Every page is available at two protocol versions. Search engines must rely on canonical tags to consolidate them, and links or bookmarks to HTTP URLs keep users on an unencrypted connection. Google's canonicalization guidance states a preference for HTTPS pages as canonical and lists redirects as a strong signal for consolidating duplicate URLs.
- **Recommendation:** Add a website-wide, server-level 301 redirect from HTTP to the equivalent HTTPS URL, then consider adding an HSTS header after the redirects are verified. Update internal links that still use `http://`.
- **Implementation complexity:** Low (assumes a server or CDN configuration change; confirm with the hosting team)
- **Related standard:** [Google Search Central: consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) and [redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Legacy document redirects point to HTTP destinations

- **Finding ID:** SEO-NITA-004
- **Page or component:** 61 legacy document URLs under `/sites/default/files/...` (previous Drupal paths), mostly PDFs linked from About NITA and financial-report pages; full list in the crawl export.
- **Priority:** Low
- **Evidence:** The 2026-11-16 crawl records 61 internal URLs returning 301, each with one inlink and each redirecting to an `http://nita.illinois.gov/uploads/files/general/Drupal-Old/...` destination. On 2026-11-19, one example (`Spanish-Title-VI-Notice-to-Public.pdf`) returned 301 to its HTTP destination, which then returned 200 over HTTP. See [`internal_all.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/internal_all.csv) and [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt).
- **Impact:** Users and crawlers following these links pass through a redirect and land on an unencrypted document URL. Once `SEO-NITA-003` is fixed, each would become a two-step redirect chain. The documents include Title VI notices and financial reports that users may need.
- **Recommendation:** Update the internal links to point directly to the current HTTPS document URLs, and change the redirect targets to HTTPS so external links to the old paths resolve in one step.
- **Implementation complexity:** Low to Medium (depends on whether redirects are managed in the CMS or server configuration)
- **Related standard:** [Google Search Central: redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Blog pagination pages declare the first page as canonical

- **Finding ID:** SEO-NITA-005
- **Page or component:** [On Track blog](https://nita.illinois.gov/blog) pagination (`/blog/p2`, `/blog/p3`, and later pages).
- **Priority:** Low
- **Evidence:** On 2026-11-19, `/blog/p2` and `/blog/p3` returned 200, linked to the next page with standard anchors, and declared `https://nita.illinois.gov/blog` as canonical. The 2026-11-16 crawl records `/blog/p2` as “Canonicalised” to `/blog`. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt) and [`canonicals_all.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/canonicals_all.csv).
- **Impact:** Later listing pages contain different posts from the first page, so the canonical signal is inaccurate. Search engines may give less weight to these pages and the links on them, which are a crawl path to older posts. The XML sitemap partly offsets this because it lists individual posts.
- **Recommendation:** Give each paginated listing page a self-referencing canonical URL. Keep sequential links between pages.
- **Implementation complexity:** Low (template change)
- **Related standard:** [Google Search Central: pagination best practices](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)

### Blog tag archive titles do not identify their topics

- **Finding ID:** SEO-NITA-001
- **Page or component:** Seven `/blog/tags/` archives: [eTOD](https://nita.illinois.gov/blog/tags/etod), [community planning](https://nita.illinois.gov/blog/tags/community-planning), [how to use transit](https://nita.illinois.gov/blog/tags/how-to-use-transit), [Pace](https://nita.illinois.gov/blog/tags/pace), [CTA](https://nita.illinois.gov/blog/tags/cta), [Metra](https://nita.illinois.gov/blog/tags/metra), and [RTA](https://nita.illinois.gov/blog/tags/rta).
- **Priority:** Low
- **Evidence:** Screaming Frog's `Page Titles > All` export records the same title, “NITA | Northern Illinois Transit Authority,” for all seven archives. On 2026-11-18, a public spot check of the [CTA archive](https://nita.illinois.gov/blog/tags/cta) confirmed that it lists CTA-related posts while its title does not identify the topic. See [`page_titles_all.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/page_titles_all.csv).
- **Impact:** In a search result or browser tab, these pages are difficult to distinguish by subject. Google may generate title links from other page signals, so the exported title alone does not predict the exact result shown.
- **Recommendation:** If these archives are intended to be discoverable in search, give each a concise, topic-specific title that identifies the archive and NITA. First confirm that each archive should remain indexable.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#influence-your-title-links)

### Thirteen pages share a generic meta description

- **Finding ID:** SEO-NITA-002
- **Page or component:** Homepage, blog landing and pagination pages, selected blog topics, and the seven tag archives; the complete affected URL list is in the evidence export.
- **Priority:** Low
- **Evidence:** `Meta Description > All` contains 87 HTML page records. Thirteen use the same description beginning “Committed to achieving a vision of safe, reliable, accessible public transportation…” including the homepage, `/blog`, `/blog/p2`, `/blog/invest`, `/blog/move`, `/blog/plan`, and the seven tag archives. See [`meta_description_all.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/meta_description_all.csv).
- **Impact:** The repeated description does not summarize the distinct purpose of these pages when used as a search snippet. Google may instead create a snippet from page content.
- **Recommendation:** Write concise descriptions for the homepage and any priority blog landing/archive pages intended for search. Confirm the indexability and editorial purpose of archive and pagination pages before producing copy for all of them.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: control your snippets](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#control-your-snippets)

## Content observations under review

Manual review priorities (rider decision content, program naming, time-sensitive budget and fare content, and the RTA-to-NITA editorial transition) are listed in the [matrix](seo-review-matrix.md#public-content-inventory-and-review-priorities). They are validation priorities, not findings at this stage.

## Positive Observations

- All 87 HTML page records in the crawl have a title, meta description, and H1 populated. This does not assess whether their content is effective.
- The website publishes an XML sitemap index with five child sitemaps, referenced from `robots.txt`, covering general pages, news, categories, and press releases.
- The homepage includes a JSON-LD `WebSite` graph, providing a base for further structured data. Its content has not yet been validated.

## Limitations

- The 2026-11-16 crawl used Text Only rendering. No crawled page is deeper than crawl depth 2, although deeper pages are linked in the raw HTML; a crawl depth limit is the likely cause and must be confirmed. Until a re-crawl, sitemap-only URLs are not classified as orphaned, invalid, or problematic.
- The 2026-11-16 structured-data export reports no markup although markup exists, and the image export has no alternative-text data. Neither is used as evidence of absence.
- Live checks are single dated fetches of the listed URLs; protocol behavior was confirmed on two pages and is presumed website-wide pending the re-crawl.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- Performance/Core Web Vitals, mobile, internal linking, blocked-resource rendering impact, and external-link 403 responses have not yet been assessed.
