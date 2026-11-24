// Run in the browser after the page has loaded (~4 s), with the viewport
// emulated at 375x812 (mobile) or 1280x800 (desktop) for comparison.
// Records layout, text, heading, link, tap-target, table, and overlay signals.
(() => {
  const vw = innerWidth, vh = innerHeight;
  const vis = (el) => { const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return false; const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const desc = (el) => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.') : '');
  // Horizontal overflow: elements whose right edge passes the viewport, outside a scrollable or clipped ancestor.
  const clipped = (el) => { for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) { const o = getComputedStyle(p).overflowX; if (o === 'auto' || o === 'scroll' || o === 'hidden' || o === 'clip') return true; } return false; };
  const wide = [...document.querySelectorAll('body *')].filter((el) => vis(el) && el.getBoundingClientRect().right > vw + 1 && !clipped(el)).map((el) => desc(el) + ' w=' + Math.round(el.getBoundingClientRect().width)).slice(0, 8);
  // Visible text and headings.
  const words = (document.body.innerText.match(/\w+/g) || []).length;
  const heads = [...document.querySelectorAll('h1,h2,h3')].filter((h) => h.textContent.trim());
  const hidden_heads = heads.filter((h) => !vis(h)).map((h) => h.tagName.toLowerCase() + ':' + h.textContent.replace(/\s+/g, ' ').trim().slice(0, 60));
  // Font sizes of visible text-bearing elements.
  let small = 0, minFont = 99; const smallEx = [];
  document.querySelectorAll('p,li,a,span,td,th,label,button,small,div').forEach((el) => {
    if (![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim().length > 2) || !vis(el)) return;
    const fs = parseFloat(getComputedStyle(el).fontSize); minFont = Math.min(minFont, fs);
    if (fs < 12) { small++; if (smallEx.length < 5) smallEx.push(fs + 'px ' + el.textContent.trim().slice(0, 40)); }
  });
  // Tap targets: visible links/buttons not inside running text, smaller than 24x24 CSS px.
  const inText = (el) => !!el.closest('p,li p,td') && el.closest('p');
  const targets = [...document.querySelectorAll('a[href],button,input:not([type=hidden]),select,[role=button]')].filter(vis);
  const tiny = targets.filter((el) => { const r = el.getBoundingClientRect(); return (r.width < 24 || r.height < 24) && !inText(el); });
  const tinyEx = tiny.slice(0, 8).map((el) => { const r = el.getBoundingClientRect(); return Math.round(r.width) + 'x' + Math.round(r.height) + ' ' + (el.getAttribute('aria-label') || el.textContent.replace(/\s+/g, ' ').trim() || desc(el)).slice(0, 40); });
  // Tables wider than the viewport and whether they scroll inside a container.
  const tables = [...document.querySelectorAll('table')].filter(vis).map((t) => { const r = t.getBoundingClientRect(); return { w: Math.round(r.width), cols: (t.rows[0] || { cells: [] }).cells.length, scroll_container: clipped(t) }; });
  // Fixed or sticky overlays covering a large share of the first screen.
  const overlays = [...document.querySelectorAll('body *')].filter((el) => { const p = getComputedStyle(el).position; if (p !== 'fixed' && p !== 'sticky') return false; if (!vis(el)) return false; const r = el.getBoundingClientRect(); return r.width * r.height > 0.15 * vw * vh; }).map((el) => desc(el) + ' ' + Math.round(el.getBoundingClientRect().height) + 'px');
  // Navigation: visible links in the header and the menu toggle.
  const header = document.querySelector('header') || document.querySelector('nav');
  const navVisible = header ? [...header.querySelectorAll('a[href]')].filter(vis).length : null;
  const toggle = [...document.querySelectorAll('button,[role=button],a')].filter(vis).find((b) => /menu|navigation|nav/i.test((b.getAttribute('aria-label') || '') + ' ' + b.textContent + ' ' + (b.className || '')) && b.getBoundingClientRect().top < 150);
  return JSON.stringify({ url: location.href, vw, vh, scrollWidth: document.documentElement.scrollWidth, overflow_px: document.documentElement.scrollWidth - vw, wide, visible_words: words, headings: heads.length, hidden_heads, min_font: minFont, small_text_elems: small, smallEx, targets: targets.length, tiny_targets: tiny.length, tinyEx, tables, overlays, header_links_visible: navVisible, menu_toggle: toggle ? (toggle.getAttribute('aria-label') || toggle.textContent.trim() || desc(toggle)).slice(0, 40) + ' aria-expanded=' + toggle.getAttribute('aria-expanded') : null, images_wider_than_vw: [...document.images].filter((i) => vis(i) && i.getBoundingClientRect().width > vw + 1).length });
})();
