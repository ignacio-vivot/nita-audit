"""Check the status of external links found on NITA (SEO Step 2, part F).

Input: links_external.csv from the 2026-11-19 link-discovery run (unique external
URLs and the first NITA page linking to each). Each URL is requested with HEAD;
if HEAD fails or returns 4xx/5xx, it is retried with GET. Redirects are followed
and the final URL is recorded. Requests are sequential with a fixed delay.

Usage: python3 -I external_link_check.py <links_external.csv> <output_csv> [delay]
"""
import csv
import ssl
import sys
import time
import urllib.error
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36 seo-audit-link-check")


def fetch(url, method):
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.geturl(), ""
    except urllib.error.HTTPError as e:
        return e.code, e.geturl() if hasattr(e, "geturl") else url, ""
    except ssl.SSLError as e:
        return 0, url, f"ssl: {e}"
    except Exception as e:
        return 0, url, f"{type(e).__name__}: {e}"


def main():
    src, out = sys.argv[1], sys.argv[2]
    delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.2
    rows = list(csv.DictReader(open(src)))
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "first_found_on", "status", "final_url", "method", "error"])
        for i, r in enumerate(rows, 1):
            u = r["url"]
            status, final, err = fetch(u, "HEAD")
            method = "HEAD"
            if status == 0 or status >= 400:
                status, final, err = fetch(u, "GET")
                method = "GET"
            w.writerow([u, r["first_found_on"], status, final if final != u else "", method, err[:200]])
            if i % 200 == 0:
                print(f"{i}/{len(rows)}", flush=True)
            time.sleep(delay)


if __name__ == "__main__":
    main()
