# Search Engine Optimization (SEO) — mytransitbenefit.com

## Assessment Scope

- **Website:** [mytransitbenefit.com](https://www.mytransitbenefit.com/)
- **Review date:** 2026-11-19 to 2026-11-24 (crawl 2026-11-19; Step 2 checks 2026-11-20; Step 3 manual and AI-assisted review 2026-11-24)
- **Pages, templates, or journeys reviewed:** Complete four-page scope confirmed by the user on 2026-11-19: [homepage](https://www.mytransitbenefit.com/), [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), and [Employers](https://www.mytransitbenefit.com/employers); plus the `/404` URL listed in the sitemap. Rendered review on 2026-11-24 (raw HTML compared with the rendered page; [comparison](../../../evidence/public-technical/2026-11-24/rendered-review/raw-vs-rendered.csv)); mobile and content review on 2026-11-24 ([content review](../../../evidence/public-technical/2026-11-24/content-review/README.md)).
- **Methods and tools:** Screaming Frog SEO Spider 25.1 free version, full Spider crawl with default configuration on 2026-11-19 ([README](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/README.md)); curl 8.7.1 ([`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)); public sitemap and `robots.txt`; Schema.org Validator and Google Rich Results Test; PageSpeed Insights (Lighthouse 13.6.0) through its web interface ([README](../../../evidence/public-technical/2026-11-24/README.md)); Chromium browser review in the Claude desktop app, including raw and rendered HTML comparison and mobile emulation at 375×812 ([rendered review](../../../evidence/public-technical/2026-11-24/rendered-review/README.md), [mobile review](../../../evidence/public-technical/2026-11-24/mobile-review/README.md)); Google autocomplete and a seven-query result sample ([content review](../../../evidence/public-technical/2026-11-24/content-review/README.md)); Google Search Central guidance. Step 3 was AI-assisted: Claude ran the browser checks and analyses, and the team reviewed each part.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Review complete; ready for team review** (2026-11-24).

The website's technical base is sound for its size: HTTP and non-www requests redirect to the HTTPS www homepage, the four pages are indexable with self-referencing canonicals and distinct meta descriptions, page content does not depend on JavaScript, and the pages fit a phone screen. The review found 8 issues: 4 Medium and 4 Low.

- **Medium:** the sitemap lists a `/404` URL that returns 200 and is indexable (`SEO-MTB-001`); mobile pages load slowly in lab tests because masthead images are oversized, static files are not cached, and Employers loads a map and reCAPTCHA three times (`SEO-MTB-006`; no field data is available); the structured data describes NITA as a business with a misspelled name and a former RTA email address (`SEO-MTB-004`); and all four titles and the homepage description are cut off with a literal ellipsis (`SEO-MTB-002`).
- **Low:** the website has no direct link to NITA and its logo and social links are still labeled RTA (`SEO-MTB-007`); inner-page H1s are slogans (`SEO-MTB-003`); image `alt` text often repeats file names (`SEO-MTB-005`); and the Employers page misnames the Illinois Transportation Benefits Program Act and describes its 2024 start as upcoming (`SEO-MTB-008`).

Recommendations are classified and sequenced in “Recommendation types and confirmations” below and in the [roadmap](../06-recommendations-and-roadmap.md). This review does not establish rankings, clicks, or Google index status.

### Findings at a glance

Findings are listed in report order: by priority, then technical issues first. IDs are stable references assigned when each finding was created, so they are not consecutive. Timing is the suggested grouping in the [roadmap](../06-recommendations-and-roadmap.md).

| ID | Finding | Priority | Complexity | Timing |
| --- | --- | --- | --- | --- |
| [`SEO-MTB-001`](#sitemap-lists-a-404-url-that-returns-200-and-is-indexable) | Sitemap lists a “404” URL that returns 200 and is indexable | Medium | Low | Immediate |
| [`SEO-MTB-006`](#pages-load-slowly-on-mobile-because-images-are-oversized-and-not-cached) | Pages load slowly on mobile because images are oversized and not cached | Medium | Low to Medium | Short-term |
| [`SEO-MTB-004`](#structured-data-describes-nita-as-a-business-with-the-wrong-name-and-an-rta-email) | Structured data describes NITA as a business with the wrong name and an RTA email | Medium | Low | Immediate |
| [`SEO-MTB-002`](#page-titles-and-the-homepage-description-are-truncated-with-a-literal-ellipsis) | Page titles and the homepage description are truncated with a literal ellipsis | Medium | Low | Immediate |
| [`SEO-MTB-007`](#the-program-website-does-not-link-to-nita-directly-and-its-news-links-use-former-rta-urls) | The program website does not link to NITA directly, and its news links use former RTA URLs | Low | Low | Short-term |
| [`SEO-MTB-003`](#h1-headings-are-slogans-that-do-not-name-the-page-topic) | H1 headings are slogans that do not name the page topic | Low | Low | Short-term |
| [`SEO-MTB-005`](#image-alternative-text-repeats-file-names-and-the-footer-logo-is-labeled-rta) | Image alternative text repeats file names, and the footer logo is labeled “RTA” | Low | Low | Short-term |
| [`SEO-MTB-008`](#the-employers-page-names-the-illinois-commuter-benefit-law-incorrectly-and-describes-it-as-upcoming) | The Employers page names the Illinois commuter benefit law incorrectly and describes it as upcoming | Low | Low | Short-term |

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

### Pages load slowly on mobile because images are oversized and not cached

- **Finding ID:** SEO-MTB-006
- **Page or component:** All four pages; masthead images, server caching headers, and the Employers page embeds.
- **Priority:** Medium
- **Evidence:** PageSpeed Insights on 2026-11-24 ([`psi-results.jsonl`](../../../evidence/public-technical/2026-11-24/psi-results.jsonl), [`psi-details.txt`](../../../evidence/public-technical/2026-11-24/psi-details.txt), [`step3a-header-checks.txt`](../../../evidence/public-technical/2026-11-24/step3a-header-checks.txt)). Google has no field data for the website (too few Chrome users), so only lab results are available:

  | Page | Mobile score | Mobile FCP | Mobile LCP | Desktop score | Desktop LCP | Page weight |
  | --- | --- | --- | --- | --- | --- | --- |
  | [Homepage](https://www.mytransitbenefit.com/) (two runs) | 45 / 49 | 7.4 s | 17.9 s / 15.2 s | 89 | 2.1 s | 3.5 MB |
  | [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits) | 43 | 7.4 s | 14.1 s | 93 | 0.9 s | 2.9 MB |
  | [Employees](https://www.mytransitbenefit.com/employees) | 51 | 7.4 s | 16.6 s | 91 | 1.9 s | 3.2 MB |
  | [Employers](https://www.mytransitbenefit.com/employers) | 39 | 2.6 s | 18.0 s | 61 | 2.0 s | 8.3 MB |

  Causes identified:
  - **Oversized masthead images:** the LCP element on each page is a PNG masthead, for example `_mastheadImage/home.png` (1,018 KiB, 1140×566, displayed at 364×181 on mobile; estimated savings 913–915 KiB) and `_mastheadImage/employer.png` (974 KiB). The partner logos are also large PNGs (`icon-watertaxi.png` 170 KiB).
  - **No browser caching:** the server sends no `Cache-Control` or `Expires` header for first-party images, CSS, JavaScript, or fonts (checked with curl on `employer.png`, `icon-watertaxi.png`, and `/dist/app.css`), so returning visitors and visitors moving between pages download them again; Lighthouse estimates 1.3–4.5 MB of savings per page. NITA's website does send these headers. This does not change the lab scores above, which always simulate a first visit with an empty cache; it affects repeat and multi-page visits.
  - **Heavy embeds on Employers:** an ArcGIS map iframe from `rtagis.maps.arcgis.com` (about 1.3 MB of map code and images, loaded with the page) and Google reCAPTCHA listed three times (352 KiB each), plus two Google tag scripts (330 KiB).
  - Images without `width` and `height`; the masthead is not marked `fetchpriority="high"`.
- **Impact:** These pages are the program's enrollment entry points for employees and employers. On a mid-range phone with a slow connection, the lab test shows the main image appearing after 14–18 seconds, which risks visitors leaving before reading the offer. Without field data, the real-user experience cannot be confirmed; desktop results are acceptable except on Employers.
- **Recommendation:** Convert masthead and logo images to WebP or AVIF and serve sizes matched to the display (`srcset`), add `fetchpriority="high"` to the masthead and `width`/`height` to images, configure the web server to send long `Cache-Control` lifetimes for static files (as NITA's server does), and load the Employers map only on demand (for example `loading="lazy"` on the iframe or a click-to-load preview) with reCAPTCHA loaded once. Re-test with PageSpeed Insights.
- **Implementation complexity:** Low to Medium (server configuration and image export are low; changing the map embed needs a design decision)
- **Related standard:** [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp) and [web.dev: HTTP cache](https://web.dev/articles/http-cache)

### Structured data describes NITA as a business with the wrong name and an RTA email

- **Finding ID:** SEO-MTB-004
- **Page or component:** JSON-LD on all four pages (CMS SEO plugin settings).
- **Priority:** Medium
- **Evidence:** On 2026-11-20 each page contained a JSON-LD graph whose organization nodes reuse NITA's identifiers (`@id: "https://nita.illinois.gov#identity"` and `"#creator"`) but describe them differently from NITA's own website ([extracted JSON-LD](../../../evidence/public-technical/2026-11-20/structured-data/)). The Schema.org Validator (0 errors, 0 warnings) displays these values for the homepage, and Google's Rich Results Test reports the markup as valid ([results and screenshots](../../../evidence/public-technical/2026-11-20/structured-data/validation-results.md)), because the problem is the content of the values, not their syntax:

  | Property | mytransitbenefit.com (`#identity`) | nita.illinois.gov (`#identity`) |
  | --- | --- | --- |
  | `@type` | `LocalBusiness` | `GovernmentOrganization` |
  | `name` | Northern Illinois **Transportation** Authority | Northern Illinois **Transit** Authority |
  | `email` | `webadmin@rtachicago.org` | `website@nita.illinois.gov` |
  | `priceRange` | `$` | — |
  | `geo` | 41.877930, -87.628420 | — |

  The `#creator` node on My Transit Benefit is also a `LocalBusiness` with `priceRange: "$"` and the RTA email, but with the correct name. As on NITA's website, the page-level node is `@type: "WebSite"` on every page (`SEO-NITA-016`); its `headline` values hold the complete titles that the HTML `<title>` truncates (`SEO-MTB-002`).
- **Impact:** Search engines and AI systems that read this markup receive a misspelled agency name, a former RTA email address, and a commercial business type with a price range for a public program, and the same identifier is described two different ways across NITA's two websites. This reduces the clarity and consistency of the machine-readable information about who runs the program.
- **Recommendation:** Change the organization type to `GovernmentOrganization` (or reference NITA's entity without redefining it), correct the name to “Northern Illinois Transit Authority”, replace `webadmin@rtachicago.org` with a current NITA address, and remove `priceRange` and `geo` unless intended. Align these settings with NITA's website and validate with the Rich Results Test.
- **Implementation complexity:** Low (plugin configuration)
- **Related standard:** [Google Search Central: Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization) and [schema.org/GovernmentOrganization](https://schema.org/GovernmentOrganization)

### Page titles and the homepage description are truncated with a literal ellipsis

- **Finding ID:** SEO-MTB-002
- **Page or component:** `<title>` of all four pages and the homepage meta description (CMS SEO settings).
- **Priority:** Medium
- **Evidence:** On 2026-11-19 the HTML source titles were “Everybody Wins with Money-Saving NITA… | NITA Transit Benefit Program” (homepage), “How Much Can You Save with NITA… | NITA Transit Benefit Program,” “Want to Cut Your Monthly Commute Bill… | NITA Transit Benefit Program,” and “A Smart Move: NITA Transit Benefits… | NITA Transit Benefit Program.” The ellipsis character is in the source, not added by a tool. Screaming Frog measured the titles at 606–653 px, above the roughly 580 px that commonly displays on desktop results. The homepage meta description is also cut off: “The Chicago NITA Transit Benefit Fare Program can cut employees' monthly commute bills by up to 40%. Employers can save over 7% on payroll taxes. Here's…” (153 characters, confirmed on 2026-11-20). NITA's website shows the same truncation on 1,279 descriptions and 63 titles (`SEO-NITA-012`), which points to a shared CMS SEO setting. See [`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt), [`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt), and [`page_titles_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/page_titles_all.csv).
- **Impact:** The titles stop mid-phrase, before stating the page topic (for example, “pre-tax transit benefits for employees”). A search result or browser tab shows an incomplete sentence, and the most descriptive words are missing. Google may rewrite title links that it considers unhelpful.
- **Recommendation:** Write complete, concise titles that state each page's topic and audience first and the brand second (for example, a title for the Employees page that names pre-tax transit and parking benefits for employees). Complete the homepage description. Change the CMS SEO setting that truncates titles and descriptions with an ellipsis, together with NITA's website.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: influence title links](https://developers.google.com/search/docs/appearance/title-link)

### The program website does not link to NITA directly, and its news links use former RTA URLs

- **Finding ID:** SEO-MTB-007
- **Page or component:** Links from the four pages to nita.illinois.gov: header and footer, the homepage news cards, and the Employers page text.
- **Priority:** Low
- **Evidence:** On 2026-11-24 every link on the four pages was extracted from the raw HTML ([raw HTML files](../../../evidence/public-technical/2026-11-24/rendered-review/raw-html/); method in the [rendered review README](../../../evidence/public-technical/2026-11-24/rendered-review/README.md)). None links to `nita.illinois.gov`. The only paths to NITA content are four links to former RTA blog URLs that redirect (301) to NITA's blog:

  | Page | Link text | URL in the page | Final destination (2026-11-24) |
  | --- | --- | --- | --- |
  | [Homepage](https://www.mytransitbenefit.com/) | Learn More | `https://www.rtachicago.org/blog/2023/07/25/legislation-expands-transit-benefit-program-to-workplaces-across-the-chicago-region` | [NITA blog post, 2023-07-25](https://nita.illinois.gov/blog/2023/07/25/legislation-expands-transit-benefit-program-to-workplaces-across-the-chicago-region) |
  | [Homepage](https://www.mytransitbenefit.com/) | Learn More | `https://www.rtachicago.org/blog/2021/07/23/transit-benefit-fare-program-adds-parking-option-to-increase-flexibility-as-riders-return` | [NITA blog post, 2021-07-23](https://nita.illinois.gov/blog/2021/07/23/transit-benefit-fare-program-adds-parking-option-to-increase-flexibility-as-riders-return) |
  | [Employers](https://www.mytransitbenefit.com/employers) (twice) | “Transit Benefits Program Act, which went into effect on January 1, 2024” and “Transit Benefits Program Act, which goes into effect on January 1, 2024” | the same 2023 RTA blog URL | the same NITA blog post |

  The header logo links to the homepage with the label “Regional Transportation Authority”, the footer agency strip labels the program's own homepage “RTA”, and the six social links read “RTA on Facebook” and so on, although they point to NITA's accounts (`facebook.com/NITAchicago`, `instagram.com/nita_chicago`, `x.com/NITA_Chicago`, `youtube.com/@NITAChicagoland`, `threads.com/@nita_chicago`, `tiktok.com/@nita_chicago`). In the other direction, NITA's menu links to the program through the shortcut `/riders/transit-benefit-fare-program`, which redirects (302) to `https://www.mytransitbenefit.com/`, and the [Riders](https://nita.illinois.gov/riders) page links to it directly (“Learn More”).
- **Impact:** The program website names NITA in its titles and structured data, but gives users and search engines no direct link to the agency that runs it, and its only NITA links pass through the former RTA domain. Clear links between the two websites help users confirm the program is official and help search engines connect the program to NITA; the labels that still say RTA undercut that connection after the September 1, 2026 name change.
- **Recommendation:** Add a direct link to NITA's website in the header or footer (for example “A program of the Northern Illinois Transit Authority”), update the two news cards and the Employers links to the `nita.illinois.gov` URLs, and change the logo, footer, and social link labels from RTA to NITA. Coordinate with `SEO-MTB-004` (structured data) and `SEO-MTB-005` (image text).
- **Implementation complexity:** Low (template and content edits)
- **Related standard:** [Google Search Central: SEO starter guide, links](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

### H1 headings are slogans that do not name the page topic

- **Finding ID:** SEO-MTB-003
- **Page or component:** H1 of the [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), and [Employers](https://www.mytransitbenefit.com/employers) pages.
- **Priority:** Low
- **Evidence:** In the 2026-11-19 crawl and the live source on 2026-11-20 ([`internal_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/internal_all.csv), [`step2c-live-checks.txt`](../../../evidence/public-technical/2026-11-20/step2c-live-checks.txt)):

  | Page | H1 | Second H1 | First H2s |
  | --- | --- | --- | --- |
  | [Homepage](https://www.mytransitbenefit.com/) | NITA Pre-Tax Transit Benefits Program. Enroll Now and Save. | — | How the Program Works; I'm an Employer |
  | [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits) | A Deep Dive into The Heart of Our Program. | — | About Transit Benefits; How the Program Works |
  | [Employees](https://www.mytransitbenefit.com/employees) | Your Tax Savings Starts Here! | Login | Employees; How you save |
  | [Employers](https://www.mytransitbenefit.com/employers) | Save Money, Go Green, and Attract Talent! | — | Employers; How you save |

  Only the homepage H1 names the program. On the three inner pages the topic (“Employees”, “Employers”) appears only in an H2, and the Employees page marks the login box heading as an H1.
- **Impact:** On a four-page website each H1 carries much of the page's topical signal. Slogans such as “Your Tax Savings Starts Here!” do not say that the page explains pre-tax transit and parking benefits for employees, which makes the page's purpose less clear to search engines and to screen-reader users who navigate by headings.
- **Recommendation:** Make each inner page's H1 state its topic and audience (for example “Pre-tax transit benefits for employees” and “Commuter benefits for employers”), keep the slogan as a subheading or lead text, and change the “Login” heading to a lower heading level or a non-heading element. Coordinate heading changes with the accessibility section.
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

### Image alternative text repeats file names, and the footer logo is labeled “RTA”

- **Finding ID:** SEO-MTB-005
- **Page or component:** Image `alt` attributes on the four pages: the footer logo, navigation icons, and content images.
- **Priority:** Low
- **Evidence:** On 2026-11-20 every `<img>` on the four pages was extracted from the live HTML and each `alt` value was compared with its file name ([`image-alt-review.csv`](../../../evidence/public-technical/2026-11-20/image-alt-review.csv), classified with [`classify_image_alt.py`](../../../evidence/public-technical/2026-11-20/classify_image_alt.py)). All 72 images (29 unique files) have an `alt` attribute; 38 occurrences (21 unique images) equal the file name. Some of these are acceptable short labels that happen to match the file name (for example “Employees” or “Region”), but others contain file codes or suffixes:

  | `alt` value | Image file | Page |
  | --- | --- | --- |
  | RTA | `/dist/img/nita-logo-badge.svg` | Footer logo linking to `/` on all four pages; the header logo uses “Northern Illinois Transit Authority Logo” |
  | Getty Images 1502422361 tiny | `GettyImages-1502422361_tiny.jpeg` | [Employers](https://www.mytransitbenefit.com/employers) |
  | Coworkers fn; Person on train fn | `coworkers-fn.jpg`; `person-on-train-fn.jpg` | [Homepage](https://www.mytransitbenefit.com/) |
  | 221107 NITA 1574 X3; 22 NITA 1337 X3 | `221107-RTA-1574-X3.jpg`; `22-RTA-1337-X3.jpeg` | [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits); [Employees](https://www.mytransitbenefit.com/employees). “RTA” in the file name appears as “NITA” in the `alt`, which suggests a text replacement on asset titles |
  | NITA Transit Benefit Fare Program Cards COMBINED | `RTA-Transit-Benefit-Fare-Program-Cards-COMBINED.png` | [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits) |
  | Transit Benefit Program rv; Community rv | `Transit-Benefit-Program-rv.svg`; `Community-rv.svg` | [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits) |
  | Ventra iphone | `ventra-iphone.png` | [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits) |

  Two news images on the homepage (`221107-RTA-1554.jpg` and `tbfp-blog-1110x545-1.jpg`) use the generic “News Image”. The home link in the header and footer has the screen-reader text “Regional Transportation Authority”.
- **Impact:** On a four-page website, image `alt` text is one of the few on-page signals about the program's photos and illustrations. File codes and suffixes add no meaning, and the logo and home-link labels name the former agency. The same text is read aloud by screen readers; that impact is assessed in the accessibility section.
- **Recommendation:** Change the footer logo `alt` and the home-link label to “NITA” or “Northern Illinois Transit Authority”, write short descriptions for the content photos (for example, coworkers commuting by train), give icons an empty `alt=""` where a visible label already names the item, and apply the same asset alternative-text field recommended for NITA's website (`SEO-NITA-017`).
- **Implementation complexity:** Low
- **Related standard:** [Google Search Central: image SEO best practices](https://developers.google.com/search/docs/appearance/google-images#use-descriptive-alt-text); accessibility criteria are assessed in the accessibility section.

### The Employers page names the Illinois commuter benefit law incorrectly and describes it as upcoming

- **Finding ID:** SEO-MTB-008
- **Page or component:** [Employers](https://www.mytransitbenefit.com/employers) page text about the Illinois law that requires covered employers to offer a pre-tax commuter benefit.
- **Priority:** Low
- **Evidence:** On 2026-11-24 the Employers page said ([page text](../../../evidence/public-technical/2026-11-24/content-review/page-text/www-mytransitbenefit-com-employers.md)): “…comply with the new Transit Benefits Program Act, which goes into effect on January 1, 2024.” and, further down, “…comply with the Transit Benefits Program Act, which went into effect on January 1, 2024.” Both link to a 2023 RTA blog post through `rtachicago.org` (see `SEO-MTB-007`). The statute and the employer articles found in a Google search the same day call the law the “Transportation Benefits Program Act”, and the suggestions for “transit benefits program act” offered “transportation benefits program act illinois” ([search sample](../../../evidence/public-technical/2026-11-24/content-review/search-sample-2026-11-24.md), query 6; [`autocomplete-2026-11-24.txt`](../../../evidence/public-technical/2026-11-24/content-review/autocomplete-2026-11-24.txt)). The page describes covered employers as those “with more than 50 full-time or part-time employees”; the legal summaries in the same results describe the threshold as 50 or more covered employees. In that search the Employers page was shown with its meta description. For “pre tax transit benefit chicago”, the homepage appeared on the first page after CTA, City of Chicago, Ventra, and other pages, two of them with older monthly limits ($325 and $270); the state's Commuter Savings Program page confirms $340 for 2026.
- **Impact:** Employers researching their obligations search by the law's name and look for current, accurate requirements. An incorrect name, a 2024 effective date written in the future tense, and a threshold worded differently from the law weaken the page as the official program's answer to those searches and could confuse employers checking whether they are covered.
- **Recommendation:** Use the law's official name (Transportation Benefits Program Act) with a link to the statute on ilga.gov, rewrite both sentences in the past tense, confirm the employer threshold and coverage area wording with NITA's legal team, and consider a short employer section that summarizes who is covered and how the program helps them comply. Keep the 2026 monthly limit current each January.
- **Implementation complexity:** Low (content edit after legal review)
- **Related standard:** [Google Search Central: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

## Recommendation types and confirmations

Each recommendation is classified as **technical** (server, CMS configuration, or template changes), **editorial** (content and wording changes made by editors), or both. The last column lists what NITA or another owner should confirm before acting; recommendations that change URLs, redirects, or indexing wait for that confirmation (Step 4 part C, 2026-11-24).

| Finding | Priority | Type | Confirm before acting |
| --- | --- | --- | --- |
| `SEO-MTB-001` | Medium | Technical | CMS team: whether the error template depends on the `/404` entry. |
| `SEO-MTB-006` | Medium | Technical | NITA: whether the Employers map must load with the page; hosting team: caching headers. |
| `SEO-MTB-004` | Medium | Technical | NITA: the contact email and how the program should be described as part of NITA. |
| `SEO-MTB-002` | Medium | Technical and editorial | NITA communications: title wording. |
| `SEO-MTB-007` | Low | Editorial | NITA communications: how the program is attributed to NITA in the header or footer. |
| `SEO-MTB-003` | Low | Editorial | NITA communications: H1 wording. |
| `SEO-MTB-005` | Low | Technical and editorial | None. |
| `SEO-MTB-008` | Low | Editorial | NITA legal team: the law name, employer threshold, and coverage wording. |

## Observations under review

- **Legacy and third-party links (reviewed in Step 2 part F):** no external link is confirmed broken. The links to `rtachicago.org` blog posts redirect to the matching NITA posts; see `SEO-MTB-007`. A script is loaded from `unpkg.com` with the floating `@latest` version, which 302-redirects to a pinned version on every page; pinning the version is a maintenance and performance consideration to review in Step 3.

## Positive Observations

- On 2026-11-19, `http://www.mytransitbenefit.com/` and `https://mytransitbenefit.com/` each returned a single 301 redirect to `https://www.mytransitbenefit.com/`. Only the homepage was tested.
- The four HTML pages in the 2026-11-19 crawl have distinct meta descriptions and self-referencing canonicals, and none of the 31 crawled images is missing alternative text. See [`meta_description_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/meta_description_all.csv), [`canonicals_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/canonicals_all.csv), and [`crawl_overview.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/crawl_overview.csv).
- On all four pages the content, metadata, links, and structured data are in the HTML sent by the server; the rendered page after scripts run is the same apart from 2 words of interface text ([`raw-vs-rendered.csv`](../../../evidence/public-technical/2026-11-24/rendered-review/raw-vs-rendered.csv)). The robots-blocked form and tag-manager assets therefore do not hide indexable content.
- On a 375 px phone screen the four pages fit the width (Employees and Employers, compared at 1280 px, show the same headings and text as on desktop), and the mobile menu has the same three links as the desktop menu; all user agents receive the same HTML ([`mobile-results.csv`](../../../evidence/public-technical/2026-11-24/mobile-review/mobile-results.csv)).
- The pages communicate distinct audiences (employees and employers) and calls to action. Full enrollment journeys were not tested.

## Limitations

- The 2026-11-19 crawl (default configuration, Text Only) replaces the undocumented 2026-11-16 crawl and confirms the four-page scope. The free Screaming Frog version does not extract structured data, so markup is validated manually.
- The public spot checks did not submit forms, follow authenticated flows, or verify transaction completion.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- Performance was measured with PageSpeed Insights on 2026-11-24 (lab data only; Google has no field data for the website). Lab tests run on Google's servers with simulated device and network conditions, so the tester's location does not affect them; field data, where available, reflects real Chrome users. Mobile checks used Chromium device emulation at 375×812, not physical phones ([method](../../../evidence/public-technical/2026-11-24/mobile-review/README.md)). Internal linking and content accuracy have not yet been assessed.
