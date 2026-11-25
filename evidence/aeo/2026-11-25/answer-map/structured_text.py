"""Convert answer pages to text with structure markers (AEO Step 2, part A).

Reads raw HTML saved by question_headings.py and writes one Markdown file per page with:
- headings as "#", "##", ... ;
- accordion content (<details>) wrapped as "[ACCORDION: label]" ... "[/ACCORDION]";
- tables as "[TABLE]" rows "| a | b |" "[/TABLE]";
- elements hidden until clicked (class "hidden", tab panels) marked "[HIDDEN-PANEL]";
- a running word count "{w=N}" at each heading, counting words of page content from
  the H1 (menus, footer, scripts, and forms are skipped), so answer position can be read.

Usage: python3 -I structured_text.py <html_dir> <out_dir> <file1.html> [file2.html ...]
"""
import os
import re
import sys
from html.parser import HTMLParser

SKIP = {"nav", "footer", "script", "style", "form", "noscript", "svg", "select", "template"}
BLOCK = {"p", "li", "div", "section", "br", "tr", "figcaption", "blockquote", "dd", "dt"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.stack = [], 0, []
        self.started, self.words = False, 0
        self.head, self.hbuf = None, []
        self.cell = False
        self.summary, self.sbuf = False, []

    def emit(self, s):
        self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "")
        if tag in SKIP:
            self.skip += 1
        if self.skip:
            self.stack.append((tag, False))
            return
        hidden = (" hidden " in f" {cls} " or a.get("role") == "tabpanel" or "x-show" in a or ":class" in a) and tag in ("div", "section", "ul")
        self.stack.append((tag, hidden))
        if hidden:
            self.emit("\n[HIDDEN-PANEL]\n")
        if tag in ("h1", "h2", "h3", "h4", "h5"):
            if tag == "h1":
                self.started = True
            self.head, self.hbuf = tag, []
        elif tag == "details":
            self.emit("\n[ACCORDION")
        elif tag == "summary":
            self.summary, self.sbuf = True, []
        elif tag == "table":
            self.emit("\n[TABLE]\n")
        elif tag in ("td", "th"):
            self.emit(" | ")
        elif tag == "a" and a.get("href"):
            self.emit(" [link:" + a["href"][:120] + "] ")
        elif tag in BLOCK:
            self.emit("\n")
        if tag == "li":
            self.emit("- ")

    def handle_endtag(self, tag):
        while self.stack:
            t, hidden = self.stack.pop()
            if t in SKIP and self.skip:
                self.skip -= 1
            if hidden and not self.skip:
                self.emit("\n[/HIDDEN-PANEL]\n")
            if t == tag:
                break
        if self.skip:
            return
        if tag == self.head:
            text = " ".join("".join(self.hbuf).split())
            self.emit(f"\n\n{'#' * int(tag[1])} {text} {{w={self.words}}}\n")
            self.head = None
        elif tag == "summary" and self.summary:
            self.emit(": " + " ".join("".join(self.sbuf).split()) + "]\n")
            self.summary = False
        elif tag == "details":
            self.emit("\n[/ACCORDION]\n")
        elif tag == "table":
            self.emit("\n[/TABLE]\n")
        elif tag == "tr":
            self.emit("\n")

    def handle_data(self, d):
        if self.skip:
            return
        if self.head:
            self.hbuf.append(d)
            return
        if self.summary:
            self.sbuf.append(d)
            return
        if self.started:
            self.words += len(re.findall(r"\w+", d))
        self.emit(d)


def main():
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for name in sys.argv[3:]:
        p = P()
        p.feed(open(os.path.join(src, name), errors="replace").read())
        text = "".join(p.out)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
        open(os.path.join(out, name.replace(".html", ".md")), "w").write(text + f"\n\n(total content words: {p.words})\n")


if __name__ == "__main__":
    main()
