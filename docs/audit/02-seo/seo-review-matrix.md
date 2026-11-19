# SEO Review Matrix — NITA websites

Use this matrix to track every review area committed in the [project proposal](../../project-overview.md#22-search-engine-optimization-seo). It records checks that pass as well as issues. A matrix status is not a finding; findings are created only for evidence-backed issues or opportunities that merit action. Status definitions follow the [authoring guide](../authoring-guide.md#3-review-controls-and-coverage).

This matrix is the single place for coverage detail and caveats; the site reports link here instead of repeating them.

## Page-level review scope

Crawl-wide technical checks may use the available exports within their recorded coverage limits. Manual page-level review uses the URLs below.

**My Transit Benefit — confirmed complete four-URL scope (user confirmed 2026-11-19):**

- [Homepage](https://www.mytransitbenefit.com/)
- [Behind the benefits](https://www.mytransitbenefit.com/behind-the-benefits)
- [Employees](https://www.mytransitbenefit.com/employees)
- [Employers](https://www.mytransitbenefit.com/employers)

**NITA — agreed representative URLs (12 core pages plus 3 targeted template checks; confirmed 2026-11-19):**

Core page sample:

| URL | Why it represents the content or template |
| --- | --- |
| [Homepage](https://nita.illinois.gov/) | Main entry point, global information architecture, and currently featured announcements and calls to action. |
| [Riders](https://nita.illinois.gov/riders) | Rider audience hub and route into the core service tasks. |
| [How to ride](https://nita.illinois.gov/riders/how-to-ride) | Trip-planning guide, maps, and handoffs to CTA, Metra, and Pace information. |
| [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) | High-value, multi-agency fares/payment page with detailed tables and date-sensitive information. |
| [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs) | Eligibility, application steps, registration locations, and program handoffs. |
| [Access Program](https://nita.illinois.gov/riders/access) | Income-based fare program; review how it is distinguished from the separate “Access to Transit” infrastructure program. |
| [Accessible transit](https://nita.illinois.gov/riders/accessible-transit) | ADA Paratransit information, application/certification, eligibility, appeal, and alternative services. |
| [Communities](https://nita.illinois.gov/communities) | Municipal/local-government audience hub. |
| [Community Planning](https://nita.illinois.gov/communities/community-planning) | Core planning program, current project list, and related informational content. |
| [Access to Transit](https://nita.illinois.gov/communities/access-to-transit-program) | Separate capital/infrastructure program with project tables and investment outcomes. |
| [2027 NITA Regional Budget](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget) | Current, time-sensitive funding content, public engagement, and comment form. |
| [How the system is working](https://nita.illinois.gov/region/how-system-working) | Regional explanatory content and handoff to system data/reporting. |

Targeted editorial/template checks:

| URL | Why it represents the content or template |
| --- | --- |
| [On Track blog](https://nita.illinois.gov/blog) | Blog listing, pagination, and category/archive structure, including the transition from RTA-authored historical posts to NITA posts. |
| [NITA expands the Access fare pilot](https://nita.illinois.gov/blog/2026/10/01/nita-expanding-access-pilot-program-to-cta-and-pace-starting-october-1-offering-income-based-reduced-fare-transit-regionwide) | Recent article template about a high-interest rider program; review date, figures, links, and relationship to the program page. |
| [CTA blog tag archive](https://nita.illinois.gov/blog/tags/cta) | Targeted check of one tag archive associated with `SEO-NITA-001` and repeated archive metadata. |

The 15 URLs are a representative sample, not a page-by-page review of the 1,613 HTML pages in the crawl baseline. The sitemap includes 419 press-release URLs, a content type not in the sample; in Step 2, inspect a representative press release and the [press-release index](https://nita.illinois.gov/news/press-releases), then decide whether to add one targeted sample URL.

## Public content inventory and review priorities

The 2026-11-19 crawl baseline contains 1,613 HTML pages returning 200, most of them blog posts, press releases, tag archives, and paginated listings; the core sections (About NITA, Communities, Riders, Region, Transit Funding) account for fewer than 100 pages. The public global navigation separates Region, Communities, Riders, Transit Funding, News, and About NITA, so the website serves several audiences and intents.

Manual review priorities:

- **Rider decision content:** trip planning, fares, reduced-fare eligibility, Access, and accessible transit. These pages combine NITA, CTA, Metra, and Pace information; confirm agency ownership of each step and the currency of links, dates, fares, and eligibility details.
- **Local-government program content:** Community Planning and Access to Transit have distinct audiences and current project information; check terminology, descriptive titles, and paths from the Communities hub.
- **Time-sensitive content:** on 2026-11-19 the homepage still invited users to register for a November 12 budget hearing, and the “Paying for your ride” page labels some Metra fare tables “Effective February 1, 2024.” Validate with current sources before classifying either as a finding.
- **Program naming:** “Access Program” (reduced fares) and “Access to Transit” (pedestrian/bicycle infrastructure) need clearly distinct link labels and page context.
- **Editorial transition:** the blog states that posts published before September 1, 2026 were written by RTA. Check that older material is clearly dated and not presented as current NITA guidance. Press-release URLs also remain under the legacy `/about-rta/press-releases/` path while the index lives at `/news/press-releases`; record this as context. Do not recommend changing established URLs without a redirect plan and client agreement.
- **Content depth:** 71 of 1,613 pages have fewer than 200 extracted words in the 2026-11-19 baseline. Use this to guide human review only.

## Review controls and current status

| Proposal area / control | What to verify | Primary method and evidence | NITA status | My Transit Benefit status |
| --- | --- | --- | --- | --- |
| Crawl configuration and coverage | Crawl settings (depth limit, rendering, extraction options) support the conclusions drawn from the exports. | Crawl READMEs: [NITA link discovery](../../../evidence/crawls/link-discovery/2026-11-19/README.md), [NITA List mode](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/README.md), [My Transit Benefit](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/README.md). | **Verified — no issue observed.** 2026-11-19 baseline: complete link discovery (no depth limit, queue empty, max depth 66) plus Screaming Frog List mode over 1,736 URLs. Limits: raw HTML only, no structured-data extraction. Supersedes the 2026-11-16 crawl. | **Verified — no issue observed.** 2026-11-19 full Spider crawl with default configuration, 64 URLs; four HTML pages. |
| Technical SEO and crawlability | Status codes, redirect destinations/chains, blocked resources, broken internal links, and coverage gaps. | Screaming Frog exports; curl header checks. | **Finding recorded.** `SEO-NITA-004`: 141 internal links to legacy documents redirect to HTTP. Needs Step 2 analysis: 50 internal URLs return 404, 2 malformed links return 403, 2 linked PDFs return 404. | **In progress.** Four pages return 200; links to `rtachicago.org` redirect; `unpkg.com` `@latest` script redirects. Review in Step 2. |
| HTTPS and protocol consistency | HTTP requests redirect to HTTPS; canonicals, internal links, and redirects use HTTPS. | curl header checks; `internal_all.csv`; canonicals. | **Finding recorded.** `SEO-NITA-003`: HTTP pages return 200 without redirecting. Related evidence: one internally linked HTTP press-release URL; one tag archive canonical pointed to HTTP in the crawl but to HTTPS on 2026-11-19. | **Verified — no issue observed.** On 2026-11-19, HTTP and non-www homepage requests returned 301 to `https://www.mytransitbenefit.com/`. Only the homepage was tested. |
| Indexability and search engine accessibility | Directives, canonicals, robots controls, resource access, and soft 404 responses. Do not infer Google index status. | Screaming Frog `Directives` and `Canonicals`; curl; browser spot checks. Search Console excluded. | **Finding recorded.** `SEO-NITA-005`: blog pagination pages canonicalize to `/blog`. Needs validation: `/404` returns 200 and is in the sitemap; out-of-range pagination (`/blog/p100`, `/news/press-releases/p100`) returns 200. Directive review remains. | **Finding recorded.** `SEO-MTB-001`: `/404` returns 200, is indexable, and is in the sitemap. All four confirmed pages have self-referencing canonicals. |
| Page titles | Missing/duplicate titles and whether titles describe the page. | Screaming Frog `Page Titles`; curl; manual review. | **Finding recorded.** `SEO-NITA-001`: all 155 tag archive URLs use the brand-only title. 1,199 of 1,613 titles exceed about 580 px; review templates in Step 2. | **Finding recorded.** `SEO-MTB-002`: all four titles contain a literal ellipsis. |
| Meta descriptions | Missing/duplicate descriptions and whether descriptions summarize priority pages. | Screaming Frog `Meta Description`; manual comparison. | **Finding recorded.** `SEO-NITA-002`: 292 pages share the generic description. | **In progress.** Four descriptions are present and distinct; manual validation remains. |
| Heading structure | Heading presence, hierarchy, and meaning on representative pages. | Screaming Frog `H1`/`H2`; manual rendered review. | **In progress.** All 1,613 pages have an H1; 24 have more than one. Multiple H1s are not an SEO defect by themselves; review meaning and coordinate with accessibility. | **In progress.** H1s are campaign slogans rather than topic statements (for example “Your Tax Savings Starts Here!”); Employees has a second H1 “Login.” Assess in Step 3 as a content/keyword opportunity. |
| URL structure and internal linking | URL clarity/consistency, navigation and contextual links to priority pages, broken links, and crawl paths. | Crawl URL/link exports plus manual navigation. | **In progress.** Older posts and press releases are reachable only through sequential pagination, up to 66 clicks from the homepage; press releases sit under `/about-rta/` while the index is `/news/press-releases`. Assess in Step 2 and Step 3. | **Not assessed.** |
| Sitemap configuration | Sitemap accessibility, included URL types/status/canonicals, comparison with discovered pages. | Public sitemap XML and [`sitemap-crawl-comparison.csv`](../../../evidence/public-technical/2026-11-19/sitemap-crawl-comparison.csv). | **In progress.** 1,280 of 1,286 sitemap URLs are reachable through links; 6 are not, including `/404` (returns 200). 450 linked HTML URLs are not in the sitemap (mainly tag archives and pagination). Four listed URLs return 302 to external tools. See [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv). | **Finding recorded.** `SEO-MTB-001` (`/404` listed). The four confirmed pages match 200 crawl entries. |
| `robots.txt` configuration | Public directives and sitemap declarations; blocked paths/resources versus page purpose. | Public `robots.txt` files and crawl evidence. | **In progress.** Disallows `/cpresources/`, `/vendor/`, `/.env`, `/cache/`; blocks Freeform form CSS/JS, reCAPTCHA, and a GTM integration script. Confirm rendering impact with a rendered test. | **In progress.** Same directives and blocked asset types. |
| Structured data and schema markup | Markup presence, syntax/eligibility, and match with visible facts. | Rich Results Test or Schema.org Validator and curl on the page-level sample (structured-data extraction is not available in the free Screaming Frog version). | **Needs manual validation.** The 2026-11-16 export reports zero types, but the homepage contains a JSON-LD `WebSite` graph; the export is not valid evidence of absence. | **Needs manual validation.** Same export issue; the JSON-LD `WebSite` graph references `https://nita.illinois.gov#identity`. Confirm the intended publisher identity. |
| Page performance and Core Web Vitals | Representative templates; lab diagnostics separate from field Core Web Vitals. | Dated PageSpeed Insights/Lighthouse runs, mobile and desktop. | **Not assessed.** | **Not assessed.** |
| Mobile SEO considerations | Priority content and links accessible and usable on mobile. | Manual mobile review; PSI mobile runs. | **Not assessed.** | **Not assessed.** |
| Content organization and keyword optimization opportunities | Information grouping, page purpose, audience language, topical coverage, qualitative query alignment. | Public navigation/content review; documented public search-feature sample. | **In progress.** CTA tag archive spot-checked; broader review remains. | **Not assessed.** |
| Image alternative text | Alt text on meaningful images in representative pages. | Screaming Frog Spider image exports (My Transit Benefit); rendered review of the NITA page-level sample. | **Not assessed.** List mode does not crawl images; review on the page-level sample. | **Verified — no issue observed.** None of the 31 crawled images is missing alt text or the alt attribute (2026-11-19 crawl). Whether the alt text is meaningful is reviewed in the accessibility section. |
| Technical issues that may affect organic visibility | Synthesis of validated controls; avoid duplicate findings. | Cross-check completed matrix rows. | **In progress.** | **In progress.** |

## Evidence and review log

Keep source exports under the dated `evidence/crawls/screaming-frog/` folders read-only.

| Date | Website | Control(s) reviewed | Method / evidence | Reviewer notes or follow-up |
| --- | --- | --- | --- | --- |
| 2026-11-16 | NITA | Crawl inventory and exports | [Screaming Frog exports and README](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/) | 496 URLs, 100% of discovered queue. Depth limit and extraction settings not recorded. |
| 2026-11-16 | My Transit Benefit | Crawl inventory and exports | [Screaming Frog exports and README](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-16/) | Completion, rendering, and configuration not recorded. |
| 2026-11-18 | NITA | Blog archive title/content spot check | [CTA tag archive](https://nita.illinois.gov/blog/tags/cta) | Archive lists CTA-related posts; title does not identify the topic. |
| 2026-11-18 | My Transit Benefit | Public page spot checks | [Homepage](https://www.mytransitbenefit.com/), [employees](https://www.mytransitbenefit.com/employees), [employers](https://www.mytransitbenefit.com/employers) | Surface-level review; enrollment journeys not submitted. |
| 2026-11-19 | Both websites | Page-level scope | User confirmed the four My Transit Benefit URLs and the 15-URL NITA sample. | Agreed URLs appear in crawl inventory and public navigation. |
| 2026-11-19 | Both websites | Robots and sitemap review | [Robots/sitemap files and URL-level comparison](../../../evidence/public-technical/2026-11-19/README.md) | Unmatched URLs are not automatically orphan or error findings. |
| 2026-11-19 | Both websites | Protocol, redirects, pagination, soft 404, titles, JSON-LD presence | [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt) (curl 8.7.1) | Supports `SEO-NITA-003`–`005` and `SEO-MTB-001`–`002`; shows the structured-data exports are unreliable and a probable crawl depth limit. |
| 2026-11-19 | Both websites | Crawl baseline (Step 1 redo) | [Link discovery](../../../evidence/crawls/link-discovery/2026-11-19/README.md), [NITA List mode](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/README.md), [My Transit Benefit crawl](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/README.md) | Step 1 closed. 2026-11-16 crawls superseded; findings re-pointed and counts updated. |
| 2026-11-19 | Both websites | Crawl approach and access decisions | Team decision; URL estimates from the sitemap inventory and live pagination probes. | Step 1 crawl baseline redone with the free version (no paid license): NITA via link discovery plus List mode; My Transit Benefit via one full spider crawl. No Search Console or analytics access requested from DHD at this stage. |

## Related reports

- [NITA SEO report](nita-illinois-gov.md)
- [My Transit Benefit SEO report](mytransitbenefit-com.md)
- [SEO work plan](seo-audit-plan.md)
