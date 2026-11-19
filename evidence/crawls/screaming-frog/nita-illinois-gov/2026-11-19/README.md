# NITA crawl — 2026-11-19 (crawl baseline run B2)

Replaces the 2026-11-16 crawl as the SEO crawl baseline (the earlier folder is kept unchanged). See the [SEO work plan](../../../../../docs/audit/02-seo/seo-audit-plan.md#crawl-baseline-method).

- **Tool:** Screaming Frog SEO Spider 25.1, free version (no license), run headless from the command line.
- **Mode and configuration:** List mode with the application's default List configuration (no settings changed; the free version cannot load configuration files). List mode requests only the listed URLs; it does not follow links or crawl images, CSS, JS, or external links. Text Only rendering; default Screaming Frog user agent.
- **Input:** 1,736 unique URLs = the 1,286 URLs in the 2026-11-19 sitemap files plus the 1,730 HTML URLs reached by the [link-discovery run (B1)](../../../link-discovery/2026-11-19/README.md); 1,280 URLs are in both. Built with [`build_url_lists.py`](build_url_lists.py) into four lists below the 500-URL limit.
- **Batches:** `batch-01` to `batch-04` (450, 450, 450, and 386 URLs), run 2026-11-19 between 16:55 and 17:04 (UTC−3), each about 1 minute 15 seconds. All listed URLs were crawled.

## Command (per batch)

```bash
ScreamingFrogSEOSpiderLauncher --headless --crawl-list list-NN.txt --output-folder batch-NN \
  --export-tabs "Internal:All,Response Codes:All,Page Titles:All,Meta Description:All,H1:All,H2:All,Canonicals:All,Directives:All" \
  --save-report "Crawl Overview,Redirects:All Redirects"
```

## Files

| File | Content |
| --- | --- |
| `list-01.txt` … `list-04.txt` | Exact List-mode input. |
| `url-sources.csv` | Each URL with its source (sitemap, link discovery, or both) and batch. |
| `batch-NN/` | Raw Screaming Frog exports per batch. |
| `url-inventory.csv` | Derived join of `url-sources.csv`, B1 depth and first linking page, and the Screaming Frog status, indexability, canonical, and title. Replaces `evidence/public-technical/2026-11-19/sitemap-crawl-comparison.csv` for coverage questions. |

## Summary of results

Raw observations for Step 2 analysis, not findings.

- **Status:** 1,613 URLs returned 200 (all HTML), 63 returned 301, 8 returned 302, 50 returned 404, and 2 returned 403.
- **Indexability:** 255 of the 1,613 HTML pages are canonicalized to another URL, mainly paginated listings (blog, blog categories, press releases, paginated tag archives) and meeting-material pages. No page has a `noindex` directive.
- **Titles:** every page has a title. 156 pages use the brand-only title “NITA | Northern Illinois Transit Authority” (all 155 tag archive URLs plus one other); 1,199 titles exceed about 580 pixels.
- **Descriptions:** every page has a meta description; 292 share the generic description beginning “Committed to achieving a vision…”, including all 155 tag archive URLs.
- **Tag archives:** 155 URLs: 78 tag pages and 77 paginated tag pages. Two tag canonicals use `http://` (`/blog/tags/chicago`, `/blog/tags/moving-you`). The tag list includes a misspelled duplicate (`/blog/tags/acces-to-transit` alongside `/blog/tags/access-to-transit`).
- **Headings:** every page has an H1; 24 pages have more than one.
- **Content length:** 71 pages have fewer than 200 extracted words.

## Interpretation limits

- Structured-data extraction is not available in the free version. Do not use these exports as evidence of absent markup.
- Coverage of URLs that are neither in the sitemap nor linked through `<a href>` (for example, JavaScript-only links) is not established.
