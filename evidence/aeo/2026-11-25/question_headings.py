"""Extract headings, accordion labels, and question-style text from pages (AEO Step 1).

Fetches each URL in the input list, keeps the raw HTML in <out_dir>/html/, and writes
one row per heading (h1-h4) and per accordion label (<summary>) with a flag for
question style: text ending in "?" or starting with how, what, who, when, where, why,
which, can, do, does, is, are, will, should.

Usage: python3 -I question_headings.py <urls.txt> <out_dir>
"""
import csv
import os
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser

Q = re.compile(r"^(how|what|who|when|where|why|which|can|do|does|is|are|will|should)\b", re.I)
SKIP = {"nav", "footer", "script", "style", "form"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows, self.cur, self.buf, self.skip = [], None, [], 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if not self.skip and tag in ("h1", "h2", "h3", "h4", "summary"):
            self.cur, self.buf = tag, []

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag == self.cur:
            t = " ".join("".join(self.buf).split())
            if t:
                self.rows.append((tag, t))
            self.cur = None

    def handle_data(self, d):
        if self.cur:
            self.buf.append(d)


def slug(u):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"^https?://", "", u.lower())).strip("-")[:100]


def main():
    urls = [u.strip() for u in open(sys.argv[1]) if u.strip()]
    out = sys.argv[2]
    os.makedirs(os.path.join(out, "html"), exist_ok=True)
    with open(os.path.join(out, "page-headings.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "order", "element", "text", "question_style"])
        for u in urls:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (compatible; aeo-audit/1.0)"})
            try:
                html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
            except Exception as e:
                w.writerow([u, 0, "error", str(e)[:100], ""])
                continue
            open(os.path.join(out, "html", slug(u) + ".html"), "w").write(html)
            p = P()
            p.feed(html)
            for i, (tag, t) in enumerate(p.rows, 1):
                w.writerow([u, i, tag, t, "yes" if (t.endswith("?") or Q.match(t)) else ""])
            time.sleep(0.3)


if __name__ == "__main__":
    main()
