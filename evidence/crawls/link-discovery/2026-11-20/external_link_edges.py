"""Record every NITA page that links to an external URL with a non-2xx/3xx result
(SEO Step 2, part F).

links_external.csv (2026-11-19 link discovery) stores only the first page linking
to each external URL. This script re-reads every HTML page that returned 200 in B1
and records each <a href> whose resolved, fragment-free URL had a status of 0
(connection error) or >= 400 in nita-external-link-status.csv, with anchor text.
Sequential requests with a fixed delay.

Usage: python3 -I external_link_edges.py <b1_pages_csv> <status_csv> <output_csv> [delay]
"""
import csv
import sys
import time
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin, urlsplit

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


def main():
    pages_csv, status_csv, out = sys.argv[1], sys.argv[2], sys.argv[3]
    delay = float(sys.argv[4]) if len(sys.argv) > 4 else 0.2
    status = {}
    for r in csv.DictReader(open(status_csv)):
        s = int(r["status"])
        if s == 0 or s >= 400:
            status[r["url"]] = (r["status"], r["error"])
    rows = list(csv.DictReader(open(pages_csv)))
    pages = [r["url"] for r in rows if r["status"] == "200" and r["content_type"] == "text/html"]
    host = urlsplit(pages[0]).hostname
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_url", "raw_href", "target_url", "target_status", "target_error", "anchor_text"])
        for i, page in enumerate(pages, 1):
            req = urllib.request.Request(page, headers={"User-Agent": UA})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    html = r.read().decode("utf-8", "replace")
            except Exception as e:
                w.writerow([page, "", "", f"fetch-error: {e}", "", ""])
                continue
            p = AnchorParser()
            p.feed(html)
            for href, text in p.anchors:
                if href.startswith(("mailto:", "tel:", "javascript:", "#")):
                    continue
                absu = urldefrag(urljoin(page, href))[0]
                if urlsplit(absu).hostname == host:
                    continue
                if absu in status:
                    st, err = status[absu]
                    w.writerow([page, href, absu, st, err[:120], text])
            if i % 200 == 0:
                print(f"{i}/{len(pages)}", flush=True)
            time.sleep(delay)


if __name__ == "__main__":
    main()
