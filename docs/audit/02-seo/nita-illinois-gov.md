# Search Engine Optimization (SEO) — nita.illinois.gov

## Assessment Scope

- **Website:** [nita.illinois.gov](https://nita.illinois.gov/)
- **Review date:** 2026-11-19
- **Pages, templates, or journeys reviewed:** Crawl-level review of 87 HTML page records and associated exported URLs from the 2026-11-16 crawl; current public content/navigation review on 2026-11-19; and public sitemap inventory captured on 2026-11-19. The sitemap contains 1,286 unique URLs, far more than the crawl discovered. A 15-URL representative manual-review sample is documented in the [SEO review matrix](seo-review-matrix.md#page-level-review-scope); detailed manual evaluation of that sample remains in progress.
- **Methods and tools:** Screaming Frog SEO Spider 25.1, Text Only; dated CSV exports in [`evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/); public browser review; Google Search Central guidance.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft — initial crawl and content inventory.** The 2026-11-16 crawl contains 87 HTTP 200 HTML page records, organized mainly around riders, communities, the regional transit system, transit funding, institutional information, and a blog/news archive. The public sitemap inventory captured on 2026-11-19 contains 1,286 unique URLs, including 419 press-release URLs and a larger news archive; only 83 sitemap URLs match the crawl after HTTP/HTTPS normalization. The difference is not yet explained and does not by itself show that URLs are orphaned or invalid. The crawl completed below the free URL limit but only covers discovered URLs. Seven crawled blog tag archives share a brand-only title and 13 crawled pages share one generic meta description. Current fare tables and time-sensitive budget calls to action need manual currency checks. This review does not establish rankings, clicks, or Google index status.

## Findings

### Blog tag archive titles do not identify their topics

- **Finding ID:** SEO-NITA-001
- **Page or component:** Seven `/blog/tags/` archives: [eTOD](https://nita.illinois.gov/blog/tags/etod), [community planning](https://nita.illinois.gov/blog/tags/community-planning), [how to use transit](https://nita.illinois.gov/blog/tags/how-to-use-transit), [Pace](https://nita.illinois.gov/blog/tags/pace), [CTA](https://nita.illinois.gov/blog/tags/cta), [Metra](https://nita.illinois.gov/blog/tags/metra), and [RTA](https://nita.illinois.gov/blog/tags/rta).
- **Priority:** Low
- **Evidence:** Screaming Frog's `Page Titles > All` export records the same title, “NITA | Northern Illinois Transit Authority,” for all seven archives. On 2026-11-18, a public spot check of the [CTA archive](https://nita.illinois.gov/blog/tags/cta) confirmed that its page lists CTA-related posts, while its title does not identify the archive topic. See [`page_titles_all.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/page_titles_all.csv).
- **Impact:** In a search result or browser tab, these pages are difficult to distinguish by subject. Google recommends titles that are unique, clear, concise, and accurate; it may also generate title links from other page signals, so the exported title alone does not predict the exact result shown.
- **Recommendation:** If these archives are intended to be discoverable in search, give each a concise, topic-specific title that identifies the archive and NITA. First confirm that each archive should remain indexable and offers enough distinct value to merit a search landing page.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#influence-your-title-links)

### Thirteen pages share a generic meta description

- **Finding ID:** SEO-NITA-002
- **Page or component:** Homepage, blog landing and pagination pages, selected blog topics, and the seven tag archives; the complete affected URL list is recorded in the evidence export.
- **Priority:** Low
- **Evidence:** `Meta Description > All` contains 87 HTML page records. Thirteen use the same description beginning “Committed to achieving a vision of safe, reliable, accessible public transportation…” including the homepage, `/blog`, `/blog/p2`, `/blog/invest`, `/blog/move`, `/blog/plan`, and the seven tag archives. See [`meta_description_all.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/meta_description_all.csv).
- **Impact:** The repeated description does not summarize the distinct purpose of these pages when it is used as a search snippet. Google may instead create a snippet from page content, and does not guarantee use of the meta description.
- **Recommendation:** Write concise descriptions that accurately summarize the homepage and any priority blog landing/archive pages intended for search. Confirm the desired indexability and editorial purpose of archive and pagination pages before producing copy for all of them.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: control your snippets](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#control-your-snippets)

## Content inventory and review priorities

The crawl and current public navigation show an audience-led structure for riders, municipalities/communities, regional transit information, transit funding, news, and About NITA. The 87 crawled HTML records are concentrated in the blog/news archive and About NITA pages, followed by Communities and Riders. The sitemap reveals a broader public URL corpus that the crawl did not discover: 1,286 unique URLs across category, news, general-page, and press-release sitemaps. In particular, 419 press-release URLs are a content type not represented by the agreed 15-URL sample. Phase 2 should inspect representative examples and decide whether the sample needs adjustment before drawing conclusions about this archive; the sitemap discrepancy alone does not establish an SEO problem. Core rider information is organized around trip planning, fares, reduced-fare programs, and accessibility. Community content covers planning assistance and pedestrian/bicycle access projects; regional/funding pages explain the system and current budget process. The homepage currently foregrounds the 2027 budget, along with community, holiday-travel, and rider-priority content. These themes are reflected in the agreed [12-page core sample and three targeted editorial checks](seo-review-matrix.md#page-level-review-scope).

Manual review should pay particular attention to content ownership and currency across NITA, CTA, Metra, and Pace; eligibility and application steps on rider program pages; and the distinction between the reduced-fare “Access Program” and the community infrastructure “Access to Transit” program. The public fare page labels some Metra fare tables as effective February 1, 2024, and the homepage observed on 2026-11-19 still invited users to register for a November 12 budget hearing. Verify these time-sensitive items with current source information before classifying them as findings. They are validation priorities, not additional findings at this stage.

The blog says that posts published before September 1, 2026 were written by RTA and are retained for historical purposes. Review whether dates and agency context remain clear on those posts so historical content is not mistaken for current NITA guidance.

## Positive Observations

- The Screaming Frog dashboard recorded 496 total URLs (401 internal, 95 external) and 100% completion, below the free crawl limit of 500. This means the crawl completed its discovered queue; it does not prove that every existing or unlinked site URL was discovered. See the [crawl README](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/README.md).
- The public sitemap index and all five child sitemaps were downloaded and compared against the crawl. This provides a second URL inventory, but the 1,203 sitemap URLs absent from the crawl still need response and discovery-path validation before they can be classified. See the [dated evidence README](../../../evidence/public-technical/2026-11-19/README.md).
- All 87 HTML page records in the exported title, meta description, and H1 reports had those elements populated. This does not assess whether their content is effective or accurate.

## Limitations

- The crawl used Text Only rendering and is a snapshot from 2026-11-16. JavaScript-rendered content and changes after that date were not assessed.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- The current public review has inspected the site navigation and spot-checked pages across the recommended sample, but has not completed a detailed page-by-page assessment of that sample. Search-result appearance and whether archive pages should be indexed also require further review.
- Performance/Core Web Vitals, the cause and significance of sitemap/crawl differences, robots-blocked resource impact, internal redirect source links, image alternative text, and structured-data suitability have not yet been validated as findings.
