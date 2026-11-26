# UX Audit Work Plan — NITA websites

## Purpose and governing scope

This work plan operationalizes the Design & User Experience (UX) scope in [`docs/project-overview.md`](../../project-overview.md#25-design--user-experience-ux). That proposal is the source of truth for what the client was told would be reviewed. The UX assessment covers both [nita.illinois.gov](https://nita.illinois.gov/) and [mytransitbenefit.com](https://www.mytransitbenefit.com/) and includes:

1. Navigation structure and information architecture.
2. Visual hierarchy and content presentation.
3. User journeys and clarity of key actions.
4. Mobile responsiveness and usability.
5. Consistency across pages and interface elements.
6. Calls to action and user engagement opportunities.
7. Content readability and accessibility.
8. Friction points and usability improvements.

The proposal calls for practical recommendations that can enhance the existing experience without necessarily requiring a complete redesign, based on manual review of representative pages, templates, and key user journeys — not an exhaustive page-by-page review.

## Audience and objectives (nita.illinois.gov)

Before expanding page coverage past the homepage, the site's audiences and purpose were confirmed from three independent sources rather than assumed: the project's own [transit system context note](../../transit-system-context.md), the SEO section's [review matrix](../02-seo/seo-review-matrix.md), and the AEO section's [question inventory](../03-aeo/aeo-audit-plan.md). All three converge on the same multi-audience map, which the homepage's own "Quick Links" dropdown (`UX-NITA-004`) independently reflects:

| Audience | Primary objective | Where it lives in the navigation |
| --- | --- | --- |
| Riders / general public (largest, most frequent) | Transactional: how to ride, pay fare, apply for reduced/free fare programs | Riders, Public Safety |
| Municipalities / local governments (partners, not end riders) | Planning support, zoning, funding programs | Communities |
| Public / civic engagement / press | Budget public comment, public meetings, news | News, Funding |
| Institutional / compliance (small, high-stakes) | Transparency, FOIA, investor relations, vendor/procurement, careers | About NITA |

This reframes navigation/IA observations: a department-style navigation is not inherently wrong for a public authority with legal obligations toward multiple constituencies (see `UX-NITA-005`), but Riders — the largest, most frequent audience — currently carries the same visual weight as much smaller, lower-frequency audiences. Page/journey selection (below) is chosen to cover all four audiences, not only the templates convenient to reuse from the SEO sample.

## Relationship to other sections

- **Accessibility & ADA** (section 01) owns WCAG success criteria: color contrast, keyboard operability, screen-reader semantics, alt text. If a UX observation is really a WCAG violation, record it in accessibility and cross-reference the ID here instead of duplicating it. Record it in UX only when the effect on usability extends beyond the WCAG criterion itself (e.g., a focus state is technically compliant but still confusing).
- **SEO** (section 02) already produced a confirmed, representative page sample for both websites (see [SEO review matrix](../02-seo/seo-review-matrix.md)). Reuse that sample as the UX page-level scope by default (see below) instead of renegotiating a new list, unless a UX-specific journey requires a page outside it.

## Method: heuristic evaluation, not subjective preference

This is a **heuristic evaluation**, a recognized UX audit method: each observation is checked against a named usability principle and tied to a user goal, not to personal visual taste. Use Jakob Nielsen's 10 usability heuristics as the evaluation lens:

1. Visibility of system status
2. Match between system and the real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

Per the [authoring guide, section 6](../authoring-guide.md#6-section-specific-guidance): describe the user goal, the steps or friction observed, and the effect on task completion or confidence. Avoid subjective design judgments without a user-centered reason — "the heading is small" is not a finding; "the heading is visually subordinate to surrounding text, so the primary action on this page is easy to miss" is.

## Agreed access boundary

The audit is limited to publicly accessible pages, resources, and public testing tools, consistent with the project-wide decision already applied to SEO. No analytics, session recordings, heatmaps, or user research (surveys, interviews, usability testing with real users) are in scope. This means actual task-completion rates, drop-off points, and user sentiment cannot be measured directly — they are inferred from heuristic review of the public interface. Mark anything that would require analytics or user research **Not verifiable in public scope**.

## Site-wide vs. page-specific findings

Pages share components — header, primary navigation, footer, language switcher, button styles — so the same defect can surface on every page reviewed. Do not file a new finding per page for the same root issue. Each finding in a site report states a **Scope**:

- **Site-wide:** a shared component's defect, observed on one page but applying everywhere that component appears (e.g., the header logo, language switcher, mobile menu panel).
- **Component:** shared by some, not all, pages (e.g., a specific tabbed section reused on two of several pages).
- **Page:** unique to one page's own content or a component that exists only there (e.g., a page-specific tool or widget).

Before recording a finding on a newly-reviewed page, check the existing Site-wide findings first. If the same defect recurs, add that page as supporting evidence to the existing finding ID rather than creating a new one; only open a new ID when the page reveals a genuinely different issue.

## How to record the audit

Use a UX review matrix (`ux-review-matrix.md`, to be created at the start of Step 1) as the control checklist for both websites, following the general [review controls and coverage method](../authoring-guide.md#3-review-controls-and-coverage). Give each of the 8 proposal areas, per website, a status, review date, method, and evidence reference. Findings are a separate, linked record in the site reports (`nita-illinois-gov.md`, `mytransitbenefit-com.md`), using IDs `UX-NITA-###` / `UX-MTB-###`.

## Tools and evidence

| Tool or source | Use | Evidence and limits |
| --- | --- | --- |
| Public browser, desktop + mobile viewport (devtools emulation and at least one real mobile device if available) | Walk each representative page and journey; observe navigation, hierarchy, CTAs, responsiveness. | Record date, viewport/device, and browser. A manual walkthrough is a sample, not a usability test with real users. |
| Screenshots | Capture the specific element or layout being discussed. | Save under `evidence/ux/<site>/` with a descriptive filename; link from the finding. |
| Existing SEO/accessibility crawl exports (`evidence/crawls/screaming-frog/**`) | Reuse for page inventory, template grouping, and broken-link context — do not re-crawl. Read-only. | Already dated and scoped in the SEO work; cite rather than duplicate. |
| PageSpeed Insights / Lighthouse (if not already cited from SEO) | Cross-reference only where a performance signal (e.g., slow interaction) plausibly affects perceived usability. | Cite the SEO section's results where they already exist rather than re-running tests. |

## Work sequence

### Step 1 — Confirm scope and representative pages/journeys

1. Adopt the SEO-confirmed page sample as the default UX page-level scope: the 4 My Transit Benefit URLs and the 15 NITA URLs/templates in the [SEO review matrix](../02-seo/seo-review-matrix.md). Record any addition needed to cover a distinct user journey or audience not represented there and the reason. **2026-11-24:** the SEO sample has no institutional/compliance-audience page (see audience map above); added `/about-nita` and `/about-nita/transparency` (FOIA/transparency hub) to the NITA scope for this reason.

   **Resulting full NITA scope: 17 pages** (the SEO section's 16 + these 2 additions) — comparable in scale to the SEO section's own total sample of 20 pages (16 NITA + 4 My Transit Benefit), not a smaller or separately-negotiated scope. Pages are worked through in small batches across multiple sessions (see Current work status below for which batch is active and which pages are done); a batch size (e.g. 6-7 pages at a time) is a *session-sized chunk of this plan*, never the plan's total page count. Read this file's Current work status section, not a batch mentioned in any one conversation, to know the real total and what remains.

   **Decision, 2026-11-26:** the SEO section's 4th targeted-template check — one press release (legacy `/about-rta/press-releases/...` path) — is deliberately **excluded** from the UX scope. Reasoning: a press release uses the same generic article template as an "On Track" blog post (heading, date, body, image, links); UX has a blog article in scope already and reading a press release is not a materially different user task. If something press-release-specific turns up while reviewing the blog, note it there rather than reopening this as a separate page.
2. Define the key user journeys to walk end-to-end rather than page-by-page, for example: a rider finding how to pay for a ride, a rider applying for a reduced-fare program, an employer/employee understanding My Transit Benefit, a community member finding a planning program.
3. Create the UX review matrix with one row per proposal area, per website, status `Not assessed`.

**Output:** confirmed page/journey scope, UX review matrix skeleton.

### Step 2 — Desktop heuristic walkthrough

1. For each representative page: evaluate navigation/information architecture, visual hierarchy, consistency of interface elements (buttons, links, spacing, typography) against the 10 heuristics.
2. For each key journey: walk it end-to-end, noting every point of friction, ambiguity, or dead end — not just the destination page.
3. Evaluate calls to action: are primary actions visually distinct, consistently labeled, and placed where the journey needs them?
4. Update the UX review matrix with status and evidence as each area is covered; do not wait until the end to record no-issue results.

**Output:** desktop findings, screenshots, updated matrix statuses.

### Step 3 — Mobile and responsive walkthrough

1. Repeat the representative pages and key journeys at common mobile and tablet viewports (or a real device).
2. Compare content and functionality parity with desktop; note anything hidden, reordered, or harder to reach.
3. Check touch-target sizing, tap-friendly spacing, and readability (text size, line length) on small screens.
4. Record mobile-specific findings distinctly from desktop findings, even when related, so each is independently actionable.

**Output:** mobile/responsive findings, updated matrix statuses.

### Step 4 — Consolidate, prioritize, and close

1. Deduplicate findings across pages that share a template (report once, naming the affected page/template, not once per instance).
2. Validate every finding against the [authoring guide](../authoring-guide.md#4-finding-format): user goal, evidence, impact, recommendation, priority, complexity, stable ID.
3. Cross-check against the accessibility section to avoid duplicate findings; link rather than repeat.
4. Order each site report's findings by priority and user/business impact.
5. Give every matrix row a final status and feed prioritized UX actions into the cross-site roadmap ([`06-recommendations-and-roadmap.md`](../06-recommendations-and-roadmap.md)).

**Output:** completed UX matrix, both site reports, prioritized recommendations.

## Completion criteria

The UX workstream is ready for consolidation when:

- All 8 proposal areas are represented in the matrix for both websites.
- Every control has an explicit final status and traceable evidence (screenshot, page/journey reference) or a documented limitation.
- Desktop and mobile are both covered for every representative page and key journey.
- Each finding is tied to a user goal and a named heuristic or observed effect, not a subjective preference.
- No duplicate findings with the accessibility section; cross-references are used instead.
- The site reports and roadmap inputs are consistent with the matrix and authoring guide.

## Current work status — 2026-11-26

Read this section first in any new session before assuming a page count or next step; it is the authoritative status, not a number mentioned in any single conversation.

- **Full confirmed scope:** 17 NITA pages (SEO's 16-page sample, minus the press release which UX deliberately excludes — see Step 1 decision log — plus `/about-nita` and `/about-nita/transparency`) + 4 My Transit Benefit pages = 21 pages total across both sites. See Step 1 above for how this was derived.
- **Closed so far (11 of 17 NITA pages):** Homepage, Riders (`/riders`), How to ride (`/riders/how-to-ride`), Discounted Fare and Ride Free Programs (`/riders/free-and-reduced-fare-programs`), Access Program (`/riders/access`), Paying for your ride (`/riders/paying-for-your-ride`), Accessible transit (`/riders/accessible-transit`), Communities (`/communities`), Community Planning (`/communities/community-planning`), Access to Transit (`/communities/access-to-transit-program`), 2027 Regional Transit Budget (`/transit-funding/2027-regional-transit-budget`). Closing Riders also covered the global header/navigation and footer (shared components present on every page), surfacing several site-wide findings; some of those (`UX-NITA-010`, `UX-NITA-016`, `UX-NITA-017`) were confirmed to reproduce identically on later pages. A shared intro-banner component that silently hides page text (`UX-NITA-018`) was first noticed incidentally on Discounted Fare/Ride Free and confirmed on 4 pages so far (clips on 2, doesn't on 2, depending on each page's text length). Paying for your ride looked like a repeat of known components at a glance, but introduced a genuinely new content type (fare comparison tables) that overflow the viewport on mobile with no scroll cue (`UX-NITA-019`) — confirming that the lighter spot-check protocol still needs a full check of anything genuinely new on an otherwise-familiar page. 21 findings recorded (`UX-NITA-001`–`021`) in [nita-illinois-gov.md](nita-illinois-gov.md); see its "Findings at a glance" table. `UX-NITA-020` (a layout gap/misalignment in Accessible transit's Metra tab) was added after that page was already closed, flagged by Fernando on a later look — closing a page doesn't prevent adding a finding found afterward. Review matrix rows for all closed pages are complete in [ux-review-matrix.md](ux-review-matrix.md).
- **Review protocol for pages that reuse only already-audited components:** after closing a few pages, it became clear the site reuses a small set (~5-6) of shared content components (intro banner, diagonal CTA block, tabbed sections, FAQ/accordion blocks, related-posts list, header, footer) across many inner pages. For a page built entirely from components already audited elsewhere, a full from-scratch heuristic/mobile/tablet/language walkthrough is redundant (see [[feedback-ux-audit-pacing]] for why this came up and how it was agreed with Fernando). Instead: (a) check whether each known risky component's defect (`UX-NITA-010`, `UX-NITA-018`, footer findings) actually triggers given this page's specific content — fast, e.g. a DOM height check — and (b) scan the full page once for any content or component not already covered. Reserve the full walkthrough for pages with a genuinely new template or unique interactive component. Access Program was the first page closed this way.
- **Not started (remaining 6 NITA pages of 17):** `/region/how-system-working`, `/blog` (On Track blog listing), one blog article, the CTA tag archive, `/about-nita`, `/about-nita/transparency`.
- **Not started at all:** mytransitbenefit.com (4 pages).
- **Working agreement with the reviewer (Fernando):** go one page at a time, in one continuous conversation per page (see [[feedback-ux-audit-pacing]]); close and get explicit confirmation on a page before starting the next one. A "batch of N pages" discussed in any one session is that session's planned sequence through the scope above, not a redefinition of the scope itself. Findings never attribute who (Fernando vs. Claude) found them — that goes only in `docs/internal-ux-review-log.md`, outside the client deliverable. A defect spotted incidentally on a page outside the current scope (as happened with `UX-NITA-017` and `UX-NITA-018`) is verified and recorded immediately rather than deferred, since shared/site-wide components surface the same way regardless of page order.
- **Next step:** continue through the remaining pages above, one at a time, applying the lighter spot-check protocol above wherever a page turns out to reuse only known components. Session paused after 2027 Regional Transit Budget for the day (2026-11-26); next page is `/region/how-system-working`.
