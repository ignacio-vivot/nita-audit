"""Record every internal link that points to a non-200 URL (SEO Step 2, part B).

The 2026-11-19 link-discovery run (B1) stored only the first page linking to each
URL. This script re-reads every HTML page that returned 200 in B1 and records all
<a href> links whose target returned a non-200 status in B1 (404, 403, 301, 302),
with the anchor text. Sequential requests with a fixed delay.

Usage: python3 -I link_edges.py <b1_pages_csv> <output_csv> [delay_seconds]
"""
import csv
import sys
import time
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin, urlsplit, urlunsplit

UA = "Mozilla/5.0 (compatible; seo-audit-link-discovery/1.0)"


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors, self._href, self._text = [], None, []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.anchors.append((self._href.strip(), " ".join("".join(self._text).split())))
            self._href = None


def norm(u):
    u = urldefrag(u)[0]
    p = urlsplit(u)
    return urlunsplit(("https", (p.netloc or "").lower(), p.path or "/", p.query, ""))


def main():
    src, out = sys.argv[1], sys.argv[2]
    delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
    rows = list(csv.DictReader(open(src)))
    status = {r["url"]: r["status"] for r in rows}
    targets = {u for u, s in status.items() if s != "200"}
    pages = [r["url"] for r in rows if r["status"] == "200" and r["content_type"] == "text/html"]
    host = urlsplit(pages[0]).hostname
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_url", "raw_href", "target_url", "target_status_b1", "anchor_text"])
        for i, page in enumerate(pages, 1):
            req = urllib.request.Request(page, headers={"User-Agent": UA})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    html = r.read().decode("utf-8", "replace")
            except Exception as e:  # record fetch failures
                w.writerow([page, "", "", f"fetch-error: {e}", ""])
                continue
            p = AnchorParser()
            p.feed(html)
            for href, text in p.anchors:
                if href.startswith(("mailto:", "tel:", "javascript:", "#")):
                    continue
                absu = urljoin(page, href)
                if urlsplit(absu).hostname != host:
                    continue
                t = norm(absu)
                if t in targets:
                    w.writerow([page, href, t, status[t], text])
            if i % 200 == 0:
                print(f"{i}/{len(pages)}", flush=True)
            time.sleep(delay)


if __name__ == "__main__":
    main()
