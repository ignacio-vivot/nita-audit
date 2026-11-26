# Working in this repository

This is the NITA website audit project (nita.illinois.gov and mytransitbenefit.com) for DHD Marketing. Before writing or editing anything, read, in this order:

1. [`README.md`](README.md) — project goals, folder structure, finding template, workflow.
2. [`docs/project-overview.md`](docs/project-overview.md) — scope, methodology, deliverables, timeline.
3. [`docs/audit/authoring-guide.md`](docs/audit/authoring-guide.md) — writing style, section structure, finding format (including Finding ID), priority/complexity definitions, and the review checklist. Follow this guide exactly when creating or editing any file under `docs/audit/`.
4. **Before working on a specific audit section** (`01-accessibility-ada`, `02-seo`, `03-aeo`, `04-geo`, `05-ux`), check that section's own folder for a `*-audit-plan.md` (e.g. [`docs/audit/05-ux/ux-audit-plan.md`](docs/audit/05-ux/ux-audit-plan.md)) and a `*-review-matrix.md`, and read them if present. These hold the section's confirmed scope, page/journey sample, methodology, and current progress — treat them as the source of truth for "how many pages" and "what's left," not an assumption made from scratch. If a section has no plan file yet, say so rather than inventing a scope.

## Rules

- Deliverables and generated files (everything under `docs/audit/`) are written in **English**. Conversation with the user can be in Spanish.
- Every finding must follow the format in `authoring-guide.md`, including a stable `Finding ID` (`[SECTION]-[SITE]-[NUMBER]`, e.g. `UX-NITA-001`, `SEO-MTB-003`).
- Treat `evidence/crawls/screaming-frog/**` as read-only raw data snapshots. Never edit or regenerate these files; only read them as evidence for findings.
- Do not claim legal non-compliance, guaranteed ranking changes, or guaranteed AI citations — describe evidence and risk instead (see authoring-guide, section 1).
