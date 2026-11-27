// Run axe-core (WCAG 2.0/2.1 Level A and AA rules) on one or more URLs with the installed Google Chrome.
// Usage: node axe-scan.mjs <out-dir> <desktop|mobile> <url> [url ...]
// Writes one JSON file per URL (full axe result) and a summary CSV of violations and incomplete ("needs review") items.
import { chromium } from 'playwright';
import { AxeBuilder } from '@axe-core/playwright';
import fs from 'node:fs';
import path from 'node:path';

const [outDir, mode, ...urls] = process.argv.slice(2);
if (!outDir || !['desktop', 'mobile'].includes(mode) || urls.length === 0) {
  console.error('Usage: node axe-scan.mjs <out-dir> <desktop|mobile> <url> [url ...]');
  process.exit(1);
}

const VIEWPORTS = {
  desktop: { viewport: { width: 1280, height: 800 } },
  mobile: { viewport: { width: 375, height: 812 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 },
};
const TAGS = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'];
const slug = (u) => u.replace(/^https?:\/\//, '').replace(/[^a-z0-9]+/gi, '-').replace(/-+$/, '').slice(0, 150);
const csvCell = (v) => `"${String(v ?? '').replace(/"/g, '""')}"`;

fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch({ channel: 'chrome', headless: true });
const context = await browser.newContext(VIEWPORTS[mode]);
const rows = [['url', 'mode', 'result_type', 'rule_id', 'impact', 'wcag_tags', 'nodes', 'help', 'first_target']];

for (const url of urls) {
  const page = await context.newPage();
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    const result = await new AxeBuilder({ page }).withTags(TAGS).analyze();
    fs.writeFileSync(path.join(outDir, `${slug(url)}--${mode}.json`), JSON.stringify(result, null, 2));
    for (const [type, list] of [['violation', result.violations], ['incomplete', result.incomplete]]) {
      for (const r of list) {
        const wcag = r.tags.filter((t) => /^wcag\d{3,}$/.test(t)).join(' ');
        rows.push([url, mode, type, r.id, r.impact, wcag, r.nodes.length, r.help, r.nodes[0]?.target?.join(' ')]);
      }
    }
    console.log(`${mode} ${url}: ${result.violations.length} violation rules, ${result.incomplete.length} needs-review rules`);
  } catch (err) {
    rows.push([url, mode, 'error', '', '', '', '', String(err.message).split('\n')[0], '']);
    console.error(`${mode} ${url}: ERROR ${err.message.split('\n')[0]}`);
  } finally {
    await page.close();
  }
  await new Promise((r) => setTimeout(r, 1000)); // about one page per second
}

const meta = {
  date: new Date().toISOString(),
  chrome: browser.version(),
  playwright: JSON.parse(fs.readFileSync(new URL('./node_modules/playwright/package.json', import.meta.url))).version,
  axe_core: JSON.parse(fs.readFileSync(new URL('./node_modules/axe-core/package.json', import.meta.url))).version,
  tags: TAGS,
  mode,
  viewport: VIEWPORTS[mode],
};
fs.writeFileSync(path.join(outDir, `run-meta--${mode}.json`), JSON.stringify(meta, null, 2));
fs.writeFileSync(path.join(outDir, `axe-summary--${mode}.csv`), rows.map((r) => r.map(csvCell).join(',')).join('\n') + '\n');
await browser.close();
