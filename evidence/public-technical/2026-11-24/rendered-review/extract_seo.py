"""Extract SEO-relevant elements from raw HTML files (stdlib only).

Usage: python3 -I extract_seo.py urls.txt raw-html/ > raw-extract.jsonl

The same fields are collected from the rendered DOM in the browser with
rendered_extract.js, so the two outputs can be compared with compare.py.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

SKIP_TEXT = {"script", "style", "noscript", "template", "svg"}


class SEOParser(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.d = {
            "lang": None, "title": None, "description": None, "robots": None,
            "canonical": None, "hreflang": [], "og": {}, "headings": [],
            "jsonld_blocks": 0, "links_internal": 0, "links_external": 0,
            "links_nofollow": 0, "main_text_words": 0, "body_text_words": 0,
            "iframes": [], "forms": 0, "noscript_blocks": 0,
        }
        self.stack = []
        self.in_title = False
        self.title_buf = []
        self.heading = None
        self.heading_buf = []
        self.skip_depth = 0
        self.main_depth = 0
        self.body_words = []
        self.main_words = []
        self.in_jsonld = False

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "html":
            self.d["lang"] = a.get("lang")
        elif tag == "title" and self.d["title"] is None:
            self.in_title = True
        elif tag == "meta":
            name = a.get("name", "").lower()
            prop = a.get("property", "").lower()
            if name == "description":
                self.d["description"] = a.get("content")
            elif name == "robots":
                self.d["robots"] = a.get("content")
            elif prop.startswith("og:"):
                self.d["og"][prop] = a.get("content")
        elif tag == "link":
            rel = a.get("rel", "").lower().split()
            if "canonical" in rel:
                self.d["canonical"] = a.get("href")
            if "alternate" in rel and a.get("hreflang"):
                self.d["hreflang"].append([a["hreflang"], a.get("href")])
        elif tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self.d["jsonld_blocks"] += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading = tag
            self.heading_buf = []
        elif tag == "a" and a.get("href"):
            href = a["href"].strip()
            if href.startswith(("mailto:", "tel:", "javascript:", "#")):
                pass
            else:
                host = urlparse(urljoin(self.base, href)).netloc.lower()
                base_host = urlparse(self.base).netloc.lower()
                if host == base_host:
                    self.d["links_internal"] += 1
                else:
                    self.d["links_external"] += 1
                if "nofollow" in a.get("rel", "").lower():
                    self.d["links_nofollow"] += 1
        elif tag == "iframe":
            self.d["iframes"].append(a.get("src") or a.get("data-src") or "")
        elif tag == "form":
            self.d["forms"] += 1
        if tag == "noscript":
            self.d["noscript_blocks"] += 1
        if tag in SKIP_TEXT:
            self.skip_depth += 1
        if tag == "main":
            self.main_depth += 1

    def handle_endtag(self, tag):
        if tag == "title" and self.in_title:
            self.in_title = False
            self.d["title"] = " ".join("".join(self.title_buf).split())
        elif self.heading == tag:
            text = " ".join("".join(self.heading_buf).split())
            self.d["headings"].append([tag, text])
            self.heading = None
        if tag in SKIP_TEXT and self.skip_depth:
            self.skip_depth -= 1
        if tag == "main" and self.main_depth:
            self.main_depth -= 1

    def handle_data(self, data):
        if self.in_title:
            self.title_buf.append(data)
        if self.heading:
            self.heading_buf.append(data)
        if not self.skip_depth:
            words = re.findall(r"\w+", data)
            self.body_words.extend(words)
            if self.main_depth:
                self.main_words.extend(words)


def slug(url):
    s = re.sub(r"^https?://", "", url).rstrip("/")
    return re.sub(r"[/.]", "-", s)[:90]


def main():
    urls = Path(sys.argv[1]).read_text().split()
    folder = Path(sys.argv[2])
    for url in urls:
        html = (folder / f"{slug(url)}.html").read_text(errors="replace")
        p = SEOParser(url)
        p.feed(html)
        d = p.d
        d["body_text_words"] = len(p.body_words)
        d["main_text_words"] = len(p.main_words)
        d["h1_count"] = sum(1 for h in d["headings"] if h[0] == "h1")
        print(json.dumps({"url": url, "source": "raw", **d}, ensure_ascii=False))


if __name__ == "__main__":
    main()
