# Recommendations and Action Roadmap

> Consolidate and sequence recommendations from both websites after the audit findings are reviewed.

**Status (2026-11-24):** Search Engine Optimization (SEO) inputs only. The SEO review is complete ([NITA report](02-seo/nita-illinois-gov.md), [My Transit Benefit report](02-seo/mytransitbenefit-com.md), [review matrix](02-seo/seo-review-matrix.md)); the accessibility, Answer Engine Optimization (AEO), Generative Engine Optimization (GEO), and user experience (UX) sections will add their recommendations before this roadmap is consolidated and re-sequenced across sections.

## Timing used for the SEO inputs

These are proposed groupings for planning, not delivery commitments:

- **Immediate:** High-priority items and Medium-priority items with low complexity and no business decision needed, plus corrections to information riders act on.
- **Short-term:** The remaining Medium-priority items that need a confirmation from NITA first, and Low-priority items with low complexity.
- **Long-term:** Items with medium complexity that need a decision, a template redesign, or work across many historical pages.

Each recommendation's type (technical or editorial) and the confirmation it needs before acting are listed in each site report under “Recommendation types and confirmations”.

## Immediate

- **Server and redirects (nita.illinois.gov):** redirect HTTP to HTTPS on every URL (`SEO-NITA-003`, High).
- **Links and information on current pages (nita.illinois.gov):** fix the broken links on Regional transit system and Paying for your ride (`SEO-NITA-008`), replace the Outlook Safe Links URLs starting with the seven core pages (`SEO-NITA-026`), and correct past dates, the expired registration-site alert, and the conflicting ADA Paratransit call hours (`SEO-NITA-027`).
- **Homepage stability (nita.illinois.gov):** reserve the slider height to fix the desktop layout shift (`SEO-NITA-019`).
- **Shared CMS settings (both websites):** remove `/404` from both sitemaps (`SEO-MTB-001`, `SEO-NITA-007`) and turn off ellipsis truncation of titles and descriptions (`SEO-MTB-002`, `SEO-NITA-012`).
- **My Transit Benefit identity:** correct the organization structured data (`SEO-MTB-004`).

## Short-Term

- **Redirect map review with NITA (nita.illinois.gov):** confirm successor pages, then send former RTA paths, the coalition URLs, and removed pages to the matching current page in one step, with HTTPS targets (`SEO-NITA-024`, `SEO-NITA-006`, `SEO-NITA-009`, `SEO-NITA-004`).
- **Titles, headings, and descriptions (both websites):** homepage and core titles in the words people search with, including permit and service names and the RTA-to-NITA change (`SEO-NITA-010`, `SEO-NITA-011`, `SEO-NITA-028`, `SEO-NITA-002`, `SEO-NITA-001`, `SEO-MTB-003`).
- **Sitemap, canonical, and structured data settings (nita.illinois.gov):** `SEO-NITA-015`, `SEO-NITA-005` (after confirming the listings should be indexed), `SEO-NITA-016`.
- **Performance (both websites):** image compression and caching on My Transit Benefit (`SEO-MTB-006`); script loading and slider images on NITA (`SEO-NITA-020`).
- **Navigation and links (both websites):** parent-page links for menu-only pages and the advisory councils (`SEO-NITA-023`), wide fare tables on phones (`SEO-NITA-022`), a direct link from My Transit Benefit to NITA and removal of RTA labels (`SEO-MTB-007`, `SEO-MTB-005`), and the Employers law wording after legal review (`SEO-MTB-008`).

## Long-Term

- **Multilingual search (nita.illinois.gov):** decide which translations should be discoverable and serve them on their own URLs (`SEO-NITA-021`).
- **News archive (nita.illinois.gov):** topic-based Related Articles, press-release tags, a shorter path to older content, unique titles and descriptions, and bulk updates of former RTA links (`SEO-NITA-025`, `SEO-NITA-013`, `SEO-NITA-014`, `SEO-NITA-018`).
- **Image alternative text (both websites):** a required alternative-text field and descriptions for content images, coordinated with the accessibility section (`SEO-NITA-017`, `SEO-MTB-005`).
- **Content governance (nita.illinois.gov):** owners and review dates for time-sensitive content and a publishing check for email-copied links (process parts of `SEO-NITA-027` and `SEO-NITA-026`).

## Prioritized Recommendations

