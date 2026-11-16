# Screaming Frog Crawl Evidence

Store Screaming Frog exports here as shared evidence for the audit. Findings in any audit section may reference these files; avoid keeping separate duplicate copies under SEO, AEO, accessibility, or UX.

## Folder structure

Create a date-stamped folder for each crawl:

```text
evidence/crawls/screaming-frog/
├── nita-illinois-gov/
│   └── YYYY-MM-DD/
└── mytransitbenefit-com/
    └── YYYY-MM-DD/
```

Use the crawl date in ISO format. Keep exports from different sites and crawl dates separate. Keep Screaming Frog's descriptive export names, such as `internal_all.csv`, `response_codes_all.csv`, `page_titles_all.csv`, and `images_all.csv`.

## Crawl notes

Each dated crawl folder should include a small `README.md` recording:

- Crawl date and starting URL.
- Crawl mode and user agent, if changed from defaults.
- URL limit or other coverage limits, including the free 500-URL cap.
- Export filenames and any filtering applied.
- Any crawl errors or exclusions that affect interpretation.

The standard export set for this audit is `Internal > All`, `Response Codes`, `Page Titles`, `Meta Description`, `H1`, `H2`, `Images`, `Canonicals`, `Directives`, `Structured Data`, and `Sitemaps`. `Meta Keywords` is intentionally excluded.

These exports are shared raw evidence, not findings by themselves. Each audit section should validate relevant rows and explain the observed impact before citing an issue. Refer to evidence with a repository-relative path, for example `evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-16/internal_all.csv`.
