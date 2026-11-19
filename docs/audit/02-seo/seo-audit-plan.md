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

## Agreed access boundary

The audit is limited to publicly accessible pages, resources, public search results, and open testing tools. Per the project decision, do not use Search Console, analytics, CMS, source code, hosting, or server access. This means actual search queries, rankings, impressions, clicks, click-through rate, conversions, and comprehensive index coverage cannot be measured. Mark these items **Not assessed / outside the public-only scope**; do not treat a public `site:` search or crawler output as a substitute for first-party reporting.

Page performance can be sampled with public PageSpeed Insights/Lighthouse. Report lab observations separately from field Core Web Vitals data; field data may be unavailable for a page or origin. Publicly observed content and technical characteristics can support qualitative opportunities, but cannot establish organic performance improvements.

## How to record the audit

Use the [SEO review matrix](seo-review-matrix.md) as the control checklist for both websites, following the general [review controls and coverage method](../authoring-guide.md#3-review-controls-and-coverage). Every in-scope control receives a status, review date, method, and evidence reference. Findings are a separate, linked record of issues or opportunities that warrant action. A completed check with no issue is recorded as **Verified — no issue observed within the stated scope**; it is not turned into a finding. Never mark a control verified based only on the absence of a crawler warning.

Use these statuses consistently:

| Status | Meaning |
| --- | --- |
| Not assessed | Work has not started for this control. |
| In progress | Some evidence has been reviewed, but the control is not complete. |
| Verified — no issue observed | The documented checks were completed and did not identify an issue within their stated limits. |
| Finding recorded | A supported issue or opportunity is documented in the relevant site report and linked by finding ID. |
| Needs manual validation | An automated signal or incomplete evidence requires human confirmation before a conclusion. |
| Not verifiable in public scope | The evidence requires private access, first-party data, or server configuration excluded from this audit. |
| Not applicable | The control does not apply; document why. |

The matrix documents **what was checked and what passed**. Site reports contain the summary, findings, selected positive observations, and limitations. Do not create findings for routine pass results. Keep raw Screaming Frog exports read-only under `evidence/crawls/screaming-frog/`.

## Tools and evidence

| Tool or source | Use | Evidence and limits |
| --- | --- | --- |
| Screaming Frog SEO Spider | Discover crawlable URLs and inspect status codes, redirects, titles, descriptions, headings, links, canonicals, directives, images, and structured data. | Preserve dated exports and record version, rendering mode, start URL, crawl scope, completion, totals, and cap. A crawl covers discovered URLs only. Free crawl limit is 500 URLs per crawl. |
| Public browser | Inspect rendered content, navigation, representative templates, redirect destinations, and page behavior. | Record URLs, date, browser/context where relevant, and concise evidence. A manual sample does not represent every page. |
| Public `robots.txt` and XML sitemap endpoints | Inspect accessibility, directives, sitemap references, and URL lists; compare sitemap URLs against crawl evidence. | A public fetch does not expose server-side rules or prove search engine treatment. Do not label missing/inaccessible endpoints as defects without checking alternate locations and context. |
| PageSpeed Insights / Lighthouse | Run representative mobile and desktop tests for page performance and mobile-related diagnostics. | Save dated results/links. Treat lab data as a snapshot; report field Core Web Vitals only when available. Scores alone are not findings. |
| Public search results | Qualitatively inspect a small, documented sample of likely queries and visible titles/snippets. | Record query, locale/context if known, date, and result URL. This is not rank tracking, index coverage, query demand, or performance data. |
| Google Rich Results Test / Schema.org Validator | Check syntax and eligibility for applicable structured data. | Manually compare markup with visible page content; validity does not establish correctness or guarantee a search feature. |

## Work sequence

### Phase 1 — Reconcile scope and establish coverage

1. Keep the proposal's ten SEO areas as the checklist; do not silently add new client commitments.
2. Review the current crawls and their README files. Confirm the recorded start URL, crawl scope, tool version, rendering, completion, URL totals, and free-limit status. The user confirmed on 2026-11-19 that My Transit Benefit has four pages and the crawl is complete; retain the missing dashboard/configuration details as evidence limitations, but do not treat page-count coverage as unresolved.
3. Compare discovered crawl URLs with public sitemap URLs and public navigation. Identify likely gaps and document them without expanding the agreed manual page scope.
4. Use the four user-confirmed My Transit Benefit URLs listed in the matrix as the complete page-level analysis scope for that website. Use the agreed 15 NITA URLs in the matrix (12 core pages plus three targeted editorial/template checks); do not imply that all 87 crawled HTML pages received manual review.
5. Update each matrix control with current status and evidence; keep unknowns open rather than inferring a pass.

**Output:** verified crawl baseline, URL/template inventory, confirmed My Transit Benefit page list, agreed NITA representative URL list, and initial matrix statuses.

### Phase 1 status — 2026-11-19

- **Complete:** proposal scope is mapped to matrix controls; crawl inventories and page-level scopes are documented; the user-confirmed four-page My Transit Benefit scope and agreed NITA 12+3 sample are recorded; selected pages were checked against crawl inventory and public navigation; robots files and all sitemap XML files were retrieved and compared with the crawl exports.
- **NITA coverage result:** the sitemap index references five child sitemaps with 1,286 unique URLs. Only 83 match the 2026-11-16 crawl after normalizing one HTTP/HTTPS scheme difference; 1,203 sitemap URLs do not appear in `internal_all.csv`. Four matches returned 302 and 79 returned 200. Eight crawled HTTP 200 HTML pages (blog pagination and tag archives) are absent from the sitemap. The cause and intended indexability of these URLs remain unverified; do not call unmatched URLs orphaned or invalid yet.
- **My Transit Benefit coverage result:** its sitemap contains five URLs. The four user-confirmed pages match 200 crawl records. The fifth URL, `/404`, is absent from the crawl and needs a response/intent check.
- The 496-URL NITA crawl completed below the free limit, so the sitemap discrepancy is not explained by the crawl stopping at 500. The original crawl did not discover most URLs listed in the sitemap; sitemap/section discovery behavior and the sitemap-only groups need Phase 2 analysis. Some sitemap URLs were updated after the crawl date.
- My Transit Benefit crawl completion and four-page site coverage are user-confirmed. The historical crawl's rendering mode, user-agent version, and exact dashboard totals remain undocumented; preserve that limitation rather than rerunning solely to reconstruct old settings.

**Next:** Phase 1 is closed with the coverage gap documented. Begin Phase 2 by triaging sitemap-only URLs by sitemap group, including a representative NITA press release; checking representative URLs/status and internal-link discovery; validating My Transit Benefit's `/404` sitemap entry; and analyzing the existing crawl's response/redirect/canonical/directive/structured-data exports. Decide whether the agreed NITA sample needs one targeted adjustment after inspecting the press-release content type. Do not label sitemap-only URLs orphaned or recommend removal without confirming their status and intended purpose.

### Phase 2 — Complete automated technical checks

1. Analyze crawlability, status codes, redirect destinations/chains, blocked resources, internal broken links, canonicals, indexability directives, and URL patterns.
2. Review titles, meta descriptions, and heading structure; group repeated template-level patterns and inspect affected page purpose before treating alerts as findings.
3. Review internal link pathways and sitemap inclusion/discovery against the crawl. Group the 1,203 NITA sitemap-only URLs by sitemap/content type, sample representative URLs and status codes (including historical press releases), and check public `robots.txt` and sitemap configuration directly. Validate My Transit Benefit's `/404` entry.
4. Extract structured data and validate applicable markup. Compare it with visible page content.
5. Review image SEO signals from the exports and representative rendered pages, including alternative text where available; classify whether a gap is SEO-related, accessibility-related, or both.
6. Convert only supported and contextually relevant issues into findings. Record controls without issues as verified in the matrix.

**Output:** dated technical evidence, a completed automated baseline for crawlable pages, matrix statuses, and validated technical findings.

### Phase 3 — Manually assess representative pages and mobile/performance

1. Inspect only the confirmed page URLs for each website in a browser, including rendered content and key public journeys. Confirm that titles, descriptions, headings, links, canonicals, and structured data align with page purpose.
2. Assess whether information architecture and internal links make the important content discoverable and understandable.
3. Identify qualitative keyword optimization opportunities from page topics, audience needs, geography, and publicly visible language. Do not claim search demand or keyword rankings without first-party or agreed external data.
4. Run representative PageSpeed Insights/Lighthouse tests in mobile and desktop modes. Record lab and field results separately and repeat unusual measurements before drawing conclusions.
5. Assess mobile SEO considerations in the rendered public experience, including content availability, navigation, page usability, and mobile performance signals.
6. Where useful, sample public search result titles/snippets for a small set of clearly documented queries. Treat this as qualitative context only.

**Output:** manual assessment notes, mobile/performance evidence, content/keyword opportunities, and updated matrix statuses.

### Phase 4 — Close controls and report recommendations

1. Review every matrix row for both websites. Each must have a final status, scope/method, date, and evidence or a reason it could not be assessed.
2. Validate all proposed findings against the authoring guide: observed evidence, user/searcher impact, recommendation, priority, complexity, and stable ID (`SEO-NITA-###` or `SEO-MTB-###`).
3. Keep verified controls visible in the matrix even when no finding results. Include only the most meaningful positive observations in the site report.
4. Separate technical issues, editorial recommendations, and items that require client/business confirmation. Do not prescribe indexing or redirect changes without confirming intended page purpose.
5. Consolidate actions in the cross-site roadmap and prepare the SEO section for final report review.

**Output:** completed SEO matrices, site reports, evidence links, prioritized recommendations, and inputs to the consolidated roadmap.

## Completion criteria

The SEO workstream is ready for consolidation when:

- All ten areas in the original proposal are represented in the matrix for both websites.
- Every control has an explicit final status and traceable evidence or a documented limitation.
- Crawl coverage and sampling limits are stated; no crawler sample is presented as exhaustive site coverage.
- Each finding is manually validated where practical and linked to its evidence and matrix control.
- Public-only limitations are explicit, and no first-party performance or comprehensive index claims are made.
- The site reports and consolidated recommendations are consistent with the matrix and authoring guide.

## Current work status

- Initial dated Screaming Frog exports exist for both websites.
- NITA crawl completion is recorded at 496 total URLs and 100% of discovered URLs. This does not establish exhaustive URL discovery.
- The user confirmed on 2026-11-19 that My Transit Benefit has four pages and its crawl is complete. The dashboard totals and rendering/configuration details were not recorded.
- The user confirmed on 2026-11-19 that the four URLs listed in the matrix are the complete My Transit Benefit page-level review scope and agreed to the 15-URL NITA sample (12 core pages plus three targeted checks).
- Initial NITA title and meta-description observations are recorded as draft findings in the site report. They remain subject to the matrix workflow and final audit review.
- Public robots and sitemap files have been collected and inventoried; interpretation of sitemap/crawl differences and blocked-resource impact, representative-page manual review, performance testing, mobile assessment, and public search-result sampling remain to be completed.
