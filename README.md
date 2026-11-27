# NITA Website Audit

Independent audit of NITA's public digital platforms for DHD Marketing. The audit covers **nita.illinois.gov** and **mytransitbenefit.com** across accessibility, SEO, AEO, GEO, and user experience.

> **Working language:** All project deliverables and generated files are written in English. Team discussion may be in Spanish.

## Project goals

- Identify and document evidence-based findings across both websites.
- Assess accessibility against WCAG 2.1 Level AA and identify potential ADA Title II risks. This audit is not a legal certification.
- Review SEO, answer-engine readiness (AEO), generative-engine readiness (GEO), and user experience (UX).
- Prioritize practical recommendations and prepare an action plan.
- Produce a final PDF report after the Markdown audit content is complete and reviewed.

## Scope and method

The review combines automated checks with manual evaluation of representative pages, templates, and user journeys. The initial assessment uses publicly available pages and resources; CMS, source-code, and server access are outside the initial scope.

The five audit sections are:

1. Accessibility & ADA
2. Search Engine Optimization (SEO)
3. Answer Engine Optimization (AEO)
4. Generative Engine Optimization (GEO)
5. User Experience (UX)

Findings should include the affected website and page, supporting evidence, impact/severity, and a practical recommendation. Use the priorities **Critical**, **High**, **Medium**, and **Low**, and estimate implementation complexity as **Low**, **Medium**, or **High** where applicable.

## Recommended documentation structure

Organize the audit **by section, with a separate subsection or file for each website**. This keeps the evaluation criteria together, makes cross-site comparison easier, and supports later prioritization across both sites. Always label each finding with its website. Keep the executive summary and consolidated action plan cross-site.

```text
.
├── README.md
├── docs/
│   ├── project-overview.md
│   └── audit/
│       ├── 00-executive-summary.md
│       ├── 01-accessibility-ada/
│       │   ├── accessibility-audit-plan.md
│       │   ├── accessibility-review-matrix.md
│       │   ├── nita-illinois-gov.md
│       │   └── mytransitbenefit-com.md
│       ├── 02-seo/
│       │   ├── seo-audit-plan.md
│       │   ├── seo-review-matrix.md
│       │   ├── nita-illinois-gov.md
│       │   └── mytransitbenefit-com.md
│       ├── 03-aeo/
│       │   ├── aeo-audit-plan.md
│       │   ├── aeo-review-matrix.md
│       │   ├── nita-illinois-gov.md
│       │   └── mytransitbenefit-com.md
│       ├── 04-geo/
│       │   ├── geo-audit-plan.md
│       │   ├── geo-review-matrix.md
│       │   ├── nita-illinois-gov.md
│       │   └── mytransitbenefit-com.md
│       ├── 05-ux/
│       │   ├── nita-illinois-gov.md
│       │   └── mytransitbenefit-com.md
│       └── 06-recommendations-and-roadmap.md
└── report/
    └── nita-website-audit.pdf  (final deliverable, when ready)
```

## Finding template

Use a consistent format so findings can be reviewed, compared, and consolidated:

```markdown
### [Short finding title]

- **Website:**
- **Page or component:**
- **Priority:** Critical / High / Medium / Low
- **Evidence:**
- **Impact:**
- **Recommendation:**
- **Implementation complexity:** Low / Medium / High
```

For accessibility findings, include the relevant WCAG success criterion when it can be identified. Record the date and method for time-sensitive or automated observations.

## Workflow

1. Select representative pages, templates, and user journeys for each website.
2. Record observations and evidence in the relevant section and site file.
3. Review and deduplicate findings; assign priority and implementation complexity.
4. Write the cross-site executive summary and recommended action plan.
5. Assemble the reviewed Markdown into a structured PDF with screenshots and references where appropriate.

## Project reference

See [`docs/project-overview.md`](docs/project-overview.md) for the full proposal, scope, methodology, deliverables, assumptions, and timeline.

See [`docs/transit-system-context.md`](docs/transit-system-context.md) for a short explanation of NITA, CTA, Metra, Pace, and the websites covered by the audit.

See [`docs/audit/authoring-guide.md`](docs/audit/authoring-guide.md) for the shared writing style, section structure, finding format, evidence standards, and review checklist.
