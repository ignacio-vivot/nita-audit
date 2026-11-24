# User Experience (UX) — nita.illinois.gov

## Assessment Scope

- **Website:** nita.illinois.gov
- **Review date:** 2026-11-24 (in progress)
- **Pages, templates, or journeys reviewed:** Homepage, reviewed in depth as a full first-pass model (desktop, iPad Pro 13 tablet viewport, and 375×812 mobile viewport); two inner pages (`/riders`, `/riders/paying-for-your-ride`) spot-checked for cross-page consistency. See the [UX review matrix](ux-review-matrix.md) for row-by-row coverage. Full representative sample ([SEO review matrix](../02-seo/seo-review-matrix.md)) still to be walked per [`ux-audit-plan.md`](ux-audit-plan.md).
- **Methods and tools:** Manual heuristic walkthrough (Nielsen's 10 usability heuristics) in a desktop browser, at the iPad Pro 13 viewport (1032×1376), and at a 375×812 mobile viewport (Chrome DevTools device emulation); manual language-switcher testing across English, Spanish, Polish, Arabic, and Urdu, including an `document.documentElement.dir`/`lang` console check; manual hover-state check on primary navigation and buttons; footer contact form reviewed for field labeling only (not submitted — see Limitations).

## Summary

_Draft — audit in progress, homepage pass complete._ The homepage review surfaced two groups of issues. First, a set of localization defects: the hero carousel overlaps itself once translated into Spanish or Polish, its first slide is not translated at all, a core navigation term is mistranslated into Polish, and Arabic/Urdu are translated but the layout is never mirrored to right-to-left. Second, a smaller set of structural/navigation issues: the homepage body offers no visible path to key tasks beyond a single dropdown, the primary navigation is organized by internal department rather than user task, and the mobile menu panel does not cover the full screen. A spot-check of two inner pages (`/riders`, `/riders/paying-for-your-ride`) found consistent header, typography, and button styling with the homepage, and `/riders` already contains a task-oriented tabbed section that the homepage lacks (see `UX-NITA-004`). See [`weglot-check.txt`](../../../evidence/public-technical/2026-11-24/rendered-review/weglot-check.txt) (SEO section) for the underlying translation mechanism (Weglot, client-side, no per-language URLs or hreflang).

## Findings

Ordered by priority, then by user or business impact. **Scope** marks whether a finding is **Site-wide** (a shared component — header, navigation, footer, translation, language switcher — observed on one page but applying everywhere it appears), **Component** (shared by some, not all, pages — e.g., a tabbed section reused on two pages), or **Page** (unique to the content/component of one specific page). Before filing a new finding on a newly-reviewed page, check whether a Site-wide finding below already covers it; if so, add that page as supporting evidence to the existing ID rather than creating a new one.

### Findings at a glance

| ID | Finding | Priority | Scope |
| --- | --- | --- | --- |
| [`UX-NITA-001`](#hero-carousel-text-overlaps-itself-and-on-page-controls-in-translated-languages) | Hero carousel text overlaps itself and on-page controls in translated languages | High | Page (homepage hero) |
| [`UX-NITA-006`](#right-to-left-languages-arabic-urdu-are-translated-but-the-layout-is-not-mirrored) | Right-to-left languages (Arabic, Urdu) are translated but the layout is not mirrored | High | Site-wide |
| [`UX-NITA-002`](#first-hero-slide-is-not-translated-by-the-sites-translation-tool) | First hero slide is not translated by the site's translation tool | Medium | Page (homepage hero) |
| [`UX-NITA-003`](#automated-translation-mistranslates-riders-in-polish-navigation) | Automated translation mistranslates "Riders" in Polish navigation | Medium | Site-wide |
| [`UX-NITA-004`](#homepage-body-offers-no-visible-path-to-key-tasks-below-the-hero) | Homepage body offers no visible path to key tasks below the hero | Medium | Page (homepage) |
| [`UX-NITA-007`](#mobile-navigation-menu-does-not-cover-the-full-screen) | Mobile navigation menu does not cover the full screen | Medium | Site-wide |
| [`UX-NITA-008`](#trip-planner-silently-redirects-to-google-maps-with-no-warning) | Trip Planner silently redirects to Google Maps with no warning | Medium | Page (How to ride) |
| [`UX-NITA-009`](#neighborhood-maps-dropdown-lists-20-options-in-no-discernible-order) | "Neighborhood Maps" dropdown lists 20+ options in no discernible order | Medium | Page (How to ride) |
| [`UX-NITA-010`](#tabbed-sections-are-hard-to-use-at-tablet-width-because-switching-tabs-requires-repeated-scrolling) | Tabbed sections are hard to use at tablet width because switching tabs requires repeated scrolling | Medium | Component (Riders, How to ride) |
| [`UX-NITA-011`](#logo-renders-at-a-tiny-size-across-a-wide-range-of-intermediate-viewport-widths) | Logo renders at a tiny size across a wide range of intermediate viewport widths | Medium | Site-wide |
| [`UX-NITA-013`](#buttons-give-no-visible-hover-feedback-on-desktop-unlike-navigation-links) | Buttons give no visible hover feedback on desktop, unlike navigation links | Medium | Site-wide |
| [`UX-NITA-005`](#riders-the-largest-and-most-frequent-audience-has-no-more-visual-weight-than-smaller-institutional-audiences) | Riders, the largest and most frequent audience, has no more visual weight than smaller institutional audiences | Low | Site-wide |
| [`UX-NITA-012`](#site-auto-translates-based-on-browser-language-without-the-visitor-choosing-it) | Site auto-translates based on browser language without the visitor choosing it | Low | Site-wide |

### Hero carousel text overlaps itself and on-page controls in translated languages

- **Finding ID:** UX-NITA-001
- **Page or component:** Homepage (`https://nita.illinois.gov/`) hero carousel component, slide 2 ("Weigh in on NITA's draft regional budget")
- **Priority:** High
- **Evidence:** Observed 2026-11-24 with the language switcher set to Spanish and Polish. In both languages, the translated heading/body text is longer than the English source and overlaps itself within the slide; the "Learn more"/"Dowiedz się więcej" button and the slide-position indicator dots overlap below the text. Reproduced at desktop width and at the iPad Pro 13 viewport (1032×1376, Chrome DevTools device emulation), so it is not limited to one breakpoint. Screenshots: [`homepage-polish-slide2-cta-overlap.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-polish-slide2-cta-overlap.png), [`homepage-spanish-slide2-text-overlap.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-spanish-slide2-text-overlap.png), [`homepage-spanish-ipad-pro-1032x1376-text-overlap.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-spanish-ipad-pro-1032x1376-text-overlap.png).
- **Impact:** Spanish- and Polish-speaking visitors — plausibly also speakers of the site's other five supported languages, given this is a shared, fixed-dimension carousel component — see a visibly broken, hard-to-read homepage hero immediately after selecting their language, including the page's most prominent call to action. This undermines usability and trust precisely for the audience the multilingual option exists to serve, and it affects the first content block every homepage visitor in these languages encounters.
- **Recommendation:** Rebuild the carousel slide layout to size itself to its content (flexible height, no fixed/absolute-positioned text block) so translated strings can wrap without overlapping the heading, body, button, or the slide-position indicator. Test the fix in every language offered by the switcher and at common breakpoints, including tablet, before publishing.
- **Implementation complexity:** Medium

### Right-to-left languages (Arabic, Urdu) are translated but the layout is not mirrored

- **Finding ID:** UX-NITA-006
- **Page or component:** Homepage (`https://nita.illinois.gov/`) and, by inference, every page (language switcher is global)
- **Priority:** High
- **Evidence:** Observed 2026-11-24. Selecting Arabic or Urdu translates the visible text (`<html lang="ar">` / `lang="ur"` confirmed via console check), but `document.documentElement.dir` is empty in both cases, and the rendered layout stays left-to-right: hero image on the right, text block on the left, "Quick Links" label and carousel indicator dots left-aligned, utility links (Careers/Contact) right-aligned only because that was already their English position. Screenshots: [`homepage-arabic-rtl-not-applied.jpg`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-arabic-rtl-not-applied.jpg), [`homepage-urdu-rtl-not-applied.jpg`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-urdu-rtl-not-applied.jpg).
- **Impact:** Arabic and Urdu readers get translated words arranged in a left-to-right structure built for English, which is disorienting to read and scan (reading order, image/text relationship, and control positions all fight the script's natural direction). This affects the entire page, not one component, for two of the seven languages the site offers.
- **Recommendation:** Set `dir="rtl"` on `<html>` (and apply the site's existing RTL stylesheet support, or add one) when Arabic or Urdu is active, so layout direction, text alignment, and element order mirror correctly, not just the words.
- **Implementation complexity:** Medium

### First hero slide is not translated by the site's translation tool

- **Finding ID:** UX-NITA-002
- **Page or component:** Homepage (`https://nita.illinois.gov/`) hero carousel, slide 1 ("NITA Ride Safe App Launches")
- **Priority:** Medium
- **Evidence:** Observed 2026-11-24 with the language switcher set to Polish (and reproduced in Arabic and Urdu). Global navigation and the slide's own button are translated, but the slide heading ("NITA Ride Safe App Launches") and body copy ("See something unsafe? Report it discreetly...") remain in English in every language tested. Screenshot: [`homepage-polish-slide1-untranslated.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-polish-slide1-untranslated.png). The site's translation layer is Weglot, a client-side DOM scan with no per-language URLs or hreflang (see [`weglot-check.txt`](../../../evidence/public-technical/2026-11-24/rendered-review/weglot-check.txt)); slide 1's content is likely rendered in a way Weglot's scan does not reach.
- **Impact:** Non-English-speaking visitors land on a page where the single most prominent message contradicts the language they just chose, forcing them to parse English for the page's lead content and signaling the translation is incomplete or unmaintained.
- **Recommendation:** Confirm why slide 1's heading/body are excluded from the Weglot translation pass (timing of render, markup structure, or explicit exclusion) and bring it into the same translation pipeline as the rest of the homepage and the other carousel slides.
- **Implementation complexity:** Medium

### Automated translation mistranslates "Riders" in Polish navigation

- **Finding ID:** UX-NITA-003
- **Page or component:** Global navigation, all pages (observed on homepage, `https://nita.illinois.gov/`)
- **Priority:** Medium
- **Evidence:** Observed 2026-11-24 with the language switcher set to Polish: the "Riders" navigation item is rendered as "Kolarze", which translates to "cyclists"/"racers" in Polish, not transit riders. Screenshot: [`homepage-polish-slide1-untranslated.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-polish-slide1-untranslated.png) (top navigation).
- **Impact:** Polish-speaking visitors see a top-level navigation label that describes a different audience (cyclists) than the intended one (transit riders), which can cause them to skip the section most relevant to them. It also demonstrates that core navigation terms are not being reviewed after automatic machine translation, which may affect other terms or languages not yet spot-checked.
- **Recommendation:** Add a manual translation override in Weglot (or the applicable glossary/exception mechanism) for "Riders" in Polish, and spot-check other top-level navigation labels across all seven supported languages for similar mistranslations.
- **Implementation complexity:** Low

### Homepage body offers no visible path to key tasks below the hero

- **Finding ID:** UX-NITA-004
- **Page or component:** Homepage (`https://nita.illinois.gov/`), body content below the hero carousel
- **Priority:** Medium
- **Evidence:** Observed 2026-11-24, desktop viewport. Below the hero carousel, the only body content before the footer is a single generic "Quick Links" control (label: "I would like to get more information about:" / a "Select an option" dropdown with four destinations). There are no visible cards, sections, or shortcuts surfacing the site's core tasks (e.g., how to ride, pay for a ride, apply for a fare program); those paths exist only inside the collapsed hamburger menu. By contrast, `/riders` already has a "How to ride transit" tabbed section (Plan your trip / Pay for your ride / Free and discounted fare programs) that is exactly this kind of task-oriented entry point — it simply is not surfaced on the homepage. Screenshot: [`homepage-body-only-quick-links-dropdown.jpg`](../../../evidence/ux/nita-illinois-gov/2026-11-24/homepage-body-only-quick-links-dropdown.jpg).
- **Impact:** First-time visitors arriving at the homepage have to open and explore the main menu to discover any of the site's primary tasks — nothing on the visible page itself orients them toward "how to ride," "pay for a ride," or similar high-frequency rider needs. This adds an avoidable step (recognition vs. recall) for exactly the audience the homepage should orient fastest.
- **Recommendation:** Add a homepage section with a small number of task- or audience-oriented entry points (for example: Riders, Communities, Pay for your ride) visible without opening the menu. The `/riders` "How to ride transit" tabbed section is a ready-made pattern that could be reused or adapted for the homepage, lowering the effort versus a new design. Separately, for the site's more complex, multi-step eligibility journeys specifically (for example the Access fare program or ADA Paratransit certification, where `SEO-NITA` findings already note confusion between "Access" and "Access to Transit"), consider a guided step-by-step tool (a short wizard asking a few qualifying questions and routing to the right program/next step) as a higher-effort, longer-term option rather than a general homepage feature.
- **Implementation complexity:** Low to Medium (reusing the existing `/riders` pattern); High (guided eligibility tool, if pursued)

### Mobile navigation menu does not cover the full screen

- **Finding ID:** UX-NITA-007
- **Page or component:** Homepage (`https://nita.illinois.gov/`) mobile navigation (hamburger menu), 375×812 viewport
- **Priority:** Medium
- **Evidence:** Observed 2026-11-24 at 375×812 (Chrome DevTools mobile emulation). Opening the hamburger menu shows a full navigation panel, but it stops short of the viewport's bottom: the homepage content behind it (carousel indicator dots and the start of "Quick Links") is visible in the gap below the "Careers / Contact" utility links. Screenshot: [`mobile-menu-overlay-gap-375px.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/mobile-menu-overlay-gap-375px.png).
- **Impact:** Mobile visitors opening the main menu see page content bleeding in underneath it, which reads as a layout bug and can make the menu feel incomplete or broken, even though every menu item is actually present and reachable.
- **Recommendation:** Make the mobile menu panel cover the full viewport height (or extend its background to the bottom of the screen) regardless of how much menu content it contains.
- **Implementation complexity:** Low

### Trip Planner silently redirects to Google Maps with no warning

- **Finding ID:** UX-NITA-008
- **Page or component:** `https://nita.illinois.gov/riders/how-to-ride`, "Trip Planner" tool
- **Priority:** Medium
- **Evidence:** Observed 2026-11-24. Filled Starting Location and Destination and clicked "Submit"; the page navigated, in the same tab, entirely away from nita.illinois.gov to `google.com/maps` with the entered addresses as query parameters. Confirmed via the page's own markup that the form's `action` is `https://www.google.com/maps` (GET). Nothing near the form or the "Submit" button indicates beforehand that this leaves the NITA site. Screenshot: [`how-to-ride-trip-planner-google-maps-redirect.jpg`](../../../evidence/ux/nita-illinois-gov/2026-11-24/how-to-ride-trip-planner-google-maps-redirect.jpg).
- **Impact:** Visitors performing the single most essential rider task (planning a trip) are taken off the NITA site without warning and without the result opening in a new tab, losing on-page context (fare information, Day Pass purchase links, accessibility notes) and having no obvious way back except the browser's back button.
- **Recommendation:** Open the Google Maps result in a new tab, and/or add a brief note or icon near the Trip Planner indicating it will use Google Maps for directions.
- **Implementation complexity:** Low

### "Neighborhood Maps" dropdown lists 20+ options in no discernible order

- **Finding ID:** UX-NITA-009
- **Page or component:** `https://nita.illinois.gov/riders/how-to-ride`, "Neighborhood Maps" selector
- **Priority:** Medium
- **Evidence:** Observed 2026-11-24. The dropdown lists over 20 neighborhood map options (e.g., "35th Lou Jones," "79th Chatham," "103rd Rosemoor," "Cicero," "Gresham," "Healy," "Homewood," "Peterson Ridge," "Western Avenue," "Wheaton," "Waukegan," "Oak Park," "Northbrook," "Naperville," "Mayfair," "Lisle," "Lake Cook," "Joliet," "Jefferson Park") with no visible alphabetical, geographic, or other logical ordering. Screenshot: [`how-to-ride-neighborhood-maps-dropdown-unordered.jpg`](../../../evidence/ux/nita-illinois-gov/2026-11-24/how-to-ride-neighborhood-maps-dropdown-unordered.jpg).
- **Impact:** A rider looking for their own neighborhood's map has to read through the entire unsorted list rather than jumping to it, adding unnecessary effort to what should be a quick lookup.
- **Recommendation:** Sort the list alphabetically (or group it geographically, e.g., by county or direction from the city), consistent with the equivalent "Bus Connection Maps" selector.
- **Implementation complexity:** Low

### Tabbed sections are hard to use at tablet width because switching tabs requires repeated scrolling

- **Finding ID:** UX-NITA-010
- **Page or component:** `https://nita.illinois.gov/riders` and `https://nita.illinois.gov/riders/how-to-ride`, "How to ride transit" tabbed sections
- **Priority:** Medium
- **Evidence:** Observed 2026-11-24 at 768×851 (tablet width). At this breakpoint, the layout under each tab stacks a tall image above its text/CTA (unlike the desktop side-by-side layout), making each tab panel much taller than the viewport. Clicking a different tab (e.g., "Pay for your ride") works correctly, but after scrolling down to read that tab's content, the tab headers scroll out of view; switching tabs again requires scrolling back up first. The user independently found and reported this behavior; reproduced directly in a second, separate check. Screenshot: [`riders-tablet-768px-tab-headers-scrolled-out.jpg`](../../../evidence/ux/nita-illinois-gov/2026-11-24/riders-tablet-768px-tab-headers-scrolled-out.jpg) (tab headers no longer visible after scrolling to the tab's content).
- **Impact:** Tablet visitors comparing the three rider options (Plan your trip / Pay for your ride / Free and discounted fare programs) cannot see the tab headers and the content at the same time, and must repeatedly scroll up and down to explore more than one tab — noticeably more friction than either the desktop (side-by-side) or mobile (simple vertical list) versions of the same component.
- **Recommendation:** At tablet widths, either keep the tab headers sticky/visible while their content scrolls, or switch to the mobile-style stacked list pattern earlier (at a wider breakpoint) so tablet visitors get the simpler layout instead of an oversized version of the desktop one.
- **Implementation complexity:** Medium

### Logo renders at a tiny size across a wide range of intermediate viewport widths

- **Finding ID:** UX-NITA-011
- **Page or component:** Global header logo, all pages (observed on `https://nita.illinois.gov/riders`)
- **Priority:** Medium
- **Evidence:** Reported by the reviewer (Fernando) and confirmed across real browser windows (not devtools emulation), after hard refresh, at three widths: ~830px, 1066px (Firefox), and 1286px (Chrome) — the "NITA" logo renders as a tiny icon-sized mark instead of its normal wordmark size, while the full desktop navigation (Region, Communities, Riders, Public Safety, Funding, News, About NITA, Search) is already displayed in its non-mobile form at the same widths. Not reproduced in this audit's automated browser tool at the same exact widths (768, 850, 926, 978, 1286, 1556px) on fresh loads — the discrepancy itself is notable and the manual, cross-browser confirmation is treated as the reliable signal here. The reviewer's DOM inspection shows Tailwind CSS utility classes (e.g., `bg-nitadarkblue-500`, `lg:block`), consistent with the project's known tech stack. Screenshots: [`riders-logo-tiny-1286px-chrome.webp`](../../../evidence/ux/nita-illinois-gov/2026-11-24/riders-logo-tiny-1286px-chrome.webp), [`riders-logo-tiny-tagalog-chrome.webp`](../../../evidence/ux/nita-illinois-gov/2026-11-24/riders-logo-tiny-tagalog-chrome.webp), [`riders-logo-tiny-english-chrome-narrow.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/riders-logo-tiny-english-chrome-narrow.png), [`riders-logo-tiny-1066px-firefox-inspector.png`](../../../evidence/ux/nita-illinois-gov/2026-11-24/riders-logo-tiny-1066px-firefox-inspector.png) (Firefox, with DOM inspector open showing Tailwind classes).
- **Impact:** Across a wide, real-world range of laptop/desktop window widths, the NITA brand mark is visually undersized next to a full desktop navigation bar, undermining visual hierarchy and brand presence precisely on the header that appears on every page.
- **Recommendation:** Developers should compare the responsive breakpoint controlling the logo's size classes against the breakpoint controlling the mobile-to-desktop navigation switch; they are likely misaligned (the nav switches to desktop form at a narrower width than the logo switches to full size), producing an intermediate range with a full nav bar and an undersized logo. Align both to the same breakpoint.
- **Implementation complexity:** Low

### Site auto-translates based on browser language without the visitor choosing it

- **Finding ID:** UX-NITA-012
- **Page or component:** Global translation behavior, all pages (observed on `https://nita.illinois.gov/riders`)
- **Priority:** Low
- **Evidence:** Observed 2026-11-24, reported by the reviewer: visiting the site in a browser configured for Tagalog loaded the page automatically translated to Tagalog ("Mga Rider," "Rehiyon," "Mga Komunidad") without the visitor selecting a language from the switcher. Screenshot: [`riders-logo-tiny-tagalog-chrome.webp`](../../../evidence/ux/nita-illinois-gov/2026-11-24/riders-logo-tiny-tagalog-chrome.webp).
- **Impact:** A visitor whose browser is configured for a non-English language is switched away from English automatically. Combined with the untranslated-content and layout gaps already found in `UX-NITA-001`, `002`, and `006`, an automatic switch into an incompletely-translated experience may be more disorienting than if the visitor had opted in deliberately via the visible language switcher.
- **Recommendation:** Confirm whether automatic language detection is an intended feature; if kept, ensure the automatically-selected language gets the same translation coverage as a manually-selected one (see `UX-NITA-002`), and consider showing a dismissible notice ("We've translated this page to Tagalog — switch back to English") so the change is not silent.
- **Implementation complexity:** Low

### Buttons give no visible hover feedback on desktop, unlike navigation links

- **Finding ID:** UX-NITA-013
- **Page or component:** Buttons site-wide (e.g., "Learn more," "Submit," "Apply now"), observed on the homepage and `/riders`
- **Priority:** Medium
- **Evidence:** Reported by the reviewer and confirmed manually in a real desktop browser, 2026-11-24: primary navigation links show a clear color change on hover, but buttons show no visible hover state at all. This matches an earlier inconclusive check in this audit (see prior Limitations note) using the automated browser tool, which could not reliably trigger CSS `:hover`; the reviewer's manual confirmation in a real browser resolves that uncertainty.
- **Impact:** On desktop, where hover is a meaningful signal, a visitor gets no visual confirmation that a button is interactive until they click it, while nearby nav links do give that signal — an inconsistent, if minor, cue about what responds to the mouse. Not applicable to mobile/touch, which has no true hover state.
- **Recommendation:** Add a hover state to buttons (e.g., a background or border color shift) consistent with the existing link hover treatment, scoped to desktop/pointer input.
- **Implementation complexity:** Low

### Riders, the largest and most frequent audience, has no more visual weight than smaller institutional audiences

- **Finding ID:** UX-NITA-005
- **Page or component:** Global primary navigation and homepage, all pages (observed on homepage, `https://nita.illinois.gov/`)
- **Priority:** Low
- **Evidence:** NITA's site is confirmed, from three independent sources, to intentionally serve several distinct audiences rather than a single one: the project's own [transit system context note](../../transit-system-context.md) ("NITA's site serves the broader regional public, riders, municipalities, and transit partners"); the SEO section's [review matrix](../02-seo/seo-review-matrix.md) ("the public global navigation separates Region, Communities, Riders, Transit Funding, News, and About NITA, so the website serves several audiences and intents," also noting that of the 1,613 crawled pages, core sections total fewer than 100 — most volume is blog/press-release content, not distinct structural audiences); and the AEO section's [question inventory](../03-aeo/aeo-audit-plan.md), independently grouped by riders, local governments, the public (budget/board/public comment), employers, and employees. The homepage's own "Quick Links" dropdown (see `UX-NITA-004`) reinforces this: its four author-chosen destinations are About NITA (institutional identity), Careers (employment), How to ride (riders), and Meeting Materials (civic governance) — a de facto summary of the same multi-audience map, chosen by the site's own content owners. Given this, a department-style navigation (Region, Communities, Riders, Public Safety, Funding, News, About NITA) is a defensible structure for a public authority with legal obligations (transparency, public comment periods, bondholder/investor relations) toward multiple constituencies — it is not simply disorganized. However, all seven categories currently carry equal visual weight, even though Riders is by far the largest and most frequent audience (a transactional, high-frequency need), while sections like About NITA serve smaller, lower-frequency audiences (governance, compliance, investors, vendors).
- **Impact:** A rider looking for fare or trip-planning information has no stronger visual cue to start at "Riders" than at any of the other six, equally weighted categories serving smaller or less frequent audiences — adding friction to the site's single highest-volume task, even though the overall multi-audience structure is itself reasonable.
- **Recommendation:** Keep the multi-audience navigation structure (it reflects real, distinct constituencies NITA is obligated to serve), but give the highest-frequency audience/task (Riders) more visual prominence — for example through placement, a distinct style, or a dedicated homepage entry point (see `UX-NITA-004`) — without restructuring the full navigation or deprioritizing the institutional/compliance sections.
- **Implementation complexity:** Medium

## Positive Observations

- The language switcher offers seven real, distinct languages (Spanish, Polish, Arabic, Chinese (Simplified), Tagalog, Urdu, Gujarati) in addition to English — a strong fit for the Chicago region's rider demographics. This makes the defects in `UX-NITA-001`, `002`, `003`, and `006` more consequential: the intent to serve these audiences is right, but execution gaps undermine it.
- Header, typography, color palette, and button styling are consistent between the homepage and the two inner pages spot-checked (`/riders`, `/riders/paying-for-your-ride`); hovering primary navigation links produces clear visual feedback (link color change).
- `/riders` already has a task-oriented "How to ride transit" tabbed section that models the kind of homepage entry point recommended in `UX-NITA-004` — a reusable pattern, not something to design from scratch.
- The hero carousel does not autoplay (confirmed by waiting 8 seconds with no change) and advances correctly via manual click on the indicator dots, so it does not create a "can't stop it" control problem.
- `/riders` (reviewed 2026-11-24) is a strong model of task-oriented design: a tabbed "How to ride transit" section (Plan your trip / Pay for your ride / Free and discounted fare programs) with clear CTAs ("Find the cost of your trip"), consistent heading/body/image pattern per section, and a closing cross-link to My Transit Benefit. It adapts cleanly to mobile (tabs stack as a vertical list) and to Spanish (tab labels wrap to two lines without breaking layout), confirming the carousel overlap bug (`UX-NITA-001`) is isolated to the homepage hero component rather than a site-wide pattern.

## Limitations

- Audit in progress — most of the agreed page/journey sample (see [`ux-audit-plan.md`](ux-audit-plan.md)) has not yet been reviewed; this file reflects a complete first-pass review of the homepage plus a light spot-check of two inner pages.
- The footer contact form was reviewed for field labeling and layout only. Submission behavior (validation messages, confirmation state) was **not verifiable in this audit**: submitting it would send a real, unwanted message to NITA, which is outside the audit's intent.
- Button hover-state feedback was initially inconclusive with the automated browser tool used for this review; resolved by the reviewer's manual confirmation in a real browser (see `UX-NITA-013`).
- Chinese (Simplified), Tagalog, and Gujarati were not individually checked for the carousel-overlap or mistranslation patterns found in Spanish, Polish, Arabic, and Urdu; given the shared component and translation mechanism, the same issues are plausible but **not confirmed** in those three languages.
- This audit's automated browser tool did not reproduce two issues the reviewer found and confirmed manually in real Chrome and Firefox windows (`UX-NITA-011`, the undersized logo; and an earlier devtools-only false lead involving a header utility-bar clipping artifact, correctly ruled out as not a site defect). The discrepancy is noted rather than resolved; it underscores that manual, cross-browser spot checks remain necessary alongside the automated pass, and other viewport-dependent issues may exist that neither method alone would catch.
