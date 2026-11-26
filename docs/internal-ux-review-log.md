# UX audit — internal review log (not for client delivery)

Tracks who found each UX finding and how, for the team's own reference. This file is **not** part of the client deliverable — everything under `docs/audit/` is the deliverable tree (see `CLAUDE.md`); this file lives outside it on purpose. Findings in the delivered reports describe only the evidence and verification method, never who on the team found it.

| Finding ID | Found by | Notes |
| --- | --- | --- |
| UX-NITA-001 | Claude | Homepage hero carousel, automated pass |
| UX-NITA-002 | Claude | Homepage hero carousel, automated pass |
| UX-NITA-003 | Claude | Homepage nav translation, automated pass |
| UX-NITA-004 | Claude | Homepage body, automated pass |
| UX-NITA-005 | Claude | Nav audience weighting, automated pass |
| UX-NITA-006 | Claude | Homepage RTL, automated pass |
| UX-NITA-007 | Claude | Homepage mobile menu, automated pass |
| UX-NITA-008 | Claude | How to ride — Trip Planner, automated pass |
| UX-NITA-009 | Claude | How to ride — Neighborhood Maps dropdown, automated pass |
| UX-NITA-010 | Fernando | Tabbed section at tablet width — found manually, Claude reproduced after |
| UX-NITA-011 | Fernando | Logo tiny at intermediate widths — confirmed manually in real Chrome/Firefox; Claude's automated tool could not reproduce it |
| UX-NITA-012 | Fernando | Auto-translation via browser language (Tagalog) — found manually |
| UX-NITA-013 | Fernando | Button hover state missing — confirmed manually, resolving an earlier inconclusive automated check |
| UX-NITA-014 | Fernando | Footer phone icon size inconsistency — flagged manually; Claude measured and confirmed via DOM |
| UX-NITA-015 | Fernando | Footer duplicate-comma text artifact in Spanish — flagged manually; Claude reproduced and traced to source `<br>` split |
| UX-NITA-016 | Fernando | Footer form Email/Home Phone field misalignment — flagged manually at 768px in Polish/Tagalog in a real browser; Claude's first attempt (at 756/974px) failed to reproduce it, then confirmed and measured at the exact width Fernando reported |
| UX-NITA-017 | Fernando | Footer page-wide horizontal overflow at ~768-950px — spotted incidentally in Tagalog/Polish while browsing outside the current review batch (`/riders/free-and-reduced-fare-programs`); Claude confirmed it also happens in English and mapped the exact width range |
| UX-NITA-018 | Fernando | Intro banner hiding "Travel Assistance Digital Library" text on `/riders/free-and-reduced-fare-programs` — spotted incidentally in the same browsing session; Claude traced it to a fixed-height `overflow:hidden` container and confirmed the same component exists (non-clipping) on `/riders` |
| UX-NITA-019 | Claude, confirmed by Fernando | Fare comparison tables overflowing at mobile width on `/riders/paying-for-your-ride` — found during the lighter spot-check pass after Fernando noted the page looked similar to others; Fernando independently confirmed the table overflowing its box after being pointed to it |
| UX-NITA-020 | Fernando | Gap and column misalignment in the Metra tab section on `/riders/accessible-transit` — flagged manually with a screenshot after the page was already closed; Claude measured it precisely via the DOM at two widths (default and 1024px) |
| UX-NITA-021 | Claude, confirmed by Fernando | Projects table silently clipped at mobile width on `/communities/community-planning` (confirmed again on `/communities/access-to-transit-program`) — found during the lighter spot-check pass; Fernando independently confirmed seeing the same clipped-with-no-scroll table; a new, more severe variant of the already-known fare-table overflow (`UX-NITA-019`) |
