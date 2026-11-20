# Structured data validation — 2026-11-20

Official validators run in a browser on 2026-11-20 (about 12:50–12:55 Chicago time) against the live URLs. Screenshots are in [`validator-screenshots/`](validator-screenshots/).

| URL | Schema.org Validator | Google Rich Results Test (Googlebot smartphone) |
| --- | --- | --- |
| https://nita.illinois.gov/ | 0 errors, 0 warnings; 2 items: `BreadcrumbList`, `WebSite` (organizations nested). A first attempt earlier the same day timed out; the retry succeeded. | Crawled successfully (12:52:02). 5 valid items: Breadcrumbs (1), Local businesses (2), Organization (2). One non-critical issue: `#creator` (`GovernmentOrganization`) missing optional field `image`. No article item detected. |
| https://nita.illinois.gov/about-rta/press-releases/northern-illinois-transit-authoritys-first-regional-budget-proposal-expands-service-creates-jobs-and-improves-safety-across-six-counties | 0 errors, 0 warnings; 2 items: `BreadcrumbList`, `WebSite`. | Crawled successfully (12:53:40). 5 valid items: Breadcrumbs (1), Local businesses (2, non-critical issues), Organization (2). No Article item detected for the press release. |
| https://www.mytransitbenefit.com/ | 0 errors, 0 warnings; 2 items: `BreadcrumbList`, `WebSite`. The nested `#identity` node shows `@type` `LocalBusiness`, name “Northern Illinois Transportation Authority”, email `webadmin@rtachicago.org`, `priceRange` “$”. | Crawled successfully (12:53:02). 5 valid items: Breadcrumbs (1), Local businesses (2), Organization (2). No issues reported. |

Interpretation: the markup is syntactically valid and eligible for the features Google detected. Validity does not show that the values are accurate or that the page types are appropriate; those observations are recorded in `SEO-NITA-016` and `SEO-MTB-004`.
