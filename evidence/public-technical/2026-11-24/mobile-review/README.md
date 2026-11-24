# Mobile review of the sample pages — 2026-11-24 (SEO Step 3, part C)

Scope: the 16 NITA and 4 My Transit Benefit sample pages (`../rendered-review/urls.txt`).

Method:

1. **Same content for every device.** Each URL was requested with curl 8.7.1 using a desktop Chrome user agent, a mobile Chrome user agent, and the Googlebot smartphone user agent; response sizes, `Vary` headers, and title, canonical, and H1 were compared (`ua-parity.txt`). All 20 pages return HTML of the same size, with the same title, canonical, and H1, to all three user agents, and declare `<meta name="viewport" content="width=device-width, initial-scale=1.0">` (responsive design, no separate mobile URLs or dynamic serving).
2. **Mobile layout checks.** Each page was opened in the Claude desktop app's built-in browser (Chromium) with the viewport emulated at 375×812 (mobile user agent and touch), between 15:58 and 16:05 UTC. After a 3–4 second wait, `mobile_check.js` recorded horizontal overflow, elements wider than the screen, visible word count (`innerText`), headings hidden by CSS, smallest visible font size, tap targets smaller than 24×24 CSS px (outside running text), tables and whether they scroll inside a container, large fixed overlays, and the menu toggle. Results are in `mobile-results.csv`.
3. **Accordions.** On pages with `<details>` accordions, all accordions were opened and the page width and table edges were measured again; the Paying for your ride result was captured in `paying-for-your-ride-cta-pace-table-375px.jpg` (CTA and Pace accordion open).
4. **Content parity with desktop.** Visible words and hidden headings were recorded again at 1280×800 for the 11 pages with hidden headings or fare tables (`desktop_visible_words` and `hidden_headings_desktop` columns). Hidden headings are the same at both widths (items in components that show one panel at a time, and the form confirmation “Thank you!”), and visible text differs by 9–21 words (menu labels).
5. **Navigation.** On the NITA homepage the mobile menu was opened and its links compared with the desktop menu, which stays in the HTML but is hidden below the `lg` breakpoint. For the third-level pages missing from the mobile menu, the parent page's HTML was searched for links outside the header (`nav-parity.txt`).

Files:

- `ua-parity.txt` — desktop, mobile, and Googlebot smartphone responses for the 20 pages.
- `mobile_check.js` — the browser script used for step 2.
- `mobile-results.csv` — one row per page with the step 2 to 4 measurements.
- `nav-parity.txt` — desktop-only menu links and the parent-page link checks.
- `paying-for-your-ride-cta-pace-table-375px.jpg` — screenshot of the CTA and Pace fare table at 375 px.

Other observations recorded in `mobile-results.csv`, not reported as SEO findings: the smallest text on most pages is the 11.2 px reCAPTCHA notice in the footer form; breadcrumb links and blog category labels are 21–22 px tall, just under 24 px; footer form checkboxes are 16×16 px. Tap-target and text-size issues are assessed in the accessibility section. The Weglot language switcher is fixed to the bottom-right corner and covers part of the text as the page scrolls.

Limits: Chromium device emulation, not physical phones; one width (375 px) for layout checks; pages were not tested in landscape or with browser zoom.
