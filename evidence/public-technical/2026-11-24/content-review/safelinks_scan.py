"""Find Microsoft Outlook Safe Links URLs in any attribute of the cached NITA pages
(SEO Step 3, part E). Decodes each to its destination and the mailbox in its data
parameter. The cache is the gzip HTML written by internal_link_graph.py (first line of
each file is the page URL).

Usage: python3 -I safelinks_scan.py <html_cache_dir> <output_csv>
"""
import csv
import glob
import gzip
import os
import re
import sys
import urllib.parse

ATTR = re.compile(r'(\w+)="(https?://[a-z0-9.-]*safelinks\.protection\.outlook\.com/[^"]+)"', re.I)


def main():
    cache, out = sys.argv[1], sys.argv[2]
    rows = []
    for f in glob.glob(os.path.join(cache, "*.gz")):
        url, html = gzip.open(f, "rt").read().split("\n", 1)
        for m in ATTR.finditer(html):
            value = m.group(2).replace("&amp;", "&")
            q = urllib.parse.parse_qs(urllib.parse.urlsplit(value).query)
            dest = q.get("url", [""])[0]
            email = ";".join(re.findall(r"[\w.+-]+@[\w.-]+", urllib.parse.unquote(q.get("data", [""])[0])))
            start, end = html.rfind("<a", 0, m.start()), html.find("</a>", m.end())
            tag = html[start:end]
            href = re.search(r'href="([^"]*)"', tag)
            text = re.sub(r"<[^>]+>", "", tag[tag.find(">") + 1:]).strip()
            rows.append((url, m.group(1).lower(), href.group(1) if href else "", dest, email, text[:80]))
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["page_url", "attribute", "href_in_page", "decoded_destination", "email_in_safelinks_data", "link_text"])
        w.writerows(sorted(rows))


if __name__ == "__main__":
    main()
