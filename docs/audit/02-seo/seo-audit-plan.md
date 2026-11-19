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

The proposal notes that access to analytics data may be requested if needed to support specific findings. Read-only Search Console access would resolve the open index-coverage questions (sitemap-only URLs, HTTP/HTTPS duplicates, pagination). Raise this with DHD as an option; do not assume it will be granted.

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

Completed: proposal scope mapped to matrix controls; crawl inventories documented; the user-confirmed four-page My Transit Benefit scope and agreed NITA 12+3 sample recorded; robots files and all sitemap XML files retrieved and compared with the crawl exports.

Results and open questions carried into Step 2:

- **NITA sitemap/crawl gap.** The sitemap index lists 1,286 unique URLs; 83 match the 2026-11-16 crawl and 1,203 do not. See the [evidence README](../../../evidence/public-technical/2026-11-19/README.md).
- **Probable crawl-configuration cause.** No crawled NITA page is deeper than crawl depth 2, yet `/blog/p2` links to `/blog/p3` with a standard anchor in the raw HTML, and `/blog/p3` returns 200 (see [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)). A text-only crawl without a depth limit should have followed that link. The gap may therefore come from a crawl depth limit rather than from the website. Confirm the configuration before interpreting the gap.
- **Structured-data exports are not usable as evidence of absence.** Both 2026-11-16 exports report zero structured-data types, but both homepages contain a JSON-LD block. Screaming Frog does not extract structured data unless it is enabled.
- **Image alternative text is not in the exports.** `images_all.csv` contains size and inlink data only.
- **My Transit Benefit** coverage is user-confirmed (four pages). Its crawl configuration was not recorded.

### Step 2 — Re-crawl and complete automated technical checks

1. **Confirm and correct the crawl configuration.** Check the Spider limits (crawl depth, folder depth, max URLs) used on 2026-11-16. Enable JSON-LD, Microdata, and RDFa extraction with validation, and the image alt-text export. Record all settings in the new crawl README.
2. **Resolve the 500-URL limit before re-crawling NITA.** An unrestricted crawl of NITA is expected to exceed 500 URLs (the sitemap alone lists 1,286). Choose one documented approach and record it in the matrix:
   - **Option A (recommended within current scope):** crawl NITA with images, CSS, JS, and external links excluded from storage so the 500-URL budget is spent on internal HTML; then crawl representative sitemap samples in List mode (for example, the five category URLs, a systematic sample of news and press-release URLs, and the 19 general-page sitemap URLs not found in the original crawl).
   - **Option B:** run separate subfolder crawls (`/blog/`, `/about-rta/press-releases/`, other sections) and record each one's coverage.
   - **Option C:** use a licensed Screaming Frog seat. The proposal excludes paid tools unless agreed, so this requires DHD's agreement.
3. Re-crawl My Transit Benefit with the same documented configuration (small cost; replaces the undocumented crawl and the invalid structured-data export).
4. Store new exports in new dated folders. Do not edit or overwrite the 2026-11-16 snapshots.
5. Analyze crawlability, status codes, redirect destinations/chains, HTTP/HTTPS consistency, soft 404 responses, blocked resources, internal broken links, canonicals, indexability directives, pagination, and URL patterns.
6. Review titles, meta descriptions, and heading structure; group template-level patterns and inspect affected page purpose before treating alerts as findings.
7. Review internal link pathways and sitemap inclusion/discovery against the new crawl. Sample representative sitemap-only URLs per group, including historical press releases.
8. Validate structured data with the Rich Results Test or Schema.org Validator and compare it with visible content, including the identity values in the My Transit Benefit `WebSite` graph.
9. Review image alternative text from the new export and representative rendered pages; classify each gap as SEO-related, accessibility-related, or both, and coordinate with the accessibility section to avoid duplicate findings.
10. Treat external-link 403 responses from transit operators (for example metra.com, ventrachicago.com) as likely bot blocking until confirmed in a browser; do not report them as broken links without that check.

**Output:** documented crawl configuration, dated technical evidence, completed automated baseline, matrix statuses, and validated technical findings.

### Step 3 — Manually assess representative pages and mobile/performance

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

## Current work status — 2026-11-19

- Step 1 is closed. Step 2 starts with crawl-configuration confirmation and the 500-URL decision above.
- Draft findings: `SEO-NITA-001` to `SEO-NITA-005` and `SEO-MTB-001` to `SEO-MTB-002`. The protocol, redirect, pagination-canonical, soft 404, and title findings were verified with dated live checks on 2026-11-19.
- Open decisions for the team: crawl approach for NITA (Option A, B, or C) and whether to ask DHD for read-only Search Console access.
