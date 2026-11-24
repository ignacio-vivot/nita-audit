// Run in the browser after the page has loaded (~4 s). Re-fetches the page's
// raw HTML (no JavaScript executed, parsed with DOMParser) and compares it with
// the rendered DOM. Returns the rendered values and every field that differs.
(async () => {
  const ex = (doc) => {
    const q = (s) => doc.querySelector(s);
    const at = (s, a) => (q(s) ? q(s).getAttribute(a) : null);
    const words = (el) => { if (!el) return 0; const c = el.cloneNode(true); c.querySelectorAll('script,style,noscript,template,svg').forEach((n) => n.remove()); return (c.textContent.match(/\w+/g) || []).length; };
    let li = 0, le = 0;
    doc.querySelectorAll('a[href]').forEach((a) => { const h = a.getAttribute('href').trim(); if (/^(mailto:|tel:|javascript:|#)/i.test(h)) return; let u; try { u = new URL(h, location.href); } catch (e) { return; } if (u.host === location.host) li++; else le++; });
    return {
      lang: doc.documentElement.getAttribute('lang'),
      title: (q('title') || {}).textContent?.replace(/\s+/g, ' ').trim() ?? null,
      description: at('meta[name="description"]', 'content'),
      robots: at('meta[name="robots"]', 'content'),
      canonical: at('link[rel="canonical"]', 'href'),
      og_title: at('meta[property="og:title"]', 'content'),
      og_url: at('meta[property="og:url"]', 'content'),
      hreflang: [...doc.querySelectorAll('link[rel="alternate"][hreflang]')].map((l) => l.getAttribute('hreflang') + ' ' + l.getAttribute('href')).join(' | '),
      headings: [...doc.querySelectorAll('h1,h2,h3,h4,h5,h6')].map((h) => h.tagName.toLowerCase() + ':' + h.textContent.replace(/\s+/g, ' ').trim()).join(' || '),
      jsonld_blocks: doc.querySelectorAll('script[type="application/ld+json"]').length,
      links_internal: li, links_external: le,
      main_words: words(q('main')),
      body_words: words(doc.body),
      images: doc.querySelectorAll('img').length,
    };
  };
  const html = await (await fetch(location.href, { cache: 'no-store' })).text();
  const raw = ex(new DOMParser().parseFromString(html, 'text/html'));
  const ren = ex(document);
  const diffs = {};
  for (const k of Object.keys(ren)) if (JSON.stringify(raw[k]) !== JSON.stringify(ren[k])) diffs[k] = { raw: raw[k], rendered: ren[k] };
  return JSON.stringify({ url: location.href, checked: new Date().toISOString(), rendered: ren, diffs });
})();
