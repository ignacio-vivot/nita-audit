"""List the "Related Articles" links of every NITA blog post and press release
(SEO Step 3, part D).

Reads the gzip HTML cache written by internal_link_graph.py (first line of each file
is the page URL) and, for each blog post or press release, records the post and
press-release links between the "Related Articles" label and the <footer> element.

Usage: python3 -I related_articles.py <html_cache_dir> <output_csv>
"""
import csv
import glob
import gzip
import os
import re
import sys

LINK = re.compile(r'href="(https://nita\.illinois\.gov/(?:blog/\d{4}/[^"]+|about-rta/press-releases/[^"]+))"')


def main():
    cache, out = sys.argv[1], sys.argv[2]
    per = {}
    for f in glob.glob(os.path.join(cache, "*.gz")):
        url, html = gzip.open(f, "rt").read().split("\n", 1)
        if not re.search(r"/blog/\d{4}/", url) and "/press-releases/" not in url:
            continue
        i = html.find("Related Articles")
        if i < 0:
            per[url] = ()
            continue
        links = []
        for m in LINK.finditer(html[i:html.find("<footer", i)]):
            if m.group(1) not in links:
                links.append(m.group(1))
        per[url] = tuple(links)
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_url", "related_article_count", "related_articles"])
        for u in sorted(per):
            w.writerow([u, len(per[u]), " | ".join(per[u])])


if __name__ == "__main__":
    main()
