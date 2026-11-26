"""Content structure inventory of the AEO sample pages (AEO Step 2, part B).

For each page in structure-pages.tsv (url, path to raw HTML), counts the structures that
answer systems and readers use to find answers: headings by level, empty headings,
skipped heading levels, heading texts used more than once, question-style headings and accordion labels, lists, tables
(with header cells or captions), definition lists, accordions (<details>), and panels
hidden until a click (class "hidden", role="tabpanel", Alpine x-show or :class). Words
are counted from the first H1, outside menus, footers, forms, and scripts, as in
../answer-map/structured_text.py. Also records the words between the H1 and the next
heading (the opening passage) and the share of content words inside accordions or
hidden panels.

Writes structure-inventory.csv (one row per page) and heading-outlines.md (the heading
outline of each page with accordion labels, word positions, and hidden-content marks).

Usage: python3 -I structure_inventory.py structure-pages.tsv
"""
import csv
import re
from collections import Counter
import sys
from html.parser import HTMLParser

SKIP = {"nav", "footer", "script", "style", "form", "noscript", "svg", "select", "template"}
HEAD = ("h1", "h2", "h3", "h4", "h5", "h6")
Q = re.compile(r"^(how|what|who|when|where|why|which|can|do|does|is|are|will|should)\b", re.I)


def question(t):
    return t.endswith("?") or bool(Q.match(t))


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.skip = [], 0
        self.started = False
        self.words = 0
        self.hidden_words = 0          # words inside an accordion body or hidden panel
        self.in_details = 0
        self.in_hidden = 0
        self.cur, self.buf = None, []  # heading or summary being read
        self.outline = []              # (kind, text, words_at, in_accordion, in_hidden)
        self.c = {k: 0 for k in ("ul", "ol", "li", "table", "table_th", "table_caption", "dl",
                                 "details", "hidden_panel")}
        self.table_has_th = []
        self.intro_words = None        # words between first H1 and next heading

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
        if self.skip:
            self.stack.append((tag, False))
            return
        cls = a.get("class") or ""
        hidden = tag in ("div", "section", "ul") and (
            " hidden " in f" {cls} " or a.get("role") == "tabpanel" or "x-show" in a or ":class" in a)
        self.stack.append((tag, hidden))
        if hidden:
            self.in_hidden += 1
            if self.started:
                self.c["hidden_panel"] += 1
        if tag in HEAD or tag == "summary":
            self.cur, self.buf = tag, []
            if tag == "h1" and not self.started:
                self.started = True
                self.words = 0
            elif tag in HEAD and self.started and self.intro_words is None and self.outline:
                self.intro_words = self.words
        if not self.started:
            return
        if tag == "details":
            self.in_details += 1
            self.c["details"] += 1
        elif tag in ("ul", "ol", "li", "dl"):
            self.c[tag] += 1
        elif tag == "table":
            self.c["table"] += 1
            self.table_has_th.append(False)
        elif tag == "th" and self.table_has_th:
            self.table_has_th[-1] = True
        elif tag == "caption":
            self.c["table_caption"] += 1

    def handle_endtag(self, tag):
        while self.stack:
            t, hidden = self.stack.pop()
            if t in SKIP and self.skip:
                self.skip -= 1
            if hidden:
                self.in_hidden -= 1
            if t == "details" and self.in_details and self.started:
                self.in_details -= 1
            if t == tag:
                break
        if self.skip:
            return
        if tag == self.cur:
            text = " ".join("".join(self.buf).split())
            self.outline.append((tag, text, self.words, self.in_details > (0 if tag == "summary" else 0),
                                 self.in_hidden > 0))
            self.cur = None
        if tag == "table" and self.table_has_th:
            if self.table_has_th.pop():
                self.c["table_th"] += 1

    def handle_data(self, d):
        if self.skip:
            return
        if self.cur:
            self.buf.append(d)
            return
        if not self.started:
            return
        n = len(re.findall(r"\w+", d))
        self.words += n
        if self.in_details or self.in_hidden:
            self.hidden_words += n


def analyse(path):
    p = P()
    p.feed(open(path, errors="replace").read())
    heads = [(k, t) for k, t, *_ in p.outline if k in HEAD]
    levels = [int(k[1]) for k, _ in heads]
    skips = sorted({f"h{a}>h{b}" for a, b in zip(levels, levels[1:]) if b > a + 1})
    labels = [t for k, t, *_ in p.outline if k == "summary"]
    row = {
        "content_words": p.words,
        "intro_words": p.intro_words if p.intro_words is not None else p.words,
        **{k: levels.count(int(k[1])) for k in HEAD[:5]},
        "empty_headings": sum(1 for _, t in heads if not t),
        "level_skips": " ".join(skips),
        "repeated_heading_texts": "; ".join(f"{t} (x{n})" for t, n in Counter(t for _, t in heads if t).most_common() if n > 1)[:300],
        "question_headings": sum(1 for _, t in heads if t and question(t)),
        "accordions": p.c["details"],
        "question_accordion_labels": sum(1 for t in labels if question(t)),
        "headings_inside_accordions_or_panels": sum(1 for k, t, _, acc, hid in p.outline if k in HEAD and (acc or hid)),
        "hidden_panels": p.c["hidden_panel"],
        "pct_words_in_accordions_or_panels": round(100 * p.hidden_words / p.words) if p.words else 0,
        "lists_ul": p.c["ul"], "lists_ol": p.c["ol"], "list_items": p.c["li"],
        "tables": p.c["table"], "tables_with_header_cells": p.c["table_th"], "tables_with_caption": p.c["table_caption"],
        "definition_lists": p.c["dl"],
    }
    return row, p.outline


def main():
    pages = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
    rows, md = [], ["# Heading outlines of the AEO sample pages (2026-11-25)", "",
                    "Generated by `structure_inventory.py`. `{w=N}`: content words between the H1 and the element. "
                    "`▸` accordion label; `[accordion]` heading inside an accordion; `[hidden]` inside a panel hidden until a click; "
                    "`(empty)` heading with no text; `?` question-style.", ""]
    for pg in pages:
        row, outline = analyse(pg["html"])
        rows.append({"url": pg["url"], **row})
        md += [f"## {pg['url']}", ""]
        for k, t, w, acc, hid in outline:
            if k == "summary":
                line = f"{'  ' * 2}▸ {t}"
            else:
                line = f"{'  ' * (int(k[1]) - 1)}{k.upper()} {t or '(empty)'}"
            flags = (" ?" if t and question(t) else "") + (" [accordion]" if acc and k != "summary" else "") + (" [hidden]" if hid else "")
            md.append(f"- {line} {{w={w}}}{flags}")
        md.append("")
    with open("structure-inventory.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    open("heading-outlines.md", "w").write("\n".join(md))


if __name__ == "__main__":
    main()
