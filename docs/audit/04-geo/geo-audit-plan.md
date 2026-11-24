# GEO Audit Work Plan — NITA websites

## Purpose and governing scope

This work plan operationalizes the Generative Engine Optimization (GEO) scope in [`docs/project-overview.md`](../../project-overview.md#24-generative-engine-optimization-geo). That proposal is the source of truth for what the client was told would be reviewed. The GEO assessment covers both [nita.illinois.gov](https://nita.illinois.gov/) and [mytransitbenefit.com](https://www.mytransitbenefit.com/) and asks how effectively AI-powered search and generative platforms, such as ChatGPT, Perplexity, and Google Gemini, can discover, interpret, and reference their content. It includes:

1. Content accessibility for AI-powered search systems.
2. Semantic structure and content organization.
3. Structured data and machine-readable information.
4. Content clarity, authority, and contextual relevance.
5. Opportunities to improve content visibility in AI-generated answers.
6. Recommendations to improve the likelihood of content being accurately retrieved, summarized, and referenced by generative search platforms.

The proposal calls for automated analysis plus expert manual review of representative pages, templates, and key journeys, and for practical improvements that support visibility in AI-driven search experiences. Like the other sections, the result is a set of evidence-based findings with priority, implementation complexity, and inputs to the action plan.

The GEO work is organized in four **steps** (Step 1–4), mirroring the [SEO work plan](../02-seo/seo-audit-plan.md) and the [AEO work plan](../03-aeo/aeo-audit-plan.md). They are internal to this workstream and are distinct from the three project phases in the proposal.

## Boundaries with SEO and AEO

GEO looks at the websites from the side of generative platforms: whether their crawlers and retrieval systems can reach the content, whether the content and its publisher are unambiguous, and whether the answers those platforms give about NITA and the transit benefit program are accurate and cite the official pages. To avoid duplicate findings:

| Topic | Covered in | GEO use |
| --- | --- | --- |
| Search engine crawlability, indexability, redirects, metadata, performance | SEO (complete) | Cite the SEO finding when it also limits AI retrieval (for example `SEO-NITA-021`, translations not visible to crawlers); do not re-report it. |
| Whether a page contains a clear, direct answer to a question | AEO | GEO reuses the AEO question inventory and answer map, and assesses what generative platforms do with those answers. |
| Structured data validity | SEO (`SEO-NITA-016`, `SEO-MTB-004`) | GEO covers entity identity: whether markup and other machine-readable sources describe NITA and the program consistently across the web. |
| Google AI Overviews | AEO captures them for priority questions | GEO compares AI Overviews with ChatGPT, Perplexity, and Gemini answers for the same prompts. |

## Agreed access boundary

The audit is limited to publicly accessible pages, resources, public search results, public AI platforms, and open testing tools, with no Search Console, analytics, CMS, source code, hosting, or server logs (project decision, 2026-11-19). Without server logs, it is not possible to see which AI crawlers actually visit the websites, how often, or what they receive; mark these **Not verifiable in public scope**.

Generative answers change with the platform, model version, mode (with or without web search), signed-in state, location, conversation history, and time. Tests run through a US connection with a Chicago, Illinois IP address, in a new conversation for each prompt, with web search enabled where the platform offers it, and record all of these conditions. A prompt sample shows how platforms answer on that date; it is not a measure of visibility, share of voice, or traffic, and no finding may promise citation or inclusion in generative answers ([authoring guide](../authoring-guide.md#6-section-specific-guidance)).

Prompts sent to AI platforms contain only public, generic questions about NITA's services; no client or personal data is entered. Platforms that require an account (for example Gemini) are used only after a team member signs in in the built-in browser; the reviewer does not create accounts or enter credentials.

## How to record the audit

Create a GEO review matrix (`geo-review-matrix.md`) with one row per proposal area for each website, following the [review controls and coverage method](../authoring-guide.md#3-review-controls-and-coverage) and the status definitions in the authoring guide. Findings use the IDs `GEO-NITA-###` and `GEO-MTB-###` and the finding format in the [authoring guide](../authoring-guide.md#4-finding-format), including the “Findings at a glance” table when a file has more than five findings. Update the two GEO site reports to the guide's section structure before the first finding is recorded.

Store new evidence in dated folders under `evidence/geo/`, each with a README that states method, date, platform conditions, and limits. Save AI answers as text with their cited URLs (not only screenshots) so they can be compared. Reference SEO and AEO evidence in place; do not copy it.

## What SEO already collected and how GEO reuses it

| SEO evidence | Location | GEO use |
| --- | --- | --- |
| `robots.txt` of both websites (2026-11-19): only `User-agent: *` rules for `/cpresources/`, `/vendor/`, `/.env`, `/cache/`; no rules for AI crawlers | [NITA](../../../evidence/public-technical/2026-11-19/nita-robots.txt), [My Transit Benefit](../../../evidence/public-technical/2026-11-19/mytransitbenefit-robots.txt) | Starting point for crawler access: AI crawlers are not blocked by `robots.txt`. Step 2 re-checks the live files and tests server responses. |
| Raw and rendered HTML match on the 20 sample pages; same HTML for desktop, mobile, and Googlebot smartphone | [`rendered-review/`](../../../evidence/public-technical/2026-11-24/rendered-review/README.md), [`mobile-review/ua-parity.txt`](../../../evidence/public-technical/2026-11-24/mobile-review/ua-parity.txt) | Content is readable by crawlers that do not run JavaScript, which many AI crawlers do not. |
| Translations exist only in the browser, on the English URLs (`SEO-NITA-021`) | [`weglot-check.txt`](../../../evidence/public-technical/2026-11-24/rendered-review/weglot-check.txt) | Explains why AI platforms cannot cite NITA content in Spanish, Polish, Chinese, and other languages; test with non-English prompts. |
| JSON-LD of the 20 sample pages and validator results (`SEO-NITA-016`, `SEO-MTB-004`) | [`structured-data/`](../../../evidence/public-technical/2026-11-20/structured-data/) | Entity identity: `GovernmentOrganization` on NITA, a misnamed `LocalBusiness` with an RTA email on My Transit Benefit, `sameAs` profiles. |
| XML sitemaps and the sitemap/crawl comparison | [`sitemaps/`](../../../evidence/public-technical/2026-11-20/sitemaps/), [`sitemap-crawl-comparison.csv`](../../../evidence/public-technical/2026-11-19/sitemap-crawl-comparison.csv) | Machine-readable discovery of current pages. |
| Seven Google result pages, two with AI Overviews (“nita chicago” citing Wikipedia, news, county websites, and NITA; “chicago transit trip planner” citing mostly CTA) | [`search-sample-2026-11-24.md`](../../../evidence/public-technical/2026-11-24/content-review/search-sample-2026-11-24.md) | First evidence of which sources generative answers rely on for NITA topics. |
| Fare check, time-sensitive content, and conflicting facts (`SEO-NITA-027`) | [`content-review/`](../../../evidence/public-technical/2026-11-24/content-review/README.md) | Basis of the fact sheet used to score AI answers for accuracy. |
| RTA-to-NITA naming: legacy redirects (`SEO-NITA-024`), third-party pages still describing “RTA” programs (`SEO-NITA-028`), My Transit Benefit labels and links (`SEO-MTB-007`) | SEO reports and evidence | Entity consistency: whether AI answers treat NITA and the RTA correctly and point to current URLs. |
| Outlook Safe Links URLs that hide real destinations (`SEO-NITA-026`) and external links to closed RTA domains (`SEO-NITA-018`) | [`safelinks-urls.csv`](../../../evidence/public-technical/2026-11-24/content-review/safelinks-urls.csv), [external link classification](../../../evidence/crawls/link-discovery/2026-11-20/nita-external-link-classification.csv) | Source references that machines cannot follow or that lead to retired domains. |
| Internal link graph and page inventory | [`link-discovery/2026-11-24/`](../../../evidence/crawls/link-discovery/2026-11-24/README.md), [`url-inventory.csv`](../../../evidence/crawls/screaming-frog/nita-illinois-gov/2026-11-19/url-inventory.csv) | Which pages are the main source for each topic; the share of historical RTA-era content that platforms may retrieve. |
| AEO question inventory and answer map (when complete) | `evidence/aeo/` | Prompt set for platform tests and the expected official answer for each prompt. |

## What GEO needs to collect

1. **AI crawler access test.** The live `robots.txt` of both websites checked against the published user agents of the main AI crawlers (for example OpenAI's `GPTBot`, `OAI-SearchBot`, and `ChatGPT-User`; `PerplexityBot` and `Perplexity-User`; Anthropic's `ClaudeBot`; Google's `Google-Extended` control token; `Bingbot`, which feeds Bing-based answers; and `CCBot`), plus requests to sample pages with those user-agent strings to see whether the server or a firewall answers differently. A request with a borrowed user agent does not come from the platform's own IP addresses, so a block confirms a user-agent rule but a success does not prove the real crawler is allowed.
2. **Fact sheet.** A dated list of about 30 official facts that answers should get right: what NITA is and when it replaced the RTA, fares and passes, reduced fare, Ride Free, and Access eligibility and how to apply, ADA Paratransit application steps and phone numbers, the Ride Safe app, the 2027 budget and comment deadline, the transit benefit monthly limit and enrollment, and the Illinois law for employers. Each fact cites its official URL; conflicts found on the websites are recorded as conflicts, not resolved by the reviewer.
3. **Prompt set.** About 25 prompts for NITA and 10 for My Transit Benefit, taken from the AEO question inventory and written as people ask AI assistants (for example “How do I renew my RTA Ride Free permit?”, “What is NITA in Chicago?”, “Does my Chicago employer have to offer pre-tax transit benefits?”), including entity prompts, comparison prompts, and three to five prompts in Spanish and Polish. The team approves the set before testing.
4. **Platform answer sample.** For each prompt, one run on ChatGPT (with search), Perplexity, Gemini, and Google AI Overviews or AI Mode where shown: answer text, cited URLs, whether NITA or My Transit Benefit is cited, whether the cited URL is current, accuracy against the fact sheet, and whether the answer presents the RTA as the current agency. A subset is repeated to show variability.
5. **Entity and source review.** How NITA and the program are described by sources that platforms cite: Wikipedia and Wikidata, the Illinois state website, CTA, Metra, Pace, Ventra, county and municipal pages, and news. Record the name, description, URL, and whether it still refers to the RTA.
6. **Machine-readable inventory.** JSON-LD (from SEO), sitemaps, RSS or Atom feeds, public data portals, and PDF documents among the main sources (whether text is extractable), plus the presence of emerging files such as `llms.txt`, noted as observations only because they are not an established standard and major platforms have not confirmed using them.
7. **Authority and context signals.** On the sample pages: publication and update dates, named authors or offices, sources for figures, contact details, and statements of official status; and whether historical RTA-era content is clearly dated so platforms do not present it as current.

## Tools and evidence

| Tool or source | Use | Evidence and limits |
| --- | --- | --- |
| curl with AI crawler user-agent strings | Server and firewall responses to AI crawler user agents. | Borrowed user agents do not reproduce the crawlers' IP addresses or verification. |
| Built-in Chromium browser in the Claude desktop app | Run prompts on ChatGPT, Perplexity, Gemini, and Google; read cited pages. | US connection with a Chicago, Illinois IP address; signed out unless a team member signs in; answers vary by model and date. |
| Google and Bing result pages | AI Overviews and AI Mode for Google; Bing results as an input to Bing-based answers. | Qualitative; record settings and date. |
| SEO and AEO evidence | Crawlability, rendering, structured data, question inventory, answer map, and fact checks. | Snapshots from their review dates. |
| Scripts in the evidence folders (Python standard library) | User-agent tests, answer and citation tables, accuracy scoring against the fact sheet. | Saved with the evidence so results can be reproduced. |

## Work sequence

Method (team decision, 2026-11-24, same as SEO Step 3): the GEO review is AI-assisted. The reviewer (Claude) runs the collection and analysis; the team approves the fact sheet and the prompt set, signs in to platforms that require an account, and reviews each part before the next. GEO Step 2 part C depends on the AEO question inventory and answer map (AEO Step 2 part A).

### Step 1 — Scope, fact sheet, and prompt set

1. Create the GEO review matrix and update the two site reports to the authoring guide structure.
2. Build the fact sheet from the websites and partner sources, recording conflicts.
3. Draft the prompt set from the AEO question inventory and add entity, comparison, and non-English prompts; agree it with the team.
4. Agree which platforms and modes are tested and who signs in where an account is needed.

**Output:** GEO matrix, approved fact sheet and prompt set, platform test plan.

### Step 2 — Collect access, entity, and answer evidence

Work in parts and review each with the team before the next: (A) AI crawler access and machine-readable inventory, items 1 and 3; (B) entity and source review, item 4; (C) platform answer sample, items 5 and 6.

1. Test AI crawler access and record `robots.txt` rules, server responses, and machine-readable sources.
2. Review how NITA and the program are described across the sources platforms cite.
3. Run the prompt set on each platform, save answers and citations, and score accuracy and citation against the fact sheet.

**Output:** dated evidence folders, access test results, entity source table, and the platform answer sample with accuracy and citation scores.

### Step 3 — Assess interpretation, authority, and opportunities

Work in parts: (A) content accessibility for AI systems, item 1; (B) semantic structure and machine-readable information, items 2 and 3; (C) clarity, authority, and context, item 4; (D) visibility and accuracy opportunities, items 5 and 6.

1. Identify barriers to retrieval (blocked crawlers, content only in PDFs or images, translations only in the browser, hidden or email-wrapped links).
2. Assess whether page structure, headings, and markup let platforms identify NITA's services, eligibility rules, and contacts as distinct facts.
3. Assess clarity and authority: official status, dates, sources, consistency between pages, and how clearly historical RTA content is separated from current guidance.
4. From the answer sample, identify topics where platforms cite other sources instead of NITA, repeat outdated or conflicting facts, or present the RTA as current, and trace each to a cause on the websites or in third-party sources; recommend practical changes, without promising citation.

**Output:** GEO findings for both websites with evidence, priority, and complexity; matrix statuses.

### Step 4 — Close controls and report recommendations

Same as SEO Step 4: (A) give every matrix row a final status; (B) validate the findings against the authoring guide and order them by priority; (C) classify recommendations as technical, editorial, or requiring client confirmation, noting that changes to third-party sources (for example Wikipedia or partner websites) depend on those owners; (D) add GEO inputs to the [roadmap](../06-recommendations-and-roadmap.md), grouped with related SEO and AEO actions, and add the “Findings at a glance” table.

**Output:** completed GEO matrix, site reports, evidence links, and roadmap inputs.

## Completion criteria

The GEO workstream is ready for consolidation when:

- All six proposal areas are represented in the matrix for both websites, each with a final status and evidence or a documented limitation.
- The fact sheet, prompt set, and platform answers are saved with dates and conditions, and every scored answer can be traced to its prompt, platform, and cited URLs.
- Crawler access conclusions state what public tests can and cannot show; anything that needs server logs is marked **Not verifiable in public scope**.
- No finding promises visibility, citation, or inclusion in generative answers.
- Findings cross-reference related SEO and AEO findings instead of repeating them, and the site reports, matrix, and roadmap are consistent with the authoring guide.

## Open decisions for the team

- Approve the fact sheet and prompt set (Step 1).
- Confirm the platforms and modes to test, and who signs in to platforms that require an account.

## Current work status — 2026-11-24

- Plan drafted. Step 1 not started; Step 2 part C waits for the AEO question inventory and answer map. SEO evidence listed above is available for reuse.
