# My Transit Benefit crawl — 2026-11-19

Replaces the 2026-11-16 crawl as the SEO crawl baseline (the earlier folder is kept unchanged).

- **Starting URL:** `https://www.mytransitbenefit.com/`
- **Tool:** Screaming Frog SEO Spider 25.1, free version (no license), run headless from the command line.
- **Mode and configuration:** Spider mode with the application's default configuration. The free version cannot save or load configuration files, so no settings were changed. Defaults include no crawl-depth limit, Text Only rendering, images/CSS/JS checked, external links checked, and the default Screaming Frog user agent.
- **Completion:** 64 URLs encountered, 60 crawled, 4 internal URLs blocked by `robots.txt` (`/cpresources/` form, reCAPTCHA, and tag-manager assets). 42 internal URLs (4 HTML pages, 31 images, 1 PDF, CSS/JS, and the 4 blocked URLs) and 22 external URLs. Well below the 500-URL limit.
- **Duration:** 00:00:11.

## Command

```bash
ScreamingFrogSEOSpiderLauncher --headless --crawl https://www.mytransitbenefit.com/ \
  --output-folder <this folder> \
  --export-tabs "Internal:All,Response Codes:All,Page Titles:All,Meta Description:All,H1:All,H2:All,Images:All,Images:Missing Alt Text,Images:Missing Alt Attribute,Canonicals:All,Directives:All,Sitemaps:All" \
  --save-report "Crawl Overview,Redirects:All Redirects"
```

## Files

Standard exports listed in the parent [Screaming Frog evidence guide](../../README.md), plus `images_missing_alt_text.csv`, `images_missing_alt_attribute.csv`, `crawl_overview.csv`, and `redirects.csv` (redirect chains). `Sitemaps:All` is empty because sitemap crawling is off by default.

## Interpretation limits

- Structured-data extraction is not available in the free version; `crawl_overview.csv` reports zero pages with structured data although JSON-LD is present. Do not use it as evidence of absence.
- These are raw crawl artifacts. Automated issue counts have not been reviewed or accepted as audit findings.
