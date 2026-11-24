// Run in the browser console after the page has loaded (wait ~5 s for scripts).
// Collects the same fields as extract_seo.py from the rendered DOM.
(() => {
  const q = (s) => document.querySelector(s);
  const attr = (s, a) => (q(s) ? q(s).getAttribute(a) : null);
  const words = (el) => {
    if (!el) return 0;
    const c = el.cloneNode(true);
    c.querySelectorAll('script,style,noscript,template,svg').forEach((n) => n.remove());
    return (c.textContent.match(/\w+/g) || []).length;
  };
  const og = {};
  document.querySelectorAll('meta[property^="og:"]').forEach((m) => { og[m.getAttribute('property').toLowerCase()] = m.getAttribute('content'); });
  let li = 0, le = 0, nf = 0;
  document.querySelectorAll('a[href]').forEach((a) => {
    const h = a.getAttribute('href').trim();
    if (/^(mailto:|tel:|javascript:|#)/i.test(h)) return;
    let u; try { u = new URL(h, location.href); } catch (e) { return; }
    if (u.host === location.host) li++; else le++;
    if (/nofollow/i.test(a.getAttribute('rel') || '')) nf++;
  });
  const headings = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map((h) => [h.tagName.toLowerCase(), h.textContent.replace(/\s+/g, ' ').trim()]);
  const visibleH1 = [...document.querySelectorAll('h1')].map((h) => {
    const r = h.getBoundingClientRect(); const cs = getComputedStyle(h);
    return { text: h.textContent.replace(/\s+/g, ' ').trim(), visible: r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' };
  });
  return JSON.stringify({
    url: location.href,
    source: 'rendered',
    lang: document.documentElement.getAttribute('lang'),
    title: document.title,
    description: attr('meta[name="description"]', 'content'),
    robots: attr('meta[name="robots"]', 'content'),
    canonical: attr('link[rel="canonical"]', 'href'),
    hreflang: [...document.querySelectorAll('link[rel="alternate"][hreflang]')].map((l) => [l.getAttribute('hreflang'), l.getAttribute('href')]),
    og,
    headings,
    h1_count: headings.filter((h) => h[0] === 'h1').length,
    h1_visibility: visibleH1,
    jsonld_blocks: document.querySelectorAll('script[type="application/ld+json"]').length,
    links_internal: li, links_external: le, links_nofollow: nf,
    main_text_words: words(q('main')),
    body_text_words: words(document.body),
    iframes: [...document.querySelectorAll('iframe')].map((f) => f.getAttribute('src') || f.getAttribute('data-src') || ''),
    forms: document.querySelectorAll('form').length,
    weglot_switcher: !!q('.weglot-container, .wg-drop, [class*="weglot"]'),
    weglot_languages: [...document.querySelectorAll('.weglot-container a, .wg-li, [class*="weglot"] li')].map((e) => e.textContent.trim()).filter(Boolean).slice(0, 20),
  });
})();
