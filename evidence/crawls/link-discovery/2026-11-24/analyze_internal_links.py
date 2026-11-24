"""Summarize the NITA internal link graph (SEO Step 3, part D).

Inputs: nita-internal-link-edges.csv (internal_link_graph.py) and the 2026-11-19 B1
pages.csv (status, crawl depth, redirect location). Outputs, in the output folder:

- nita-page-inlinks.csv: one row per HTML page returning 200 in B1, with page type,
  crawl depth, and the number of distinct linking pages by region (body = page
  content; nav = menus; footer; hero = breadcrumb/banner; top = logo bar).
- nita-anchor-text-summary.csv: anchor texts used for internal body links, with
  counts and the number of distinct targets (shows generic anchors such as
  "Learn more").
- nita-links-to-redirects.csv: internal links whose target redirected in B1, grouped
  by target, region, and redirect destination.

Usage: python3 -I analyze_internal_links.py <edges_csv> <b1_pages_csv> <out_dir>
"""
import csv
import os
import re
import sys
from collections import Counter, defaultdict


def page_type(url):
    path = url.split("nita.illinois.gov", 1)[1] or "/"
    if path in ("/", ""):
        return "homepage"
    if re.search(r"/p\d+$", path):
        return "pagination"
    if path.startswith("/blog/tags/"):
        return "tag archive"
    if re.match(r"^/blog/\d{4}/", path):
        return "blog post"
    if path.startswith("/about-rta/press-releases/") or path.startswith("/news/press-releases/"):
        return "press release"
    if path.startswith("/blog") or path.startswith("/news"):
        return "listing"
    return "core page"


def main():
    edges_csv, pages_csv, out = sys.argv[1], sys.argv[2], sys.argv[3]
    pages = {r["url"]: r for r in csv.DictReader(open(pages_csv))}
    html200 = {u for u, r in pages.items() if r["status"] == "200" and r["content_type"] == "text/html"}
    src = defaultdict(lambda: defaultdict(set))
    anchors = Counter()
    anchor_targets = defaultdict(set)
    redirects = Counter()
    for e in csv.DictReader(open(edges_csv)):
        if e["region"] == "fetch-error":
            continue
        t, s, reg = e["target_url"], e["source_url"], e["region"]
        if t != s:
            src[t][reg].add(s)
        if reg == "body":
            a = " ".join(e["anchor_text"].split()).lower()
            anchors[a] += 1
            anchor_targets[a].add(t)
        p = pages.get(t)
        if p and p["status"] in ("301", "302"):
            redirects[(t, p["status"], p["location"], reg)] += 1
    with open(os.path.join(out, "nita-page-inlinks.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "page_type", "crawl_depth_b1", "body_linking_pages", "nav_linking_pages",
                    "footer_linking_pages", "hero_linking_pages", "top_linking_pages", "all_linking_pages", "title"])
        for u in sorted(html200):
            r = src.get(u, {})
            allp = set().union(*r.values()) if r else set()
            w.writerow([u, page_type(u), pages[u]["crawl_depth"], len(r.get("body", ())), len(r.get("nav", ())),
                        len(r.get("footer", ())), len(r.get("hero", ())), len(r.get("top", ())), len(allp),
                        pages[u]["title"]])
    with open(os.path.join(out, "nita-anchor-text-summary.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["anchor_text_lowercase", "body_link_instances", "distinct_targets"])
        for a, n in anchors.most_common():
            w.writerow([a, n, len(anchor_targets[a])])
    with open(os.path.join(out, "nita-links-to-redirects.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["target_url", "status_b1", "redirect_location", "region", "link_instances"])
        for (t, st, loc, reg), n in sorted(redirects.items(), key=lambda x: -x[1]):
            w.writerow([t, st, loc, reg, n])


if __name__ == "__main__":
    main()
