"""Structure assessment of the AEO sample pages (AEO Step 3, part C).

Reads the 31 HTML pages listed in ../../2026-11-25/structure/structure-pages.tsv (the
Step 2 part B sample; paths in that file are relative to its folder) and records the
elements that answer systems use to identify an answer, from the first H1 down and outside
menus, footers, forms, and scripts (the same rules as structure_inventory.py):

- heading-issues.csv: empty headings, a heading with the same text as the heading before
  it, headings that repeat the H1, H1s after the first, skipped levels, headings inside an
  accordion at the same or a higher level than the nearest heading outside any accordion
  (the section the accordion belongs to), and heading texts used three or more times on a
  page;
- accordion-sections.csv: each accordion label (<summary>) with the heading it falls under
  in the page outline (the nearest heading before it, and the nearest H2 or H1);
- tables.csv: each table with its section, whether it is inside an accordion or a hidden
  panel, its size, header cells (<th>), <thead>, <caption>, and its first row;
- step-blocks.csv: numbered steps that are not an ordered list (<ol>): a number in its own
  element (for example <span>1</span>) or a number typed at the start of a paragraph;
- question-paragraphs.csv: questions written as bold text inside a paragraph
  (<p><strong>…?</strong>) rather than as a heading or an accordion label.

Usage: python3 -I structure_assessment.py [pages.tsv]
(default: the Step 2 part B page list; another list with the same columns can be given,
for example to rerun the assessment on a later fetch of the same pages)
"""
import csv
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser

