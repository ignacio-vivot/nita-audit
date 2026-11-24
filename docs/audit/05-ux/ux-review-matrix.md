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
| 9 | Calls to action and user engagement opportunities | Footer contact form: labels, validation, clarity | Desktop, 2026-11-24: field labels/layout reviewed; not submitted | **Needs manual validation** | Labels present, no visible required-field indicators; submission behavior not testable without sending a real message | — |
| 10 | Content readability and accessibility | Homepage copy readability (non-WCAG aspects: tone, scannability, jargon) | Not yet checked | **Not assessed** | — | — |
| 11 | Consistency across pages and interface elements | Homepage interface patterns (buttons, color use, spacing) match inner pages | Desktop, 2026-11-24: compared with `/riders`, `/riders/paying-for-your-ride` | **Verified — no issue observed** | Header, typography, color palette, and button styling consistent across the three pages checked | — |

### Riders overview (`https://nita.illinois.gov/riders`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User journeys and clarity of key actions | Page surfaces primary rider tasks with clear CTAs | Desktop, 2026-11-24 | **Verified — no issue observed** | Tabbed "How to ride transit" section (Plan your trip / Pay for your ride / Free and discounted fare programs), each with a clear CTA | — |
| 2 | Mobile responsiveness and usability | Tabbed section adapts to phone width | 375×812, 2026-11-24 | **Verified — no issue observed** | Tabs stack as a vertical list, readable, no overlap | — |
| 3 | Visual hierarchy and content presentation | Component handles translated (longer) text without overlap | Spanish, desktop, 2026-11-24 | **Verified — no issue observed** | Tab labels wrap to two lines cleanly; contrasts with the homepage carousel (`UX-NITA-001`) | — |
| 4 | Consistency across pages and interface elements | Cross-links to related programs (e.g., My Transit Benefit) | Desktop, 2026-11-24 | **Verified — no issue observed** | Closing "Transit Benefit for Commuters" section links out appropriately | — |
| 5 | Mobile responsiveness and usability | Tabbed section usable at tablet width (768-978px) | 768, 850, 926, 978px, 2026-11-24; reviewer-reported, reproduced | **Finding recorded** | Tab headers scroll out of view; must scroll up to switch tabs | `UX-NITA-010` |
| 6 | Consistency across pages and interface elements | Header logo renders at consistent size across viewport widths | Reviewer-tested in real Chrome and Firefox windows (not devtools), hard-refreshed, at ~830/1066/1286px; not reproduced in this audit's automated browser at matching widths | **Finding recorded** (reviewer-confirmed; tool discrepancy noted) | Logo renders tiny while desktop nav is already shown | `UX-NITA-011` |
| 7 | Content readability and accessibility | Automatic language detection/switching behavior | Reviewer-reported, 2026-11-24 | **Finding recorded** | Page auto-translated to Tagalog without visitor selection | `UX-NITA-012` |

### How to ride (`https://nita.illinois.gov/riders/how-to-ride`)

| # | Proposal area | Control / question | Scope and method | Status | Evidence / notes | Related findings |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User journeys and clarity of key actions | Trip Planner tool completes its task without unexpected behavior | Desktop, 2026-11-24: filled and submitted with test addresses | **Finding recorded** | Silently navigates to Google Maps in the same tab, no warning | `UX-NITA-008` |
| 2 | Navigation structure and information architecture | Map/resource selector dropdowns are easy to scan | Desktop, 2026-11-24 | **Finding recorded** | "Neighborhood Maps" dropdown (20+ items) has no discernible order | `UX-NITA-009` |
| 3 | Mobile responsiveness and usability | Trip Planner and tabbed sections adapt to phone width | 375×812, 2026-11-24 | **Verified — no issue observed** | Fields and tabs stack cleanly, full-width, readable | — |
| 4 | Consistency across pages and interface elements | Tabbed "How to ride" (CTA Buses/Trains, Metra, Pace) component matches the pattern seen on `/riders` | Desktop, 2026-11-24 | **Verified — no issue observed** | Same tab pattern reused consistently | — |

### Other NITA pages/journeys (per `ux-audit-plan.md` sample)

Remaining pages in this round's batch (Access Program/Discounted Fare, Communities, On Track blog, About NITA, Transparency/FOIA) not yet started.

## mytransitbenefit.com

Not yet started.

## Change log

| Date | Change |
| --- | --- |
| 2026-11-24 | Matrix created. Homepage rows 1, 3, 5, 6 reflect findings already recorded in `nita-illinois-gov.md`; rows 2, 4, 7–11 opened as `Not assessed` to track remaining homepage coverage before moving to other pages. |
| 2026-11-24 | Homepage first pass closed as a full model: added row 2b (RTL layout, finding recorded); closed rows 4, 8, 11 as verified/no-issue or needs-manual-validation; row 7 (mobile) upgraded to finding recorded; row 9 (footer form) marked needs-manual-validation (not submitted — see site report Limitations). Row 2 (remaining languages) and row 10 (readability) remain `Not assessed`. Homepage is not 100% closed, but every control has an explicit status; remaining gaps are intentional and documented, not silent.
