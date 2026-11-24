"""Extract the visible page text of the sample pages from raw HTML, without menus,
footer, scripts, styles, and forms (SEO Step 3, part E). Headings are marked with
'#' by level and links are written as [text](href) so link labels can be reviewed.

Usage: python3 -I extract_text.py <urls_txt> <raw_html_dir> <out_dir>
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SKIP = {"script", "style", "noscript", "template", "svg", "nav", "footer", "form", "select"}
BLOCK = {"p", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "div", "section", "details", "summary", "br", "td", "th", "figcaption", "blockquote"}


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.href, self.atext = [], 0, None, []
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "body":
            self.in_body = True
        if tag in SKIP:
            self.skip += 1
        if self.skip:
            return
        if tag in BLOCK:
            self.out.append("\n")
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append("#" * int(tag[1]) + " ")
        if tag == "li":
            self.out.append("- ")
        if tag in ("td", "th"):
            self.out.append(" | ")
        if tag == "a":
            self.href, self.atext = a.get("href") or "", []

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
            return
        if self.skip:
            return
        if tag == "a" and self.href is not None:
            t = " ".join("".join(self.atext).split())
            self.out.append(f"[{t}]({self.href})")
            self.href = None
        if tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if self.skip or not self.in_body:
            return
        if self.href is not None:
            self.atext.append(data)
        else:
            self.out.append(data)


def slug(url):
    return re.sub(r"[/.]", "-", re.sub(r"^https?://", "", url).rstrip("/"))[:90]


def main():
    urls = Path(sys.argv[1]).read_text().split()
    src, out = Path(sys.argv[2]), Path(sys.argv[3])
    for u in urls:
        p = TextParser()
        p.feed((src / f"{slug(u)}.html").read_text(errors="replace"))
        text = "".join(p.out)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
        (out / f"{slug(u)}.md").write_text(f"<!-- {u} (raw HTML fetched 2026-11-24 ~15:33 UTC) -->\n\n{text}\n")


if __name__ == "__main__":
    main()
