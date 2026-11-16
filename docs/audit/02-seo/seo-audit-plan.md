# SEO Audit Plan — NITA websites

## Objective

Assess technical discoverability, indexability, on-page signals, content relevance, structured data, mobile performance, and organic search performance for:

- [nita.illinois.gov](https://nita.illinois.gov)
- [mytransitbenefit.com](https://mytransitbenefit.com)

The review is limited to information publicly available by visiting the websites and public search results. No Search Console, analytics, CMS, hosting, or other authenticated access will be used. It identifies issues and opportunities; it does not promise rankings or traffic gains. Search engine guidance and public performance data can change, so record the review date and tool versions with each observation.

## Tools and access

### Public checks (no account access required)

| Tool | Use | Limits |
| --- | --- | --- |
| Screaming Frog SEO Spider (free) | Crawl up to 500 URLs per website; export status codes, redirects, titles, descriptions, headings, canonicals, directives, links, and image attributes. | The free version is capped at 500 URLs per crawl and restricts saving, configuration, JavaScript rendering, and integrations. If a site exceeds the cap, record the coverage limit and use a representative sample under the agreed public-only scope. [Product details](https://www.screamingfrog.co.uk/seo-spider/) |
| PageSpeed Insights / Lighthouse | Repeat mobile and desktop lab checks on representative templates; capture Core Web Vitals field data when available. | Lab results are diagnostic snapshots, not a substitute for real-user data. CrUX field data is only available when there is sufficient data for a URL or origin. [About PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about) |
| Browser and search-result spot checks | Inspect rendered pages, public search snippets, redirects, robots.txt, sitemap availability, and how key pages appear in search. | Search results vary by location, device, and time; they are samples, not a complete index report. |
| Structured Data Testing Tool (Google Rich Results Test) and Schema.org Validator | Validate applicable markup and identify syntax/eligibility issues. | A valid result does not establish that the markup is accurate, useful, or guaranteed to display. Google only supports rich result features for specific schema types. [Google structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) |

### Access boundary

No account access or private data is part of this audit. Use public pages, public search result samples, public technical endpoints, and openly available testing tools only. Where public evidence cannot establish index status, traffic, query demand, conversions, or server configuration, explicitly mark that area as not verifiable within scope rather than requesting access.

## What can be automated

I can collect and organize repeatable public observations, and analyze supplied exports:

- Discover linked URLs and compare crawl results against XML sitemaps.
- Report HTTP errors, redirect chains/loops, broken internal links, orphan candidates (when sitemap and crawl data are available), duplicate or missing titles/descriptions/headings, canonical and robots directives, and common URL-pattern issues.
- Extract headings, links, image alt attributes, language hints, and structured data for review; flag missing or inconsistent patterns.
- Run repeatable mobile/desktop PageSpeed checks on a representative template sample and summarize lab/field results separately.
- Compare publicly visible search-result samples for selected queries, recording the query, location/language context where known, date, result URL, title, and snippet. This is a qualitative sample and not a substitute for query-volume or performance data.
- Maintain a findings log with source, date, method, URL, priority, and complexity; deduplicate repeated template-level issues and draft a prioritized action list.

Automation produces candidates and evidence, not final judgments. Crawler warnings need validation against page purpose and site rules; a technically valid signal can still be wrong for the content.

## What needs manual review

- Choose representative templates and likely important user tasks from public navigation and page content. Crawl coverage alone cannot establish business importance.
- Judge whether the page answers the intended user's question, uses clear and accurate terminology, matches likely query intent, and has enough useful context. This includes Spanish/English language intent where applicable.
- Review search snippets and likely target queries in their real context, including geography and user needs. Without first-party search data, query prioritization is qualitative and must be labeled as such.
- Confirm whether a URL should be indexed, redirected, canonicalized, or excluded. The correct choice depends on content ownership, policy, task flow, and duplicate-page intent.
- Verify structured data reflects visible page facts and an actually applicable Google-supported feature.
- Assess internal-link usefulness, navigation labels, trust/authority cues, public-sector accuracy, and whether content is current. These require subject-matter confirmation.
- Interpret performance results alongside the page's purpose and user impact. A Lighthouse score is not a ranking or conversion diagnosis.
- Treat client priorities and internal business outcomes as unknown unless they are stated in public content; qualify recommendations where that context could change priority.

## Work plan

### Step 1 — Confirm scope and inventory

1. Record the publicly observable audiences, tasks, language, geography, navigation, and any recent changes that are mentioned on the sites.
2. Check each site's public robots.txt and sitemap endpoints and build an initial URL/template inventory.
3. Select approximately 8–12 representative pages per website, including the homepage, primary navigation destinations, benefit/eligibility/enrollment pages, supporting content, and contact/help pages. Adjust the sample to actual site structure and public discoverability.

**Output:** public scope, representative URL list, and any exclusions or unobservable items.

### Step 2 — Automated technical baseline

1. Crawl each domain with Screaming Frog in standard mode, respecting site crawl rules and avoiding aggressive request rates.
2. Record crawl coverage and the 500-URL limit; compare discovered pages with sitemap URLs and manually review any crawl gaps.
3. Check status codes, redirect destinations, canonicals, indexability directives, titles, meta descriptions, headings, internal links, image alt presence, language signals, and structured data.
4. Run PSI/Lighthouse on the selected templates in mobile and desktop modes; repeat anomalous results before treating them as findings.
5. Save dated exports/screenshots or shareable PSI links as audit evidence.

**Output:** crawl and performance evidence, with automated alerts separated from verified findings.

### Step 3 — Public search observations and manual assessment

1. Sample public search results for a small set of likely user queries for each website; record date, query, language/location context, visible title/snippet, and landing page. Do not infer search volume, ranking history, or comprehensive index coverage from these samples.
2. Review public sitemap and robots.txt behavior and inspect the selected priority URLs directly. Public checks cannot reproduce Search Console's site-wide indexing reports or Googlebot's full historical view.
3. Manually assess query intent, content completeness and clarity, metadata accuracy, internal-link pathways, page purpose, SERP context, and structured data truthfulness.
4. Mark traffic, clicks, impressions, CTR, conversions, and non-public indexing diagnostics as not assessed.

**Output:** validated findings and evidence, including items that cannot be concluded from public information alone.

### Step 4 — Findings and recommendations

1. Write findings separately for NITA and My Transit Benefit, following the audit authoring guide and stable IDs (`SEO-NITA-001`, `SEO-MTB-001`, etc.).
2. Prioritize based on reach and impact to critical user tasks, not a tool score alone; estimate implementation complexity separately.
3. Group repeated template issues, identify quick fixes, and distinguish engineering, CMS/editorial, analytics, and further-investigation actions.
4. Carry public-evidence recommendations into the consolidated roadmap, clearly marking assumptions that depend on non-public business context.

**Output:** completed SEO findings files, evidence references, and SEO actions ready for the cross-site roadmap.

## Suggested schedule

| Work | Estimate |
| --- | --- |
| Scope and public URL inventory | 0.5 day |
| Crawls and technical baseline for both websites | 0.5–1 day |
| Performance sampling and public search-result review | 0.5–1 day |
| Manual content/intent review and client clarification | 1–2 days |
| Findings, QA, and prioritization | 0.5–1 day |

Expected effort is about **3–5 working days** for the SEO workstream. This fits within the project proposal's broader 3–4 week audit timeline.

## Decisions and dependencies

- Use only no-cost/public tools and public data under the agreed scope. Start with the Screaming Frog free crawl; document any coverage limit rather than adding paid access.
- Do not claim actual Google query performance, impressions, clicks, CTR, conversion outcomes, or comprehensive index status. Those data are outside this public-only scope; mark them not assessed.
- Search-result samples are time- and context-dependent snapshots, not reliable rank tracking or a measure of query demand.
- Keep the initial audit read-only. Findings may recommend changes, but implementation and post-change measurement are separate work.
