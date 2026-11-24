# NITA internal link graph — 2026-11-24 (SEO Step 3, part D)

The 2026-11-19 link discovery (B1, [README](../2026-11-19/README.md)) records only the first page that links to each URL. For the information architecture and internal linking review, every HTML page that returned 200 in B1 was read again and every internal link was recorded with the part of the page it sits in.

## Method

- **Script:** [`internal_link_graph.py`](internal_link_graph.py) (Python 3 standard library only).
- **Command:** `python3 -I internal_link_graph.py ../2026-11-19/nita-illinois-gov/pages.csv nita-internal-link-edges.csv 0.3 <html_cache_dir>`
- **Run:** 2026-11-24, 16:12 to 17:02 UTC (`run-started.txt`, `run.log`). 1,609 pages requested sequentially with a 0.3 s delay; no fetch errors. The HTML cache was kept locally for the analysis and is not part of the evidence.
- **Page regions:** from the nearest enclosing element in the page template: `nav` (the desktop and mobile menus), `footer`, `hero` (the `<header>` banner with breadcrumb, title, and, on some pages, introductory text), `top` (logo and utility links before the banner), and `body` (page content after the banner, including related-post blocks and the partner agency strip). In-content links are `body` and, for introductory text, `hero`.
- **Not covered:** links added by JavaScript (none found on the sample pages in Step 3 part B), external links (see the [2026-11-20 folder](../2026-11-20/README.md)), and links in documents.

## Files

| File | Content |
| --- | --- |
| `nita-internal-link-edges.csv.gz` | 197,373 internal links (gzip of a 51 MB CSV): source page, raw `href`, resolved target (fragment removed, https), region, anchor text (or `aria-label` / image `alt`), and `rel`. |
| `nita-page-inlinks.csv` | One row per HTML page: page type, B1 crawl depth, and the number of distinct pages linking to it from each region. Produced by [`analyze_internal_links.py`](analyze_internal_links.py). |
| `nita-anchor-text-summary.csv` | Anchor texts of `body` links with instance counts and number of targets (22,353 body links). |
| `nita-links-to-redirects.csv` | Internal links whose target redirected in B1, grouped by target, status, destination, and region. |
| `nita-legacy-redirects-to-section-pages.csv` | 49 former RTA paths that redirect to a section overview page, with link counts, a sample linking page and anchor, and the current page on the same subject where one exists (19). Produced by [`legacy_redirects.py`](legacy_redirects.py). |
| `nita-related-articles.csv` | The “Related Articles” links of each blog post and press release, extracted from the HTML cache by [`related_articles.py`](related_articles.py). |

To reproduce the summaries: `gunzip -k nita-internal-link-edges.csv.gz`, then run `analyze_internal_links.py` and `legacy_redirects.py` with the B1 `pages.csv`.

## Summary of results

Raw observations; findings are in the [NITA SEO report](../../../../docs/audit/02-seo/nita-illinois-gov.md) (`SEO-NITA-023`, `SEO-NITA-024`, `SEO-NITA-025`).

- **Core pages** (62 non-blog, non-press URLs returning 200): all within 7 clicks of the homepage; 43 are in the global menu. Pages not in the menu and with at most one content link include `/nita-rider-advisory-council` and `/nita-ada-advisory-council` (one 2026-09-25 post), `/grant-support-letters`, `/investor-relations-sub`, and `/transit-funding/2024-regional-transit-budget`; `/forward-for-all` is reached only through the `/forwardforall` redirect.
- **Blog posts and press releases:** 791 of 792 posts have a Related Articles block, but only five different sets of linked posts appear; 442 posts from 2015–2020 all show the same six 2020 posts. The 420 press releases have no related links and no tag links.
- **Redirects in links:** the menu links on every page to three shortcut URLs that 302-redirect to external tools (`/region/regional-transit-data`, `/riders/transit-benefit-fare-program`, `/riders/free-and-reduced-fare-programs/registration-sites`). In page content, 160 links on 132 pages point to former RTA paths that 301-redirect to section overview pages.
- **Anchor text:** generic anchors are rare in content links (“learn more” 21, “here” 16, “click here” 2). The most frequent content anchor, “RTA” (1,697 links), is mostly the partner agency strip above the footer, which links “RTA” to NITA's homepage (see `SEO-NITA-017`); file-name anchors such as “22 RTA 0646” come from linked thumbnail images (`SEO-NITA-017`).
