"""List the JSON-LD types on the pages AEO added to the SEO sample (AEO Step 2, part D).

Reads ../../2026-11-25/proposed-sample.csv, takes the rows marked "Proposed addition"
(HTML pages only; the Registration Sites URL redirects to a map), parses every
application/ld+json block in the raw HTML saved on 2026-11-25 (../../2026-11-25/html/),
and writes jsonld-types-aeo-additions.csv with the number of blocks and the @type values.
The 20 SEO sample pages were extracted on 2026-11-20 (evidence/public-technical/2026-11-20/structured-data/).

Usage: python3 -I jsonld_types.py
"""
import csv
import json
import re

BASE = "../../2026-11-25/"


def slug(u):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"^https?://", "", u.lower())).strip("-")[:100]


def types(x, out):
    if isinstance(x, dict):
        t = x.get("@type")
        if t:
            out.add(t if isinstance(t, str) else "/".join(t))
        for v in x.values():
            types(v, out)
    elif isinstance(x, list):
        for v in x:
            types(v, out)
    return out


def main():
    rows = []
    for r in csv.DictReader(open(BASE + "proposed-sample.csv")):
        u = r["url"]
        if not r["status"].startswith("Proposed") or u.endswith(".pdf") or "registration-sites" in u:
            continue
        html = open(BASE + "html/" + slug(u) + ".html", errors="replace").read()
        blocks = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.S)
        found = set()
        for b in blocks:
            try:
                types(json.loads(b), found)
            except ValueError:
                found.add("PARSE-ERROR")
        rows.append({"url": u, "jsonld_blocks": len(blocks), "types": "; ".join(sorted(found))})
    with open("jsonld-types-aeo-additions.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["url", "jsonld_blocks", "types"])
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
