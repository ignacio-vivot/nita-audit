"""Google autocomplete suggestions for question-style seed phrases (AEO Step 1).

Requests https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=<seed>
for each seed in the input file (format: audience<TAB>seed) and writes one row per
suggestion. Qualitative only: suggestions show phrasing, not search volume.

Usage: python3 -I autocomplete_questions.py <seeds.tsv> <output.csv>
"""
import csv
import json
import sys
import time
import urllib.parse
import urllib.request


def main():
    seeds = [l.rstrip("\n").split("\t") for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    with open(sys.argv[2], "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["audience", "seed", "rank", "suggestion"])
        for audience, seed in seeds:
            url = ("https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q="
                   + urllib.parse.quote(seed))
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            try:
                data = json.loads(urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace"))
                sugg = data[1]
            except Exception as e:
                sugg = [f"ERROR {e}"]
            for i, s in enumerate(sugg[:10], 1):
                w.writerow([audience, seed, i, s])
            if not sugg:
                w.writerow([audience, seed, 0, ""])
            time.sleep(1)


if __name__ == "__main__":
    main()
