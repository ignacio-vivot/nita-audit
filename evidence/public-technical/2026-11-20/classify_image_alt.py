"""Classify alt text in image-alt-review.csv (SEO Step 2, part F).

Rewrites the `assessment` column with a rule-based label:
  empty-alt              alt="" (decorative image)
  url-as-alt             alt is a URL
  outdated-brand         NITA logo file with alt "RTA"
  library-caption        alt holds photo-library caption text ("IMAGE LIBRARY")
  filename-derived       alt equals the file name with separators turned into spaces
                         (also after the CMS replaced "RTA" with "NITA"); compared
                         case-insensitively on letters and digits only, after
                         removing the CMS upload suffix (_YYYY-MM-DD-HHMMSS_xxxx)
  text-alt               any other text; descriptive quality judged manually
Usage: python3 -I classify_image_alt.py image-alt-review.csv
"""
import csv
import re
import sys
from pathlib import PurePosixPath
from urllib.parse import unquote, urlsplit


def key(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def classify(src, alt):
    a = alt.strip()
    stem = PurePosixPath(unquote(urlsplit(src).path)).stem
    stem = re.sub(r"_\d{4}-\d{2}-\d{2}-\d{6}_[a-z0-9]{4}$", "", stem)
    if a == "":
        return "empty-alt"
    if re.match(r"https?://", a):
        return "url-as-alt"
    if "nita-logo" in src and a == "RTA":
        return "outdated-brand"
    if "IMAGE LIBRARY" in a.upper():
        return "library-caption"
    k = key(a)
    if k in (key(stem), key(stem.replace("RTA", "NITA"))):
        return "filename-derived"
    return "text-alt"


def main():
    path = sys.argv[1]
    rows = list(csv.DictReader(open(path)))
    fields = list(rows[0].keys())
    for r in rows:
        r["assessment"] = classify(r["img_src"], r["alt"])
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
