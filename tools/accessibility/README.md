# Accessibility audit tools

Scripts for the accessibility section ([work plan](../../docs/audit/01-accessibility-ada/accessibility-audit-plan.md)). Installed on 2026-11-27 after team approval.

| Package | Version | License | Use |
| --- | --- | --- | --- |
| [playwright](https://playwright.dev/) | 1.65.1 | Apache-2.0 | Drives the installed Google Chrome (158.0.8127.88 on 2026-11-27) headless. No Playwright browser was downloaded. |
| [axe-core](https://github.com/dequelabs/axe-core) | 4.14.1 | MPL-2.0 | WCAG rule engine. |
| [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm) | 4.14.1 | MPL-2.0 | Runs axe-core inside a Playwright page. |

Versions are pinned in `package.json` and `package-lock.json`. `node_modules/` is not committed.

## Setup

Requires Node.js (24 used) and Google Chrome.

```bash
cd tools/accessibility && PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm ci
```

## Scripts

- `axe-scan.mjs` — runs axe-core with the tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` on one or more URLs at desktop (1280×800) or mobile (375×812) width, about one page per second. Writes the full axe JSON per URL, a summary CSV of violations and “needs review” items, and `run-meta--<mode>.json` with date and tool versions.

```bash
node axe-scan.mjs <out-dir> desktop https://nita.illinois.gov/
```

Save audit outputs in dated folders under `evidence/accessibility/`, not here. Axe checks only part of each WCAG criterion: an empty result is not a pass ([work plan](../../docs/audit/01-accessibility-ada/accessibility-audit-plan.md#can-the-checks-be-automated-as-in-seo)).
