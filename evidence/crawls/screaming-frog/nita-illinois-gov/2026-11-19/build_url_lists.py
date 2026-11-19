"""Build Screaming Frog List-mode input files for the NITA crawl baseline (run B2).

Input: the 2026-11-19 sitemap XML files and the B1 link-discovery pages.csv.
Output: list-01.txt, list-02.txt, ... (at most 450 URLs each) and url-sources.csv
recording whether each URL came from the sitemap, link discovery, or both.

Usage: python3 -I build_url_lists.py <repo_root> <output_dir>
"""
import csv
import glob
import re
import sys
from pathlib import Path

BATCH = 450

root, out = Path(sys.argv[1]), Path(sys.argv[2])
sitemap_files = glob.glob(str(root / "evidence/public-technical/2026-11-19/nita-sitemaps-1-*.xml"))
sitemap = set()
for f in sitemap_files:
    for loc in re.findall(r"<loc>([^<]+)</loc>", Path(f).read_text()):
        if not loc.endswith(".xml"):
            sitemap.add(loc.strip())

discovered = set()
pages = root / "evidence/crawls/link-discovery/2026-11-19/nita-illinois-gov/pages.csv"
with open(pages) as f:
    for row in csv.DictReader(f):
        if row["content_type"] == "text/html" or row["status"].startswith("3"):
            discovered.add(row["url"])

urls = sorted(sitemap | discovered)
out.mkdir(parents=True, exist_ok=True)
with open(out / "url-sources.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["url", "in_sitemap", "found_by_link_discovery", "list_file"])
    for i, u in enumerate(urls):
        w.writerow([u, u in sitemap, u in discovered, f"list-{i // BATCH + 1:02d}.txt"])
for b in range(0, len(urls), BATCH):
    (out / f"list-{b // BATCH + 1:02d}.txt").write_text("\n".join(urls[b:b + BATCH]) + "\n")
print(f"sitemap={len(sitemap)} discovered={len(discovered)} union={len(urls)} "
      f"batches={(len(urls) + BATCH - 1) // BATCH}")
