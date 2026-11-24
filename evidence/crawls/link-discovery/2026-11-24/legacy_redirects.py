"""List internal content links to former RTA paths that redirect to a section overview
page, with the current page on the same subject where one exists (SEO Step 3, part D).

Inputs: nita-internal-link-edges.csv (gunzip the .gz) and the 2026-11-19 B1 pages.csv
(status and redirect location). EQUIVALENT maps former paths to current pages
identified by reviewing page titles and the B1 inventory; every mapped page returned
200 in B1.

Usage: python3 -I legacy_redirects.py <edges_csv> <b1_pages_csv> <output_csv>
"""
import csv
import sys
from collections import Counter, defaultdict

BASE = "https://nita.illinois.gov"
SECTION_PAGES = {BASE + p for p in ("/communities", "/riders", "/transit-funding", "/about-rta", "/about-nita", "/riders/how-to-ride")}
EQUIVALENT = {
    "/plans-programs/access-transit-program": "/communities/access-to-transit-program",
    "/plans-programs/community-planning": "/communities/community-planning",
    "/plans-programs/grants-projects/community-planning": "/communities/community-planning",
    "/plans-programs/programs-and-projects/section-5310-enhanced-mobility-seniors-and-individuals": "/region/section-5310",
    "/plans-programs/programs-and-projects/section-5310": "/region/section-5310",
    "/rider-resources/rta-fare-programs": "/riders/free-and-reduced-fare-programs",
    "/rider-resources/reduced-fare/ride-free-permits": "/riders/free-and-reduced-fare-programs",
    "/rider-resources/rta-fare-programs/reduced-fare-permits": "/riders/free-and-reduced-fare-programs",
    "/rider-resources/reduced-fare/reduced-fare-permits": "/riders/free-and-reduced-fare-programs",
    "/rider-resources/reduced-fare/reduced-fare": "/riders/free-and-reduced-fare-programs",
    "/plan-your-trip/travel-tips/paying-your-ride": "/riders/paying-for-your-ride",
    "/finance-management/investor-relations/investor-relations": "/about-nita/investor-relations",
    "/about-us/careers": "/careers",
    "/about-us/board-meetings": "/about-nita/boards-and-committees",
    "/about-us/board-meetings/meetings-archive": "/about-nita/boards-and-committees/meeting-materials",
    "/about-us/media/press-release-archives/2021-press-releases/transit-ridership-survey-reveals":
        "/about-rta/press-releases/transit-ridership-survey-reveals-challenges-for-chicago-region-in-covids-wake",
    "/about-us/media/press-release-archives/2017-press-releases/rta-gets-creative-2017-promote-transit":
        "/about-rta/press-releases/rta-gets-creative-in-2017-to-promote-transit-ridership",
    "/about-us/media/press-release-archives/2022-press-releases/chicagolands-regional-transit-system":
        "/about-rta/press-releases/chicagolands-regional-transit-system-breaks-pandemic-ridership-records",
    "/about-us/media/press-release-archives/2020-press-releases/rta-launches-online-dashboard-showing":
        "/about-rta/press-releases/rta-launches-online-dashboard-showing-covid-19-effects-on-regional-transit-network",
}


def main():
    edges_csv, pages_csv, out = sys.argv[1], sys.argv[2], sys.argv[3]
    pages = {r["url"]: r for r in csv.DictReader(open(pages_csv))}
    st = defaultdict(lambda: [0, set(), Counter()])
    for e in csv.DictReader(open(edges_csv)):
        if e["region"] != "body":
            continue
        p = pages.get(e["target_url"])
        if p and p["status"] == "301" and p["location"].rstrip("/") in SECTION_PAGES:
            s = st[e["target_url"]]
            s[0] += 1
            s[1].add(e["source_url"])
            s[2][e["anchor_text"][:80]] += 1
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["legacy_url", "redirects_to_b1", "final_destination", "body_link_instances", "linking_pages",
                    "sample_linking_page", "sample_anchor_text", "equivalent_current_page"])
        for u, v in sorted(st.items(), key=lambda x: -x[1][0]):
            loc = pages[u]["location"]
            final = pages.get(loc, {}).get("location") or loc
            path = u[len(BASE):]
            w.writerow([u, loc, final, v[0], len(v[1]), sorted(v[1])[0], v[2].most_common(1)[0][0],
                        BASE + EQUIVALENT[path] if path in EQUIVALENT else ""])


if __name__ == "__main__":
    main()
