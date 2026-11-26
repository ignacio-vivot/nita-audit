"""Program and agency names used on the AEO sample pages (AEO Step 2, part B).

Converts each page in structure-pages.tsv to content text with
../answer-map/structured_text.py (menus, footers, forms, and scripts skipped; text before
the first H1, such as header labels, dropped; link URLs removed so only visible words are
counted), then counts each term in terms.tsv
(group, label, regular expression). Matching is case-insensitive unless the label ends in
"(case-sensitive)". The two application PDFs (text in ../answer-map/) are included.

Writes term-usage.csv: one row per term with occurrences, number of pages, and the pages.

Usage: python3 -I term_usage.py structure-pages.tsv terms.tsv
"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "answer-map"))
from structured_text import P  # noqa: E402


def page_text(path):
    p = P()
    p.feed(open(path, errors="replace").read())
    t = "".join(p.out)
    m = re.search(r"(^|\n)# ", t)  # count from the first H1, as in structured_text's word positions
    t = t[m.start():] if m else t
    t = re.sub(r"\[link:[^\]]*\]", " ", t)
    t = re.sub(r"\[ACCORDION\s*: ([^\]]*)\]", r" \1 ", t)  # keep accordion labels, which are visible text
    t = re.sub(r"\{w=\d+\}|\[/?(ACCORDION|TABLE|HIDDEN-PANEL)[^\]]*\]", " ", t)
    return " ".join(t.replace("’", "'").split())


def short(url):
    return re.sub(r"^https?://(www\.)?", "", url).rstrip("/") or url


def main():
    pages = [(short(r["url"]), page_text(r["html"])) for r in csv.DictReader(open(sys.argv[1]), delimiter="\t")]
    for pdf in ("Reduced-Fare-Application-240301-mk-v12", "RTA-Ride-Free-Application-240117-v11"):
        pages.append((pdf + ".pdf", " ".join(open(f"../answer-map/{pdf}.txt").read().replace("’", "'").split())))
    with open("term-usage.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["group", "term", "occurrences", "pages", "page_list"])
        for t in csv.DictReader(open(sys.argv[2]), delimiter="\t"):
            flags = 0 if t["label"].endswith("(case-sensitive)") else re.I
            rx = re.compile(t["regex"], flags)
            hits = [(u, len(rx.findall(txt))) for u, txt in pages]
            hits = [(u, n) for u, n in hits if n]
            w.writerow([t["group"], t["label"], sum(n for _, n in hits), len(hits),
                        "; ".join(f"{u} ({n})" for u, n in hits)])


if __name__ == "__main__":
    main()
