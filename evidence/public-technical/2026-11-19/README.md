# Public robots and sitemap evidence — 2026-11-19

Raw public files were saved here without editing. `sitemap-crawl-comparison.csv` is a derived exact-URL comparison against the 2026-11-16 Screaming Frog `Internal > All` exports; `scheme-normalized` matches only account for HTTP-to-HTTPS differences (and slash normalization).

## Robots files

| Website | Public URL | Evidence file |
| --- | --- | --- |
| NITA | https://nita.illinois.gov/robots.txt | `nita-robots.txt` |
| My Transit Benefit | https://www.mytransitbenefit.com/robots.txt | `mytransitbenefit-robots.txt` |

## Sitemap files

The NITA `Sitemap:` directive points to an index containing five child sitemap files. All five were downloaded, along with the My Transit Benefit sitemap.

| Website | Sitemap evidence files |
| --- | --- |
| NITA | `nita-sitemaps-1-sitemap.xml` and its five `nita-sitemaps-1-*-sitemap*.xml` child files |
| My Transit Benefit | `mytransitbenefit-sitemap.xml` |

## Comparison summary

- **NITA:** The sitemap index references five child sitemaps with 1,286 unique URLs. Of these, 82 exactly match URLs in the crawl; one additional sitemap URL matches a crawled URL after normalizing HTTP to HTTPS. The comparison therefore has 83 matches and 1,203 sitemap URLs not present in `internal_all.csv`. Of the matches, 79 returned 200 and four returned 302 in the crawl. Eight crawled HTTP 200 HTML pages (the blog pagination/tag archives) are not listed in the sitemap after scheme normalization.
- **My Transit Benefit:** The sitemap contains five URLs: the four user-confirmed page URLs (all present with 200 responses in the crawl) plus `/404`, which is not present in `internal_all.csv` and needs response/intent validation.
- **Interpretation:** Sitemap inclusion and crawl discovery are different signals. The comparison does not establish that unmatched URLs are orphaned, invalid, or should be removed. Some sitemap entries were updated after the 2026-11-16 crawl; status and internal-link discovery need follow-up.

NITA's sitemap inventory by child file:

| Sitemap group | URLs | Present in crawl after scheme normalization | Not present in crawl |
| --- | ---: | ---: | ---: |
| Category group: news | 5 | 3 | 2 |
| News section, page 1 | 500 | 24 | 476 |
| News section, page 2 | 289 | 0 | 289 |
| General pages | 73 | 54 | 19 |
| Press releases | 419 | 2 | 417 |
| **Total** | **1,286** | **83** | **1,203** |

The four crawled sitemap URLs returning 302 lead to dashboards (ArcGIS), regional transit data (RTAMS), registration sites (ArcGIS), and the transit benefit fare program (My Transit Benefit). Review whether the sitemap should list these redirecting URLs or their destinations and whether internal links point directly to the destinations. The crawl also contains eight 200 HTML blog pagination/tag URLs absent from the sitemap; this difference needs intent/indexability review. The comparison is an inventory aid, not a finding by itself.

See `sitemap-crawl-comparison.csv` for URL-level results and source sitemap filenames.

## Live HTTP checks

`live-http-checks.txt` records raw response headers and short HTML extracts captured with curl 8.7.1 on 2026-11-19 (17:36 UTC). It supports the protocol/redirect, pagination canonical, soft 404, title, and JSON-LD observations in the SEO reports. Highlights, all to be read with the limits of a single dated fetch:

- `http://nita.illinois.gov/` and `http://nita.illinois.gov/riders` return 200 without redirecting to HTTPS; no `Strict-Transport-Security` header was returned on HTTPS. The HTTP homepage declares an HTTPS canonical.
- A legacy `/sites/default/files/...` PDF returns 301 to an `http://` URL under `/uploads/files/general/Drupal-Old/`, which then returns 200 over HTTP.
- `/blog`, `/blog/p2`, and `/blog/p3` all return 200, link to the next page with standard anchors, and declare `https://nita.illinois.gov/blog` as canonical.
- `https://www.mytransitbenefit.com/404` returns 200 with the homepage title, `robots: all`, and a self-referencing canonical; a nonexistent URL on the same website correctly returns 404.
- Both homepages contain one JSON-LD block (`WebSite` graph). The 2026-11-16 Screaming Frog `Structured Data` exports report zero types, so they should not be used as evidence of absent markup.
