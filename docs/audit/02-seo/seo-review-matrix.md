# SEO Review Matrix — NITA websites

Use this matrix to track every review area committed in the [project proposal](../../project-overview.md#22-search-engine-optimization-seo). It records checks that pass as well as issues. A matrix status is not a finding; findings are created only for evidence-backed issues or opportunities that merit action.

## Status definitions

- **Not assessed:** No review has been completed for this control.
- **In progress:** Some review is complete, but the full control is not.
- **Verified — no issue observed:** The documented checks are complete and found no issue within their stated scope and limits.
- **Finding recorded:** A supported issue or opportunity is documented in the site report and linked by ID.
- **Needs manual validation:** Automated or incomplete evidence needs human review before a conclusion.
- **Not verifiable in public scope:** The check requires private access, first-party data, or server configuration excluded from this audit.
- **Not applicable:** The control does not apply; explain why.

## Review controls and current status

### Page-level review scope

The My Transit Benefit page-level scope is user-confirmed. The NITA list below is the agreed representative sample, selected from the full crawl inventory, public navigation, key user tasks, content types, and current SEO observations. Crawl-wide technical checks may use the available exports while respecting their recorded coverage limits.

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
| [On Track blog](https://nita.illinois.gov/blog) | Blog listing and category/archive structure, including the transition from RTA-authored historical posts to NITA posts. |
| [NITA expands the Access fare pilot](https://nita.illinois.gov/blog/2026/10/01/nita-expanding-access-pilot-program-to-cta-and-pace-starting-october-1-offering-income-based-reduced-fare-transit-regionwide) | Recent article template about a high-interest rider program; review date, figures, links, and relationship to the program page. |
| [CTA blog tag archive](https://nita.illinois.gov/blog/tags/cta) | Targeted check of one tag archive associated with `SEO-NITA-001` and repeated archive metadata. |

The 12 core URLs cover both audience hubs, priority rider tasks, community programs, current budget content, and regional information. Three targeted editorial checks validate the blog listing/article/archive patterns and an existing metadata observation. Together, the 15 URLs are a representative sample, not a page-by-page review of all 87 HTML records or the larger sitemap corpus. The sitemap adds 419 press-release URLs, with only one URL matching the crawl after scheme normalization. In Phase 2, inspect a representative press release and its archive/context, then decide whether this content type warrants replacing or adding a targeted sample URL. The agreed sample remains unchanged until that review.

### Public content inventory and preliminary assessment

The dated Screaming Frog export contains 87 HTTP 200 HTML records with titles. By URL grouping, the largest clusters are Blog (36), About NITA (12), Communities (10), Riders (9), Region (5), and Transit Funding (5); the remainder includes News, contact, careers, and policy pages. The public global navigation likewise separates Region, Communities, Riders, Transit Funding, News, and About NITA. The site therefore has multiple distinct audiences and content intents, rather than one single rider-information purpose.

The content inventory points to these review priorities:

- **Rider decision content:** trip planning, fares, reduced-fare eligibility, Access, and accessible transit. These pages combine information from NITA, CTA, Metra, and Pace, so confirm which agency owns each step and that links, dates, fares, and eligibility details remain current.
- **Local-government program content:** Community Planning and Access to Transit have distinct audiences and provide current project information, reports, and tables. Check terminology, descriptive titles, and paths from their shared Communities hub.
- **Current public-policy content:** the 2027 budget page and homepage have time-sensitive calls to action. On 2026-11-19, the homepage still invited users to register for a November 12 hearing; confirm whether that past date should be removed or reframed. Treat this as a content-currency check, not a confirmed SEO finding.
- **Program naming:** “Access Program” is a reduced-fare offering for eligible riders; “Access to Transit” is a pedestrian/bicycle infrastructure program. Review internal-link labels and page context so searchers can tell them apart.
- **Editorial transition:** the blog states that posts published before September 1, 2026 were written by RTA and are retained as historical content. Check that older material remains clearly dated and does not present superseded agency/program information as current.
- **Fare information:** the live “Paying for your ride” page labels some Metra fare tables “Effective February 1, 2024.” Validate these figures and effective dates with the transit operators before calling them current or outdated.

Screaming Frog reports a median text word count of 807 across the 87 HTML records (range 76–3,538); eight records are below 200 words. Word count includes only what the crawler extracted and does not measure usefulness, completeness, or quality. Use it to guide human review, not as a standalone SEO issue.

| Proposal area / control | What to verify | Primary method and evidence | NITA status | My Transit Benefit status |
| --- | --- | --- | --- | --- |
| Technical SEO and crawlability | Crawl discovers public, internally linked pages and resources; record status codes, redirect destinations/chains, blocked resources, broken internal links, and coverage gaps. | Screaming Frog exports, crawl summary, public navigation and sitemap comparison. | **In progress.** Crawl completed at 496 discovered URLs; discovered-URL coverage is not exhaustive. | **In progress.** User confirmed on 2026-11-19 that the site has four pages and the crawl is complete; URL-level status/link review remains. |
| Indexability and search engine accessibility | Review indexability directives, canonicals, robots controls, resource access, and whether representative page content is publicly accessible as rendered. Do not infer Google index status. | Screaming Frog `Directives` and `Canonicals`; public `robots.txt`; browser spot checks. Search Console excluded. | **In progress.** Directives export exists; public robots and representative-page checks remain. | **In progress.** Directives/canonical exports exist; coverage and public robots/page checks remain. |
| Page titles | Check missing/duplicate titles and whether representative titles describe the corresponding page. | Screaming Frog `Page Titles`; manual page-purpose and public-page spot checks. | **Finding recorded.** `SEO-NITA-001` covers seven tag archive titles; extend manual review to selected templates. | **In progress.** Four exported HTML titles are distinct; representative manual validation remains. |
| Meta descriptions | Check missing/duplicate descriptions and whether descriptions accurately summarize priority pages. | Screaming Frog `Meta Description`; manual content comparison. | **Finding recorded.** `SEO-NITA-002` covers 13 repeated descriptions; validate page priorities and intent. | **In progress.** Four exported HTML descriptions are distinct; manual validation remains. |
| Heading structure | Check heading presence, hierarchy, and meaning on representative pages; treat crawler counts as prompts, not defects by themselves. | Screaming Frog `H1` / `H2`; manual rendered-page review. | **In progress.** Exports show H1s present; multiple headings and hierarchy need context. | **In progress.** Four-page export exists; manual structure review remains. |
| URL structure and internal linking | Review URL clarity/consistency, navigation and contextual links to priority pages, broken links, and crawl paths. | Crawl URL/link exports plus manual navigation and representative journeys. | **Not assessed.** | **Not assessed.** |
| Sitemap configuration | Locate public XML sitemap(s), inspect accessibility and included URL types/status/canonicals, and compare listed URLs with discovered pages. | Public sitemap XML files and [`sitemap-crawl-comparison.csv`](../../../evidence/public-technical/2026-11-19/sitemap-crawl-comparison.csv). | **In progress.** Sitemap index and five children contain 1,286 URLs, including 419 press releases; 83 match the crawl (including one HTTP/HTTPS normalization) and 1,203 do not. Eight crawled 200 HTML pages are absent from the sitemap. Phase 2 should sample the press-release corpus and determine why URL sets differ; no orphan/removal conclusion yet. | **In progress.** Sitemap has five URLs: the four confirmed pages match 200 crawl entries; `/404` is not in the crawl and needs validation. |
| `robots.txt` configuration | Locate and inspect public directives and sitemap declarations; compare any blocked paths/resources with observed page purpose. | Public `robots.txt` files and crawl evidence. | **In progress.** File declares the sitemap index and disallows `/cpresources/`, `/vendor/`, `/.env`, and `/cache/`; crawl reports four blocked `cpresources` assets. Confirm whether blocked assets affect search rendering. | **In progress.** File declares the sitemap and disallows `/cpresources/`, `/vendor/`, `/.env`, and `/cache/`; crawl reports four blocked resources. Confirm whether blocked assets affect search rendering. |
| Structured data and schema markup | Identify markup, validate syntax/eligibility where applicable, then compare properties with visible page facts. | Screaming Frog `Structured Data`; Rich Results Test or Schema.org Validator; manual content check. | **Needs manual validation.** Automated export needs suitability/content validation. | **Needs manual validation.** Automated export needs suitability/content validation. |
| Page performance and Core Web Vitals | Test representative page templates; separate lab diagnostics from field Core Web Vitals and record data availability. | Dated PageSpeed Insights/Lighthouse runs, mobile and desktop; repeat anomalous results. | **Not assessed.** | **Not assessed.** |
| Mobile SEO considerations | Confirm priority content and links remain accessible and usable on mobile; consider mobile performance observations. | Manual mobile browser review of representative pages and journeys; PSI mobile runs. | **Not assessed.** | **Not assessed.** |
| Content organization and keyword optimization opportunities | Assess information grouping, page purpose, user/audience language, topical coverage, and qualitative query alignment. Do not claim keyword demand/rank without data. | Public navigation/content review, representative-page sample, optional dated public search-result sample. | **In progress.** CTA tag archive spot-checked; broader page/topic review remains. | **Not assessed.** |
| Technical issues that may affect organic visibility | Synthesize relevant validated crawlability, indexability, metadata, structured data, performance, and mobile controls; avoid duplicate findings. | Cross-check completed matrix controls and linked evidence. | **In progress.** Initial metadata findings only. | **Not assessed.** |

## Evidence and review log

Add dated evidence links as controls are reviewed. Keep source exports under the dated `evidence/crawls/screaming-frog/` folders read-only.

| Date | Website | Control(s) reviewed | Method / evidence | Reviewer notes or follow-up |
| --- | --- | --- | --- | --- |
| 2026-11-16 | NITA | Crawlability; titles; descriptions; headings; directives; canonicals; structured data | [Screaming Frog exports and README](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/) | Crawl marked 100% complete at 496 total URLs; discovered URLs are not proof of exhaustive coverage. |
| 2026-11-16 | My Transit Benefit | Crawlability; titles; descriptions; headings; directives; canonicals; structured data | [Screaming Frog exports and README](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-16/) | Completion, total, rendering, and user-agent details not recorded. |
| 2026-11-18 | NITA | Blog archive title/content spot check | [CTA tag archive](https://nita.illinois.gov/blog/tags/cta) | Confirms the checked archive lists CTA-related posts; other tag archives still need manual checks. |
| 2026-11-18 | My Transit Benefit | Public page spot checks | [Homepage](https://www.mytransitbenefit.com/), [employees](https://www.mytransitbenefit.com/employees), [employers](https://www.mytransitbenefit.com/employers) | Surface-level review only; key enrollment journeys not submitted or completed. |
| 2026-11-19 | My Transit Benefit | Crawl coverage confirmation | User confirmed the site has four pages and the crawl is complete. | Dashboard totals and crawl rendering/configuration details remain unrecorded; four-page coverage is no longer an open question. |
| 2026-11-19 | My Transit Benefit | Page-level review scope | User confirmed the four URLs listed above are the complete analysis scope. | Use these four URLs for manual review and page-level checks. |
| 2026-11-19 | NITA | Public content inventory and representative URL selection | Review of the 2026-11-16 Screaming Frog page inventory, current public navigation/content, and original proposal scope; user confirmed the proposed set. | Agreed 15-URL sample above: 12 core pages plus three targeted editorial/template checks. |
| 2026-11-19 | Both websites | Public navigation and URL-scope check | Compared agreed page-level URL lists with public navigation and crawl inventories. | Agreed URLs appear in crawl inventory and public navigation. |
| 2026-11-19 | Both websites | Robots and sitemap review | [Downloaded robots/sitemap files and URL-level crawl comparison](../../../evidence/public-technical/2026-11-19/README.md). | NITA has 1,286 sitemap URLs with a large crawl-discovery gap; My Transit Benefit sitemap includes `/404` in addition to the four confirmed pages. These require Phase 2 validation; unmatched URLs are not automatically orphan/error findings. |

## Related reports

- [NITA SEO report](nita-illinois-gov.md)
- [My Transit Benefit SEO report](mytransitbenefit-com.md)
- [SEO work plan](seo-audit-plan.md)