PAGES = "../../2026-11-25/structure/structure-pages.tsv"
SKIP = {"nav", "footer", "script", "style", "form", "noscript", "svg", "select", "template"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
HEAD = ("h1", "h2", "h3", "h4", "h5", "h6")
NUM = re.compile(r"^\d{1,2}$")
TYPED = re.compile(r"^(\d{1,2})[.)]\s+\S")


def norm(s):
    return " ".join(s.split())


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.skip, self.started = [], 0, False
        self.details, self.hidden = [], 0       # stack of accordion labels; hidden-panel depth
        self.cur, self.buf = None, []            # heading or summary being read
        self.headings = []                       # (level, text, in_accordion, accordion_label, enclosing_level)
        self.summaries = []                      # (label, nearest heading, nearest H2/H1)
        self.tables, self.tstack = [], []
        self.elem_text = []                      # text buffers of open span/div/p elements
        self.numbers = []                        # (number, kind, index in event list)
        self.events = []                         # running text chunks, for step text
        self.in_p, self.strong, self.strong_buf = 0, 0, []
        self.questions = []
        self.ol = 0

    # helpers
    def last_heading(self, maxlevel=6):
        for lv, t, *_ in reversed(self.headings):
            if lv <= maxlevel:
                return f"H{lv} {t or '(empty)'}"
        return ""

    def outside_level(self):
        """Level of the nearest heading before this point that is not inside any accordion."""
        for lv, t, acc, lab, _ in reversed(self.headings):
            if not acc:
                return lv
        return 1

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in VOID:
            return
        if tag in SKIP:
            self.skip += 1
        cls = a.get("class") or ""
        hid = (not self.skip) and tag in ("div", "section", "ul") and (
            " hidden " in f" {cls} " or a.get("role") == "tabpanel" or "x-show" in a or ":class" in a)
        self.stack.append((tag, hid))
        if self.skip:
            return
        if hid:
            self.hidden += 1
        if tag in HEAD or tag == "summary":
            self.cur, self.buf = tag, []
            if tag == "h1":
                self.started = True
        if not self.started:
            return
        if tag == "details":
            self.details.append("")
        elif tag == "table":
            self.tstack.append({"section": self.last_heading(), "accordion": self.details[-1] if self.details else "",
                                "hidden": self.hidden > 0, "rows": [], "th": 0, "thead": False, "caption": ""})
        elif tag == "tr" and self.tstack:
            self.tstack[-1]["rows"].append([])
        elif tag in ("td", "th") and self.tstack:
            if tag == "th":
                self.tstack[-1]["th"] += 1
            if not self.tstack[-1]["rows"]:
                self.tstack[-1]["rows"].append([])
            self.tstack[-1]["rows"][-1].append("")
        elif tag == "thead" and self.tstack:
            self.tstack[-1]["thead"] = True
        elif tag == "ol":
            self.ol += 1
        if tag in ("span", "div", "p"):
            self.elem_text.append([tag, []])
        if tag == "p":
            self.in_p += 1
        if tag in ("strong", "b") and self.in_p:
            self.strong += 1
            if self.strong == 1:
                self.strong_buf = []

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            t, hid = self.stack.pop()
            if t in SKIP and self.skip:
                self.skip -= 1
            elif hid and not self.skip:
                self.hidden -= 1
            if t == tag:
                break
        if self.skip:
            return
        if tag == self.cur:
            text = norm("".join(self.buf))
            if tag == "summary":
                if self.details:
                    self.details[-1] = text
                self.summaries.append((text, self.last_heading(), self.last_heading(2)))
            elif self.started:
                in_acc = bool(self.details)
                self.headings.append((int(tag[1]), text, in_acc, self.details[-1] if in_acc else "",
                                      self.outside_level() if in_acc else None))
            self.cur = None
            return
        if not self.started:
            return
        if tag == "details" and self.details:
            self.details.pop()
        elif tag == "caption" and self.tstack:
            pass
        elif tag == "table" and self.tstack:
            self.tables.append(self.tstack.pop())
        if tag in ("span", "div", "p") and self.elem_text and self.elem_text[-1][0] == tag:
            _, buf = self.elem_text.pop()
            text = norm("".join(buf))
            if NUM.match(text) and tag != "p":
                self.numbers.append((int(text), "number in its own element", len(self.events)))
        if tag in ("strong", "b") and self.strong:
            self.strong -= 1
            if self.strong == 0:
                q = norm("".join(self.strong_buf))
                if q.endswith("?"):
                    self.questions.append((self.last_heading(), q))
        if tag == "p" and self.in_p:
            self.in_p -= 1

    def handle_data(self, d):
        if self.skip:
            return
        if self.cur:
            self.buf.append(d)
            return
        if not self.started:
            return
        if self.tstack and self.tstack[-1]["rows"] and self.tstack[-1]["rows"][-1]:
            self.tstack[-1]["rows"][-1][-1] += d
        for _, buf in self.elem_text:
            buf.append(d)
        if self.strong:
            self.strong_buf.append(d)
        t = norm(d)
        if t:
            m = TYPED.match(t)
            if m and not self.tstack:
                self.numbers.append((int(m.group(1)), "number typed in the text", len(self.events)))
            self.events.append(t)


def sequences(p):
    """Group step numbers that run 1, 2, 3 … into sequences, with the text after each number."""
    seqs, cur = [], []
    for n, kind, i in p.numbers:
        if n == 1:
            if len(cur) > 1:
                seqs.append(cur)
            cur = [(n, kind, i)]
        elif cur and n == cur[-1][0] + 1 and kind == cur[-1][1]:
            cur.append((n, kind, i))
    if len(cur) > 1:
        seqs.append(cur)
    out = []
    for s in seqs:
        steps = []
        for k, (n, kind, i) in enumerate(s):
            end = s[k + 1][2] if k + 1 < len(s) else i + 3
            if kind == "number in its own element" and k + 1 < len(s):
                end -= 1          # the next step's number is the last chunk before its index
            txt = re.sub(r"^\d{1,2}[.)]\s*", "", " ".join(p.events[i:end]))
            steps.append(f"{n}. {txt[:90]}")
        out.append((s[0][1], steps, s[0][2]))
    return out


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else PAGES
    base = os.path.dirname(src)
    pages = list(csv.DictReader(open(src, encoding="utf-8"), delimiter="\t"))
    hi, acc, tab, steps, qs = [], [], [], [], []
    for pg in pages:
        url = pg["url"]
        p = P()
        p.feed(open(os.path.join(base, pg["html"]), encoding="utf-8", errors="replace").read())
        h = p.headings
        h1 = h[0][1] if h else ""
        counts = Counter(t for _, t, *_ in h if t)
        prev = None
        for i, (lv, t, in_acc, lab, outside) in enumerate(h):
            issues = []
            if not t:
                issues.append(("empty heading", ""))
            if prev and t and t == prev[1]:
                issues.append(("same text as the heading before it", f"H{prev[0]} before"))
            if i and t and t == h1:
                issues.append(("repeats the H1", ""))
            if lv == 1 and i:
                issues.append(("H1 after the first", ""))
            if prev and lv > prev[0] + 1:
                issues.append(("skipped level", f"H{prev[0]} > H{lv}"))
            if in_acc and outside is not None and lv <= outside:
                issues.append(("heading inside an accordion at the level of the section it belongs to",
                               f"accordion “{lab}” in an H{outside} section"))
            if t and counts[t] >= 3 and counts[t] != -1:
                issues.append(("text used three or more times", f"{counts[t]} times"))
                counts[t] = -1          # report once per text
            for kind, detail in issues:
                hi.append([url, kind, f"H{lv}", t or "(empty)", detail])
            prev = (lv, t)
        for label, near, h2 in p.summaries:
            acc.append([url, label, near, h2])
        for n, t in enumerate(p.tables, 1):
            rows = [r for r in t["rows"] if any(norm(c) for c in r)]
            first = " | ".join(norm(c) for c in rows[0]) if rows else ""
            tab.append([url, n, t["section"], t["accordion"], "yes" if t["hidden"] else "no", len(rows),
                        max((len(r) for r in rows), default=0), t["th"], "yes" if t["thead"] else "no",
                        t["caption"] or "", first[:160]])
        for kind, st, _ in sequences(p):
            steps.append([url, kind, len(st), p.ol, " / ".join(st)])
        for sec, q in p.questions:
            qs.append([url, sec, q])

    def write(name, header, rows):
        with open(name, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(rows)

    write("heading-issues.csv", ["url", "issue", "level", "heading", "detail"], hi)
    write("accordion-sections.csv", ["url", "accordion_label", "nearest_heading_before", "nearest_h2_or_h1_before"], acc)
    write("tables.csv", ["url", "table", "section", "accordion", "in_hidden_panel", "rows", "columns", "th_cells",
                         "thead", "caption", "first_row"], tab)
    write("step-blocks.csv", ["url", "how_numbers_are_written", "steps", "ordered_lists_on_page", "steps_text"], steps)
    write("question-paragraphs.csv", ["url", "section", "question"], qs)


if __name__ == "__main__":
    main()
