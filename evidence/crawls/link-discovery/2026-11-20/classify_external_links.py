"""Classify NITA external links with a non-2xx/3xx result (SEO Step 2, part F).

Inputs: nita-external-link-status.csv and nita-external-broken-link-edges.csv.
Output: nita-external-link-classification.csv, one row per external URL with
status 0 or >= 400, with the number of links and linking pages and a label:
  confirmed-not-found   the server answered 404 or 410
  confirmed-no-dns      the host does not resolve (rechecked on 2026-11-20 with
                        dig against 1.1.1.1; hosts that resolved are pending)
  confirmed-bad-cert    blog.rtachicago.org: certificate does not match the host
                        (confirmed in a browser on 2026-11-20)
  pending-validation    403, 400, 402, 429, 5xx, 999, timeouts, refused
                        connections, other TLS errors, and hosts that resolved on
                        recheck; these need validation by another method
Usage: python3 -I classify_external_links.py <status_csv> <edges_csv> <output_csv>
"""
import csv
import sys
from collections import defaultdict
from urllib.parse import urlsplit

NO_DNS = {
    "bashonwabash.org", "bbysgrleg4y", "drupal.rtachicago.org", "gettingamericatowork.com",
    "gettingamericatowork.org", "illinoistransportationsymposium.com", "kimballcurb.org",
    "lagrangeforward.org", "lgpetparade.org", "rideonrtachicago.com", "shoup.bol.ucla.edu",
    "tripplanner.rtachicago.com", "tripplanner.rtachicago.org", "tripsweb.rtachicago.com",
    "web.rtachicago.org", "www.57thstreetartfair.org", "www.blog.rtachicago.org",
    "www.chariot.com", "www.downtownpartners.com", "www.drivelesslivemore.com",
    "www.getonboardil.org", "www.gettingamericatowork.com", "www.gettingamericatowork.org",
    "www.illinoistransportationsymposium.com", "www.lagrangeendlesssummerfest.com",
    "www.lessstaxingcommute.com", "www.willconnects2040.org",
}


def label(url, status, error):
    host = (urlsplit(url).hostname or "").lower()
    if status in ("404", "410"):
        return "confirmed-not-found"
    if status == "0" and "nodename" in error and host in NO_DNS:
        return "confirmed-no-dns"
    if status == "0" and "CERTIFICATE_VERIFY_FAILED" in error and host == "blog.rtachicago.org":
        return "confirmed-bad-cert"
    return "pending-validation"


def main():
    status_csv, edges_csv, out = sys.argv[1:4]
    links, pages = defaultdict(int), defaultdict(set)
    for r in csv.DictReader(open(edges_csv)):
        links[r["target_url"]] += 1
        pages[r["target_url"]].add(r["source_url"])
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "status", "error", "final_url", "classification", "links", "linking_pages", "first_found_on"])
        for r in csv.DictReader(open(status_csv)):
            s = int(r["status"])
            if s and s < 400:
                continue
            u = r["url"]
            w.writerow([u, r["status"], r["error"][:80], r["final_url"],
                        label(u, r["status"], r["error"]), links[u], len(pages[u]), r["first_found_on"]])


if __name__ == "__main__":
    main()
