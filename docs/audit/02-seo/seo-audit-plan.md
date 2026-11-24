# SEO Audit Work Plan — NITA websites

## Purpose and governing scope

This work plan operationalizes the SEO scope in [`docs/project-overview.md`](../../project-overview.md#22-search-engine-optimization-seo). That proposal is the source of truth for what the client was told would be reviewed. The SEO assessment covers both [nita.illinois.gov](https://nita.illinois.gov/) and [mytransitbenefit.com](https://www.mytransitbenefit.com/) and includes:

1. Technical SEO and website crawlability.
2. Indexability and search engine accessibility.
3. Page titles, meta descriptions, and heading structure.
4. URL structure and internal linking.
5. Sitemap and `robots.txt` configuration.
6. Structured data and schema markup.
7. Page performance and Core Web Vitals.
8. Mobile SEO considerations.
9. Content organization and keyword optimization opportunities.
10. Technical issues that may affect organic visibility.

The proposal calls for automated analysis plus expert manual review of representative pages, templates, and key journeys—not exhaustive review of every page. It also calls for actionable recommendations, supporting evidence, prioritization, implementation-complexity estimates, and an action plan.

The SEO work is organized in four **steps** (Step 1–4). They are internal to this workstream and are distinct from the three project phases in the proposal (Initial Assessment, Detailed Audit, Reporting & Recommendations).

## Agreed access boundary

The audit is limited to publicly accessible pages, resources, public search results, and open testing tools. Per the project decision, do not use Search Console, analytics, CMS, source code, hosting, or server access. This means actual search queries, rankings, impressions, clicks, click-through rate, conversions, and comprehensive index coverage cannot be measured. Mark these items **Not verifiable in public scope**; do not treat a public `site:` search or crawler output as a substitute for first-party reporting.

The proposal notes that access to analytics data may be requested if needed. On 2026-11-19 the team decided not to request Search Console or analytics access from DHD at this stage; index-coverage questions remain **Not verifiable in public scope** unless that decision changes.

Page performance can be sampled with public PageSpeed Insights/Lighthouse. Report lab observations separately from field Core Web Vitals data; field data may be unavailable for a page or origin. Publicly observed content and technical characteristics can support qualitative opportunities, but cannot establish organic performance improvements.

## How to record the audit

Use the [SEO review matrix](seo-review-matrix.md) as the control checklist for both websites, following the general [review controls and coverage method](../authoring-guide.md#3-review-controls-and-coverage) and the status definitions in the authoring guide. Every in-scope control receives a status, review date, method, and evidence reference. Findings are a separate, linked record in the site reports. Never mark a control verified based only on the absence of a crawler warning, and never treat an export as evidence of absence unless the relevant extraction was enabled in the crawl configuration.

The matrix is the single place for coverage detail and caveats. Site reports carry the summary, findings, selected positive observations, and limitations, and link to the matrix rather than repeating it. Keep raw Screaming Frog exports read-only under `evidence/crawls/screaming-frog/`.

## Tools and evidence

| Tool or source | Use | Evidence and limits |
| --- | --- | --- |
| Screaming Frog SEO Spider | Discover crawlable URLs and inspect status codes, redirects, titles, descriptions, headings, links, canonicals, directives, images, and structured data. | Preserve dated exports and record version, rendering mode, start URL, crawl scope, **crawl depth limit**, **structured-data extraction settings**, completion, totals, and cap. A crawl covers discovered URLs only. The free version is limited to 500 URLs per crawl. |
| curl / public browser | Inspect response headers, redirects, canonicals, rendered content, navigation, representative templates, and page behavior. | Save raw output with date and tool version, as in [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt). A manual sample does not represent every page. |
| Public `robots.txt` and XML sitemap endpoints | Inspect directives, sitemap references, and URL lists; compare sitemap URLs against crawl evidence. | A public fetch does not expose server-side rules or prove search engine treatment. |
| PageSpeed Insights / Lighthouse | Run representative mobile and desktop tests for page performance and mobile-related diagnostics. | Save dated results/links. Treat lab data as a snapshot; report field Core Web Vitals only when available. Scores alone are not findings. |
| Google Rich Results Test / Schema.org Validator | Check syntax and eligibility for applicable structured data. | Manually compare markup with visible page content; validity does not establish correctness or guarantee a search feature. |
| Public search features (results, autocomplete, “People also ask”, Google Trends) | Qualitative context for page topics, user language, and visible titles/snippets for a small, documented query set. | Record query, date, and locale/context. This is not rank tracking, query volume, or performance data. |

## Work sequence

### Step 1 — Reconcile scope and establish coverage (closed 2026-11-19)

1. Keep the proposal's ten SEO areas as the checklist; do not silently add new client commitments.
2. Produce a valid crawl baseline for both websites, with the configuration recorded in each crawl README. See [Crawl baseline: method](#crawl-baseline-method).
3. Compare discovered crawl URLs with public sitemap URLs and public navigation. Document likely gaps without expanding the agreed manual page scope.
4. Use the four user-confirmed My Transit Benefit URLs and the agreed 16 NITA URLs in the matrix (15 agreed on 2026-11-19 plus one press release added on 2026-11-20) as the page-level analysis scope.
5. Update each matrix control with current status and evidence; keep unknowns open rather than inferring a pass.

**Output:** verified crawl baseline, URL/template inventory, confirmed page-level scopes, and initial matrix statuses.

**Status — 2026-11-19: closed.** Scope mapping, page-level scopes, and the robots/sitemap download were completed first. The crawl baseline was then redone because the 2026-11-16 crawls could not support coverage conclusions (no page deeper than crawl depth 2, structured-data and alt-text exports unusable, and an undocumented My Transit Benefit configuration). The 2026-11-16 crawl folders stay in the repository unchanged but are **superseded**; analysis and findings now cite the 2026-11-19 baseline.

Baseline results:

- **NITA:** 1,736 URLs = the 1,286 sitemap URLs plus 1,730 HTML URLs reached through internal links ([B1 README](../../../evidence/crawls/link-discovery/2026-11-19/README.md), [B2 README](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/README.md)). Only 6 sitemap URLs are not reached through links (`/404`, `/blog/uncategorized`, `/regsitehub`, `/ridersurvey26`, `/saveada`, `/take-action`); the earlier 1,203-URL gap was a crawl artifact. 450 linked HTML URLs are not in the sitemap (mainly tag archives and paginated listings). Maximum link depth is 66.
- **My Transit Benefit:** full crawl of the four-page website, 64 URLs ([README](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/README.md)).
- **Findings re-pointed:** `SEO-NITA-001`, `002`, `004`, `005`, and `SEO-MTB-002` now cite the new baseline; their counts were updated (for example, 155 tag archive URLs instead of 7, and 141 legacy document links instead of 61).

The team decided on 2026-11-19 to use the free Screaming Frog version (no paid license). The method below works within the free version's limits.

#### Crawl baseline: method

The free Screaming Frog version runs headless from the command line but cannot load configuration files, so Include/Exclude rules and crawl options cannot be changed in a scripted run. A default spider crawl of NITA on 2026-11-19 stopped at the 500-URL limit while still at crawl depth 2, because images, PDFs, and external links fill the budget before the deep pagination is reached. The baseline therefore combines three runs, each documented in its own evidence README:

| Run | Website | Tool and mode | Purpose |
| --- | --- | --- | --- |
| B1 — Link discovery | NITA | Python link-discovery script ([`link_discovery.py`](../../../evidence/crawls/link-discovery/2026-11-19/link_discovery.py)): follows internal `<a href>` links from the homepage with no depth limit, fetches HTML only, respects `robots.txt`, checks internal documents/images with HEAD, and records external links without requesting them. | Which URLs are reachable through internal links, at what depth, and from which page; HTTP-scheme links; internal resource status. |
| B2 — Technical data | NITA | Screaming Frog 25.1, List mode, headless, default configuration, in batches below 500 URLs. Input: the union of sitemap URLs and B1-discovered HTML URLs. | Status, indexability, titles, descriptions, headings, canonicals, and directives for every known HTML URL. List mode crawls only the listed URLs. |
| B3 — Full spider | My Transit Benefit | Screaming Frog 25.1, Spider mode, headless, default configuration. | Complete crawl of the four-page website with resources and external links ([README](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/README.md)). |

Then rebuild the sitemap/crawl comparison against B1 and B2 in a new dated evidence folder; it replaces the 2026-11-19 comparison. A sitemap URL that B1 did not reach is a candidate for a discovery-path check, not yet an orphan finding.

Free-version limits that remain: no JavaScript rendering, no structured-data extraction, and no image alt-text detail for NITA pages (B2 List mode does not crawl images). Structured data and JavaScript-dependent content are validated on the page-level sample in Step 2 and Step 3; image alternative text is reviewed on the sample and coordinated with the accessibility section.

### Step 2 — Complete automated technical checks

Work in parts and review each with the team before the next: (A) crawlability and indexability, items 1 and 8; (B) broken and malformed internal links, item 7; (C) titles, descriptions, and headings, item 2; (D) sitemap and discovery, item 3; (E) structured data, item 4; (F) image alternative text and external links, items 5 and 6.

Progress: part A completed 2026-11-20 (`SEO-NITA-006` and `SEO-NITA-007` added); part B completed 2026-11-20 (`SEO-NITA-008` and `SEO-NITA-009` added); part C completed 2026-11-20 (`SEO-NITA-010` to `014` and `SEO-MTB-003` added); part D completed 2026-11-20 (`SEO-NITA-015` added); part E completed 2026-11-20 (`SEO-NITA-016` and `SEO-MTB-004` added); part F completed 2026-11-20 (`SEO-NITA-017`, `SEO-NITA-018`, and `SEO-MTB-005` added; 315 external URLs blocked or not loading from Argentina left pending for a US check). Step 2 is complete. See the matrix log.

Uses the 2026-11-19 crawl baseline from Step 1: [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv), the B1 link-discovery files, and the My Transit Benefit crawl.

1. Analyze crawlability, status codes, redirect destinations/chains, HTTP/HTTPS consistency, soft 404 responses, blocked resources, internal broken links, canonicals, indexability directives, pagination, and URL patterns.
2. Review titles, meta descriptions, and heading structure; group template-level patterns and inspect affected page purpose before treating alerts as findings.
3. Review internal link pathways and sitemap inclusion/discovery using `url-inventory.csv`: check all 6 sitemap URLs not reached through internal links, decide whether the 450 linked HTML URLs absent from the sitemap (mainly tag archives and pagination) should be listed, and review the sitemap URLs that redirect. Inspect a representative historical press release.
4. Validate structured data with the Rich Results Test or Schema.org Validator and compare it with visible content, including the identity values in the My Transit Benefit `WebSite` graph.
5. Review image alternative text: for My Transit Benefit, use the 2026-11-19 Spider image exports; for NITA, review the rendered page-level sample, because List mode does not crawl images. Classify each gap as SEO-related, accessibility-related, or both, and coordinate with the accessibility section to avoid duplicate findings.
6. Treat external-link 403 responses from transit operators (for example metra.com, ventrachicago.com) as likely bot blocking until confirmed in a browser.
7. Analyze the 50 internal URLs returning 404 and the 2 malformed links (403) recorded by link discovery, separating links on current pages from links in historical posts and press releases.
8. Check the signals found on 2026-11-19 (curl): NITA `/404` returns 200 and is listed in the sitemap; out-of-range pagination such as `/blog/p100` and `/news/press-releases/p100` returns 200; the news sitemap lists a post dated 1970-01-01 (`/blog/1970/01/01/take-rta-survey`). Confirm each before recording findings.

**Output:** dated technical evidence, completed automated baseline, matrix statuses, and validated technical findings.

### Step 3 — Manually assess representative pages and mobile/performance

Method (team decision, 2026-11-24): Step 3 is AI-assisted. The reviewer (Claude) opens pages in a Chromium browser, compares raw and rendered HTML, runs PageSpeed Insights through its web interface, emulates a mobile viewport, and analyzes the collected evidence; the team reviews the conclusions after each part. Limits to record in the reports: PageSpeed runs one URL at a time (the keyless API quota was exhausted on 2026-11-24); mobile checks use Chromium device emulation, not physical devices; keyword opportunities are qualitative, without search-volume data, and any public search checks run from Argentina, so they do not reflect results seen in the Chicago region.

Work in parts and review each with the team before the next: (A) performance and Core Web Vitals, item 4; (B) rendered review of the sample pages, item 1; (C) mobile SEO, item 5; (D) information architecture and internal links, item 2; (E) content and keyword opportunities, item 3, including the content observations listed in the matrix.

Progress: part A completed 2026-11-24 (`SEO-NITA-019`, `SEO-NITA-020`, and `SEO-MTB-006` added); part B completed 2026-11-24 (rendered and raw HTML match on all 20 sample pages; `SEO-NITA-021` added for translations not visible to search engines; heading observations updated); part C completed 2026-11-24 (`SEO-NITA-022` and `SEO-NITA-023` added; no My Transit Benefit mobile issue beyond performance); part D completed 2026-11-24 (full internal link graph; `SEO-NITA-024`, `SEO-NITA-025`, and `SEO-MTB-007` added; `SEO-NITA-023` corrected); part E completed 2026-11-24 (`SEO-NITA-026` to `SEO-NITA-028` and `SEO-MTB-008` added). Step 3 is complete. See the matrix log.

1. Inspect the confirmed page URLs for each website in a browser, including rendered content and key public journeys. Confirm that titles, descriptions, headings, links, canonicals, and structured data align with page purpose.
2. Assess whether information architecture and internal links make important content discoverable and understandable.
3. Identify qualitative keyword optimization opportunities from page topics, audience needs, geography, and publicly visible language, supported by a small documented sample of public search features. Do not claim search demand or rankings.
4. Run representative PageSpeed Insights/Lighthouse tests in mobile and desktop modes. Record lab and field results separately and repeat unusual measurements before drawing conclusions.
5. Assess mobile SEO considerations in the rendered public experience: content parity, navigation, page usability, and mobile performance signals.

**Output:** manual assessment notes, mobile/performance evidence, content/keyword opportunities, and updated matrix statuses.

### Step 4 — Close controls and report recommendations

1. Give every matrix row a final status, scope/method, date, and evidence or a reason it could not be assessed.
2. Validate all findings against the authoring guide: observed evidence, impact, recommendation, priority, complexity, and stable ID (`SEO-NITA-###` or `SEO-MTB-###`).
3. Order each site report's findings by priority so the most consequential technical issues lead the section.
4. Separate technical issues, editorial recommendations, and items that require client/business confirmation. Do not prescribe indexing, URL, or redirect changes without confirming intended page purpose.
5. Consolidate actions in the cross-site roadmap and prepare the SEO section for final report review.

**Output:** completed SEO matrices, site reports, evidence links, prioritized recommendations, and inputs to the consolidated roadmap.

## Completion criteria

The SEO workstream is ready for consolidation when:

- All ten areas in the original proposal are represented in the matrix for both websites.
- Every control has an explicit final status and traceable evidence or a documented limitation.
- Crawl configuration, coverage, and sampling limits are stated; no crawler sample is presented as exhaustive site coverage.
- Each finding is manually validated where practical and linked to its evidence and matrix control.
- Public-only limitations are explicit, and no first-party performance or comprehensive index claims are made.
- The site reports and consolidated recommendations are consistent with the matrix and authoring guide.

## Current work status — 2026-11-24

- Step 1 is closed with the 2026-11-19 crawl baseline. Step 2 is complete (parts A to F, 2026-11-20). Step 3 is complete (AI-assisted, parts A to E, 2026-11-24). Step 4 (close the matrix, validate findings, and prepare the roadmap) is next. Open item: check the 315 external URLs marked `review-*` in `nita-external-links-browser-check.csv` (85 domains, one sample URL each in `nita-external-pending-domains.csv`) from a US connection.
- Draft findings: `SEO-NITA-001` to `SEO-NITA-028` and `SEO-MTB-001` to `SEO-MTB-008`. The protocol, redirect, pagination-canonical, soft 404, and title findings were verified with dated live checks on 2026-11-19.
- Decisions recorded 2026-11-19: the crawl baseline is redone with the free Screaming Frog version (no paid license) plus a documented link-discovery script, and no Search Console or analytics access is requested from DHD at this stage.