| Recommendation | Website | Priority | Complexity | Suggested Timing |
| --- | --- | --- | --- | --- |
| SEO — Redirect every HTTP URL to HTTPS with a server-level 301; add HSTS after verification. (`SEO-NITA-003`) | nita.illinois.gov | High | Low | Immediate |
| SEO — Fix the Data Portal button and the two Access card links on current pages. (`SEO-NITA-008`) | nita.illinois.gov | Medium | Low | Immediate |
| SEO — Replace the 68 Outlook Safe Links URLs with direct links, core pages first; add a CMS check. (`SEO-NITA-026`) | nita.illinois.gov | Medium | Low | Immediate |
| SEO — Correct past dates, the expired alert, and the conflicting paratransit hours; set review dates for time-sensitive content. (`SEO-NITA-027`) | nita.illinois.gov | Medium | Low to Medium | Immediate |
| SEO — Reserve the homepage slider height so the page does not shift while loading. (`SEO-NITA-019`) | nita.illinois.gov | Medium | Low | Immediate |
| SEO — Remove `/404` from the sitemap and mark it `noindex` (same fix as `SEO-NITA-007`). (`SEO-MTB-001`) | mytransitbenefit.com | Medium | Low | Immediate |
| SEO — Correct the organization structured data (name, type, email). (`SEO-MTB-004`) | mytransitbenefit.com | Medium | Low | Immediate |
| SEO — Rewrite the four titles and turn off ellipsis truncation in the shared CMS setting (with `SEO-NITA-012`). (`SEO-MTB-002`) | mytransitbenefit.com | Medium | Low | Immediate |
| SEO — Confirm successors and redirect former RTA paths to the matching current page; update internal links. (`SEO-NITA-024`) | nita.illinois.gov | Medium | Low | Short-term |
| SEO — Confirm the coalition destination and replace the six-hop redirect chain with one 301. (`SEO-NITA-006`) | nita.illinois.gov | Medium | Low | Short-term |
| SEO — Give the homepage a descriptive title and one stable H1. (`SEO-NITA-010`) | nita.illinois.gov | Medium | Low | Short-term |
| SEO — Rewrite core page titles to lead with the page topic. (`SEO-NITA-011`) | nita.illinois.gov | Medium | Low | Short-term |
| SEO — Compress and resize masthead images, add caching headers, and load the Employers map on demand. (`SEO-MTB-006`) | mytransitbenefit.com | Medium | Low to Medium | Short-term |
| SEO — Point legacy document redirects and links to HTTPS URLs (with the `SEO-NITA-003` server work). (`SEO-NITA-004`) | nita.illinois.gov | Low | Low to Medium | Short-term |
| SEO — Remove `/404` from the sitemap and mark it `noindex`. (`SEO-NITA-007`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Exclude shortcut and placeholder entries from the sitemap. (`SEO-NITA-015`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Give paginated listings self-referencing canonicals, after confirming they should be indexed. (`SEO-NITA-005`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Fix broken internal links in historical posts and add confirmed redirects for removed pages. (`SEO-NITA-009`) | nita.illinois.gov | Low | Medium | Short-term |
| SEO — Link menu-only and single-link pages from their parent pages, including the advisory councils. (`SEO-NITA-023`) | nita.illinois.gov | Low | Low to Medium | Short-term |
| SEO — Make wide fare tables scroll inside their container on phones. (`SEO-NITA-022`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Correct the structured data types, logo, `sameAs`, and press-release breadcrumbs. (`SEO-NITA-016`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Stop truncating titles and descriptions with an ellipsis (shared CMS setting). (`SEO-NITA-012`) | nita.illinois.gov | Low | Low to Medium | Short-term |
| SEO — Write descriptions for the homepage and the core pages with placeholder text. (`SEO-NITA-002`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Name the topic in tag archive titles and H1s; replace “Connections Blog”. (`SEO-NITA-001`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Use permit and service names in rider program titles; note the RTA-to-NITA change (with `SEO-NITA-011`). (`SEO-NITA-028`) | nita.illinois.gov | Low | Low | Short-term |
| SEO — Defer the Weglot script, limit reCAPTCHA to the form, and optimize slider images. (`SEO-NITA-020`) | nita.illinois.gov | Low | Medium | Short-term |
| SEO — Add a direct link to NITA and replace RTA labels and links. (`SEO-MTB-007`) | mytransitbenefit.com | Low | Low | Short-term |
| SEO — Make inner-page H1s name the topic and audience. (`SEO-MTB-003`) | mytransitbenefit.com | Low | Low | Short-term |
| SEO — Correct the logo label and file-name `alt` text. (`SEO-MTB-005`) | mytransitbenefit.com | Low | Low | Short-term |
| SEO — Correct the law name and tense on Employers after legal review. (`SEO-MTB-008`) | mytransitbenefit.com | Low | Low | Short-term |
| SEO — Decide which translations to expose, then serve them on their own URLs with `hreflang`. (`SEO-NITA-021`) | nita.illinois.gov | Medium | Medium | Long-term |
| SEO — Base Related Articles on shared topics, tag press releases, and shorten the archive path. (`SEO-NITA-025`) | nita.illinois.gov | Low | Medium | Long-term |
| SEO — Fix outbound links on current pages, then rewrite former RTA domain links in bulk. (`SEO-NITA-018`) | nita.illinois.gov | Low | Medium | Long-term |
| SEO — Make recurring post and budget page titles unique. (`SEO-NITA-013`) | nita.illinois.gov | Low | Low to Medium | Long-term |
| SEO — Replace copied meta descriptions with page-specific ones. (`SEO-NITA-014`) | nita.illinois.gov | Low | Low to Medium | Long-term |
| SEO — Add a required alternative-text field and describe content images (with the accessibility section). (`SEO-NITA-017`) | nita.illinois.gov | Low | Medium | Long-term |

Open item: 315 external URLs (480 links on 85 domains) that could not be checked from Argentina await a check from a US connection; results may add links to `SEO-NITA-018`.
