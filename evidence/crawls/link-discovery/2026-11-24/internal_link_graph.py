"""Record every internal link on every NITA HTML page, with the page region it sits in
(SEO Step 3, part D: information architecture and internal links).

The 2026-11-19 link discovery (B1) stores only the first page linking to each URL.
This script re-reads every HTML page that returned 200 in B1 and writes one row per
internal <a href>: source page, raw href, resolved target (fragment removed, scheme
set to https), page region, anchor text (or aria-label / image alt text when the
link has no text), and rel. Regions come from the nearest enclosing element: "nav"
(<nav>: desktop and mobile menus), "footer" (<footer>), "hero" (<header>: the page
banner with breadcrumb and title); other links are "top" (logo and utility links
before the banner) or "body" (page content after the banner). Sequential requests with a fixed delay.

Usage: python3 -I internal_link_graph.py <b1_pages_csv> <output_csv> [delay] [html_cache_dir]
"""
import csv
import gzip
import os
import sys
import time
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin, urlsplit, urlunsplit

UA = "Mozilla/5.0 (compatible; seo-audit-link-discovery/1.0)"
REGIONS = ("nav", "footer", "header")


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # open region tags
        self.links = []
        self._a = None
        self.after_hero = False

    def region(self):
        for t in ("footer", "nav", "header"):
            if t in self.stack:
                return {"header": "hero"}.get(t, t)
        return "body" if self.after_hero else "top"

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag in REGIONS:
            self.stack.append(tag)
        elif tag == "a":
            self._a = {"href": a.get("href"), "rel": a.get("rel", ""), "aria": a.get("aria-label", ""),
                       "text": [], "alt": [], "region": self.region()}
        elif tag == "img" and self._a is not None and a.get("alt"):
            self._a["alt"].append(a["alt"])

    def handle_endtag(self, tag):
        if tag in REGIONS and tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass
            if tag == "header":
                self.after_hero = True
        elif tag == "a" and self._a is not None:
            if self._a["href"]:
                text = " ".join("".join(self._a["text"]).split())
                label = text or self._a["aria"] or " ".join(self._a["alt"])
                self.links.append((self._a["href"].strip(), label, self._a["region"], self._a["rel"]))
            self._a = None

    def handle_data(self, data):
        if self._a is not None:
            self._a["text"].append(data)


def norm(url):
    s = urlsplit(urldefrag(url)[0])
    return urlunsplit(("https", s.netloc.lower(), s.path or "/", s.query, ""))


def main():
    pages_csv, out = sys.argv[1], sys.argv[2]
    delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
    cache = sys.argv[4] if len(sys.argv) > 4 else None
    rows = list(csv.DictReader(open(pages_csv)))
    pages = [r["url"] for r in rows if r["status"] == "200" and r["content_type"] == "text/html"]
    host = urlsplit(pages[0]).hostname
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_url", "raw_href", "target_url", "region", "anchor_text", "rel"])
        for i, page in enumerate(pages, 1):
            req = urllib.request.Request(page, headers={"User-Agent": UA})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    html = r.read().decode("utf-8", "replace")
            except Exception as e:
                w.writerow([page, "", "", "fetch-error", str(e)[:120], ""])
                continue
            if cache:
                with gzip.open(os.path.join(cache, f"{i:05d}.html.gz"), "wt") as g:
                    g.write(page + "\n" + html)
            p = LinkParser()
            p.feed(html)
            for href, label, region, rel in p.links:
                if href.startswith(("mailto:", "tel:", "javascript:", "#")):
                    continue
                absu = urljoin(page, href)
                if urlsplit(absu).hostname != host:
                    continue
                w.writerow([page, href, norm(absu), region, label, rel])
            if i % 200 == 0:
                print(f"{i}/{len(pages)}", flush=True)
            time.sleep(delay)


if __name__ == "__main__":
    main()
