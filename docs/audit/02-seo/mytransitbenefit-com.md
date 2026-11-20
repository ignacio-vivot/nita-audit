# Search Engine Optimization (SEO) — mytransitbenefit.com

## Assessment Scope

- **Website:** [mytransitbenefit.com](https://www.mytransitbenefit.com/)
- **Review date:** 2026-11-19
- **Pages, templates, or journeys reviewed:** Complete four-page scope confirmed by the user on 2026-11-19: [homepage](https://www.mytransitbenefit.com/), [Behind the Benefits](https://www.mytransitbenefit.com/behind-the-benefits), [Employees](https://www.mytransitbenefit.com/employees), and [Employers](https://www.mytransitbenefit.com/employers); plus the `/404` URL listed in the sitemap. Manual review is in progress.
- **Methods and tools:** Screaming Frog SEO Spider 25.1 free version, full Spider crawl with default configuration on 2026-11-19 ([README](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/README.md)); curl 8.7.1 ([`live-http-checks.txt`](../../../evidence/public-technical/2026-11-19/live-http-checks.txt)); public sitemap and `robots.txt`; public browser review; Google Search Central guidance.
- **Control checklist:** [SEO review matrix](seo-review-matrix.md#review-controls-and-current-status)

## Summary

**Draft.** The website's technical base is sound for its size: HTTP and non-www requests redirect to the HTTPS www homepage, and the four pages are indexable with self-referencing canonicals and distinct meta descriptions. Four issues were found; the most significant is the structured data, which describes NITA as a business with a misspelled name and a former RTA email address. A `/404` page listed in the sitemap returns 200 and is indexable; all four page titles and the homepage description contain a literal ellipsis that cuts off the text; and the inner pages' H1s are campaign slogans that do not name the page topic.

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

## Observations under review

- **Legacy and third-party links:** the 2026-11-19 crawl shows links to `rtachicago.org` blog posts that redirect, and a script loaded from `unpkg.com` with the floating `@latest` version, which redirects on every page. Review in Step 2.

## Positive Observations

- On 2026-11-19, `http://www.mytransitbenefit.com/` and `https://mytransitbenefit.com/` each returned a single 301 redirect to `https://www.mytransitbenefit.com/`. Only the homepage was tested.
- The four HTML pages in the 2026-11-19 crawl have distinct meta descriptions and self-referencing canonicals, and none of the 31 crawled images is missing alternative text. See [`meta_description_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/meta_description_all.csv), [`canonicals_all.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/canonicals_all.csv), and [`crawl_overview.csv`](../../../evidence/crawls/screaming-frog/mytransitbenefit-com/2026-11-19/crawl_overview.csv).
- The pages communicate distinct audiences (employees and employers) and calls to action. Full enrollment journeys were not tested.

## Limitations

- The 2026-11-19 crawl (default configuration, Text Only) replaces the undocumented 2026-11-16 crawl and confirms the four-page scope. The free Screaming Frog version does not extract structured data, so markup is validated manually.
- The public spot checks did not submit forms, follow authenticated flows, or verify transaction completion.
- Public crawl data cannot establish Google index coverage, rankings, queries, traffic, click-through rate, or conversions. Search Console and analytics are outside the agreed scope.
- Performance/Core Web Vitals, mobile, internal linking, image alternative text, the rendering impact of four robots-blocked form and tag-manager assets, and content accuracy have not yet been assessed.
