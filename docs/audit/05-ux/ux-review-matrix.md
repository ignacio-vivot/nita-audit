# UX Review Matrix — NITA websites

Control checklist for the UX workstream, following the general [review controls and coverage method](../authoring-guide.md#3-review-controls-and-coverage) and the status definitions in the authoring guide. This matrix is the single place for coverage detail; site reports ([nita-illinois-gov.md](nita-illinois-gov.md), [mytransitbenefit-com.md](mytransitbenefit-com.md)) carry the summary, findings, positive observations, and limitations, and link here rather than repeating it.

Each row states the control, the scope/method applied so far, the current status, and linked finding IDs. A row can be revisited and its status updated as coverage grows; do not mark a row `Verified — no issue observed` until it has actually been checked within a stated scope.

## nita.illinois.gov

### Homepage (`https://nita.illinois.gov/`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Hero carousel renders correctly in every supported language | Desktop + iPad Pro 13 (1032×1376); English, Spanish, Polish, Arabic, Urdu checked 2026-11-24 | **Finding recorded** | Text overlap (ES/PL) and untranslated slide 1 (all languages tested) | `UX-NITA-001`, `UX-NITA-002` |
| 2 | Visual hierarchy and content presentation | Hero carousel renders correctly in remaining supported languages (Chinese, Tagalog, Gujarati) | Not yet checked | **Not assessed** | Same component/mechanism as row 1; pattern plausible but unconfirmed | — |
| 2b | Content readability and accessibility | Right-to-left languages (Arabic, Urdu) render with mirrored layout | Desktop, 2026-11-24; `dir`/`lang` confirmed via console | **Finding recorded** | `dir` empty for both; layout stays left-to-right | `UX-NITA-006` |
| 3 | Consistency across pages and interface elements | Content/navigation translation quality (machine translation spot-check) | Polish nav spot-checked 2026-11-24 | **Finding recorded** (partial coverage) | "Riders" → "Kolarze" (cyclists) | `UX-NITA-003` |
| 4 | User journeys and clarity of key actions | Carousel interaction controls: manual advance, pause/stop if autoplaying | Desktop, 2026-11-24: waited 8s (no autoplay change), clicked indicator dot (advanced correctly) | **Verified — no issue observed** | No autoplay; manual advance works via dots | — |
| 5 | Navigation structure and information architecture | Homepage surfaces primary tasks/audiences without opening the main menu | Desktop, 2026-11-24; compared with `/riders` tabbed section | **Finding recorded** | Only a generic "Quick Links" dropdown below the hero; reusable pattern exists on `/riders` | `UX-NITA-004` |
| 6 | Navigation structure and information architecture | Primary navigation reflects user tasks/audiences, not only internal structure | Desktop, 2026-11-24 | **Finding recorded** | 7 department-level categories, equal weight | `UX-NITA-005` |
| 7 | Mobile responsiveness and usability | Homepage usable at common phone width (375px) | 375×812 (Chrome DevTools mobile emulation), 2026-11-24: hero and body content checked | **Finding recorded** (partial — menu checked; full-page scroll not re-verified beyond hero) | Mobile menu panel leaves a gap exposing page content underneath | `UX-NITA-007` |
| 8 | Consistency across pages and interface elements | Hover/focus visual feedback on nav items and buttons | Desktop, 2026-11-24: nav link hover confirmed; button hover confirmed absent by reviewer in a real browser (resolving this audit's earlier tool-based inconclusive check) | **Verified — no issue observed** (nav links); **Finding recorded** (buttons) | Nav item changes color on hover; buttons show no hover state | `UX-NITA-013` |
| 9 | Calls to action and user engagement opportunities | Footer contact form: labels, validation, clarity | Desktop, 2026-11-24: field labels/layout reviewed; not submitted. Revisited 2026-11-26 at 768px (Polish, Tagalog) | **Finding recorded** (field alignment); **Needs manual validation** (submission behavior, not testable without sending a real message) | Email/Home Phone fields misalign when one label wraps to more lines than the other | `UX-NITA-016` |
| 9b | Consistency across pages and interface elements | Footer contact icons (phone entries) render at a consistent size | Desktop, 2026-11-24 (English) and 2026-11-26 (Polish), 974px and 768px | **Finding recorded** | Icon shrinks as its adjacent text wraps to more lines; more visible in Polish (longer translated labels) | `UX-NITA-014` |
| 9c | Content readability and accessibility | Footer "nearest customer service location" sentence translates cleanly | Spanish and Polish, 2026-11-26 | **Finding recorded** (Spanish); **Verified — no issue observed** (Polish) | Spanish renders a stray duplicate comma from a mid-sentence `<br>` split; not present in Polish | `UX-NITA-015` |
| 9d | Consistency across pages and interface elements | Footer navigation list repeats the same translation defects as the primary nav | Polish, 2026-11-26 | **Verified — no issue observed** (confirms existing finding, no new defect) | Footer nav also shows "Kolarze" for "Riders" — same root cause, not a new issue | `UX-NITA-003` |
| 9e | Mobile responsiveness and usability | Footer's three-column layout fits the viewport at tablet widths | 700-1024px range tested, 2026-11-26, English/Tagalog/Polish (first noticed on `/riders/free-and-reduced-fare-programs`, outside the current page batch, since the footer is a shared site-wide component) | **Finding recorded** | Page-wide horizontal overflow from ~768px to ~950px, in every language tested, not just translated ones | `UX-NITA-017` |
| 10 | Content readability and accessibility | Homepage copy readability (non-WCAG aspects: tone, scannability, jargon) | Not yet checked | **Not assessed** | — | — |
| 11 | Consistency across pages and interface elements | Homepage interface patterns (buttons, color use, spacing) match inner pages | Desktop, 2026-11-24: compared with `/riders`, `/riders/paying-for-your-ride` | **Verified — no issue observed** | Header, typography, color palette, and button styling consistent across the three pages checked | — |

### Riders overview (`https://nita.illinois.gov/riders`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User journeys and clarity of key actions | Page surfaces primary rider tasks with clear CTAs | Desktop, 2026-11-24 | **Verified — no issue observed** | Tabbed "How to ride transit" section (Plan your trip / Pay for your ride / Free and discounted fare programs), each with a clear CTA | — |
| 2 | Mobile responsiveness and usability | Tabbed section adapts to phone width | 375×812, 2026-11-24 (layout/overlap check); revisited 2026-11-26 (tab-switching interaction) | **Finding recorded** | Tabs stack as a vertical list without overlap, but switching tabs has the same scroll problem as tablet width, and it is worse on mobile (headers scroll out after a single scroll gesture) | `UX-NITA-010` |
| 3 | Visual hierarchy and content presentation | Component handles translated (longer) text without overlap | Spanish, desktop, 2026-11-24 | **Verified — no issue observed** | Tab labels wrap to two lines cleanly; contrasts with the homepage carousel (`UX-NITA-001`) | — |
| 4 | Consistency across pages and interface elements | Cross-links to related programs (e.g., My Transit Benefit) | Desktop, 2026-11-24 | **Verified — no issue observed** | Closing "Transit Benefit for Commuters" section links out appropriately | — |
| 5 | Mobile responsiveness and usability | Tabbed section usable at tablet width (768-978px) | 768, 850, 926, 978px, 2026-11-24; reviewer-reported, reproduced | **Finding recorded** | Tab headers scroll out of view; must scroll up to switch tabs | `UX-NITA-010` |
| 6 | Consistency across pages and interface elements | Header logo renders at consistent size across viewport widths | Reviewer-tested in real Chrome and Firefox windows (not devtools), hard-refreshed, at ~830/1066/1286px; not reproduced in this audit's automated browser at matching widths | **Finding recorded** (reviewer-confirmed; tool discrepancy noted) | Logo renders tiny while desktop nav is already shown | `UX-NITA-011` |
| 7 | Content readability and accessibility | Automatic language detection/switching behavior | Reviewer-reported, 2026-11-24 | **Finding recorded** | Page auto-translated to Tagalog without visitor selection | `UX-NITA-012` |

### How to ride (`https://nita.illinois.gov/riders/how-to-ride`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User journeys and clarity of key actions | Trip Planner tool completes its task without unexpected behavior | Desktop, 2026-11-24: filled and submitted with test addresses | **Finding recorded** | Silently navigates to Google Maps in the same tab, no warning | `UX-NITA-008` |
| 2 | Navigation structure and information architecture | Map/resource selector dropdowns are easy to scan | Desktop, 2026-11-24 (Neighborhood Maps); 2026-11-26 (Bus Connection Maps also checked) | **Finding recorded** | Both "Neighborhood Maps" and "Bus Connection Maps" dropdowns (20+ items each) have no discernible order | `UX-NITA-009` |
| 3 | Mobile responsiveness and usability | Trip Planner and tabbed sections adapt to phone width | 375×812, 2026-11-24 | **Verified — no issue observed** | Fields and tabs stack cleanly, full-width, readable | — |
| 4 | Consistency across pages and interface elements | Tabbed "How to ride" (CTA Buses/Trains, Metra, Pace) component matches the pattern seen on `/riders` | Desktop, 2026-11-24; tablet (768px) revisited 2026-11-26 | **Finding recorded** | Same tab pattern reused consistently in layout, but also shares `/riders`' tablet/mobile tab-scroll defect | `UX-NITA-010` |

### Discounted Fare and Ride Free Programs (`https://nita.illinois.gov/riders/free-and-reduced-fare-programs`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner (text + photo) renders all its content | Desktop, 1116×844, 2026-11-26; English, Spanish | **Finding recorded** | Fixed-height, overflow-hidden container silently hides text longer than the photo; 44px hidden in English, 296px (entire final paragraph) hidden in Spanish | `UX-NITA-018` |
| 2 | User journeys and clarity of key actions | Registration Site Alerts, holiday closures, CTA/Metra/Pace eligibility accordions expand correctly | Desktop, 2026-11-26 | **Verified — no issue observed** | All tested accordions expand/collapse correctly with accurate content | — |
| 3 | User journeys and clarity of key actions | "How to apply/renew/replace a Ride Free Permit" tabbed section | Desktop and 768px, 2026-11-26 | **Finding recorded** | Shares the same tablet tab-header-scroll defect as `/riders` and `/riders/how-to-ride` | `UX-NITA-010` |
| 4 | Mobile responsiveness and usability | Page adapts to phone width (375px), including the intro banner | 375×812, 2026-11-26 | **Verified — no issue observed** | Intro banner stacks without clipping at mobile width; rest of page stacks cleanly | — |
| 5 | Mobile responsiveness and usability | Page layout fits tablet widths (~768-950px) without horizontal overflow | 768px, 2026-11-26 | **Finding recorded** | Shares the site-wide footer overflow defect | `UX-NITA-017` |

### Access Program (`https://nita.illinois.gov/riders/access`)

Reviewed with a lighter, spot-check protocol rather than a full repeat walkthrough: this page reuses the same ~5-6 shared components already audited on prior pages (intro banner, diagonal CTA block, tabbed section, FAQ accordion, related-posts list, footer). For a page built entirely from already-audited components, the efficient check is (a) whether each known risky component's defect triggers on this page's specific content, and (b) a scan for any content or component not already covered — not a from-scratch heuristic/mobile/tablet/language pass.

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner renders all its content | Desktop, 2026-11-26; English, Spanish | **Finding recorded** | Confirms `UX-NITA-018` on a 4th page: 100px hidden in English, 260px in Spanish | `UX-NITA-018` |
| 2 | Consistency across pages and interface elements | Page composed entirely of already-audited shared components (no unique content/component found) | Desktop, 2026-11-26, full scroll | **Verified — no issue observed** | Intro banner, diagonal "Apply Now" CTA, "Who is eligible / How do I get Access" tabs, FAQ accordion, related-posts list, footer — all already-known patterns |

### Paying for your ride (`https://nita.illinois.gov/riders/paying-for-your-ride`)

Opened with the lighter spot-check protocol (page looked similar to others at a glance), but its fare comparison tables are a content type not seen on prior pages, so that part got a full check.

| # | Proposal area | Control / method | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner renders all its content | Desktop, 2026-11-26; English, Spanish | **Verified — no issue observed** | This page's intro text is short enough to fit within the banner's fixed height in both languages tested | — |
| 2 | Mobile responsiveness and usability | Fare comparison tables (CTA/Pace, Metra, others) fit the viewport at mobile width | 375×812, 2026-11-26 | **Finding recorded** | Tables overflow the viewport with no horizontal-scroll wrapper; the rightmost column (e.g. "Cash Reduced") ends up almost entirely off-screen with no scroll cue | `UX-NITA-019` |
| 3 | Consistency across pages and interface elements | Accordions (fare tables, by transit provider) expand/collapse correctly | Desktop, 2026-11-26 | **Verified — no issue observed** | CTA and Pace, Metra accordions tested, both expand correctly with accurate content | — |

### Accessible transit (`https://nita.illinois.gov/riders/accessible-transit`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner renders all its content, including its in-page jump links | Desktop, 2026-11-26, English | **Finding recorded** | Confirms `UX-NITA-018` on a 5th page; this time clips part of an in-page jump-link list, not just body copy | `UX-NITA-018` |
| 2 | User journeys and clarity of key actions | Embedded accessibility-features video plays and has captions | Desktop, 2026-11-26 | **Verified — no issue observed** | YouTube embed opens in a modal, plays correctly, captions available (CC button) |  — |
| 3 | Consistency across pages and interface elements | Remaining content (tabs, accordions, related posts) matches already-audited patterns | Desktop, 2026-11-26, full scroll | **Verified — no issue observed** | No new component or defect found |  — |
| 4 | Visual hierarchy and content presentation | Transit-mode tab sections (photo + text, two-column layout) are internally consistent | Desktop default width and 1024px, 2026-11-26 | **Finding recorded** | Flagged after this page was already closed; 284px empty gap on one column, 48px column misalignment between the two text rows, measured at both widths | `UX-NITA-020` |

### Communities (`https://nita.illinois.gov/communities`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner renders all its content | Desktop, 2026-11-26, English, Spanish | **Finding recorded** | Confirms `UX-NITA-018` on a 6th page: fits in English, 56px hidden in Spanish | `UX-NITA-018` |
| 2 | Mobile responsiveness and usability | "Local Planning" tabbed section (Community Planning / Access to Transit) usable at tablet width | 768px, 2026-11-26 | **Finding recorded** | Shares the tablet tab-header-scroll defect | `UX-NITA-010` |
| 3 | Consistency across pages and interface elements | Remaining content matches already-audited patterns | Desktop, 2026-11-26, full scroll | **Verified — no issue observed** | Diagonal CTA block, tools/resources block, footer — all already-known patterns |  — |

### Community Planning (`https://nita.illinois.gov/communities/community-planning`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner renders all its content | Desktop, 2026-11-26, English, Spanish | **Verified — no issue observed** | Fits within the fixed-height banner in both languages tested | — |
| 2 | Mobile responsiveness and usability | "2026 Community Planning Program of Projects" table fits the viewport at mobile width | 375×812, 2026-11-26 | **Finding recorded** | Table is clipped by an ancestor `overflow-hidden`, not just page overflow — "Project Description" column (header and every row) cut mid-word with no way to reveal it | `UX-NITA-021` |

### Access to Transit (`https://nita.illinois.gov/communities/access-to-transit-program`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner renders all its content | Desktop, 2026-11-26, English | **Finding recorded** | Confirms `UX-NITA-018` on a 7th page: 100px hidden in English | `UX-NITA-018` |
| 2 | Mobile responsiveness and usability | "2026 NITA Access to Transit Program of Projects" table fits the viewport at mobile width | 375×812, 2026-11-26 | **Finding recorded** | Confirms `UX-NITA-021` on a 2nd table/page: "Applicant" and "County" columns pushed entirely off-screen, unreachable | `UX-NITA-021` |

### 2027 Regional Transit Budget (`https://nita.illinois.gov/transit-funding/2027-regional-transit-budget`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Visual hierarchy and content presentation | Intro banner renders all its content | Desktop, 2026-11-26, English | **Finding recorded** | Confirms `UX-NITA-018` on an 8th page: 12px hidden in English (minor) | `UX-NITA-018` |
| 2 | Mobile responsiveness and usability | Budget tables fit the viewport at mobile width | 375×812, 2026-11-26 | **Verified — no issue observed** | Both tables on this page (327px) fit within the 375px viewport; narrower content than the project-listing tables | — |
| 3 | Calls to action and user engagement opportunities | "Submit a comment" public-comment form: field alignment across languages | Desktop, 430px, 700px, 2026-11-26; English, Spanish | **Verified — no issue observed** | Unlike the footer form (`UX-NITA-016`), this form's fields stack to a single column at narrower widths rather than pairing side by side, so the two-label misalignment pattern does not apply here |  — |

### Other NITA pages/journeys (per `ux-audit-plan.md` sample)

Remaining pages (On Track blog, About NITA, Transparency/FOIA) not yet started.

## mytransitbenefit.com

Not yet started.

## Change log

| Date | Change |
| --- | --- |
| 2026-11-24 | Matrix created. Homepage rows 1, 3, 5, 6 reflect findings already recorded in `nita-illinois-gov.md`; rows 2, 4, 7–11 opened as `Not assessed` to track remaining homepage coverage before moving to other pages. |
| 2026-11-24 | Homepage first pass closed as a full model: added row 2b (RTL layout, finding recorded); closed rows 4, 8, 11 as verified/no-issue or needs-manual-validation; row 7 (mobile) upgraded to finding recorded; row 9 (footer form) marked needs-manual-validation (not submitted — see site report Limitations). Row 2 (remaining languages) and row 10 (readability) remain `Not assessed`. Homepage is not 100% closed, but every control has an explicit status; remaining gaps are intentional and documented, not silent. |
| 2026-11-26 | Riders closed, with the global header and footer (shared by every page) reviewed alongside it: upgraded Riders row 2 to finding recorded (mobile tab-scroll issue, `UX-NITA-010`); added homepage rows 9b-9d for footer icon sizing (`UX-NITA-014`), the Spanish footer translation artifact (`UX-NITA-015`), and footer nav repeating the known "Kolarze" defect (`UX-NITA-003`, no new ID); upgraded row 9 to finding recorded for footer form field misalignment (`UX-NITA-016`). Logo finding `UX-NITA-011` reproduced and range-mapped independently (no longer reviewer-only); priority raised to High alongside `UX-NITA-010`. Next: How to ride (`/riders/how-to-ride`), continuing the partial coverage already recorded below. |
| 2026-11-26 | Access Program, Paying for your ride, Accessible transit, and Communities closed with the spot-check protocol: `UX-NITA-018` confirmed clipping on 3 more pages (worse in Spanish); `UX-NITA-019` added (fare tables overflow at mobile width, found via the new content on Paying for your ride); `UX-NITA-010` confirmed on 2 more tab instances. After Accessible transit was already closed, Fernando flagged a layout gap/misalignment in its Metra tab section, added as `UX-NITA-020`. Next: `/communities/community-planning`. |
| 2026-11-26 | Discounted Fare and Ride Free Programs closed: no new page-specific defects found; confirmed it shares `UX-NITA-010` (tab scroll) and `UX-NITA-017` (footer overflow), and surfaced a new, more serious finding (`UX-NITA-018`, intro banner silently hiding text when longer than its photo) first noticed incidentally here, worse in Spanish than English. Access Program closed with a lighter spot-check protocol (see that page's matrix section) since it reuses only already-audited components; confirmed `UX-NITA-018` again on a 4th page. Next: continuing through the remaining pages, applying the spot-check protocol wherever a page turns out to reuse only known components. |
| 2026-11-26 | How to ride closed: row 2 updated to cover both map dropdowns being unordered, correcting an earlier unverified claim that "Bus Connection Maps" was properly sorted (`UX-NITA-009`); row 4 upgraded to finding recorded, confirming the page's own tab component (CTA Buses/Trains/Metra/Pace) shares `UX-NITA-010`'s tablet scroll defect. Added homepage row 9e for a new footer finding (`UX-NITA-017`, page-wide horizontal overflow at ~768-950px), first noticed incidentally on `/riders/free-and-reduced-fare-programs` and confirmed to reproduce on How to ride and in every language tested. Next: `/riders/free-and-reduced-fare-programs`, already partially explored. |
