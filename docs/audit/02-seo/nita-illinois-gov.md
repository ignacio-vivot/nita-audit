# Search Engine Optimization (SEO) — nita.illinois.gov

## Assessment Scope

- **Website:** [nita.illinois.gov](https://nita.illinois.gov/)
- **Review date:** 2026-11-19
- **Pages, templates, or journeys reviewed:** Crawl-level review of 1,736 URLs (1,613 HTML pages returning 200), combining the 1,286-URL public sitemap with every HTML URL reachable through internal links; dated live header and HTML checks on 2026-11-19; navigation and spot checks across the agreed 16-URL sample listed in the [SEO review matrix](seo-review-matrix.md#page-level-review-scope). Detailed manual evaluation of the sample is in progress.
- **Methods and tools:** link-discovery script with no depth limit ([B1 README](../../../evidence/crawls/link-discovery/2026-11-19/README.md)); Screaming Frog SEO Spider 25.1 free version, List mode, Text Only ([B2 README](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/README.md)); curl 8.7.1 ([`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)); public browser review; Google Search Central guidance.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** The most consequential observation so far is protocol handling: the website serves pages over unencrypted HTTP without redirecting to HTTPS, and 141 internal links to legacy documents redirect to HTTP destinations. Canonical tags point to HTTPS, which limits but does not remove the risk of split signals and unencrypted visits. Redirect handling for the former coalition pages is broken: a six-hop chain ends in a 404. Two current pages, including Paying for your ride, link to “not found” pages, and 102 blog posts and press releases, mostly from the RTA period, contain broken internal links. On-page metadata is the other main theme: the homepage title is “Home”, core page titles are slogans rather than topics, and the CMS truncates most titles and descriptions with an ellipsis. Paginated listings declare their first page as canonical. Metadata observations are lower priority: 155 tag archive URLs share a brand-only title, and 292 pages share one generic meta description.

The 2026-11-19 crawl baseline replaces the 2026-11-16 crawl, which stopped short of deep pagination ([method](seo-audit-plan.md#crawl-baseline-method)). With complete link discovery, only 6 of the 1,286 sitemap URLs are not reached through internal links; the earlier gap of 1,203 URLs was a crawl artifact. The new baseline also surfaces items for Step 2: 50 internal links returning 404, content up to 66 clicks from the homepage, and malformed links in older posts. This review does not establish rankings, clicks, or Google index status.

## Findings

### HTTP pages load without redirecting to HTTPS

- **Finding ID:** SEO-NITA-003
- **Page or component:** Website-wide protocol handling; confirmed on every template tested over HTTP (homepage, rider, community, funding, blog listing and post, press-release listing and release, tag archive, and a PDF).
- **Priority:** Medium
- **Evidence:** On 2026-11-19, `curl -sI` requests to `http://nita.illinois.gov/` and `http://nita.illinois.gov/riders` returned `HTTP/1.1 200 OK` with no `Location` header. On 2026-11-20, HTTP requests to ten URLs across templates, including a PDF, all returned 200 without redirecting ([`step2a-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2a-live-checks.txt)). The `www.` host redirects correctly to `https://nita.illinois.gov/`, so only the HTTP scheme is affected. The HTTPS homepage returned no `Strict-Transport-Security` header. The HTTP homepage declares `https://nita.illinois.gov/` as canonical. The 2026-11-19 crawl baseline also found two internal links that use `http://` (to a press release and to `/popa`) and two tag archives whose canonical uses `http://` (`/blog/tags/chicago`, `/blog/tags/moving-you`). See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt), [`pages.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/pages.csv), and [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv). By contrast, My Transit Benefit redirects HTTP to HTTPS.
- **Impact:** Every page is available at two protocol versions. Search engines must rely on canonical tags to consolidate them, and links or bookmarks to HTTP URLs keep users on an unencrypted connection. Google's canonicalization guidance states a preference for HTTPS pages as canonical and lists redirects as a strong signal for consolidating duplicate URLs.
- **Recommendation:** Add a website-wide, server-level 301 redirect from HTTP to the equivalent HTTPS URL, then consider adding an HSTS header after the redirects are verified. Update internal links and canonicals that still use `http://`.
- **Implementation complexity:** Low (assumes a server or CDN configuration change; confirm with the hosting team)
- **Related standard:** [Google Search Central: consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) and [redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Coalition page redirects pass through six hops and end in a 404

- **Finding ID:** SEO-NITA-006
- **Page or component:** Redirects for the former “Transit Is the Answer” coalition pages: `/region/transit-is-the-answer/join-the-transit-is-the-answer-coalition`, `/region/transit-is-the-answer/coalition`, `/coalition`, `/transit-funding/coalition`, `/riders/coalition`, and `/communities/coalition`.
- **Priority:** Medium
- **Evidence:** On 2026-11-20, a request to `/region/transit-is-the-answer/join-the-transit-is-the-answer-coalition` passed through six 301 redirects (`/region/transit-is-the-answer/coalition` → `/coalition` → `/transit-funding/coalition` → `/riders/coalition` → `/communities/coalition` → `/region/coalition`) and ended at a 404 page ([`step2a-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2a-live-checks.txt)). The starting URL is linked from a 2023 blog post about reduced fares; the 2026-11-19 crawl baseline recorded the same chain ([`pages.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/pages.csv), and the batch `redirects.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/)). The coalition remains active (blog posts through 2026), and `/region/transit-is-the-answer` redirects to the external website `transitistheanswer.org`.
- **Impact:** Users following old coalition links, including any external links or bookmarks to these URLs, reach a “not found” page after several redirects instead of current coalition information. Search engines following the chain find no destination to consolidate signals to. Google follows a limited number of redirect hops and recommends avoiding chains.
- **Recommendation:** Point each of the six old coalition URLs directly, in one 301, to the current coalition destination (for example the relevant page on `transitistheanswer.org` or a NITA page about the coalition), and update the link in the 2023 blog post.
- **Implementation complexity:** Low (redirect configuration; confirm the intended destination with NITA)
- **Related standard:** [Google Search Central: redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Links on two current pages lead to “not found” pages

- **Finding ID:** SEO-NITA-008
- **Page or component:** [Regional transit system](https://nita.illinois.gov/region) (“The NITA Data Portal” button) and [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) (two “NITA-issued Access card” links).
- **Priority:** Medium
- **Evidence:** Live checks on 2026-11-20 ([`step2b-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2b-live-checks.txt)):

  | Page | Link text | `href` in the HTML | Resolved URL | Status |
  | --- | --- | --- | --- | --- |
  | [`/region`](https://nita.illinois.gov/region) | The NITA Data Portal (button, opens in a new tab) | `https://nita.illinois.gov/data` | `https://nita.illinois.gov/data` | 404 |
  | [`/riders/paying-for-your-ride`](https://nita.illinois.gov/riders/paying-for-your-ride) | NITA-issued Access card | `getaccess.org` | `https://nita.illinois.gov/riders/getaccess.org` | 404 |
  | [`/riders/paying-for-your-ride`](https://nita.illinois.gov/riders/paying-for-your-ride) | NITA-issued Access card; | `getaccess.org` | `https://nita.illinois.gov/riders/getaccess.org` | 404 |

  The Access card links omit `https://`, so browsers treat `getaccess.org` as a relative path on the NITA website. The second link also carries a `title` attribute with a Microsoft Outlook Safe Links URL (`https://gcc02.safelinks.protection.outlook.com/?url=http%3A%2F%2Fgetaccess.org%2F&data=…Natalie.Rzucidlo%40RTACHICAGO.ORG…`), pasted from an email; it shows as a tooltip and exposes a staff email address and tracking parameters in the page source. NITA's own `/dashboards` URL currently redirects to an ArcGIS Experience dashboard (`https://experience.arcgis.com/experience/b1a29e850bf44bf087e01277eabfcaad/page/Home`), a likely destination for the Data Portal button. The complete link records are in [`nita-broken-link-edges.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-broken-link-edges.csv).
- **Impact:** Riders looking for how to get an Access card, a reduced-fare task on a high-value page, and users looking for regional data reach an error page instead of the intended destination. Broken links on core pages also stop crawlers from following those paths.
- **Recommendation:** Change both Access card links to the full `https://getaccess.org/` address (or the current Access program page) and delete the Safe Links `title` attribute. Point the Data Portal button to the current data destination (for example the dashboard `/dashboards` redirects to) or add a 301 redirect from `/data`. Check other pages edited from email content for pasted Safe Links URLs.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: make links crawlable](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)

### Homepage title says only “Home” and its H1s come from rotating announcements

- **Finding ID:** SEO-NITA-010
- **Page or component:** [Homepage](https://nita.illinois.gov/) (`<title>` and H1 elements of the homepage template).
- **Priority:** Medium
- **Evidence:** On 2026-11-20 the homepage source contained ([`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)):
  - `<title>Home | Northern Illinois Transit Authority</title>`
  - three H1 elements, one per announcement slide: “NITA Ride Safe App Launches”, “Weigh in on NITA's draft regional budget”, and “Municipalities can apply for assistance in adhering to POPA”
  - the generic meta description ending in “…and combats…” (see `SEO-NITA-002` and `SEO-NITA-012`)

  No heading or title on the page states what NITA is or does. The 2026-11-19 crawl recorded the first two H1s.
- **Impact:** The homepage is the main entry point for searches on the agency's name, which changed from RTA to NITA on September 1, 2026. “Home” gives search engines and users no description of the page, and the H1s change with each announcement, so the page's main topic is unclear to search engines and to users of assistive technology.
- **Recommendation:** Give the homepage a descriptive title that names the agency and its role (for example, “Northern Illinois Transit Authority (NITA) | Regional transit for northeastern Illinois”, wording to be confirmed with NITA). Use one stable H1 that states the same, and mark up announcement slide headings as H2 or lower.
- **Implementation complexity:** Low (template and content change)
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/appearance/title-link) and [SEO starter guide: headings](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

### Core page titles use slogans instead of the page topic

- **Finding ID:** SEO-NITA-011
- **Page or component:** Title field of core pages (rider, community, funding, region, and About NITA sections): 25 of 63 core pages have a title that shares no significant word with the page's H1.
- **Priority:** Medium
- **Evidence:** In the 2026-11-19 crawl baseline, many core pages use a tagline as the title while the H1 and URL state the topic. Titles and H1s of the agreed core sample ([`nita-metadata-review.csv`](../../../evidence/public-technical/2026-11-20/nita-metadata-review.csv); live examples in [`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)):

  | Page | Title (before “ \| Northern Illinois Transit Authority”) | H1 | Title width (px) |
  | --- | --- | --- | ---: |
  | [`/riders`](https://nita.illinois.gov/riders) | Welcome aboard the Chicago region's transit network | Riders | 786 |
  | [`/riders/how-to-ride`](https://nita.illinois.gov/riders/how-to-ride) | Your guide to getting around town | How to ride | 612 |
  | [`/riders/paying-for-your-ride`](https://nita.illinois.gov/riders/paying-for-your-ride) | Affordable and seamless payment | Paying for your ride | 616 |
  | [`/riders/free-and-reduced-fare-programs`](https://nita.illinois.gov/riders/free-and-reduced-fare-programs) | Discounted Fares | Discounted Fare and Ride Free Programs | 465 |
  | [`/riders/access`](https://nita.illinois.gov/riders/access) | Access Program | Access Program | 457 |
  | [`/riders/accessible-transit`](https://nita.illinois.gov/riders/accessible-transit) | There’s always a ride available, regardless of your ability | Accessible transit | 809 |
  | [`/communities`](https://nita.illinois.gov/communities) | Keeping communities safe and connected | Communities | 685 |
  | [`/communities/community-planning`](https://nita.illinois.gov/communities/community-planning) | Keeping our communities accessible | Community Planning | 638 |
  | [`/communities/access-to-transit-program`](https://nita.illinois.gov/communities/access-to-transit-program) | Improving your transit experience every step of the way | Access to Transit | 802 |
  | [`/transit-funding/2027-regional-transit-budget`](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget) | Budgeting with NITA | 2027 NITA Regional Budget | 492 |
  | [`/region/how-system-working`](https://nita.illinois.gov/region/how-system-working) | Keeping things on track | How the system is working | 520 |

  Other examples: `/about-nita/boards-and-committees` (“NITA is governed by the Board of Directors and other committees.”), `/transit-funding/financial-documents` (“Transparency and accountability are crucial to NITA.”), `/about-nita/transparency/audit` (“Providing independent, objective assurance”). The suffix “ | Northern Illinois Transit Authority” adds about 300 px to every title; 27 of the 63 core titles exceed the roughly 580 px commonly shown on desktop results, so the brand is often cut off.
- **Impact:** Titles are a primary signal of what a page is about and are usually shown as the clickable headline in search results. A rider searching for fares, reduced fares, or paratransit sees slogans such as “Affordable and seamless payment” instead of words that match the task. Google may rewrite titles it considers unhelpful, which makes results less predictable.
- **Recommendation:** Rewrite core page titles to lead with the page topic in the words riders and municipalities use (for example “Fares and ways to pay for CTA, Metra, and Pace”, “Paratransit and accessible transit”, “Community Planning Program for local governments”), keeping slogans for on-page copy. Consider a shorter suffix such as “ | NITA” once the new name is established, or keep the full name only on the homepage.
- **Implementation complexity:** Low (content change in the CMS; about 60 pages)
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/appearance/title-link)

### Legacy document redirects point to HTTP destinations

- **Finding ID:** SEO-NITA-004
- **Page or component:** 141 internal links to legacy document URLs under `/sites/default/files/...` (previous Drupal paths), mainly on [Financial documents](https://nita.illinois.gov/transit-funding/financial-documents) (54) and historical press releases (49); full list in the evidence file.
- **Priority:** Low
- **Evidence:** On 2026-11-19, link discovery checked 1,004 internal document and image links with HEAD requests. All 141 that returned 301 redirect to an `http://nita.illinois.gov/uploads/files/general/Drupal-Old/...` destination. One example (`Spanish-Title-VI-Notice-to-Public.pdf`) was followed: the HTTP destination returned 200. Two other linked PDFs return 404 (`TransitIstheAnswer.pdf`, `Travel-Information-Action-Plan.pdf`). See [`links_resources.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/links_resources.csv) and [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt).
- **Impact:** Users and crawlers following these links pass through a redirect and land on an unencrypted document URL. Once `SEO-NITA-003` is fixed, each would become a two-step redirect chain. The documents include Title VI notices and financial reports that users may need.
- **Recommendation:** Update the internal links to point directly to the current HTTPS document URLs, and change the redirect targets to HTTPS so external links to the old paths resolve in one step. Restore or remove the links to the two missing PDFs.
- **Implementation complexity:** Low to Medium (depends on whether redirects are managed in the CMS or server configuration)
- **Related standard:** [Google Search Central: redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Sitemap lists a “404” page that returns 200 and is indexable

- **Finding ID:** SEO-NITA-007
- **Page or component:** [`/404`](https://nita.illinois.gov/404) and the [general-pages sitemap](../../../evidence/public-technical/2026-11-19/nita-sitemaps-1-section-pages-1-sitemap.xml).
- **Priority:** Low
- **Evidence:** On 2026-11-20, `/404` returned HTTP 200 with the title “404 | Northern Illinois Transit Authority”, `<meta name="robots" content="all">`, and a self-referencing canonical; it is listed in the general-pages sitemap. A nonexistent URL on the same website correctly returned 404 with `robots: none`, so `/404` appears to be a published CMS entry rather than the error response ([`step2a-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2a-live-checks.txt)). My Transit Benefit has the same pattern (`SEO-MTB-001`).
- **Impact:** The sitemap asks search engines to crawl and index an error-page entry. If indexed, a “404” page could appear in search results for NITA. The effect is limited to one URL among about 1,300 in the sitemap.
- **Recommendation:** Exclude `/404` from the sitemap and mark it `noindex`, or unpublish it if the error template does not depend on it. Apply the same fix on both websites, since they share the CMS setup.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: soft 404 errors](https://developers.google.com/search/docs/crawling-indexing/http-network-errors#soft-404-errors)

### Older blog posts and press releases contain broken internal links

- **Finding ID:** SEO-NITA-009
- **Page or component:** 102 blog posts and press releases, almost all from the RTA period, containing 169 links to 49 internal URLs that return 404 or 403. One affected press release is from the NITA period (September 2026).
- **Priority:** Low
- **Evidence:** On 2026-11-20, every HTML page from the crawl baseline was re-read and every internal link to a URL returning 404 or 403 was recorded with its source page, raw `href`, and link text ([`nita-broken-link-edges.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-broken-link-edges.csv); method in the [README](../../../evidence/crawls/link-discovery/2026-11-20/README.md)). Spot checks on 2026-11-20 confirmed the 404 responses ([`step2b-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2b-live-checks.txt)). The links fall into five groups:

  **1. Encoded backslash links: 74 links in 18 posts (2016–2022).** The links have `href="%5C"`, left over from content migration, and resolve to `<post URL>/%5C` (404). For example, the 2022-06-17 post has `<a href="%5C">RTA’s four-part Transportation Tuesday Series</a>`, `<a href="%5C">Read a recent report</a>`, and `<a href="%5C">interactive story map</a>`. Affected posts (links per post):

  | Links | Post |
  | ---: | --- |
  | 12 | [`/blog/2018/10/05/the-story-of-the-seat-celebrating-manufacturing-day-today-with-freedman-seating-company`](https://nita.illinois.gov/blog/2018/10/05/the-story-of-the-seat-celebrating-manufacturing-day-today-with-freedman-seating-company) |
  | 10 | [`/blog/2018/03/12/rta-brings-together-planning-voices-from-around-the-region-for-connected-communities`](https://nita.illinois.gov/blog/2018/03/12/rta-brings-together-planning-voices-from-around-the-region-for-connected-communities) |
  | 8 | [`/blog/2018/08/31/let-the-rta-help-you-go-back-to-school`](https://nita.illinois.gov/blog/2018/08/31/let-the-rta-help-you-go-back-to-school) |
  | 7 | [`/blog/2017/06/28/sharing-tod-success-stories-from-the-north-side-to-the-south-side`](https://nita.illinois.gov/blog/2017/06/28/sharing-tod-success-stories-from-the-north-side-to-the-south-side) |
  | 5 | [`/blog/2017/07/06/let-public-transportation-do-the-work-for-you-even-on-your-day-off`](https://nita.illinois.gov/blog/2017/07/06/let-public-transportation-do-the-work-for-you-even-on-your-day-off) |
  | 4 | [`/blog/2022/06/17/transportation-tuesday-recap-making-the-connection-how-the-rtas-interagency-signage-program-helps-solve-a-complex-regional-problem`](https://nita.illinois.gov/blog/2022/06/17/transportation-tuesday-recap-making-the-connection-how-the-rtas-interagency-signage-program-helps-solve-a-complex-regional-problem) |
  | 4 | [`/blog/2018/05/04/what-is-transit-oriented-development`](https://nita.illinois.gov/blog/2018/05/04/what-is-transit-oriented-development) |
  | 3 | [`/blog/2019/05/17/infrastructure-week-highlight-paces-priority-projects`](https://nita.illinois.gov/blog/2019/05/17/infrastructure-week-highlight-paces-priority-projects) |
  | 3 | [`/blog/2019/05/15/national-infrastructure-week-highlight-metras-priority-projects`](https://nita.illinois.gov/blog/2019/05/15/national-infrastructure-week-highlight-metras-priority-projects) |
  | 3 | [`/blog/2019/05/13/national-infrastructure-week-highlight-ctas-priority-projects`](https://nita.illinois.gov/blog/2019/05/13/national-infrastructure-week-highlight-ctas-priority-projects) |
  | 3 | [`/blog/2018/06/22/recapping-a-successful-dump-the-pump`](https://nita.illinois.gov/blog/2018/06/22/recapping-a-successful-dump-the-pump) |
  | 3 | [`/blog/2017/06/16/dump-the-pump-was-a-success`](https://nita.illinois.gov/blog/2017/06/16/dump-the-pump-was-a-success) |
  | 2 | [`/blog/2016/02/01/rta-regional-and-downtown-maps-are-available`](https://nita.illinois.gov/blog/2016/02/01/rta-regional-and-downtown-maps-are-available) |
  | 2 | [`/blog/2019/04/22/get-on-board-and-go-green`](https://nita.illinois.gov/blog/2019/04/22/get-on-board-and-go-green) |
  | 2 | [`/blog/2018/12/12/talking-transit-out-and-about`](https://nita.illinois.gov/blog/2018/12/12/talking-transit-out-and-about) |
  | 1 | [`/blog/2019/05/21/city-club-chicago-the-time-to-invest-in-transit-is-now`](https://nita.illinois.gov/blog/2019/05/21/city-club-chicago-the-time-to-invest-in-transit-is-now) |
  | 1 | [`/blog/2019/04/16/check-out-the-new-95th-street-cta-red-line-station`](https://nita.illinois.gov/blog/2019/04/16/check-out-the-new-95th-street-cta-red-line-station) |
  | 1 | [`/blog/2019/03/06/revamping-ctas-articulated-buses`](https://nita.illinois.gov/blog/2019/03/06/revamping-ctas-articulated-buses) |

  **2. RTA-era paths with no redirect: 51 links on 48 pages to 19 URLs**, mostly in press releases. The website already redirects many RTA-era paths (57 working 301s), but not these:

  | Links | Broken URL | Typical link text | Example source page |
  | ---: | --- | --- | --- |
  | 11 | `/index.php/plans-programs/community-planning` | RTA's Community Planning Program | [`/about-rta/press-releases/mount-prospect-completes-corridor-plan-for-rand-road`](https://nita.illinois.gov/about-rta/press-releases/mount-prospect-completes-corridor-plan-for-rand-road) |
  | 8 | `/index.php/home` | www.RTAchicago.org | [`/about-rta/press-releases/regional-transportation-authority-rta-board-meeting-dates-for-2016`](https://nita.illinois.gov/about-rta/press-releases/regional-transportation-authority-rta-board-meeting-dates-for-2016) |
  | 5 | `/index.php/plans-programs/grants-projects/community-planning` | Community Planning program | [`/about-rta/press-releases/cmap-rta-call-for-projects-press-release-9-16-19`](https://nita.illinois.gov/about-rta/press-releases/cmap-rta-call-for-projects-press-release-9-16-19) |
  | 5 | `/home` | “trailer” | [`/about-rta/press-releases/regional-transit-agencies-thank-riders-and-celebrate-dump-the-pump-day-2018`](https://nita.illinois.gov/about-rta/press-releases/regional-transit-agencies-thank-riders-and-celebrate-dump-the-pump-day-2018) |
  | 4 | `/index.php/plans-programs/access-transit-program` | Access to Transit | [`/blog/2021/12/10/explore-2021-rta-local-planning-projects-and-successes-in-interactive-implementation-report`](https://nita.illinois.gov/blog/2021/12/10/explore-2021-rta-local-planning-projects-and-successes-in-interactive-implementation-report) |
  | 3 | `/index.php/finance-management/2018-regional-transit-operating-budget-and-capital-program` | www.RTAChicago.org | [`/about-rta/press-releases/rta-board-approves-2-9-billion-2016-regional-transit-operating-budget-and-3-9-billion-2016-2020-regional-capital-program`](https://nita.illinois.gov/about-rta/press-releases/rta-board-approves-2-9-billion-2016-regional-transit-operating-budget-and-3-9-billion-2016-2020-regional-capital-program) |
  | 3 | `/index.php/rider-resources/reduced-fare/military-service-fare-program` | www.RTAChicago.org | [`/about-rta/press-releases/rta-reminds-riders-transit-is-best-option-for-veterans-day-festivities`](https://nita.illinois.gov/about-rta/press-releases/rta-reminds-riders-transit-is-best-option-for-veterans-day-festivities) |
  | 1 each | `/index.php/plans-programs/2023-regional-transit-strategic-plan`, `/financemanagement/operating-capital`, `/index.php/about-us/media/press-release-archives/2019-press-releases/rta-access-transit-program-awards`, `/index.php/plans-programs/grants-projects`, `/cp/apply`, `/programs-and-projects/community-planning/2018-community-planning-program-projects`, `/index.php/plan-your-trip/travel-tips/riding-metra-trains/maps`, `/dump-pump-2016`, `/applications`, `/index.php/rider-resources/accessible-transit/travel-training`, `/dump-pump-pledge-sweepstakes-official-rules`, `/media/rta-leader-tax-recovery-work/united-airlines-lawsuit` | — | See the evidence file |

  **3. Removed or renamed pages: 36 links on 28 pages to 6 URLs.**

  | Links | Broken URL | Link text | Example source page |
  | ---: | --- | --- | --- |
  | 25 (20 pages) | `/region/transformingtransit` | Transforming Transit | [`/about-rta/press-releases/our-vision-for-transits-future-a-stronger-rta-empowered-to-lead-a-world-class-system`](https://nita.illinois.gov/about-rta/press-releases/our-vision-for-transits-future-a-stronger-rta-empowered-to-lead-a-world-class-system) and 2025 blog posts |
  | 7 (6 pages) | `/transit-funding/fiscalcliff` | the Chicago region’s looming transit fiscal cliff | [`/blog/2025/08/07/whats-next-for-the-transit-fiscal-cliff-rta-works-with-service-boards-to-delay-service-cuts-continues-push-for-funding`](https://nita.illinois.gov/blog/2025/08/07/whats-next-for-the-transit-fiscal-cliff-rta-works-with-service-boards-to-delay-service-cuts-continues-push-for-funding) |
  | 1 | `/blog.` (trailing period inside the link) | https://nita.illinois.gov/blog. | [`/about-rta/press-releases/nita-board-of-directors-holds-first-meeting-names-new-agency-leadership-and-expands-reduced-fare-programs`](https://nita.illinois.gov/about-rta/press-releases/nita-board-of-directors-holds-first-meeting-names-new-agency-leadership-and-expands-reduced-fare-programs) (NITA period, 2026) |
  | 1 | `/region/regional-collaboration` | Regional Coordination Division | [`/blog/2025/06/12/rta-welcomes-summer-2025-interns`](https://nita.illinois.gov/blog/2025/06/12/rta-welcomes-summer-2025-interns) |
  | 1 | `/about-nita/staff` | staff | [`/blog/2024/03/21/rta-launches-new-rider-focused-citizens-advisory-board`](https://nita.illinois.gov/blog/2024/03/21/rta-launches-new-rider-focused-citizens-advisory-board) |
  | 1 | `/blog/2023/03/23/how-to-use-transit-during-the-kennedy-expressway-construction` | Learn how to use transit during construction | [`/blog/2023/07/25/legislation-expands-transit-benefit-program-to-workplaces-across-the-chicago-region`](https://nita.illinois.gov/blog/2023/07/25/legislation-expands-transit-benefit-program-to-workplaces-across-the-chicago-region) |

  **4. Links without a scheme or protocol: 6 links on 6 pages.** The `href` values omit `https://` or `mailto:`, so they resolve as paths on the NITA website:

  | `href` in the HTML | Link text | Pages |
  | --- | --- | --- |
  | `massels@RTAchicago.org` (should be `mailto:`) | massels@RTAchicago.org | 3 press releases, including [`/about-rta/press-releases/rta-closing-customer-service-offices-in-response-to-covid-19-staff-working-remotely-march-board-of-directors-meeting-canceled`](https://nita.illinois.gov/about-rta/press-releases/rta-closing-customer-service-offices-in-response-to-covid-19-staff-working-remotely-march-board-of-directors-meeting-canceled) |
  | `www.rtachicago.org/news` | Subscribe | [`/blog/2022/11/14/the-rta-launched-a-new-website-explore-it-now`](https://nita.illinois.gov/blog/2022/11/14/the-rta-launched-a-new-website-explore-it-now) |
  | `blog.rtachicago.org/subscribe` | Subscribe | [`/blog/2021/11/16/public-forum-focuses-on-lessons-from-the-pandemic-in-planning-for-transits-future`](https://nita.illinois.gov/blog/2021/11/16/public-forum-focuses-on-lessons-from-the-pandemic-in-planning-for-transits-future) |
  | `GetonBoardIL.org` | GetonBoardIL.org | [`/about-rta/press-releases/leaders-call-for-transit-investment-at-get-on-board-day-event`](https://nita.illinois.gov/about-rta/press-releases/leaders-call-for-transit-investment-at-get-on-board-day-event) |

  **5. Word-processor code left inside the link: 2 links (403).**

  | Source page | Link text | Text appended to the `href` |
  | --- | --- | --- |
  | [`/blog/2024/08/27/transit-station-activations-in-rogers-park-joliet-bring-live-music-games-and-more`](https://nita.illinois.gov/blog/2024/08/27/transit-station-activations-in-rogers-park-joliet-bring-live-music-games-and-more) | In May, the RTA announced | `%22%20/t%20%22_blank` (a Word `\t "_blank"` field switch) |
  | [`/blog/2025/06/16/plan-to-improve-access-to-transit-commercial-investment-in-auburn-gresham-underway`](https://nita.illinois.gov/blog/2025/06/16/plan-to-improve-access-to-transit-commercial-investment-in-auburn-gresham-underway) | that began in 2022 | `%22%20/h%20HYPERLINK%20%22…` (a Word `HYPERLINK` field) |
- **Impact:** Readers of archived content reach error pages, and crawlers spend requests on dead ends. Because most affected pages are historical, the effect on current tasks is limited; the 2025 links about Transforming Transit and the fiscal cliff and the September 2026 NITA board press release are the most likely to still be read.
- **Recommendation:** Add 301 redirects for removed pages with clear successors (for example `/region/transformingtransit` to the [Transforming Transit tag archive](https://nita.illinois.gov/blog/tags/transforming-transit) or a current page, `/transit-funding/fiscalcliff` to the [fiscal cliff tag archive](https://nita.illinois.gov/blog/tags/fiscal-cliff) or current funding page, and `/index.php/plans-programs/community-planning` to [Community Planning](https://nita.illinois.gov/communities/community-planning)), and consider a rule for the remaining `/index.php/...` paths. Remove or correct the `href="%5C"` links with a CMS search. Add `https://` or `mailto:` to the links in group 4, remove the trailing period in the NITA board press release, and clean the two links in group 5.
- **Implementation complexity:** Medium (many pages; partly scriptable in the CMS)
- **Related standard:** [Google Search Central: redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### The CMS cuts titles and descriptions off with a literal ellipsis

- **Finding ID:** SEO-NITA-012
- **Page or component:** Automatic title and meta description generation (the CMS SEO settings), affecting 1,279 meta descriptions and 63 titles among the 1,358 indexable HTML pages.
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline ([`nita-metadata-review.csv`](../../../evidence/public-technical/2026-11-20/nita-metadata-review.csv)):
  - 1,279 meta descriptions end with the “…” character, usually at 150–155 characters: 758 blog posts, 413 press releases, 76 tag archives, 25 core pages, and 7 listings. Examples: the homepage (“…advances equity, and combats…”), [`/riders/how-to-ride`](https://nita.illinois.gov/riders/how-to-ride) (“…so you can have a smooth ride in…”), [`/communities/access-to-transit-program`](https://nita.illinois.gov/communities/access-to-transit-program) (“…accessible, attractive, and safe for…”).
  - 63 titles (40 blog posts and 23 press releases) contain “…” before the brand suffix, for example “Northern Illinois Transit Authority’s first regional budget proposal expands service, creates jobs, and improves… | Northern Illinois Transit Authority”, the title of the [November 2, 2026 budget press release](https://nita.illinois.gov/about-rta/press-releases/northern-illinois-transit-authoritys-first-regional-budget-proposal-expands-service-creates-jobs-and-improves-safety-across-six-counties).
  - Descriptions extracted from the start of the body copy can begin mid-sentence: 21 posts and press releases start with a digit, for example the same budget release (“2, 2026 — The Northern Illinois Transit Authority (NITA) has released…”), and 65 press releases begin with the “CHICAGO –” dateline.
  The live source confirmed these values on 2026-11-20 ([`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)). My Transit Benefit shows the same truncation (`SEO-MTB-002`).
- **Impact:** Search snippets and titles that stop mid-word look incomplete and drop the end of the message; Google is more likely to replace them with text it selects. Because the pattern comes from a setting, it affects almost every page.
- **Recommendation:** Change the CMS SEO configuration so titles and descriptions are not truncated with an ellipsis; let search engines truncate at display time. For press releases and posts, generate descriptions from a summary field rather than the opening dateline, and write descriptions manually for core pages.
- **Implementation complexity:** Low (configuration); Medium if summary fields must be filled for older content
- **Related standard:** [Google Search Central: control your snippets](https://developers.google.com/search/docs/appearance/snippet)

### Recurring posts and press releases share identical titles

- **Finding ID:** SEO-NITA-013
- **Page or component:** 156 indexable posts, press releases, and archived budget pages in 66 groups with identical titles; full list in [`nita-metadata-review.csv`](../../../evidence/public-technical/2026-11-20/nita-metadata-review.csv) (column `title_duplicate_count`).
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, the groups are mostly weekly or yearly RTA-era releases reissued under the same headline, with `-2`, `-3`, … URL slugs, and stories published both as a blog post and as a press release. They are different pages (different dates and text; no exact duplicates by content hash). Largest groups:

  | Pages | Shared title (before the suffix) | Examples |
  | ---: | --- | --- |
  | 8 | Public Transportation Offers Best Travel Option for Summer Festivals | Press releases dated June 4 to July 15, 2015 (`…-summer-festivals`, `-2` to `-7`) and a 2015-08-24 blog post |
  | 6 | Summer Events and Festivals Mean Fun in RTA Region | Press releases dated June 13 to August 27, 2014 (`…-rta-region`, `-2` to `-6`) |
  | 4 | RTA Access to Transit Program Awarded Funding to Improve Bike and Pedestrian Connections to Transit | Blog posts from 2017 and 2019 and two press releases |
  | 4 | The RTA Celebrates National Community Planning Month | Blog posts from 2017, 2018, and 2019 and a press release |
  | 4 | RTA Awards Nine Community Planning Projects | A 2019 blog post and three press releases |
  | 4 | RTA Encourages Riders to Say “Thank You” to Transit Employees | Four press releases |
  | 3 | Register now for four-part Transportation Tuesday webinar series | Blog posts from 2022, 2023, and 2025 |
  | 3 | Budgeting with the RTA | [`/transit-funding/2023-regional-transit-budget`](https://nita.illinois.gov/transit-funding/2023-regional-transit-budget), [`/transit-funding/2024-regional-transit-budget`](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget), [`/transit-funding/2025-regional-transit-budget`](https://nita.illinois.gov/transit-funding/2025-regional-transit-budget) |

  Distribution: 54 groups of 2 pages, 6 of 3, 4 of 4, one of 6, and one of 8. Separately, the post [`/blog/2015/11/30/503`](https://nita.illinois.gov/blog/2015/11/30/503) has the brand-only title “NITA | Northern Illinois Transit Authority” and an H1 that contains only its date, “November 30, 2015”; its headline, “Good transportation system is critical to Chicago area”, is in a second H1 in the body.
- **Impact:** Identical titles make it hard for users and search engines to tell which edition is relevant in results, and search engines may show only one of them. The three budget archive pages also carry the RTA-era title “Budgeting with the RTA”.
- **Recommendation:** Add the year or edition to recurring titles (for example “… Summer Festivals (July 15, 2015)”); for the budget archive pages use the year in the title (for example “2024 Regional Transit Budget”). Fix the title and headings of the `/blog/2015/11/30/503` post. Consider whether blog copies of press releases should canonicalize to one version.
- **Implementation complexity:** Low to Medium (mostly content edits to historical entries)
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/appearance/title-link)

### Copied meta descriptions describe a different or outdated topic

- **Finding ID:** SEO-NITA-014
- **Page or component:** 100 indexable posts, press releases, and budget pages in 39 groups that share a description other than the generic site description; full list in [`nita-metadata-review.csv`](../../../evidence/public-technical/2026-11-20/nita-metadata-review.csv) (column `description_duplicate_count`).
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, descriptions were copied between entries and no longer summarize each page. Largest groups:

  | Pages | Shared description (start) | Affected pages |
  | ---: | --- | --- |
  | 10 | “The RTA is currently developing the 2023 Regional Transit Strategic Plan for Northeastern Illinois…” | Blog posts from September–October 2021, including guest posts such as [`/blog/2021/09/30/active-transportation-alliance`](https://nita.illinois.gov/blog/2021/09/30/active-transportation-alliance) |
  | 6 | “RTA Trip Planner offers easy way to plan routes CHICAGO – Summer fun is just a short ride away…” | 2015 summer festival press releases |
  | 5 | “Learn two ways transit helps the region CHICAGO – The Regional Transportation Authority (RTA)…” | Press releases on commuter celebrations |
  | 4 | “After more than a year of engagement, the RTA has released a draft regional transit strategic plan…” | Four blog posts of 2022-12-15, including [`/blog/2022/12/15/transit-is-the-answer-to-climate-change`](https://nita.illinois.gov/blog/2022/12/15/transit-is-the-answer-to-climate-change) |
  | 3 | “Every year, the RTA’s Local Planning department assists local governments…” | Local planning recap posts of 2023, 2024, and 2025 |
  | 3 | “The RTA controls the operating budgets of the CTA, Metra, and Pace. The agency will be reviewing and adopting a new budget for 2023 this coming December.” | The 2023, 2024, and 2025 budget pages |

  The budget pages were confirmed live on 2026-11-20: the [2024 budget page](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget) still describes adopting “a new budget for 2023” and refers to the RTA ([`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)).
- **Impact:** A description that does not match the page misleads users in search results, and outdated statements (RTA controlling budgets, a 2023 budget “this coming December”) conflict with NITA's current role.
- **Recommendation:** Write a specific description for each budget page and for the most-read posts in these groups; clear the copied descriptions on the rest so they are regenerated from each page's own summary (see `SEO-NITA-012`).
- **Implementation complexity:** Low to Medium (content edits)
- **Related standard:** [Google Search Central: control your snippets](https://developers.google.com/search/docs/appearance/snippet)

### Sitemap lists redirecting shortcuts and placeholder entries

- **Finding ID:** SEO-NITA-015
- **Page or component:** [XML sitemap](https://nita.illinois.gov/sitemaps-1-sitemap.xml): general-pages and news child sitemaps.
- **Priority:** Low
- **Evidence:** Of the 1,286 URLs in the 2026-11-19 sitemap, 1,278 returned 200 and were indexable; the other 8 are internal shortcut URLs that return 302 to other websites ([`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv); live on 2026-11-20 in [`step2d-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2d-live-checks.txt)):

  | Sitemap URL | Redirects (302) to | Linked from the website? |
  | --- | --- | --- |
  | [`/dashboards`](https://nita.illinois.gov/dashboards) | ArcGIS Experience dashboard | Yes |
  | [`/popamap`](https://nita.illinois.gov/popamap) | ArcGIS lookup app | Yes |
  | [`/region/regional-transit-data`](https://nita.illinois.gov/region/regional-transit-data) | `https://rtams.org/` | Yes (global navigation) |
  | [`/region/transit-is-the-answer`](https://nita.illinois.gov/region/transit-is-the-answer) | `https://transitistheanswer.org/` | Yes |
  | [`/riders/free-and-reduced-fare-programs/registration-sites`](https://nita.illinois.gov/riders/free-and-reduced-fare-programs/registration-sites) | ArcGIS “nearby” app | Yes (global navigation) |
  | [`/riders/transit-benefit-fare-program`](https://nita.illinois.gov/riders/transit-benefit-fare-program) | `https://www.mytransitbenefit.com/` | Yes (global navigation) |
  | [`/regsitehub`](https://nita.illinois.gov/regsitehub) | `https://sites.google.com/view/rtasitehub/home` | No |
  | [`/ridersurvey26`](https://nita.illinois.gov/ridersurvey26) | `https://www.research.net/r/ChiTransitFall2026` | No |

  The sitemap also lists two placeholder entries that return 200 and are indexable: the post [`/blog/1970/01/01/take-rta-survey`](https://nita.illinois.gov/blog/1970/01/01/take-rta-survey) (title “Take RTA survey”; the 1970-01-01 date in its URL and sitemap indicates a missing publication date) and the category page [`/blog/uncategorized`](https://nita.illinois.gov/blog/uncategorized) (title “Uncategorized”, not linked from the website). The `/404` entry is covered by `SEO-NITA-007`.
- **Impact:** A sitemap should list the canonical URLs a website wants indexed. Redirecting shortcuts and placeholder entries send search engines to URLs that are not content pages; search engines ignore or devalue redirecting sitemap entries, and the 1970 post and “Uncategorized” page can surface in results with misleading dates or labels.
- **Recommendation:** Exclude shortcut entries (the CMS redirect or “link” entries) from the sitemap, and unpublish or exclude the `take-rta-survey` placeholder and the `uncategorized` category. Keep using the shortcuts in navigation if useful.
- **Implementation complexity:** Low (CMS sitemap settings per section or entry type)
- **Related standard:** [Google Search Central: build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

### Structured data labels every page as a website and omits article markup

- **Finding ID:** SEO-NITA-016
- **Page or component:** JSON-LD generated by the CMS SEO plugin on every page; checked on the 16 sample URLs.
- **Priority:** Low
- **Evidence:** On 2026-11-20 each of the 16 sample pages contained one JSON-LD block with the same structure: a `WebSite` node, two `GovernmentOrganization` nodes (`#identity` and `#creator`), and a `BreadcrumbList` ([extracted JSON-LD per page](../../../evidence/public-technical/2026-11-20/structured-data/); no Microdata or RDFa found). Official validation on 2026-11-20 ([results and screenshots](../../../evidence/public-technical/2026-11-20/structured-data/validation-results.md)): the Schema.org Validator reported 0 errors and 0 warnings on the homepage and the budget press release, and Google's Rich Results Test crawled both successfully and found 5 valid items (Breadcrumbs, Local businesses, Organization), with one optional field missing (`image` on the `#creator` organization) and no Article item on the press release. Validity does not cover whether the types and values are appropriate. Observations against the schema.org vocabulary and Google's structured data documentation:
  - **Page type:** the page-level node is `@type: "WebSite"` on every page, including the blog post and press release, with the page title as `headline` (for example `"headline": "Affordable and seamless payment"` on Paying for your ride). Inner pages are not marked as `WebPage`, and posts and press releases have no `Article`, `NewsArticle`, or `BlogPosting` node, although `datePublished`, `dateModified`, `author`, and `publisher` values are already present on that node.
  - **Logo:** the `#identity` organization's `logo` is an `ImageObject` with `height` 264 and `width` 600 but no `url`, so no logo image is declared.
  - **Profiles:** no `sameAs` links to NITA's official profiles (for example social media accounts or Wikipedia/Wikidata entries, if they exist).
  - **Breadcrumbs:** the press release breadcrumb has two items, Home and the release itself, without a News or Press releases level; core pages have complete trails (for example Home › Riders › Paying for your ride).
  - **Headline values:** the JSON-LD `headline` holds the full title (for example the complete budget press-release headline), while the HTML `<title>` is truncated with “…” (`SEO-NITA-012`), which confirms the truncation happens only in the title output.
- **Impact:** Structured data helps search engines and AI systems identify what each page is and who publishes it. Labeling every page as a `WebSite` and omitting article markup and a logo URL gives a less accurate description of NITA's pages and news content. Valid markup does not guarantee any search feature.
- **Recommendation:** In the SEO plugin, set the page-level type to `WebPage` for general pages and `NewsArticle` (press releases) or `BlogPosting` (blog posts) for news entries; add the logo `url` and `sameAs` profiles to the organization; add the News or Press releases level to press-release breadcrumbs. Validate the result with the Rich Results Test.
- **Implementation complexity:** Low (plugin configuration per section)
- **Related standard:** [Google Search Central: Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article), [Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization), and [schema.org/WebPage](https://schema.org/WebPage)

### Paginated listings declare the first page as canonical

- **Finding ID:** SEO-NITA-005
- **Page or component:** 248 paginated listing pages: [On Track blog](https://nita.illinois.gov/blog) (65), blog archive (36), blog categories `/blog/plan`, `/blog/invest`, and `/blog/move` (27), [press releases](https://nita.illinois.gov/news/press-releases) (34), meeting materials (9), and paginated tag archives (77).
- **Priority:** Low
- **Evidence:** On 2026-11-19, `/blog/p2` and `/blog/p3` returned 200, linked to the next page with standard anchors, and declared `https://nita.illinois.gov/blog` as canonical. The 2026-11-19 crawl baseline shows the same pattern on every paginated listing: each page canonicalizes to the first page of its listing. Older posts and press releases are reachable only through these sequential pages, up to 66 clicks from the homepage. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt) and [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv).
- **Impact:** Later listing pages contain different items from the first page, so the canonical signal is inaccurate. Search engines may give less weight to these pages and the links on them, which are the only internal crawl path to older posts and press releases. The XML sitemap partly offsets this because it lists individual posts.
- **Recommendation:** Give each paginated listing page a self-referencing canonical URL. Keep sequential links between pages.
- **Implementation complexity:** Low (template change)
- **Related standard:** [Google Search Central: pagination best practices](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)

### Blog tag archive titles and headings do not identify their topics

- **Finding ID:** SEO-NITA-001
- **Page or component:** Blog tag archive template: 155 `/blog/tags/` URLs (78 tag pages and 77 paginated tag pages), for example [CTA](https://nita.illinois.gov/blog/tags/cta) and [Metra](https://nita.illinois.gov/blog/tags/metra).
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, all 155 tag archive URLs have the title “NITA | Northern Illinois Transit Authority.” Of the 78 tag pages, 76 are indexable with self-referencing canonicals and 2 canonicalize to their `http://` version (see `SEO-NITA-003`). On 2026-11-18, a public spot check of the [CTA archive](https://nita.illinois.gov/blog/tags/cta) confirmed that it lists CTA-related posts while its title does not identify the topic. The same template uses the H1 “Connections Blog”, the former RTA blog name, on all 76 indexable tag pages and on five blog listings (`/blog/archive`, `/blog/plan`, `/blog/invest`, `/blog/move`, `/blog/uncategorized`); confirmed live on [`/blog/tags/cta`](https://nita.illinois.gov/blog/tags/cta) on 2026-11-20 ([`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)). The tag list also contains a misspelled duplicate, `/blog/tags/acces-to-transit`, alongside `/blog/tags/access-to-transit`. See [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv) and the batch `page_titles_all.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/).
- **Impact:** In a search result or browser tab, these pages are difficult to distinguish by subject. Google may generate title links from other page signals, so the exported title alone does not predict the exact result shown.
- **Recommendation:** Update the tag archive template so the title and H1 name the tag topic (for example “CTA news and updates | NITA”) and replace the “Connections Blog” heading with the current blog name, “On Track”. Confirm which of the 78 tags should remain indexable, and merge the misspelled duplicate tag.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#influence-your-title-links)

### The homepage, archives, and some core pages have generic or placeholder descriptions

- **Finding ID:** SEO-NITA-002
- **Page or component:** 292 pages with the generic site description (85 of them indexable: the homepage, 76 tag pages, 6 blog listings, one press release, and the `/blog/1970/01/01/take-rta-survey` post) and 7 core pages whose description repeats the page name or a fragment.
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, all 1,613 HTML pages have a meta description; 292 use the same description beginning “Committed to achieving a vision of safe, reliable, accessible public transportation…”. See the batch `meta_description_all.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/) and [`nita-metadata-review.csv`](../../../evidence/public-technical/2026-11-20/nita-metadata-review.csv). Placeholder descriptions on core pages: [`/contact`](https://nita.illinois.gov/contact) (“Contact”), [`/privacy-policy`](https://nita.illinois.gov/privacy-policy) (“Privacy Policy”), [`/whistleblower-policy`](https://nita.illinois.gov/whistleblower-policy) (“Whistleblower Policy”), [`/forward-for-all`](https://nita.illinois.gov/forward-for-all) (“Forward For All”), [`/investor-relations-sub`](https://nita.illinois.gov/investor-relations-sub) (“Information for Potential Investors”), [`/about-nita/investor-relations`](https://nita.illinois.gov/about-nita/investor-relations) (“The information is provided for quick reference only.”), and [`/safety/app`](https://nita.illinois.gov/safety/app) (“One free app and one text number for CTA, Metra, and Pace.”).
- **Impact:** The repeated description does not summarize the distinct purpose of these pages when used as a search snippet. Google may instead create a snippet from page content.
- **Recommendation:** Write concise descriptions for the homepage, the seven core pages listed, and any priority blog landing/archive pages intended for search. Confirm the indexability and editorial purpose of archive and pagination pages before producing copy for all of them.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: control your snippets](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#control-your-snippets)

## Content observations under review

Manual review priorities (rider decision content, program naming, time-sensitive budget and fare content, and the RTA-to-NITA editorial transition) are listed in the [matrix](seo-review-matrix.md#public-content-inventory-and-review-priorities). They are validation priorities, not findings at this stage.

## Positive Observations

- All 1,613 HTML pages in the 2026-11-19 crawl baseline have a title, meta description, and H1, and none has a `noindex` directive. This does not assess whether their content is effective.
- The website publishes an XML sitemap index with five child sitemaps, referenced from `robots.txt`. 1,280 of its 1,286 URLs are also reachable through internal links, and the sitemap updates promptly: the Ride Safe pages and posts published on 2026-11-19 (`/safety`, `/safety/app`, and the related blog post and press release) were listed by 2026-11-20 ([current sitemap copies](../../../evidence/public-technical/2026-11-20/sitemaps/)).
- Every page carries valid JSON-LD that identifies NITA as a `GovernmentOrganization` with name, alternate name, address, telephone, and email, and core pages have complete breadcrumb trails ([extracted JSON-LD](../../../evidence/public-technical/2026-11-20/structured-data/)).

## Limitations

- The crawl baseline uses raw HTML only (no JavaScript rendering). Links generated only by JavaScript are not covered.
- The free Screaming Frog version does not extract structured data, and List mode does not crawl images, so structured data and image alternative text are reviewed on the page-level sample instead. JSON-LD was extracted from all 16 sample pages; the official validators (Schema.org Validator and Google Rich Results Test) were run on the homepage and one press release ([results](../../../evidence/public-technical/2026-11-20/structured-data/validation-results.md)).
- Live checks are single dated fetches of the listed URLs; protocol behavior was confirmed on ten URLs across templates and is presumed website-wide.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- Performance/Core Web Vitals, mobile, internal linking quality, and external links have not yet been assessed (Step 2 and Step 3).
