# Search Engine Optimization (SEO) — nita.illinois.gov

## Assessment Scope

- **Website:** [nita.illinois.gov](https://nita.illinois.gov/)
- **Review date:** 2026-11-19 to 2026-11-24 (crawl baseline 2026-11-19; Step 2 checks 2026-11-20; Step 3 manual and AI-assisted review 2026-11-24)
- **Pages, templates, or journeys reviewed:** Crawl-level review of 1,736 URLs (1,613 HTML pages returning 200), combining the 1,286-URL public sitemap with every HTML URL reachable through internal links; dated live header and HTML checks on 2026-11-19; navigation and spot checks across the agreed 16-URL sample listed in the [SEO review matrix](seo-review-matrix.md#page-level-review-scope). Rendered review of the 16 sample pages on 2026-11-24 (raw HTML compared with the rendered page after scripts run; [comparison](../../../evidence/public-technical/2026-11-24/rendered-review/raw-vs-rendered.csv)); mobile review, full internal link crawl, and content and keyword review on 2026-11-24 ([content review](../../../evidence/public-technical/2026-11-24/content-review/README.md)).
- **Methods and tools:** link-discovery script with no depth limit ([B1 README](../../../evidence/crawls/link-discovery/2026-11-19/README.md)); Screaming Frog SEO Spider 25.1 free version, List mode, Text Only ([B2 README](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/README.md)); curl 8.7.1 ([`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)); full internal link crawl of the 1,609 HTML pages on 2026-11-24 ([README](../../../evidence/crawls/link-discovery/2026-11-24/README.md)); Schema.org Validator and Google Rich Results Test; PageSpeed Insights (Lighthouse 13.6.0) through its web interface ([README](../../../evidence/public-technical/2026-11-24/README.md)); Chromium browser review in the Claude desktop app, including raw and rendered HTML comparison and mobile emulation at 375×812 ([rendered review](../../../evidence/public-technical/2026-11-24/rendered-review/README.md), [mobile review](../../../evidence/public-technical/2026-11-24/mobile-review/README.md)); Google autocomplete and a seven-query result sample ([content review](../../../evidence/public-technical/2026-11-24/content-review/README.md)); Google Search Central guidance. Step 3 was AI-assisted: Claude ran the browser checks and analyses, and the team reviewed each part.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** The most consequential observation so far is protocol handling: the website serves pages over unencrypted HTTP without redirecting to HTTPS, and 141 internal links to legacy documents redirect to HTTP destinations. Canonical tags point to HTTPS, which limits but does not remove the risk of split signals and unencrypted visits. Redirect handling for the former coalition pages is broken: a six-hop chain ends in a 404. Two current pages, including Paying for your ride, link to “not found” pages, and 102 blog posts and press releases, mostly from the RTA period, contain broken internal links. On-page metadata is the other main theme: the homepage title is “Home”, core page titles are slogans rather than topics, and the CMS truncates most titles and descriptions with an ellipsis. Paginated listings declare their first page as canonical. Metadata observations are lower priority: 155 tag archive URLs share a brand-only title, and 292 pages share one generic meta description. Step 2 also found that image `alt` text mostly repeats file names (and the footer logo is labeled “RTA”), and that 722 outbound links, mostly in historical content, lead to removed pages or closed RTA-era domains. Performance is acceptable for real users on mobile, but the homepage fails the desktop Core Web Vitals check because its slider shifts the page while loading. The rendered review confirmed that page content does not depend on JavaScript, but the website's translations into seven languages exist only in the visitor's browser, on the English URLs, so search engines cannot find them. Content review found past events and an expired alert presented as current, conflicting paratransit phone hours, 68 links copied from Outlook emails that route through Microsoft Safe Links and expose staff email addresses, and rider program pages that do not use the permit names or the former RTA name people still search with. On phones the pages serve the same content as on desktop, but the main fare tables push the page wider than the screen, and some current pages, such as public meetings and the new rider advisory councils, are linked only from the desktop menu or a single news post. Information architecture: 49 former RTA paths still linked from older content redirect to general section pages instead of the matching current page, and the blog's “Related Articles” block shows the same six 2020 posts on 442 older posts.

The 2026-11-19 crawl baseline replaces the 2026-11-16 crawl, which stopped short of deep pagination ([method](seo-audit-plan.md#crawl-baseline-method)). With complete link discovery, only 6 of the 1,286 sitemap URLs are not reached through internal links; the earlier gap of 1,203 URLs was a crawl artifact. The new baseline also surfaces items for Step 2: 50 internal links returning 404, content up to 66 clicks from the homepage, and malformed links in older posts. This review does not establish rankings, clicks, or Google index status.

## Findings

### HTTP pages load without redirecting to HTTPS

- **Finding ID:** SEO-NITA-003
- **Page or component:** Website-wide protocol handling; confirmed on every template tested over HTTP (homepage, rider, community, funding, blog listing and post, press-release listing and release, tag archive, and a PDF).
- **Priority:** High
- **Evidence:** On 2026-11-19, `curl -sI` requests to `http://nita.illinois.gov/` and `http://nita.illinois.gov/riders` returned `HTTP/1.1 200 OK` with no `Location` header. On 2026-11-20, HTTP requests to ten URLs across templates, including a PDF, all returned 200 without redirecting ([`step2a-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2a-live-checks.txt)). The `www.` host redirects correctly to `https://nita.illinois.gov/`, so only the HTTP scheme is affected. The HTTPS homepage returned no `Strict-Transport-Security` header. The HTTP homepage declares `https://nita.illinois.gov/` as canonical. The 2026-11-19 crawl baseline also found two internal links that use `http://` (to a press release and to `/popa`) and two tag archives whose canonical uses `http://` (`/blog/tags/chicago`, `/blog/tags/moving-you`). See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt), [`pages.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/pages.csv), and [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv). By contrast, My Transit Benefit redirects HTTP to HTTPS.
- **Impact:** Every page is available at two protocol versions. Search engines have to rely on canonical tags to consolidate them, and links or bookmarks to HTTP URLs keep users on an unencrypted connection. Google's canonicalization guidance states a preference for HTTPS pages as canonical and lists redirects as a strong signal for consolidating duplicate URLs. Priority is High (team decision, 2026-11-24) because the issue affects every page and template, including pages with forms, and is a recurring condition rather than an isolated defect.
- **Recommendation:** Add a website-wide, server-level 301 redirect from HTTP to the equivalent HTTPS URL, then consider adding an HSTS header after the redirects are verified. Update internal links and canonicals that still use `http://`.
- **Implementation complexity:** Low (assumes a server or CDN configuration change; confirm with the hosting team)
- **Related standard:** [Google Search Central: consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) and [redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

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

### Former RTA URLs redirect to section overview pages instead of the matching current page

- **Finding ID:** SEO-NITA-024
- **Page or component:** Redirect rules for former RTA website paths (`/plans-programs/…`, `/rider-resources/…`, `/plan-your-trip/…`, `/finance-management/…`, `/about-us/…`) and the internal links that still use them.
- **Priority:** Medium
- **Evidence:** In the 2026-11-24 link crawl of the 1,609 NITA pages, 160 links in page content, on 132 pages (mostly RTA-era press releases and blog posts), point to 49 former RTA paths that redirect (301) to a section overview page: `/communities`, `/riders`, `/riders/how-to-ride`, `/transit-funding`, or `/about-rta`, which itself redirects to `/about-nita` ([`nita-legacy-redirects-to-section-pages.csv`](../../../evidence/crawls/link-discovery/2026-11-24/nita-legacy-redirects-to-section-pages.csv), with linking pages, anchor text, and redirect targets from the 2026-11-19 crawl). For 19 of the 49 paths (90 of the 160 links), a current page on the same subject exists:

  | Former RTA path | Links (pages) | Redirects to | Current page on the same subject |
  | --- | --- | --- | --- |
  | `/plans-programs/access-transit-program` | 21 (16) | `/communities` | [Access to Transit](https://nita.illinois.gov/communities/access-to-transit-program) |
  | `/plans-programs/community-planning` | 16 (16) | `/communities` | [Community Planning](https://nita.illinois.gov/communities/community-planning) |
  | `/plans-programs/grants-projects/community-planning` | 14 (14) | `/communities` | [Community Planning](https://nita.illinois.gov/communities/community-planning) |
  | `/plans-programs/programs-and-projects/section-5310-enhanced-mobility-seniors-and-individuals` | 12 (12) | `/communities` | [Section 5310](https://nita.illinois.gov/region/section-5310) |
  | `/plans-programs/programs-and-projects/section-5310` | 5 (5) | `/communities` | [Section 5310](https://nita.illinois.gov/region/section-5310) |
  | `/rider-resources/rta-fare-programs`, `/rider-resources/reduced-fare/ride-free-permits`, and three other reduced-fare paths | 8 (8) | `/riders` | [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs) |
  | `/plan-your-trip/travel-tips/paying-your-ride` | 2 (2) | `/riders/how-to-ride` | [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) |
  | `/about-us/media/press-release-archives/2021-press-releases/transit-ridership-survey-reveals` | 4 (4) | `/about-rta` → `/about-nita` | [Transit ridership survey reveals challenges for Chicago region in COVID’s wake](https://nita.illinois.gov/about-rta/press-releases/transit-ridership-survey-reveals-challenges-for-chicago-region-in-covids-wake) |
  | Three other `/about-us/media/press-release-archives/…` paths | 4 (4) | `/about-rta` → `/about-nita` | The matching press releases under [`/about-rta/press-releases/`](https://nita.illinois.gov/news/press-releases) |
  | `/finance-management/investor-relations/investor-relations`, `/about-us/careers`, `/about-us/board-meetings`, `/about-us/board-meetings/meetings-archive` | 4 (4) | `/transit-funding` or `/about-rta` | [Investor relations](https://nita.illinois.gov/about-nita/investor-relations), [Careers](https://nita.illinois.gov/careers), [Boards and Committees](https://nita.illinois.gov/about-nita/boards-and-committees), [Meeting Materials](https://nita.illinois.gov/about-nita/boards-and-committees/meeting-materials) |

  The same rules apply to links from other websites: on 2026-11-24, `https://www.rtachicago.org/plans-programs/access-transit-program` redirected through `https://nita.illinois.gov/plans-programs/access-transit-program` to `/communities` (2 redirects), and a former RTA press-release URL reached `/about-nita` after 3 redirects. Former paths that return 404 instead are covered in `SEO-NITA-009`.
- **Impact:** A reader who follows an older link about Access to Transit, Section 5310, or reduced-fare permits lands on a general section page and has to search again. Google's site-move guidance recommends mapping each old URL to its corresponding new URL; a redirect to a general section page gives search engines a weaker match, so the relevance of links built up by the RTA-era pages may not carry over to the current program pages. The effect cannot be measured without Search Console and backlink data.
- **Recommendation:** Update the redirect map so each former path with a clear successor redirects in one step to that page (at least the 19 paths listed in the evidence file), and send former press-release paths to the matching release. Update the 160 internal links to point directly at the current URLs. Keep section-level redirects only for paths with no equivalent page.
- **Implementation complexity:** Low (redirect rules and link updates)
- **Related standard:** [Google Search Central: redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects) and [site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)

### Coalition page redirects pass through six hops and end in a 404

- **Finding ID:** SEO-NITA-006
- **Page or component:** Redirects for the former “Transit Is the Answer” coalition pages: `/region/transit-is-the-answer/join-the-transit-is-the-answer-coalition`, `/region/transit-is-the-answer/coalition`, `/coalition`, `/transit-funding/coalition`, `/riders/coalition`, and `/communities/coalition`.
- **Priority:** Medium
- **Evidence:** On 2026-11-20, a request to `/region/transit-is-the-answer/join-the-transit-is-the-answer-coalition` passed through six 301 redirects (`/region/transit-is-the-answer/coalition` → `/coalition` → `/transit-funding/coalition` → `/riders/coalition` → `/communities/coalition` → `/region/coalition`) and ended at a 404 page ([`step2a-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2a-live-checks.txt)). The starting URL is linked from a 2023 blog post about reduced fares; the 2026-11-19 crawl baseline recorded the same chain ([`pages.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/pages.csv), and the batch `redirects.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/)). The coalition remains active (blog posts through 2026), and `/region/transit-is-the-answer` redirects to the external website `transitistheanswer.org`.
- **Impact:** Users following old coalition links, including any external links or bookmarks to these URLs, reach a “not found” page after several redirects instead of current coalition information. Search engines following the chain find no destination to consolidate signals to. Google follows a limited number of redirect hops and recommends avoiding chains.
- **Recommendation:** Point each of the six old coalition URLs directly, in one 301, to the current coalition destination (for example the relevant page on `transitistheanswer.org` or a NITA page about the coalition), and update the link in the 2023 blog post.
- **Implementation complexity:** Low (redirect configuration; confirm the intended destination with NITA)
- **Related standard:** [Google Search Central: redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Translations into seven languages are visible to users but not to search engines

- **Finding ID:** SEO-NITA-021
- **Page or component:** Website-wide language switcher (Weglot translation script in the page template); checked on the 16 NITA sample pages.
- **Priority:** Medium
- **Evidence:** On 2026-11-24 every NITA sample page loaded the Weglot script (`cdn.weglot.com/weglot.min.js`) and showed a language switcher with English, Español, Polski, العربية (Arabic), 中文 (简体) (Simplified Chinese), Tagalog, اردو (Urdu), and ગુજરાતી (Gujarati); every option except English links to `#` ([`weglot-check.txt`](../../../evidence/public-technical/2026-11-24/rendered-review/weglot-check.txt)). Selecting Español on [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs) translated the page in the browser without changing the URL:

  | Element | Before (English) | After selecting Español |
  | --- | --- | --- |
  | URL | `/riders/free-and-reduced-fare-programs` | `/riders/free-and-reduced-fare-programs` (unchanged) |
  | `<html lang>` | `en` | `es` |
  | `<title>` | Discounted Fares \| Northern Illinois Transit Authority | Tarifas con descuento \| Autoridad de Transporte Público del Norte de Illinois |
  | H1 | Discounted Fare and Ride Free Programs | Tarifas reducidas y programas de transporte gratuito |
  | Canonical | self (English URL) | self (English URL) |

  The choice is stored in the browser (`localStorage` key `wglang`). No sample page has `hreflang` annotations in the raw or rendered HTML ([`raw-vs-rendered.csv`](../../../evidence/public-technical/2026-11-24/rendered-review/raw-vs-rendered.csv)); `https://nita.illinois.gov/es/`, `/pl/`, and `/zh/` return 404; subdomains such as `es.nita.illinois.gov` do not resolve; and a `?lang=es` parameter returns the English page. The translated text therefore exists only after a visitor's browser runs the script and the visitor chooses a language.
- **Impact:** Search engines index one URL per page, and Googlebot does not use the language switcher, so it sees only the English version; as a result the Spanish, Polish, Chinese, and other versions cannot be found by people searching in those languages. NITA has invested in translations for rider-critical content such as reduced fares, paratransit, and trip planning, but that content is reachable only by visitors who already arrive at the English page. This is a discoverability limit, not a defect in the translations themselves, whose quality was not reviewed.
- **Recommendation:** Decide which languages and pages should be discoverable in search, starting with rider programs. Configure the translation service to serve each language on its own URL (Weglot supports subdirectory or subdomain setups that output translated HTML and `hreflang` annotations; confirm the plan and hosting requirements with the provider), add each language version to the sitemap or `hreflang` set, and have key machine-translated pages reviewed by a fluent speaker before they are exposed to search. Coordinate with the accessibility and content sections on language support.
- **Implementation complexity:** Medium (translation service configuration, DNS or server routing, and translation review)
- **Related standard:** [Google Search Central: managing multi-regional and multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites) and [localized versions of your pages (hreflang)](https://developers.google.com/search/docs/specialty/international/localized-versions)

### Homepage content jumps during loading and fails the desktop Core Web Vitals check

- **Finding ID:** SEO-NITA-019
- **Page or component:** [Homepage](https://nita.illinois.gov/) slider (`<ul id="homeslider">`) and the content below it.
- **Priority:** Medium
- **Evidence:** PageSpeed Insights on 2026-11-24 ([`psi-results.jsonl`](../../../evidence/public-technical/2026-11-24/psi-results.jsonl), [`psi-details.txt`](../../../evidence/public-technical/2026-11-24/psi-details.txt); method in the [README](../../../evidence/public-technical/2026-11-24/README.md)):

  | Data source | Device | Cumulative Layout Shift (CLS) | Assessment |
  | --- | --- | --- | --- |
  | Field data for this URL (Chrome users, latest 28 days) | Desktop | 0.29 | Core Web Vitals **Failed** (good is 0.1 or less) |
  | Field data for this URL | Mobile | 0 | Passed |
  | Lab test, two runs | Desktop | 0.363 and 0.352 | — |
  | Lab test, two runs | Mobile | 0.596 and 0.596 | — |

  In both lab runs, Lighthouse attributed almost all the shift to the footer contact block (`<div class="w-full bg-nitadarkblue-500">`, 0.351 on desktop and 0.596 on mobile), which is pushed down after the page first renders. Code inspection explains why: the stylesheet `/dist/app.css` positions every slide of `#homeslider` absolutely and hides it until JavaScript adds the `active` class (`#homeslider li{...position:absolute...visibility:hidden}`, `#homeslider li.active{...position:relative...}`), so the slider has no height until `/dist/app.js` runs; when it does, the first slide (up to 600 px tall on desktop) appears and moves the rest of the page down. With a warm cache in the audit browser the shift was small (0.011), so it depends on how late the script runs. The other six NITA templates tested had field CLS of 0 to 0.04.
- **Impact:** Desktop visitors to the homepage see content move after it appears, which can cause misclicks and makes the page feel unstable. The homepage is the only NITA page tested that fails Google's Core Web Vitals assessment, which Google uses as one page-experience signal; passing it does not guarantee any ranking change.
- **Recommendation:** Reserve the slider's height before JavaScript runs: render the first slide with the `active` class (or `position: relative`) in the HTML, or give `#homeslider` a fixed height or `aspect-ratio` per breakpoint, and add `width` and `height` attributes to the slide images. Re-test with PageSpeed Insights and watch the field CLS over the following 28 days.
- **Implementation complexity:** Low (template and CSS change)
- **Related standard:** [web.dev: Cumulative Layout Shift](https://web.dev/articles/cls) and [Google Search Central: Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)

### Links copied from Outlook emails route through Microsoft Safe Links and include staff email addresses

- **Finding ID:** SEO-NITA-026
- **Page or component:** Rich-text content on 21 pages, including seven core pages; follows up the Safe Links attribute noted in `SEO-NITA-008`.
- **Priority:** Medium
- **Evidence:** The HTML of all 1,609 NITA pages, fetched on 2026-11-24 for the internal link review, was searched for Microsoft Outlook Safe Links URLs (`*.safelinks.protection.outlook.com`): 68 were found on 21 pages, 49 as the link address (`href`) and 19 as the hover text (`title`) of another link ([`safelinks-urls.csv`](../../../evidence/public-technical/2026-11-24/content-review/safelinks-urls.csv), with each page, attribute, decoded destination, and the email address in the URL). Each Safe Links URL contains the mailbox of the person who copied it: `melissa.meyer@rtachicago.org` (30), `Jessica.Cabe@RTACHICAGO.ORG` (16), `MeyerM@RTACHICAGO.ORG` / `meyerm@rtachicago.org` (14), `Natalie.Rzucidlo@RTACHICAGO.ORG` (4), `gerry.tumbali@nita.illinois.gov` (2), and `Robert.Morris@RTACHICAGO.ORG` (2). Core pages affected:

  | Page | In `href` | In `title` | Real destinations |
  | --- | --- | --- | --- |
  | [Getting to the Obama Presidential Center](https://nita.illinois.gov/riders/how-to-ride/getting-to-the-obama-presidential-center) | 8 | 5 | Metra station pages, Metra ticket machines, Pace ADA page, Ventra app; one `title` points to `www.rtachicago.org` |
  | [Improving the system](https://nita.illinois.gov/transit-funding/improving-the-system) | 3 | 0 | `rtams.org` capital dataset, Pace and CTA transparency pages |
  | [Accessible transit](https://nita.illinois.gov/riders/accessible-transit) | 1 | 0 | `fares.rtachicago.org` (TAP and RAP applications) |
  | [Doing Business](https://nita.illinois.gov/about-nita/doing-business) | 1 | 0 | Federal Register DBE interim final rule |
  | [Ethics & OEIG](https://nita.illinois.gov/about-nita/transparency/ethics-oeig) | 1 | 1 | `oeig.illinois.gov` |
  | [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) | 0 | 2 | `getaccess.org`, Metra Regional Connect Pass (see `SEO-NITA-008`) |
  | [How to ride](https://nita.illinois.gov/riders/how-to-ride) | 0 | 1 | `www.rtachicago.org/riders/paying-for-your-ride` |

  The other 14 pages are press releases and blog posts from 2020 to 2026; the press release [Public transit is the best way to get to the Obama Presidential Center grand opening](https://nita.illinois.gov/about-rta/press-releases/public-transit-is-the-best-way-to-get-to-the-obama-presidential-center-grand-opening) alone has 17. Some decoded destinations are themselves Mailchimp click-tracking links (`rtachicago.us3.list-manage.com/track/click…`) or `rtachicago.zoom.us` meeting links. On 2026-11-24 the two Safe Links URLs tested (Accessible transit and Ethics & OEIG) still redirected (302) to their destinations.
- **Impact:** Each link depends on Microsoft's redirect service and on the sender's mail tenant; the links send users through an extra hop and may stop working or show a warning if those settings change. Search engines see a link to `safelinks.protection.outlook.com` instead of the real destination, so the page does not clearly reference the official CTA, Metra, Pace, or state page it cites. The URLs and hover text also publish staff email addresses and mail-system identifiers in the page source, and the `title` text appears as a long URL when users hover over a link.
- **Recommendation:** Replace every Safe Links `href` with the decoded destination listed in the evidence file, remove the Safe Links `title` attributes, and replace Mailchimp tracking and former RTA Zoom links with direct URLs. To prevent recurrence, add a CMS or publishing check that rejects links containing `safelinks.protection.outlook.com`, `list-manage.com/track`, or `rtachicago` domains, and ask editors to copy links from the destination page rather than from email.
- **Implementation complexity:** Low (68 link edits on 21 pages; optional CMS validation rule)
- **Related standard:** [Google Search Central: make links crawlable](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)

### Homepage title says only “Home” and its H1s come from rotating announcements

- **Finding ID:** SEO-NITA-010
- **Page or component:** [Homepage](https://nita.illinois.gov/) (`<title>` and H1 elements of the homepage template).
- **Priority:** Medium
- **Evidence:** On 2026-11-20 the homepage source contained ([`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)):
  - `<title>Home | Northern Illinois Transit Authority</title>`
  - three H1 elements, one per announcement slide: “NITA Ride Safe App Launches”, “Weigh in on NITA's draft regional budget”, and “Municipalities can apply for assistance in adhering to POPA”
  - the generic meta description ending in “…and combats…” (see `SEO-NITA-002` and `SEO-NITA-012`)

  No heading or title on the page states what NITA is or does. The 2026-11-19 crawl recorded the first two H1s. On 2026-11-24 the homepage had four H1s, the fourth being “Ride into the holidays with CTA, Metra, and Pace”, which shows that the H1 set changes with each new announcement ([`raw-vs-rendered.csv`](../../../evidence/public-technical/2026-11-24/rendered-review/raw-vs-rendered.csv)). In a Google search for “nita chicago” on 2026-11-24, the homepage result's snippet was the footer form's hidden confirmation message, “Thank you! We have received your submission. A NITA representative will be reaching out to you shortly…”, because the page has little other text about the agency ([search sample](../../../evidence/public-technical/2026-11-24/content-review/search-sample-2026-11-24.md), query 4).
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

### Past events, an expired alert, and conflicting phone hours appear as current information

- **Finding ID:** SEO-NITA-027
- **Page or component:** Time-sensitive text on the homepage, the [2027 NITA Regional Budget](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget), [NITA Riders Advisory Council](https://nita.illinois.gov/nita-rider-advisory-council), [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs), [Accessible transit](https://nita.illinois.gov/riders/accessible-transit), and [Riders](https://nita.illinois.gov/riders) pages.
- **Priority:** Medium
- **Evidence:** The text of the 20 sample pages was extracted from the HTML fetched on 2026-11-24 ([page text](../../../evidence/public-technical/2026-11-24/content-review/page-text/); extraction script [`extract_text.py`](../../../evidence/public-technical/2026-11-24/content-review/extract_text.py)) and every date, deadline, and phone schedule was compared with the review date and with partner websites ([`time-sensitive-content.txt`](../../../evidence/public-technical/2026-11-24/content-review/time-sensitive-content.txt)):

  | Page | Text on 2026-11-24 | Status |
  | --- | --- | --- |
  | [Homepage](https://nita.illinois.gov/), slide 2 | “Submit public comment by December 4 and register for a November 12 public hearing.” | Hearing date passed; comment period still open |
  | [2027 NITA Regional Budget](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget) | “NITA will hold a public hearing … on Thursday, Nov. 12” and “will present the proposed 2027 Regional Transit Budget to county boards … in November”; meta description: “The first regional budget for the agency will be available later this fall.” | Hearing passed; the proposed budget is already on the page. The hearing registration link uses the former `rtachicago.zoom.us` account and carries browser tracking parameters (`_gl`, `ampDeviceId`, `ampSessionId`) |
  | [NITA Riders Advisory Council](https://nita.illinois.gov/nita-rider-advisory-council) | “Applications are open from September 24 through October 31, 2026.” | Application period ended |
  | [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs), “Registration Site Alerts” | “There will be no NITA services at City Hall from 11:00 a.m. – 1:00 p.m. on Monday November 23, 2026.” and a second alert for the Southeast (Atlas) Center the same day | Alert for the previous day still shown |
  | [Accessible transit](https://nita.illinois.gov/riders/accessible-transit) | TAP and RAP rides “increasing from 30 to 40 rides per month … effective July 1, 2026” and “Starting May 1, 2026, … visit https://fares.RTAChicago.org to apply” | Written as upcoming; points to the former RTA fares domain through an Outlook Safe Links URL (`SEO-NITA-026`) |
  | [Riders](https://nita.illinois.gov/riders) and [Accessible transit](https://nita.illinois.gov/riders/accessible-transit) | ADA Paratransit applications at 312-663-HELP (4357): “between 8:30 a.m. and 5:00 p.m.” (Riders) and “between 8:00 a.m. and 5:00 p.m., Monday through Friday” (Accessible transit) | Conflicting hours; Pace's paratransit page gives 8:30 am |
  | [Riders](https://nita.illinois.gov/riders) and [Accessible transit](https://nita.illinois.gov/riders/accessible-transit) | “75 percent of CTA stations … are fully ADA accessible” (Riders) and “More than 70 percent of CTA 'L' stations are accessible” (Accessible transit) | Different figures for the same statistic; no date or source given |

  In a Google search for “ada paratransit chicago application” on 2026-11-24, Google displayed the Accessible transit page with the 8:00 a.m. hours in its snippet ([search sample](../../../evidence/public-technical/2026-11-24/content-review/search-sample-2026-11-24.md), query 2). Fares on Paying for your ride were checked against CTA, Pace, and Metra the same day and match, including the Metra tables labeled “Effective February 1, 2024” ([`fare-check.txt`](../../../evidence/public-technical/2026-11-24/content-review/fare-check.txt)).
- **Impact:** Riders and residents act on dates, deadlines, and phone hours. A hearing invitation after the hearing, a closed application period presented as open, and two different call hours for paratransit applications make the official source less reliable, and search engines and AI answers can repeat the outdated text, as the paratransit snippet shows. The budget and advisory council pages are where people look for current public-participation information.
- **Recommendation:** Update the listed text now (keep the December 4 comment deadline and link to the hearing recording or materials; state the advisory council's current status; confirm the paratransit call hours with the program and use one version). Then set an owner and review dates for time-sensitive content: give homepage slides and alerts an end date in the CMS, write program changes in the past tense once they take effect, and add a “last updated” date to pages with fares, hours, or deadlines. Replace the Zoom link with a clean NITA registration or recording link.
- **Implementation complexity:** Low (content edits) to Medium (CMS expiry fields and review process)
- **Related standard:** [Google Search Central: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

### Legacy document redirects point to HTTP destinations

- **Finding ID:** SEO-NITA-004
- **Page or component:** 141 internal links to legacy document URLs under `/sites/default/files/...` (previous Drupal paths), mainly on [Financial documents](https://nita.illinois.gov/transit-funding/financial-documents) (54) and historical press releases (49); full list in the evidence file.
- **Priority:** Low
- **Evidence:** On 2026-11-19, link discovery checked 1,004 internal document and image links with HEAD requests. All 141 that returned 301 redirect to an `http://nita.illinois.gov/uploads/files/general/Drupal-Old/...` destination. One example (`Spanish-Title-VI-Notice-to-Public.pdf`) was followed: the HTTP destination returned 200. Two other linked PDFs return 404 (`TransitIstheAnswer.pdf`, `Travel-Information-Action-Plan.pdf`). See [`links_resources.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/links_resources.csv) and [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt).
- **Impact:** Users and crawlers following these links pass through a redirect and land on an unencrypted document URL. Once `SEO-NITA-003` is fixed, each would become a two-step redirect chain. The documents include Title VI notices and financial reports that users may need.
- **Recommendation:** Update the internal links to point directly to the current HTTPS document URLs, and change the redirect targets to HTTPS so external links to the old paths resolve in one step. Restore or remove the links to the two missing PDFs.
- **Implementation complexity:** Low to Medium (depends on whether redirects are managed in the CMS or server configuration)
- **Related standard:** [Google Search Central: redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

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

### Sitemap lists a “404” page that returns 200 and is indexable

- **Finding ID:** SEO-NITA-007
- **Page or component:** [`/404`](https://nita.illinois.gov/404) and the [general-pages sitemap](../../../evidence/public-technical/2026-11-19/nita-sitemaps-1-section-pages-1-sitemap.xml).
- **Priority:** Low
- **Evidence:** On 2026-11-20, `/404` returned HTTP 200 with the title “404 | Northern Illinois Transit Authority”, `<meta name="robots" content="all">`, and a self-referencing canonical; it is listed in the general-pages sitemap. A nonexistent URL on the same website correctly returned 404 with `robots: none`, so `/404` appears to be a published CMS entry rather than the error response ([`step2a-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2a-live-checks.txt)). My Transit Benefit has the same pattern (`SEO-MTB-001`).
- **Impact:** The sitemap asks search engines to crawl and index an error-page entry. If indexed, a “404” page could appear in search results for NITA. The effect is limited to one URL among about 1,300 in the sitemap.
- **Recommendation:** Exclude `/404` from the sitemap and mark it `noindex`, or unpublish it if the error template does not depend on it. Apply the same fix on both websites, since they share the CMS setup.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: soft 404 errors](https://developers.google.com/search/docs/crawling-indexing/http-network-errors#soft-404-errors)

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

### Paginated listings declare the first page as canonical

- **Finding ID:** SEO-NITA-005
- **Page or component:** 248 paginated listing pages: [On Track blog](https://nita.illinois.gov/blog) (65), blog archive (36), blog categories `/blog/plan`, `/blog/invest`, and `/blog/move` (27), [press releases](https://nita.illinois.gov/news/press-releases) (34), meeting materials (9), and paginated tag archives (77).
- **Priority:** Low
- **Evidence:** On 2026-11-19, `/blog/p2` and `/blog/p3` returned 200, linked to the next page with standard anchors, and declared `https://nita.illinois.gov/blog` as canonical. The 2026-11-19 crawl baseline shows the same pattern on every paginated listing: each page canonicalizes to the first page of its listing. Older posts and press releases are reachable only through these sequential pages, up to 66 clicks from the homepage. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt) and [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv).
- **Impact:** Later listing pages contain different items from the first page, so the canonical signal is inaccurate. Search engines may give less weight to these pages and the links on them, which are the only internal crawl path to older posts and press releases. The XML sitemap partly offsets this because it lists individual posts.
- **Recommendation:** Give each paginated listing page a self-referencing canonical URL. Keep sequential links between pages.
- **Implementation complexity:** Low (template change)
- **Related standard:** [Google Search Central: pagination best practices](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)

### External links lead to removed pages and closed domains

- **Finding ID:** SEO-NITA-018
- **Page or component:** Outbound links on 337 pages: 253 blog posts, 76 press releases, and 8 other pages (including [NITA engagement](https://nita.illinois.gov/region/nita-engagement), [Doing business](https://nita.illinois.gov/about-nita/doing-business), and the 2024–2026 regional budget pages).
- **Priority:** Low
- **Evidence:** On 2026-11-20 each of the 2,184 unique external URLs linked from NITA's HTML pages was requested with a script ([`nita-external-link-status.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-link-status.csv)), and every page was re-read to record each link to a failing URL with its source page and link text ([`nita-external-broken-link-edges.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-broken-link-edges.csv); method in the [README](../../../evidence/crawls/link-discovery/2026-11-20/README.md)). The 459 URLs with inconclusive script results (403, 400, 999, timeouts) were then opened in a browser: one sample URL per domain, and every URL on domains that loaded normally ([`nita-external-links-browser-check.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-links-browser-check.csv)). Team rule: a link that opens normally in a browser is treated as working. Only definitive failures are reported here ([`nita-external-link-classification.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-link-classification.csv)):

  | Result | Unique URLs | Links |
  | --- | --- | --- |
  | The destination website answered 404 or 410 (not found or gone) | 222 | 380 |
  | The domain no longer resolves (no DNS record; rechecked with a public resolver) | 94 | 133 |
  | `blog.rtachicago.org` serves a certificate that does not match the host | 52 | 89 |
  | Browser: legacy RTA document link redirects to a `nita.illinois.gov/files/documents/` path that returns 403 Forbidden | 28 | 41 |
  | Browser: “Page not found” | 20 | 20 |
  | Browser: certificate error (wrong host or expired), including `https://www.rtachicago.com` (expired) | 15 | 20 |
  | Browser: redirects to an unrelated generic page (APTA press releases and reports, a DOT page) | 10 | 11 |
  | Browser: account or site removed (Facebook `ChicagoRTA`, X `RTA_Chicago`, a WordPress staging site) | 8 | 26 |
  | Browser: domain parked or for sale | 2 | 2 |
  | **Total confirmed** | **451** | **722** |

  Representative browser results on 2026-11-20: [`metra.com/careers`](https://metra.com/careers) shows “Page not found”, RTA Zoom registration links show Zoom's “Page Not Found”, `x.com/RTA_Chicago` shows “This account doesn't exist”, `facebook.com/ChicagoRTA` shows “This content isn't available right now”, and `http://blog.rtachicago.org/subscribe` redirects to a 404 on `illinois.gov`. Another 315 URLs (480 links on 85 domains) remain unverified because the browser was blocked (CloudFront, Cloudflare challenges, firewalls, sign-in walls), the page did not load, or the URL could not be opened from the audit location; they are not counted in this finding and are listed for a check from the United States ([`nita-external-links-browser-check.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-links-browser-check.csv), `review-*` rows). They include NITA's own data portal, `datahub.nita.illinois.gov` (and `rtams.org`, which redirects to it).

  Broken external links on pages other than blog posts and press releases (all links):

  | Page | Link text | `href` | Result |
  | --- | --- | --- | --- |
  | [/region/nita-engagement](https://nita.illinois.gov/region/nita-engagement) | “Metra careers” | `https://metra.com/careers` | 404 |
  | [/communities/toolkits-and-education/parking-guide](https://nita.illinois.gov/communities/toolkits-and-education/parking-guide) | “The average car is parked 95% of the day” | `http://shoup.bol.ucla.edu/PayAsYouPark.htm` | Domain does not resolve |
  | [/about-nita/boards-and-committees/meeting-materials](https://nita.illinois.gov/about-nita/boards-and-committees/meeting-materials) | “Watch” | `http://bBYSGRLeg4Y` | Domain does not resolve |
  | [/about-nita/doing-business](https://nita.illinois.gov/about-nita/doing-business) | “Illinois Uniform Certification Program (IL UCP) DBE Directory” | `https://idot.illinois.gov/doing-business/certifications/disadvantaged-business-enterprise-certification/il-ucp-directory/index` | 404 |
  | [/transit-funding/2026-regional-transit-budget](https://nita.illinois.gov/transit-funding/2026-regional-transit-budget) | “Preregister for the virtual hearing here” | `https://pacebus.zoom.us/webinar/register/WN_opHp0DCGSM2afD7N6JnmaQ#/registration` | 404 |
  | [/transit-funding/2025-regional-transit-budget](https://nita.illinois.gov/transit-funding/2025-regional-transit-budget) | “Download 2025 Proposed Metra Budget” | `https://metra.com/sites/default/files/inline-files/8.5x11_ProposedBudgetBook_2025_Web_FINAL%20%28002%29.pdf` | 404 |
  | [/transit-funding/2025-regional-transit-budget](https://nita.illinois.gov/transit-funding/2025-regional-transit-budget) | “Virtual” | `https://pacebus.zoom.us/webinar/register/WN_l7VuU83ySuKFTULjcY-gAw` | 404 |
  | [/transit-funding/2025-regional-transit-budget](https://nita.illinois.gov/transit-funding/2025-regional-transit-budget) | “Virtual” | `https://pacebus.zoom.us/webinar/register/WN_lPERS2-QRxup-6ZlEqTU4w` | 404 |
  | [/transit-funding/2025-regional-transit-budget](https://nita.illinois.gov/transit-funding/2025-regional-transit-budget) | “” | `https://pacebus.zoom.us/webinar/register/WN_l7VuU83ySuKFTULjcY-gAw` | 404 |
  | [/transit-funding/2024-regional-transit-budget](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget) | “2024 Operating and Capital Program and Budget” | `https://metra.com/sites/default/files/inline-files/Brochure_8.5x11_ProposedBudgetBook_2024_Web_FINAL_0.pdf` | 404 |
  | [/transit-funding/2024-regional-transit-budget](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget) | “here” | `https://pacebus.zoom.us/webinar/register/WN_8UtqK1s9SWWHnPwsdPvPIA` | 404 |
  | [/transit-funding/2024-regional-transit-budget](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget) | “here” | `https://pacebus.zoom.us/webinar/register/WN_w4oprArJRqO6PX0afD1Erg` | 404 |
  | [/transit-funding/2024-regional-transit-budget](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget) | “Virtual” | `https://pacebus.zoom.us/webinar/register/WN_8UtqK1s9SWWHnPwsdPvPIA` | 404 |
  | [/transit-funding/2024-regional-transit-budget](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget) | “Virtual” | `https://pacebus.zoom.us/webinar/register/WN_w4oprArJRqO6PX0afD1Erg` | 404 |
  | [/transit-funding/2024-regional-transit-budget](https://nita.illinois.gov/transit-funding/2024-regional-transit-budget) | “Register for the public hearing here.” | `https://rtachicago.zoom.us/meeting/register/tZYsduivqjwiG9PSVV9tPj15QsadYAeENuIS#/registration` | 404 |
  | [/recovery](https://nita.illinois.gov/recovery) | “blog post” | `https://blog.rtachicago.org/2021/04/19/survey-shows-current-riders-are-more-likely-to-be-essential-workers-or-minorities-feel-transit-is-safe/` | Certificate invalid for host |
  | [/recovery](https://nita.illinois.gov/recovery) | “Wear Masks, Ride Responsibly” | `https://blog.rtachicago.org/2021/05/11/transit-agencies-launch-campaign-asking-riders-to-wear-masks-ride-responsibly/` | Certificate invalid for host |

  The meeting-materials link `http://bBYSGRLeg4Y` (“Watch”) appears to be a video ID entered without its YouTube address.

  Confirmed broken links by destination domain and result (four or more links):

  | Domain | Result | Links | Pages | URLs | Example link (source page → link text) |
  | --- | --- | --- | --- | --- | --- |
  | `blog.rtachicago.org` | Certificate invalid for host | 89 | 47 | 52 | [/blog/2022/09/02/clearbrook-transportation-services-connect-](https://nita.illinois.gov/blog/2022/09/02/clearbrook-transportation-services-connect-individuals-with-disabilities-to-their-communities) → “Moving You series” |
  | `rideonrtachicago.com` | Domain does not resolve | 73 | 12 | 60 | [/about-rta/press-releases/a-look-back-on-2019-state-passes-r](https://nita.illinois.gov/about-rta/press-releases/a-look-back-on-2019-state-passes-rebuild-illinois-largest-capital-bill-in-a-decade) → “worked with regional partners” |
  | `rtachicago.org` | 404/410 | 66 | 37 | 38 | [/blog/2025/08/19/coalition-members-provide-feedback-on-fundi](https://nita.illinois.gov/blog/2025/08/19/coalition-members-provide-feedback-on-funding-reform-as-fiscal-cliff-nears) → “Transforming Transit” |
  | `rtachicago.com` | 404/410 | 40 | 23 | 25 | [/blog/2019/08/22/rta-board-approves-projects-to-benefit-seni](https://nita.illinois.gov/blog/2019/08/22/rta-board-approves-projects-to-benefit-seniors-and-people-with-disabilities) → “RTA's Section 5310 webpage” |
  | `epa.gov` | 404/410 | 30 | 10 | 3 | [/about-rta/press-releases/rta-service-boards-encourage-resid](https://nita.illinois.gov/about-rta/press-releases/rta-service-boards-encourage-residents-to-go-green-and-save-some-green-by-taking-transit-on-earth-day) → “Clean Air Act” |
  | `rtachicago.org` | Redirects to a NITA document path returning 403 (browser) | 27 | 24 | 15 | [/blog/2018/09/05/design-by-transit-the-2018-community-planni](https://nita.illinois.gov/blog/2018/09/05/design-by-transit-the-2018-community-planning-program-implementation-report) → “which is linked here” |
  | `metra.com` | 404/410 | 26 | 20 | 16 | [/region/nita-engagement](https://nita.illinois.gov/region/nita-engagement) → “Metra careers” |
  | `rtachicago.zoom.us` | 404/410 | 26 | 13 | 23 | [/blog/2023/05/04/rta-begins-exploring-reduced-fares-for-ride](https://nita.illinois.gov/blog/2023/05/04/rta-begins-exploring-reduced-fares-for-riders-with-low-incomes) → “Transit is the Answer Coalition meeting on May 9” |
  | `twitter.com` | 404/410 | 25 | 19 | 4 | [/blog/2022/09/08/rta-engages-with-riders-at-community-events](https://nita.illinois.gov/blog/2022/09/08/rta-engages-with-riders-at-community-events-publishes-survey-to-hear-from-you-on-future-of-transit) → “RTA on social media” |
  | `facebook.com` | Account or site removed (browser) | 22 | 21 | 4 | [/blog/2015/09/22/are-you-ready-for-the-winter](https://nita.illinois.gov/blog/2015/09/22/are-you-ready-for-the-winter) → “Facebook” |
  | `pacebus.com` | 404/410 | 17 | 15 | 5 | [/about-rta/press-releases/rta-encourages-commuters-to-celebr](https://nita.illinois.gov/about-rta/press-releases/rta-encourages-commuters-to-celebrate-earth-day-friday-2016) → “www.pacebus.com” |
  | `rtachicago.com` | Redirects to a NITA document path returning 403 (browser) | 14 | 10 | 13 | [/blog/2018/10/18/tell-us-what-you-think-of-transit](https://nita.illinois.gov/blog/2018/10/18/tell-us-what-you-think-of-transit) → “2013-2014 Customer Satisfaction Survey” |
  | `blog.rtachicago.org` | 404/410 | 12 | 12 | 1 | [/about-rta/press-releases/rta-board-approves-2022-regional-o](https://nita.illinois.gov/about-rta/press-releases/rta-board-approves-2022-regional-operating-budget-and-2022-2026-capital-program-for-metropolitan-chicago-transit) → “Subscribe” |
  | `getonboardil.org` | Domain does not resolve | 11 | 7 | 2 | [/about-rta/press-releases/national-infrastructure-week-its-t](https://nita.illinois.gov/about-rta/press-releases/national-infrastructure-week-its-time-to-investintransit) → “www.GetonBoardIL.org” |
  | `apta.com` | Redirects to an unrelated generic page (browser) | 10 | 10 | 9 | [/blog/2023/06/01/legislative-update-lawmakers-take-important](https://nita.illinois.gov/blog/2023/06/01/legislative-update-lawmakers-take-important-steps-to-make-transit-system-less-reliant-on-fares) → “challenges” |
  | `cmap.illinois.gov` | 404/410 | 10 | 6 | 8 | [/blog/2024/04/18/transit-is-the-answer-to-meeting-illinois-c](https://nita.illinois.gov/blog/2024/04/18/transit-is-the-answer-to-meeting-illinois-climate-goals) → “modernization” |
  | `earthday.org` | 404/410 | 10 | 10 | 1 | [/about-rta/press-releases/rta-service-boards-encourage-resid](https://nita.illinois.gov/about-rta/press-releases/rta-service-boards-encourage-residents-to-go-green-and-save-some-green-by-taking-transit-on-earth-day) → “first Earth Day, celebrated nearly 47 years ago, o” |
  | `pacebus.zoom.us` | 404/410 | 8 | 3 | 5 | [/transit-funding/2026-regional-transit-budget](https://nita.illinois.gov/transit-funding/2026-regional-transit-budget) → “Preregister for the virtual hearing here” |
  | `chicagotribune.com` | 404/410 | 8 | 8 | 8 | [/blog/2017/10/09/transit-signal-priority-an-invisible-benefi](https://nita.illinois.gov/blog/2017/10/09/transit-signal-priority-an-invisible-benefit-for-riders) → “Chicago Tribune highlighted Pace’s new “Pulse” ser” |
  | `chicagobusiness.com` | Not found (browser) | 8 | 6 | 8 | [/blog/2016/09/22/cmap-study-shows-not-your-fathers-travel-tr](https://nita.illinois.gov/blog/2016/09/22/cmap-study-shows-not-your-fathers-travel-trends) → “Greg Hinz's” |
  | `web.rtachicago.org` | Domain does not resolve | 8 | 7 | 3 | [/about-rta/press-releases/rta-metra-to-hold-joint-2015-budge](https://nita.illinois.gov/about-rta/press-releases/rta-metra-to-hold-joint-2015-budget-hearings) → “2015 Proposed Operating Budget and Capital Program” |
  | `metroplanning.org` | 404/410 | 6 | 3 | 6 | [/blog/2021/03/22/rta-working-with-partners-to-improve-transp](https://nita.illinois.gov/blog/2021/03/22/rta-working-with-partners-to-improve-transportation-access-for-all) → “Universal Mobility report” |
  | `rsgsurvey.com` | 404/410 | 6 | 2 | 3 | [/blog/2020/03/02/hows-your-ride-take-this-survey](https://nita.illinois.gov/blog/2020/03/02/hows-your-ride-take-this-survey) → “https://rsgsurvey.com/cta/pages/soc?locale=4” |
  | `gettingamericatowork.com` | Domain does not resolve | 6 | 6 | 3 | [/about-rta/press-releases/rta-encourages-commuters-to-celebr](https://nita.illinois.gov/about-rta/press-releases/rta-encourages-commuters-to-celebrate-earth-day-thursday) → “www.gettingamericatowork.com/standil” |
  | `transitistheanswer.org` | 404/410 | 5 | 5 | 2 | [/blog/2024/08/27/transit-station-activations-in-rogers-park-](https://nita.illinois.gov/blog/2024/08/27/transit-station-activations-in-rogers-park-joliet-bring-live-music-games-and-more) → “RTA Public Transit Safety and Security Summit” |
  | `illinoistransportationsymposium.com` | Domain does not resolve | 5 | 4 | 3 | [/about-rta/press-releases/regional-transportation-authority-](https://nita.illinois.gov/about-rta/press-releases/regional-transportation-authority-joins-transit-and-transportation-partners-to-host-20th-annual-transportation-symposium-and-business-exchange) → “http://illinoistransportationsymposium.com” |
  | `chicago.gov` | 404/410 | 4 | 2 | 4 | [/blog/2026/06/25/how-to-ride-transit-to-kid-friendly-destina](https://nita.illinois.gov/blog/2026/06/25/how-to-ride-transit-to-kid-friendly-destinations-in-the-chicago-region) → “ice skating” |
  | `chicagohistory.org` | 404/410 | 4 | 3 | 3 | [/blog/2023/01/26/how-to-use-transit-to-celebrate-black-histo](https://nita.illinois.gov/blog/2023/01/26/how-to-use-transit-to-celebrate-black-history-month-in-the-chicago-region) → “Learn more.” |
  | `kimballcurb.org` | Domain does not resolve | 4 | 2 | 2 | [/blog/2023/06/01/curb-management-and-tod-community-planning-](https://nita.illinois.gov/blog/2023/06/01/curb-management-and-tod-community-planning-projects-kick-off-throughout-region) → “curb and mobility study” |
  | `cnt.org` | Certificate error (browser) | 4 | 3 | 3 | [/blog/2021/11/16/public-forum-focuses-on-lessons-from-the-pa](https://nita.illinois.gov/blog/2021/11/16/public-forum-focuses-on-lessons-from-the-pandemic-in-planning-for-transits-future) → “Center for Neighborhood Technology” |
  | `transitchicago.com` | 404/410 | 4 | 3 | 3 | [/blog/2021/04/19/survey-shows-current-riders-are-more-likely](https://nita.illinois.gov/blog/2021/04/19/survey-shows-current-riders-are-more-likely-to-be-essential-workers-or-minorities-feel-transit-is-safe) → “CTA” |
  | `cityofchicago.org` | 404/410 | 4 | 4 | 3 | [/about-rta/press-releases/rta-celebrates-26th-anniversary-of](https://nita.illinois.gov/about-rta/press-releases/rta-celebrates-26th-anniversary-of-americans-with-disabilities-act) → “AccessChicago 2016” |
  | `navypier.com` | 404/410 | 4 | 2 | 1 | [/about-rta/press-releases/public-transportation-offers-best-](https://nita.illinois.gov/about-rta/press-releases/public-transportation-offers-best-travel-option-for-fourth-of-july-festivities) → “Fourth of July Fireworks at Navy Pier” |
  | `willconnects2040.org` | Domain does not resolve | 4 | 1 | 2 | [/blog/2016/01/15/shaping-the-future-of-transportation-in-wil](https://nita.illinois.gov/blog/2016/01/15/shaping-the-future-of-transportation-in-will-county) → “Will Connects 2040” |
  | 95 other domains | mixed | 122 | 94 | 110 | see [`nita-external-link-classification.csv`](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-link-classification.csv) |

  Patterns in the data:
  - **Former RTA domains (339 links to 217 URLs on 164 pages):** links to `blog.rtachicago.org`, `rideonrtachicago.com`, `web.rtachicago.org`, `drupal.rtachicago.org`, `tripplanner.rtachicago.*`, `tripsweb.rtachicago.com`, `rtachicago.org`, and `rtachicago.com` (RTA Zoom links are counted under expired events). For 46 of the 52 `blog.rtachicago.org` URLs (70 links), the same post exists on NITA's website with the same path under `/blog/` and returns 200, so the link can be rewritten directly. 169 links (100 URLs, on 102 pages) go to `rtachicago.org` or `rtachicago.com` addresses that now redirect to the same path on `nita.illinois.gov` (or to `illinois.gov`), where the page returns 404 or, for 28 legacy documents under `/files/documents/`, 403 Forbidden; for example `http://www.rtachicago.com/index.php/plans-programs/grants-projects/access-to-transit.html` (8 links). Over HTTPS, `www.rtachicago.com` serves an expired certificate.
  - **Retired social accounts:** 48 links on 22 pages point to `twitter.com/RTA_Chicago` and similar RTA-era X accounts or to `facebook.com/ChicagoRTA`, which no longer exist; NITA's current accounts are [`x.com/NITA_Chicago`](https://x.com/NITA_Chicago) and [`facebook.com/NITAchicago`](https://www.facebook.com/NITAchicago/).
  - **Expired event and document links:** past Zoom hearing registrations (`rtachicago.zoom.us`, `pacebus.zoom.us`), annual Earth Day press releases that each repeat the same three EPA links and one Earth Day link, and partner documents and articles that have moved (Metra budget books, CMAP, APTA, Chicago Tribune and Crain's articles).
  - **Concentration:** the pages with the most broken links are annual look-back press releases: [Invest in transit: a look back at 2018](https://nita.illinois.gov/about-rta/press-releases/invest-in-transit-a-look-back-at-2018) (26), [A look back on 2019](https://nita.illinois.gov/about-rta/press-releases/a-look-back-on-2019-state-passes-rebuild-illinois-largest-capital-bill-in-a-decade) (22, and 22 on the [blog version](https://nita.illinois.gov/blog/2019/12/30/a-look-back-on-2019-state-passes-rebuild-illinois-largest-capital-bill-in-a-decade)), [Transit is moving forward in our region in 2017](https://nita.illinois.gov/about-rta/press-releases/transit-is-moving-forward-in-our-region-the-rta-worked-hard-for-riders-in-2017) (19), and [2016 look-back](https://nita.illinois.gov/about-rta/press-releases/rta-worked-with-service-boards-and-partners-to-move-transit-forward-in-2016) (14).
- **Impact:** Most broken links are in historical posts and press releases, where they reduce the usefulness of the archive rather than block a current task. A few affect current pages: the Doing business page links to a missing certification directory for disadvantaged business enterprises, and the NITA engagement page sends job seekers to a missing Metra careers page. Links to closed RTA domains and deleted social accounts also signal outdated content. Search engines do not penalize a website for occasional broken outbound links, but links that consistently fail make pages less helpful for users.
- **Recommendation:** Fix the links on current pages first (table above): update the IL UCP directory and Metra careers links, correct the “Watch” video link, and replace or remove expired Zoom registrations and moved budget documents on the budget pages. Then rewrite links to former RTA domains in bulk: replace `blog.rtachicago.org/…` with `nita.illinois.gov/blog/…` where the post exists (46 URLs), point RTA social links to NITA's accounts, and map the legacy `rtachicago.org` and `rtachicago.com` paths, including the `/files/documents/` PDFs, to current NITA pages or documents, together with the internal legacy redirects in `SEO-NITA-004`, `SEO-NITA-006`, and `SEO-NITA-009`. For other historical posts, update or unlink dead references, and add a periodic external link check to content maintenance. Complete the check of the 315 unverified URLs from a US connection.
- **Implementation complexity:** Medium (current-page fixes are low; bulk rewrites across about 330 historical entries need a script or CMS search-and-replace and editorial review)
- **Related standard:** [Google Search Central: SEO starter guide — link to relevant resources](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#link-to-relevant-resources)

### Some current pages are linked only from the desktop menu or from a single news post

- **Finding ID:** SEO-NITA-023
- **Page or component:** Global navigation (desktop menu `<nav class="hidden lg:flex …">`, hidden on small screens, and the mobile menu opened with “Open menu”) and in-content links to current program and governance pages.
- **Priority:** Low
- **Evidence:** On 2026-11-24 the two menus were compared on the homepage at a 375 px width ([`nav-parity.txt`](../../../evidence/public-technical/2026-11-24/mobile-review/nav-parity.txt)). Both are in the same HTML. The mobile menu lists every section overview and second-level page (35 page links plus search, Careers, and Contact); the desktop menu has 53 unique links, and its 19 extra links are 15 third-level pages and four featured blog posts. The same day, every internal link on the 1,609 NITA HTML pages was recorded with the part of the page it sits in ([`nita-internal-link-edges.csv.gz`](../../../evidence/crawls/link-discovery/2026-11-24/nita-internal-link-edges.csv.gz); linking pages per URL in [`nita-page-inlinks.csv`](../../../evidence/crawls/link-discovery/2026-11-24/nita-page-inlinks.csv); method in the [README](../../../evidence/crawls/link-discovery/2026-11-24/README.md)). Most desktop-only pages are also linked from their parent page's content, but these current pages are not:

  | Page | Desktop menu | Mobile menu | Pages linking to it in their content |
  | --- | --- | --- | --- |
  | [NITA Committees](https://nita.illinois.gov/about-nita/boards-and-committees/nita-committees) | Yes | No | None |
  | [Registration Sites](https://nita.illinois.gov/riders/free-and-reduced-fare-programs/registration-sites) (a shortcut that redirects (302) to an ArcGIS map of Reduced Fare and Ride Free registration sites) | Yes | No | None |
  | [Upcoming public meetings on transit service](https://nita.illinois.gov/region/nita-engagement/public-meetings) | Yes | No | 1: the 2026-11-02 post [What moves you?](https://nita.illinois.gov/blog/2026/11/02/what-moves-you-thousands-weigh-in-on-their-regional-transit-priorities-via-online-survey-at-union-station-event) (“View upcoming engagement opportunities”) |
  | [Getting to the Obama Presidential Center](https://nita.illinois.gov/riders/how-to-ride/getting-to-the-obama-presidential-center) | Yes | No | 1: the press release [Public transit is the best way to get to the Obama Presidential Center grand opening](https://nita.illinois.gov/about-rta/press-releases/public-transit-is-the-best-way-to-get-to-the-obama-presidential-center-grand-opening) |
  | [NITA Riders Advisory Council](https://nita.illinois.gov/nita-rider-advisory-council) | No | No | 1: the 2026-09-25 post [NITA launches Rider Advisory Councils, now accepting applications](https://nita.illinois.gov/blog/2026/09/25/nita-launches-rider-advisory-councils-now-accepting-applications) |
  | [NITA ADA Advisory Council](https://nita.illinois.gov/nita-ada-advisory-council) | No | No | 1: the same 2026-09-25 post |

  The two advisory council pages describe councils that the NITA legislation requires; they sit at top-level URLs outside [Boards and Committees](https://nita.illinois.gov/about-nita/boards-and-committees), and the Riders Advisory Council page says applications were open from September 24 through October 31, 2026. The other desktop-only pages (the five community toolkit guides, three board pages, and the Oversight audits, Ethics & OEIG, and FOIA pages) are linked from their parent page's content.
- **Impact:** Search engines can still find the menu-linked pages because the desktop menu stays in the HTML, but pages with only one contextual link, from a news post that will move down the blog listing, receive little internal signal about their importance. For phone users, these pages have no path from their section: people looking for public meetings, reduced-fare registration sites, or the advisory councils have to use search or find the right news post.
- **Recommendation:** Link each page from its parent page's content (for example a “Related pages” list on How to ride, Discounted Fare and Ride Free Programs, A Stronger Region Moves Together, and Boards and Committees). Add the two advisory councils to Boards and Committees and, for the ADA council, to Accessible transit; if their URLs are moved under `/about-nita/boards-and-committees/`, redirect the current URLs. Consider a third menu level on mobile for sections with child pages. Coordinate with the UX section, which assesses navigation.
- **Implementation complexity:** Low (content links) to Medium (mobile menu template or URL moves)
- **Related standard:** [Google Search Central: SEO starter guide, links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) and [mobile-first indexing best practices](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)

### Related Articles and pagination do not connect the archive of posts and press releases

- **Finding ID:** SEO-NITA-025
- **Page or component:** “Related Articles” block of the blog post template; press-release template; blog and press-release listings.
- **Priority:** Low
- **Evidence:** In the 2026-11-24 link crawl, 791 of the 792 blog posts have a “Related Articles” block with six links, but only five different sets of six posts appear across all of them ([`nita-related-articles.csv`](../../../evidence/crawls/link-discovery/2026-11-24/nita-related-articles.csv)): the block shows the latest posts of a group, not posts on the same topic. The largest set is frozen in 2020: 442 posts published from 2015-08-20 to 2020-07-29, on any subject, all link to the same six posts from March to July 2020:

  | Post shown in Related Articles on 442 older posts |
  | --- |
  | [How's Your Ride? Take This Survey](https://nita.illinois.gov/blog/2020/03/02/hows-your-ride-take-this-survey) (2020-03-02) |
  | [Happy International Women’s Day and Women’s History Month from the RTA](https://nita.illinois.gov/blog/2020/03/08/happy-international-womens-day-and-womens-history-month-from-the-rta) (2020-03-08) |
  | [Announcing the 2020 Access to Transit Program Call for Projects for Small-Scale Capital Projects](https://nita.illinois.gov/blog/2020/03/13/announcing-the-2020-access-to-transit-program-call-for-projects-for-small-scale-capital-projects) (2020-03-13) |
  | [Transportation Tuesday Webinar Series: Attend the 2020 RTA Annual Planning Workshop Virtually](https://nita.illinois.gov/blog/2020/04/17/transportation-tuesday-webinar-series-attend-the-2020-rta-annual-planning-workshop-virtually) (2020-04-17) |
  | [Take a survey to help improve mobility options for older adults and people with disabilities](https://nita.illinois.gov/blog/2020/05/07/take-a-survey-to-help-improve-mobility-options-for-older-adults-and-people-with-disabilities) (2020-05-07) |
  | [RTA celebrates 30 years of the Americans with Disabilities Act](https://nita.illinois.gov/blog/2020/07/29/rta-celebrates-30-years-of-the-americans-with-disabilities-act) (2020-07-29) |

  The other sets show recent posts: 180 posts show the same six NITA posts from September to November 2026, 88 a fixed set of posts from 2025 and 2026, 76 the six newest posts, and 5 posts a set of five that includes four 2022 posts and a post dated 1970-01-01 ([`/blog/1970/01/01/take-rta-survey`](https://nita.illinois.gov/blog/1970/01/01/take-rta-survey)). The 420 press releases have no related links and no tags. Older content is otherwise reached through numbered listing pages: in the 2026-11-19 crawl, blog posts are a median of 13 clicks from the homepage (364 posts more than 30 clicks) and press releases a median of 19 (72 more than 30), with a maximum of 66 ([B1 `pages.csv`](../../../evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/pages.csv)). Posts are also reachable through 78 tag archives (no more than 7 clicks deep), but those archives have generic titles (`SEO-NITA-001`).
- **Impact:** Related links are one of the few ways readers and search engines move between articles on the same subject. Showing the same 2020 announcements on 442 posts about other subjects sends links to expired surveys and events, and gives no path from an older post to current NITA content on the same topic. Deep pagination makes the archive slow to crawl and hard to browse, although every post is in the XML sitemap. The direct ranking effect is limited and depends on how much search traffic the archive receives, which this audit cannot measure.
- **Recommendation:** Change Related Articles to select posts that share a tag or category with the current post, newest first, with a fallback to the latest NITA posts; exclude posts dated 1970-01-01 and fix that post's date. Add tags or a topic link to press releases, and link press releases to the related program page (for example budget releases to the current budget page). Consider year archives or a filterable listing for posts and press releases so that older content is a few clicks from the listing page.
- **Implementation complexity:** Medium (CMS template query and listing changes)
- **Related standard:** [Google Search Central: SEO starter guide, links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) and [pagination best practices](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)

### Mobile lab tests show slow loading caused by scripts and oversized images

- **Finding ID:** SEO-NITA-020
- **Page or component:** Shared page template (header scripts and footer form) and the homepage slider image; measured on 7 templates.
- **Priority:** Low
- **Evidence:** PageSpeed Insights on 2026-11-24 ([`psi-results.jsonl`](../../../evidence/public-technical/2026-11-24/psi-results.jsonl), [`psi-details.txt`](../../../evidence/public-technical/2026-11-24/psi-details.txt)). Field data from real Chrome users passes on mobile for every template tested (LCP 1.6–1.8 s, INP 92–133 ms, CLS 0; URL-level data for the homepage, Riders, and the 2027 budget page; origin-level data for the others). The mobile lab test, which simulates a mid-range phone on a slow 4G connection, is much slower:

  | Template | Mobile lab score | Lab LCP | Desktop lab score |
  | --- | --- | --- | --- |
  | [Homepage](https://nita.illinois.gov/) (two runs) | 41 / 41 | 13.5 s / 12.2 s | 59 / 61 |
  | [Riders](https://nita.illinois.gov/riders) | 68 | 9.4 s | 74 |
  | [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) | 72 | 8.3 s | 94 |
  | [2027 regional transit budget](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget) | 52 | 7.7 s | 92 |
  | [On Track blog](https://nita.illinois.gov/blog) | 67 | 11.2 s | 90 |
  | [Blog post (2026-10-01)](https://nita.illinois.gov/blog/2026/10/01/nita-expanding-access-pilot-program-to-cta-and-pace-starting-october-1-offering-income-based-reduced-fare-transit-regionwide) | 89 | 2.2 s | 93 |
  | [Budget press release (2026)](https://nita.illinois.gov/about-rta/press-releases/northern-illinois-transit-authoritys-first-regional-budget-proposal-expands-service-creates-jobs-and-improves-safety-across-six-counties) | 79 | 2.2 s | 81 |

  Main causes reported on the homepage (similar on the other templates):
  - **Render-blocking script:** the Weglot translation script (`cdn.weglot.com/weglot.min.js`, 74.8 KiB) is loaded in `<head>` without `defer` or `async` and blocks rendering for about 1.2 s on mobile.
  - **reCAPTCHA on every page:** the footer form (`#footer-form`) loads Google reCAPTCHA; Lighthouse lists `recaptcha__en.js` twice (350.8 KiB each, about 372 KiB unused) and 441 ms of main-thread time. The blog post template, which has no reCAPTCHA, scores 89 on mobile. Two Google tag scripts (`gtag` G-KJJEV3N2SL and GTM-52F2WNB, 355 KiB) add another 150 KiB of unused code.
  - **Slider image:** the Largest Contentful Paint element is the first slide, a 437 KiB PNG (`NITA-Ride-Safe-App-Graphic-4-3-v2.png`) served at 1440×781 for a 721×611 display; Lighthouse estimates 254–266 KiB of savings from a modern format or a correctly sized file. The image is not marked `fetchpriority="high"`.
  - Images without `width` and `height` attributes, and total page weight of 2.7–4.2 MB.

  Static files on NITA are served with long cache lifetimes (for example `Cache-Control: max-age=2592000` on `/dist/app.css`; [`step3a-header-checks.txt`](../../../evidence/public-technical/2026-11-24/step3a-header-checks.txt)).
- **Impact:** Real users currently load NITA's pages within Google's “good” thresholds, so the current effect is limited. The lab results show headroom on slower phones and connections, where riders checking fares or service information would wait several seconds for the main content. Reducing script and image weight also lowers data use for mobile riders.
- **Recommendation:** Load the Weglot script with `defer` (or as Weglot recommends for non-blocking loading); load reCAPTCHA only when a user interacts with the footer form, or remove it from pages where the form is not needed; review whether both Google tag scripts are required; convert slider and masthead images to WebP or AVIF with sizes matched to their display, add `fetchpriority="high"` to the first slide, and add `width` and `height` to images. Re-test mobile and desktop with PageSpeed Insights after each change.
- **Implementation complexity:** Medium (template, plugin, and image pipeline changes)
- **Related standard:** [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp) and [Google Search Central: Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)

### Fare tables are wider than a phone screen and push the whole page sideways

- **Finding ID:** SEO-NITA-022
- **Page or component:** Data tables inside accordions on [Paying for your ride](https://nita.illinois.gov/riders/paying-for-your-ride) and [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs).
- **Priority:** Low
- **Evidence:** On 2026-11-24 the 20 sample pages were opened in a Chromium browser emulating a 375×812 phone screen ([`mobile-results.csv`](../../../evidence/public-technical/2026-11-24/mobile-review/mobile-results.csv); method in the [README](../../../evidence/public-technical/2026-11-24/mobile-review/README.md)). With accordions closed, no sample page is wider than the screen. When the fare accordions are opened, tables that are not wrapped in a scrolling container extend past the right edge and widen the whole page:

  | Page | Accordion | Table (columns) | Right edge on a 375 px screen | Page width |
  | --- | --- | --- | --- | --- |
  | Paying for your ride | CTA and Pace | Ventra Full Fare, Ventra Reduced Fare, Cash Fare, Cash Reduced (5) | 465 px; “Cash Reduced” starts off-screen | 465 px |
  | Paying for your ride | Regional Passes | Metra Zones, RDP Weekday, RDP Saturday/Sunday/Holidays (3) | 457 px | 465 px |
  | Paying for your ride | Metra | Monthly Passes by zone (5) | 427 px | 465 px |
  | Paying for your ride | Metra | Day Passes by zone (5) | 410 px | 465 px |
  | Discounted Fare and Ride Free Programs | Registration Site Alerts | four senior-center registration sites (4) | 408 px; the Northeast (Levy) Senior Center column starts off-screen | 409 px |

  The tables have `overflow-x: auto` set on the `<table>` element itself, which does not create a scrolling area, and their parent `<details>` element has no scrolling wrapper. On Community Planning, Access to Transit, and the 2027 budget page, wider tables are inside a scrolling container and the page stays 375 px wide. Screenshot: [`paying-for-your-ride-cta-pace-table-375px.jpg`](../../../evidence/public-technical/2026-11-24/mobile-review/paying-for-your-ride-cta-pace-table-375px.jpg).
- **Impact:** On a phone, riders opening the main fare tables have to drag the whole page sideways, and the browser may zoom the page out, to see the last columns. Google indexes the mobile version of pages, and the table content stays in the HTML, so the effect on search is likely small; the cost is usability on the pages riders most often need for fares and registration.
- **Recommendation:** Wrap tables in the rich-text template in a container with `overflow-x: auto` (as the Community Planning template already does), or restack the fare tables on small screens (for example one card per fare type). Re-test the accordions at 360–390 px widths.
- **Implementation complexity:** Low (template CSS or rich-text wrapper)
- **Related standard:** [Google Search Central: mobile-first indexing best practices](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) and [web.dev: responsive web design basics](https://web.dev/articles/responsive-web-design-basics)

### Structured data labels every page as a website and omits article markup

- **Finding ID:** SEO-NITA-016
- **Page or component:** JSON-LD generated by the CMS SEO plugin on every page; checked on the 16 sample URLs.
- **Priority:** Low
- **Evidence:** On 2026-11-20 each of the 16 sample pages contained one JSON-LD block with the same structure: a `WebSite` node, two `GovernmentOrganization` nodes (`#identity` and `#creator`), and a `BreadcrumbList` ([extracted JSON-LD per page](../../../evidence/public-technical/2026-11-20/structured-data/); no Microdata or RDFa found). Official validation on 2026-11-20 ([results and screenshots](../../../evidence/public-technical/2026-11-20/structured-data/validation-results.md)): the Schema.org Validator reported 0 errors and 0 warnings on the homepage and the budget press release, and Google's Rich Results Test crawled both successfully and found 5 valid items (Breadcrumbs, Local businesses, Organization), with one optional field missing (`image` on the `#creator` organization) and no Article item on the press release. Validity does not cover whether the types and values are appropriate. Observations against the schema.org vocabulary and Google's structured data documentation:
  - **Page type:** the page-level node is `@type: "WebSite"` on every page, including the blog post and press release, with the page title as `headline` (for example `"headline": "Affordable and seamless payment"` on Paying for your ride). Inner pages are not marked as `WebPage`, and posts and press releases have no `Article`, `NewsArticle`, or `BlogPosting` node, although `datePublished`, `dateModified`, `author`, and `publisher` values are already present on that node.
  - **Logo:** the `#identity` organization's `logo` is an `ImageObject` with `height` 264 and `width` 600 but no `url`, so no logo image is declared.
  - **Profiles:** no `sameAs` links to NITA's official profiles, although the footer links six of them: [Facebook](https://www.facebook.com/NITAchicago/), [Instagram](https://www.instagram.com/nita_chicago/), [X](https://x.com/NITA_Chicago), [YouTube](https://www.youtube.com/@NITAChicagoland), [Threads](https://www.threads.com/@nita_chicago), and [TikTok](https://www.tiktok.com/@nita_chicago) (checked on 2026-11-20; the Facebook page loaded as “Northern Illinois Transit Authority - NITA”).
  - **Breadcrumbs:** the press release breadcrumb has two items, Home and the release itself, without a News or Press releases level; core pages have complete trails (for example Home › Riders › Paying for your ride).
  - **Headline values:** the JSON-LD `headline` holds the full title (for example the complete budget press-release headline), while the HTML `<title>` is truncated with “…” (`SEO-NITA-012`), which confirms the truncation happens only in the title output.
- **Impact:** Structured data helps search engines and AI systems identify what each page is and who publishes it. Labeling every page as a `WebSite` and omitting article markup and a logo URL gives a less accurate description of NITA's pages and news content. Valid markup does not guarantee any search feature.
- **Recommendation:** Set, in the SEO plugin, the page-level type to `WebPage` for general pages and `NewsArticle` (press releases) or `BlogPosting` (blog posts) for news entries; add the logo `url` and the six footer profiles as `sameAs` on the organization; add the News or Press releases level to press-release breadcrumbs. Validate the result with the Rich Results Test.
- **Implementation complexity:** Low (plugin configuration per section)
- **Related standard:** [Google Search Central: Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article), [Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization), and [schema.org/WebPage](https://schema.org/WebPage)

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
- **Page or component:** 100 indexable posts, press releases, and budget pages in 39 groups that share a description other than the generic website description; full list in [`nita-metadata-review.csv`](../../../evidence/public-technical/2026-11-20/nita-metadata-review.csv) (column `description_duplicate_count`).
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

### The homepage, archives, and some core pages have generic or placeholder descriptions

- **Finding ID:** SEO-NITA-002
- **Page or component:** 292 pages with the generic website description (85 of them indexable: the homepage, 76 tag pages, 6 blog listings, one press release, and the `/blog/1970/01/01/take-rta-survey` post) and 7 core pages whose description repeats the page name or a fragment.
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, all 1,613 HTML pages have a meta description; 292 use the same description beginning “Committed to achieving a vision of safe, reliable, accessible public transportation…”. See the batch `meta_description_all.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/) and [`nita-metadata-review.csv`](../../../evidence/public-technical/2026-11-20/nita-metadata-review.csv). Placeholder descriptions on core pages: [`/contact`](https://nita.illinois.gov/contact) (“Contact”), [`/privacy-policy`](https://nita.illinois.gov/privacy-policy) (“Privacy Policy”), [`/whistleblower-policy`](https://nita.illinois.gov/whistleblower-policy) (“Whistleblower Policy”), [`/forward-for-all`](https://nita.illinois.gov/forward-for-all) (“Forward For All”), [`/investor-relations-sub`](https://nita.illinois.gov/investor-relations-sub) (“Information for Potential Investors”), [`/about-nita/investor-relations`](https://nita.illinois.gov/about-nita/investor-relations) (“The information is provided for quick reference only.”), and [`/safety/app`](https://nita.illinois.gov/safety/app) (“One free app and one text number for CTA, Metra, and Pace.”).
- **Impact:** The repeated description does not summarize the distinct purpose of these pages when used as a search snippet. Google may instead create a snippet from page content.
- **Recommendation:** Write concise descriptions for the homepage, the seven core pages listed, and any priority blog landing/archive pages intended for search. Confirm the indexability and editorial purpose of archive and pagination pages before producing copy for all of them.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: control your snippets](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#control-your-snippets)

### Blog tag archive titles and headings do not identify their topics

- **Finding ID:** SEO-NITA-001
- **Page or component:** Blog tag archive template: 155 `/blog/tags/` URLs (78 tag pages and 77 paginated tag pages), for example [CTA](https://nita.illinois.gov/blog/tags/cta) and [Metra](https://nita.illinois.gov/blog/tags/metra).
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl baseline, all 155 tag archive URLs have the title “NITA | Northern Illinois Transit Authority.” Of the 78 tag pages, 76 are indexable with self-referencing canonicals and 2 canonicalize to their `http://` version (see `SEO-NITA-003`). On 2026-11-18, a public spot check of the [CTA archive](https://nita.illinois.gov/blog/tags/cta) confirmed that it lists CTA-related posts while its title does not identify the topic. The same template uses the H1 “Connections Blog”, the former RTA blog name, on all 76 indexable tag pages and on five blog listings (`/blog/archive`, `/blog/plan`, `/blog/invest`, `/blog/move`, `/blog/uncategorized`); confirmed live on [`/blog/tags/cta`](https://nita.illinois.gov/blog/tags/cta) on 2026-11-20 ([`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)). The tag list also contains a misspelled duplicate, `/blog/tags/acces-to-transit`, alongside `/blog/tags/access-to-transit`. See [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv) and the batch `page_titles_all.csv` exports in the [B2 crawl folder](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/).
- **Impact:** In a search result or browser tab, these pages are difficult to distinguish by subject. Google may generate title links from other page signals, so the exported title alone does not predict the exact result shown.
- **Recommendation:** Update the tag archive template so the title and H1 name the tag topic (for example “CTA news and updates | NITA”) and replace the “Connections Blog” heading with the current blog name, “On Track”. Confirm which of the 78 tags should remain indexable, and merge the misspelled duplicate tag.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide#influence-your-title-links)

### Image alternative text repeats file names, and the footer logo is labeled “RTA”

- **Finding ID:** SEO-NITA-017
- **Page or component:** Image `alt` attributes across the 16 sample pages: the mobile navigation menu and the news cards in the header menu (on every page), and content images on the homepage, Riders, Communities, budget, and blog pages.
- **Priority:** Low
- **Evidence:** On 2026-11-20 every `<img>` on the 16 sample pages was extracted from the live HTML and each `alt` value was compared with its file name ([`image-alt-review.csv`](../../../evidence/public-technical/2026-11-20/image-alt-review.csv), classified with [`classify_image_alt.py`](../../../evidence/public-technical/2026-11-20/classify_image_alt.py)). All 371 images (120 unique files) have an `alt` attribute, but the values come mostly from the CMS asset title, which defaults to the file name:

  | Result | Image occurrences | Unique images |
  | --- | --- | --- |
  | `alt` is the file name with separators turned into spaces | 210 | 53 |
  | NITA logo with `alt="RTA"` | 16 | 1 |
  | `alt` holds photo-library caption text | 5 | 3 |
  | `alt` is the image URL | 1 | 1 |
  | Other text (descriptive or short labels) | 139 | 62 |

  Repeated on all 16 sample pages (template components):

  | `alt` value | Image file | Where it appears |
  | --- | --- | --- |
  | RTA | `/dist/img/nita-logo-badge-rv.svg` | Footer logo linking to `/`; the header logo on the same pages correctly uses “NITA Logo” |
  | Icon Bus Rapid Transit rv, Icon community rv, Icon Doing Business rv, Icon funding rv, Icon news rv, Icon Phone rv, Icon region rv | `/uploads/images/general/Icons/icon-*-rv.svg` | Mobile navigation menu, next to visible labels such as “Funding” and “Public Safety” |
  | Ride safe app graphic smaller | `ride-safe-app-graphic-smaller.png` | News card in the header menu, linking to the Ride Safe post of 2026-11-19 |
  | E Mlz Yh5 XYAAAB9 K | `EMlzYh5XYAAAB9K.jpeg` | News card in the header menu, linking to [How to use transit to celebrate the holidays in the Chicago region](https://nita.illinois.gov/blog/2026/11/18/how-to-use-transit-to-celebrate-the-holidays-in-the-chicago-region-2) |

  Page-specific examples:

  | Page | `alt` values that repeat the file name |
  | --- | --- |
  | [Homepage](https://nita.illinois.gov/) | NITA Ride Safe App Graphic 4 3 v2; Holiday graphic cropped; People2 |
  | [2027 regional transit budget](https://nita.illinois.gov/transit-funding/2027-regional-transit-budget) | People1; People2; People4; Image; and `alt="https://nita.illinois.gov/uploads/images/general/people3.png"` (the image URL) |
  | [Riders](https://nita.illinois.gov/riders), [How to ride](https://nita.illinois.gov/riders/how-to-ride), [Accessible transit](https://nita.illinois.gov/riders/accessible-transit), [Free and reduced fare programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs) | Icon CTA Train gray; Icon CTA Bus gray; Icon Metra Train gray; Icon Pace Bus gray; Icon Accessibility gray; Icon RTA Fare Program gray; Icon Apply gray; Icon Transit Benefit Program rv; Icon Section5310 Enhanced Mobility gray; 22 RTA 0820; Joliet Metra train 0178 |
  | [Access](https://nita.illinois.gov/riders/access) | 22 RTA 1234; 4 3; and the caption “SUMMER 2026 NITA IMAGE LIBRARY INTERMODAL FOREST PARK TRANSIT CENTER PACE AND CTA” |
  | [Communities](https://nita.illinois.gov/communities), [Access to Transit program](https://nita.illinois.gov/communities/access-to-transit-program) | Icon Community Planning gray; Icon Accesss To Transit Program gray (misspelled file name); Icon Information gray; Melrose Park before after; Fall CTA |
  | [On Track blog](https://nita.illinois.gov/blog) and [CTA tag archive](https://nita.illinois.gov/blog/tags/cta) (post thumbnails) | 221107 RTA 1589; 22 RTA 0666; 22 RTA 1153; 22 RTA 1349; 22 RTA 0327; 22 RTA 0679; 22 RTA1135; 22 RTASAMPLES 068; 22 RTA 1186 Convert to PNG; 22 RTA 1526; 20210604 173925; 2302 RT Aextras 6; Museum bus; Metra aerial blueline; NITA Open House Early Release 8 |

  Thumbnails of two 2026 posts on `/blog` use the photo-library caption as `alt` (“SUMMER 2026 NITA IMAGE LIBRARY AUSTIN GREEN LINE and 315 BUS” and “… JEFFREY JUMP + DOWNTOWN BUSES”). The same template pattern carries other legacy labels: the footer social links have the screen-reader text “RTA on Facebook”, “RTA on Instagram”, “RTA on Twitter”, “RTA on YouTube”, “RTA on Threads”, and “RTA on TikTok”, although they link to NITA's profiles. Some images are well described, for example the accessible-transit photos (“Person in wheelchair boarding CTA L train.”).
- **Impact:** Search engines use `alt` text to understand images and the pages and links that contain them, including in image search. File codes such as “22 RTA 0666” or “E Mlz Yh5 XYAAAB9 K” give no information, and the footer logo and social-link labels identify the website as RTA. The same text is read aloud by screen readers, so the accessibility impact is assessed separately in the accessibility section.
- **Recommendation:** Change the footer logo `alt` to “NITA” (or “Northern Illinois Transit Authority – Home”) and the social-link labels to “NITA on …”. Give the menu icons an empty `alt=""` because the visible label already names the link. Stop using the asset title as the default `alt`: add a required alternative-text field to image assets, write descriptions for content and post images (starting with images on core pages and in the news cards), and replace the URL and caption values on the budget, Access, and blog pages. Coordinate wording with the accessibility review.
- **Implementation complexity:** Medium (template fixes are low; describing existing images is content work across the media library)
- **Related standard:** [Google Search Central: image SEO best practices](https://developers.google.com/search/docs/appearance/google-images#use-descriptive-alt-text); accessibility criteria are assessed in the accessibility section.

### Rider program pages do not use the permit names and former RTA name that people search with

- **Finding ID:** SEO-NITA-028
- **Page or component:** Titles, H1s, descriptions, and opening text of the rider program pages: [Discounted Fare and Ride Free Programs](https://nita.illinois.gov/riders/free-and-reduced-fare-programs), [Access Program](https://nita.illinois.gov/riders/access), [Accessible transit](https://nita.illinois.gov/riders/accessible-transit), and [How to ride](https://nita.illinois.gov/riders/how-to-ride).
- **Priority:** Low
- **Evidence:** A small public sample on 2026-11-24: Google autocomplete for 22 seed phrases ([`autocomplete-2026-11-24.txt`](../../../evidence/public-technical/2026-11-24/content-review/autocomplete-2026-11-24.txt)) and seven Google searches ([`search-sample-2026-11-24.md`](../../../evidence/public-technical/2026-11-24/content-review/search-sample-2026-11-24.md)), run from Argentina with US English settings. The suggestions show phrasing, not search volume:

  | Topic | Phrasing in suggestions and related searches | Wording on the NITA page |
  | --- | --- | --- |
  | Reduced Fare and Ride Free permits | “reduced fare permit chicago”, “reduced fare permit application”, “ride free permit renewal online”, “rta reduced fare permit for seniors”, “rta reduced fare application status”, “senior ride free program chicago” | Title “Discounted Fares”; H1 and menu “Discounted Fare and Ride Free Programs”. The permit names appear in the body; the page does not mention that the permits were previously issued by the RTA |
  | ADA Paratransit | “ada paratransit application”, “ada paratransit eligibility”, “paratransit chicago phone number”, “rta paratransit chicago”, “RTA ADA Paratransit application” | Title “There's always a ride available, regardless of your ability”; H1 “Accessible transit” |
  | Access Program | “access program snap” returns no transit suggestions; the CTA and Pace pages that appear for “reduced transit fare snap chicago” explain the program as reduced fares for SNAP households | Title and H1 “Access Program”; the description starts “…proud to provide reduced fares to low income transit riders” without naming SNAP |
  | Trip planning | “chicago transit trip planner”, “rta chicago trip planner”, “rta chicago map” | Title “Your guide to getting around town” |

  In the searches, NITA pages were shown for the permit, paratransit, SNAP, and trip planner queries, with the existing titles (the slogans for Accessible transit and How to ride, “Northern Illinois Transit Authority | Access Program” for Access) or, for the permit page, its H1. Third-party pages in the same results (municipal websites, a disability-resource foundation, a travel forum) still describe these services as “RTA” programs and link to `fares.rtachicago.org`. Discounted Fare and Ride Free Programs and Paying for your ride never mention the RTA; How to ride mentions it once as NITA's predecessor (in a note on the Regional Day Pass), and Accessible transit still sends readers to “the RTA's trip planner and maps”.
- **Impact:** People continue to use the RTA name and the permit names on the cards they hold. Pages that state those terms in the title, H1, and first paragraph give search engines and readers a clearer match, and help AI answers connect the old and new names. Because NITA pages already appear for these queries in the sample, the expected benefit is better titles and snippets and fewer users ending up on outdated third-party pages, not a guaranteed ranking change.
- **Recommendation:** Use the service names people search with when the core titles are rewritten (`SEO-NITA-011`), for example “Reduced Fare and Ride Free Permits: apply, renew, replace | NITA”, “ADA Paratransit eligibility and application | NITA”, “Access Program: reduced fares for SNAP and FRESH households | NITA”, and “Plan your trip on CTA, Metra, and Pace | NITA”. Add one sentence near the top of each rider program page stating that NITA took over these programs from the RTA on September 1, 2026, at least during the transition. Ask partner and municipal websites that still describe “RTA” programs to update their wording and links.
- **Implementation complexity:** Low (content edits)
- **Related standard:** [Google Search Central: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) and [influence title links](https://developers.google.com/search/docs/appearance/title-link)

## Content observations

The manual review priorities listed in the [matrix](seo-review-matrix.md#public-content-inventory-and-review-priorities) were validated on the sample pages on 2026-11-24 ([content review](../../../evidence/public-technical/2026-11-24/content-review/README.md)):

- **Time-sensitive content:** the fares on Paying for your ride match CTA, Pace, and Metra, including the Metra tables labeled “Effective February 1, 2024”. Past events, an expired alert, and conflicting phone hours are reported in `SEO-NITA-027`.
- **Program naming:** “Access Program” (reduced fares) and “Access to Transit” (infrastructure grants) are kept apart on their pages and in link labels. The reduced-fare credential is called “Access card”, “Access permit”, and “Access Permit” in different places; one name would be clearer.
- **Editorial transition:** the On Track blog states that posts before September 1, 2026 were written by the RTA, and core pages describe earlier work as done under the RTA. Remaining RTA references in rider guidance are covered in `SEO-NITA-027` and `SEO-NITA-028`; related-post blocks in `SEO-NITA-025`.
- **Content depth:** of the 71 pages under 200 words in the crawl, the core pages are the homepage, `/region`, the funding guide, Transparency and oversight, NITA Committees, `/investor-relations-sub`, and `/404`; the rest are short posts, press releases, and listings.

## Positive Observations

- All 1,613 HTML pages in the 2026-11-19 crawl baseline have a title, meta description, and H1, and none has a `noindex` directive. This does not assess whether their content is effective.
- The website publishes an XML sitemap index with five child sitemaps, referenced from `robots.txt`. 1,280 of its 1,286 URLs are also reachable through internal links, and the sitemap updates promptly: the Ride Safe pages and posts published on 2026-11-19 (`/safety`, `/safety/app`, and the related blog post and press release) were listed by 2026-11-20 ([current sitemap copies](../../../evidence/public-technical/2026-11-20/sitemaps/)).
- On all 16 sample pages the content, metadata, links, and structured data are present in the HTML sent by the server; the rendered page after scripts run is the same apart from 2–3 words of interface text ([`raw-vs-rendered.csv`](../../../evidence/public-technical/2026-11-24/rendered-review/raw-vs-rendered.csv)). Search engines therefore do not need to run JavaScript to read the pages.
- The website uses one responsive HTML version for all devices: desktop, mobile, and Googlebot smartphone requests receive the same HTML, and on the sample pages the text and headings are the same at mobile and desktop widths ([`mobile-results.csv`](../../../evidence/public-technical/2026-11-24/mobile-review/mobile-results.csv)).
- Every page carries valid JSON-LD that identifies NITA as a `GovernmentOrganization` with name, alternate name, address, telephone, and email, and core pages have complete breadcrumb trails ([extracted JSON-LD](../../../evidence/public-technical/2026-11-20/structured-data/)).

## Limitations

- The crawl baseline uses raw HTML only (no JavaScript rendering). Links generated only by JavaScript are not covered; on the 16 sample pages, rendered and raw HTML had the same links (2026-11-24).
- The free Screaming Frog version does not extract structured data, and List mode does not crawl images, so structured data and image alternative text are reviewed on the page-level sample instead. JSON-LD was extracted from all 16 sample pages; the official validators (Schema.org Validator and Google Rich Results Test) were run on the homepage and one press release ([results](../../../evidence/public-technical/2026-11-20/structured-data/validation-results.md)).
- Live checks are single dated fetches of the listed URLs; protocol behavior was confirmed on ten URLs across templates and is presumed website-wide.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- External links were checked by script and then in a browser from Argentina on 2026-11-20. Only definitive failures are reported in `SEO-NITA-018`; 315 URLs (480 links on 85 domains) could not be verified because of bot protection, regional blocks, or pages that did not load, including NITA's own `datahub.nita.illinois.gov`, and need a check from a US connection ([browser check](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-links-browser-check.csv)).
- Image alternative text was reviewed on the 16-page sample only; screen-reader impact is assessed in the accessibility section.
- Performance was measured with PageSpeed Insights on 7 templates on 2026-11-24 (one run per URL, two for the homepage); lab results vary between runs and depend on Google's test conditions. Lab tests run on Google's servers with simulated device and network conditions, so the auditor's location (Argentina) does not affect them; field data reflects real Chrome users who visited the pages. Field data for 4 of the 7 templates is origin-level because those URLs have too few Chrome UX Report samples.
- Mobile checks used Chromium device emulation at 375×812 on the 16 sample pages, not physical phones ([method](../../../evidence/public-technical/2026-11-24/mobile-review/README.md)). Internal links were recorded on all 1,609 HTML pages on 2026-11-24 from the raw HTML ([method](../../../evidence/crawls/link-discovery/2026-11-24/README.md)); link regions are inferred from the page template's `<nav>`, `<header>`, and `<footer>` elements.
