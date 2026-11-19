# Search Engine Optimization (SEO) — mytransitbenefit.com

## Assessment Scope

- **Website:** [mytransitbenefit.com](https://www.mytransitbenefit.com/)
- **Review date:** 2026-11-19
- **Pages, templates, or journeys reviewed:** Complete four-page scope confirmed by the user on 2026-11-19: [homepage](https://www.mytransitbenefit.com/), [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), and [Employers](https://www.mytransitbenefit.com/employers); plus the `/404` URL listed in the sitemap. Manual review is in progress.
- **Methods and tools:** Screaming Frog SEO Spider 25.1 free version, full Spider crawl with default configuration on 2026-11-19 ([README](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/README.md)); curl 8.7.1 ([`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)); public sitemap and `robots.txt`; public browser review; Google Search Central guidance.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** The website's technical base is sound for its size: HTTP and non-www requests redirect to the HTTPS www homepage, and the four pages are indexable with self-referencing canonicals and distinct meta descriptions. Two issues were found. A `/404` page listed in the sitemap returns 200 and is indexable, and all four page titles contain a literal ellipsis that cuts off the topic before the brand suffix. The H1s are campaign slogans rather than topic statements; this is under review as a content and keyword opportunity.

## Findings

### Sitemap lists a “404” URL that returns 200 and is indexable

- **Finding ID:** SEO-MTB-001
- **Page or component:** [`/404`](https://www.mytransitbenefit.com/404) and the [XML sitemap](../../../evidence/public-technical/2026-11-19/mytransitbenefit-sitemap.xml).
- **Priority:** Medium
- **Evidence:** The sitemap captured on 2026-11-19 lists five URLs: the four confirmed pages and `/404`. On 2026-11-19, `/404` returned HTTP 200 with the homepage title, `<meta name="robots" content="all">`, and a self-referencing canonical. A nonexistent URL on the same website correctly returned 404, so `/404` appears to be a published CMS entry rather than the error response. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt).
- **Impact:** The sitemap asks search engines to crawl and index an error-page entry. If indexed, it could appear in results as a duplicate of the homepage title, and search engines may treat it as a soft 404. On a four-page website, it is one of five URLs submitted for indexing.
- **Recommendation:** Exclude the `/404` entry from the sitemap and mark it `noindex`, or remove it as a public entry if the error template does not depend on it. Confirm with the CMS team how the error template is configured before changing it.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: soft 404 errors](https://developers.google.com/search/docs/crawling-indexing/http-network-errors#soft-404-errors) and [build a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

### Page titles are truncated with a literal ellipsis

- **Finding ID:** SEO-MTB-002
- **Page or component:** `<title>` of all four pages (website template or CMS title field).
- **Priority:** Medium
- **Evidence:** On 2026-11-19 the HTML source titles were “Everybody Wins with Money-Saving NITA… | NITA Transit Benefit Program” (homepage), “How Much Can You Save with NITA… | NITA Transit Benefit Program,” “Want to Cut Your Monthly Commute Bill… | NITA Transit Benefit Program,” and “A Smart Move: NITA Transit Benefits… | NITA Transit Benefit Program.” The ellipsis character is in the source, not added by a tool. Screaming Frog measured the titles at 606–653 px, above the roughly 580 px that commonly displays on desktop results. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt) and [`page_titles_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/page_titles_all.csv).
- **Impact:** The titles stop mid-phrase, before stating the page topic (for example, “pre-tax transit benefits for employees”). A search result or browser tab shows an incomplete sentence, and the most descriptive words are missing. Google may rewrite title links that it considers unhelpful.
- **Recommendation:** Write complete, concise titles that state each page's topic and audience first and the brand second (for example, a title for the Employees page that names pre-tax transit and parking benefits for employees). Check whether the CMS or SEO plugin applies a character limit that inserts the ellipsis.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/appearance/title-link)

## Observations under review

- **H1 headings:** the H1s are campaign slogans (“Your Tax Savings Starts Here!”, “Save Money, Go Green, and Attract Talent!”, “A Deep Dive into The Heart of Our Program.”). Only the homepage H1 names the program. The Employees page also has a second H1, “Login.” Assess in Step 3 together with on-page topic language; coordinate with the accessibility section on heading structure.
- **Legacy and third-party links:** the 2026-11-19 crawl shows links to `rtachicago.org` blog posts that redirect, and a script loaded from `unpkg.com` with the floating `@latest` version, which redirects on every page. Review in Step 2.
- **Structured data:** the homepage JSON-LD `WebSite` graph references `https://nita.illinois.gov#identity` as author and copyright holder. This may be intentional (NITA operates the program) or a copied configuration; confirm the intended publisher identity before recording a finding.

## Positive Observations

- On 2026-11-19, `http://www.mytransitbenefit.com/` and `https://mytransitbenefit.com/` each returned a single 301 redirect to `https://www.mytransitbenefit.com/`. Only the homepage was tested.
- The four HTML pages in the 2026-11-19 crawl have distinct meta descriptions and self-referencing canonicals, and none of the 31 crawled images is missing alternative text. See [`meta_description_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/meta_description_all.csv), [`canonicals_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/canonicals_all.csv), and [`crawl_overview.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/crawl_overview.csv).
- The pages communicate distinct audiences (employees and employers) and calls to action. Full enrollment journeys were not tested.

## Limitations

- The 2026-11-19 crawl (default configuration, Text Only) replaces the undocumented 2026-11-16 crawl and confirms the four-page scope. The free Screaming Frog version does not extract structured data, so markup is validated manually.
- The public spot checks did not submit forms, follow authenticated flows, or verify transaction completion.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- Performance/Core Web Vitals, mobile, internal linking, image alternative text, the rendering impact of four robots-blocked form and tag-manager assets, and content accuracy have not yet been assessed.
