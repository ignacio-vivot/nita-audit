"""Apply the 2026-11-24 US check to the 315 external URLs left for review on 2026-11-20
(SEO Step 2 part F follow-up, SEO-NITA-018).

All checks ran through a US connection with a Chicago, Illinois IP address
(connection.txt). Steps:
1. us-script-status.csv: external_link_check.py (2026-11-20 folder) on the 315 URLs.
   200 = opens; 404 = not found.
2. For the other results, each site was opened in the Claude desktop app's built-in
   browser (Chromium). Where the website's homepage loaded, the remaining URLs on that
   website were requested from the same page (same-origin fetch), which also checks
   PDFs without downloading them. Bot challenges (Cloudflare, Akamai) were not solved.
3. DNS lookups with dig for hosts that did not respond.

Team rule (2026-11-20): a link that opens normally in a browser is working; definitive
failures are broken; anything that could not be confirmed stays for review.

Outputs: us-check-results.csv (one row per URL) and
nita-external-links-browser-check-merged.csv (the 2026-11-20 browser check with the
315 review rows replaced by the US result), used as the fourth argument of
classify_external_links.py.
Usage: python3 -I apply_us_check.py
"""
import csv
from urllib.parse import urlsplit

OK, DL = "ok", "ok-download"
NF, GEN, NODNS, NORESP, SERVER, DENIED, FORBID = (
    "broken-not-found", "broken-generic-redirect", "broken-no-dns", "broken-no-response",
    "broken-server-error", "broken-access-denied", "broken-forbidden")
BLOCK, LOGIN, NOTCHK, TEMP = "review-blocked", "review-login", "review-not-checked", "review-temporary-error"

# Per-URL results.
URL = {
    "https://www.ventrachicago.com/eventscalendar/": (GEN, "Redirects to the Ventra homepage"),
    "https://maywood-il.org/Departments/City-Clerk/Resolutions/2022/R-2022-16.aspx": (GEN, "Redirects to the maywood-il.gov homepage"),
    "http://tinyurl.com/SurveyRTA.": (NF, "TinyURL 404 (trailing period in the link)"),
    "http://tinyurl.com/qgoa675.": (NF, "TinyURL 404 (trailing period in the link)"),
    "http://tinyurl.com/ngwdncr": (NF, "Redirects to a chicago.gov AccessChicago 2012 page that returns 404"),
    "https://tinyurl.com/lk3j4dv": (NODNS, "Redirects to events.r20.constantcontact.com, which no longer resolves"),
    "http://tinyurl.com/abhjd5g": (OK, "Redirects to the Chicago Blues Festival page on chicago.gov (200)"),
    "http://tinyurl.com/ov36ajy": (OK, "Redirects to neighborsofwestloop.com festival page (200)"),
    "http://tinyurl.com/pqgtmjl": (OK, "Redirects to auroragreenfest.com page (200)"),
    "http://tinyurl.com/psw48vq": (BLOCK, "Redirects to a WordPress-hosted PDF that returns 403 to automated requests"),
    "http://chicago.metromix.com/": (SERVER, "Browser: 503 Service Temporarily Unavailable"),
    "http://hpbrewfest.com/": (GEN, "Redirects to hydeparksummerfest.com homepage, which did not load"),
    "https://ebidexchange.com/Default.aspx?cid=fea19256-6318-46d1-9c7a-d7e5a74935eb": (NOTCHK, "Redirects to procureware.com; not opened in the browser"),
    "https://www.ebidexchange.com/RegUser.aspx?cid=fea19256-6318-46d1-9c7a-d7e5a74935eb&uid=00000000-0000-0000-0000-000000000000": (NOTCHK, "Redirects to procureware.com; not opened in the browser"),
    "https://gispro2017.sched.com/": (TEMP, "Browser: Sched 503 “We'll be back in a minute”"),
    "http://mlb.mlb.com/fan_forum/greeting_card.jsp?c_id=cws": (FORBID, "Browser: plain 403 page, no bot challenge"),
    "http://take.lyft.com/friendswithtransit/": (FORBID, "Browser: 403 Forbidden, no bot challenge"),
    "http://www.dhbusinessledger.com/Content/Default/Homepage-Rotating-Articles/Article/Newsmakers-Despite-state-budget-cloud-business-poised-to-grow-in-2016/-3/303/17328": (NODNS, "Domain no longer resolves (dig)"),
    "http://www.newpf.org/freda-johnson-award": (BLOCK, "Script 403; the browser could not open the page"),
    "http://www.projectaction.org/Initiatives/YouthTransportation/TransportationEducationCurriculum.aspx": (OK, "200 on a second request"),
    "http://www.sheffieldgardenwalk.com/content/chicago-craft-beer-festival": (NORESP, "Connection closed by the server on every request"),
    "http://www.chicagoclimateaction.org/": (NORESP, "No response in the browser or by script"),
    "https://aprpullmanportermuseum.org/": (NORESP, "TLS error by script; the browser could not open the site"),
    "https://www.willcountyillinois.com/County-Offices/Special-Services/Will-Ride-Dial-A-Ride": (NORESP, "Timed out by script; the browser could not open the site"),
    "https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.apta.com%2FEquityPilot&data=05%7C01%7CJessica.Cabe%40RTACHICAGO.ORG%7C03ecd6efb65e41666af608da23b14f60%7Ca62b6cc678c04816a85c6b474f28b3b3%7C0%7C0%7C637861541698410499%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=NYKibT%2FD5h0HvOBfgoZT3vbCZmLfFj1x4LIBe37hjIo%3D&reserved=0": (DL, "Destination apta.com/EquityPilot serves a file download"),
    "https://illinoisepi.files.wordpress.com/2018/05/passing-the-buck-capital-funding-needs-final.pdf": (BLOCK, "Redirects to illinoisupdate.com, 403 to automated requests"),
    "https://journals.sagepub.com/doi/pdf/10.1177/03611981211017900": (BLOCK, "Browser: Cloudflare challenge"),
    "https://rtams.org/dataset/covid-19-transit-dashboard": (DENIED, "Redirects to datahub.nita.illinois.gov; NITA “Access denied” page (403)"),
    "https://rules.house.gov/sites/democrats.rules.house.gov/files/BILLS-116HR133SA-RCP-116-68.pdf": (FORBID, "403 from the website while its homepage loads"),
    "https://www.chicagoparkdistrict.com/events/family-fishing-douglass": (DENIED, "Chicago Park District “Access denied” page (403); homepage loads"),
    "https://www.desplaines.org/access-your-government/city-departments/community-and-economic-development/comprehensive-plan": (NF, "Redirects to desplainesil.gov, which returns 404"),
    "https://www.mta.info/document/176416": (OK, "200 on a second request"),
    "https://www.planetizen.com/news/2022/11/119603-van-ness-bus-rapid-transit-boosts-ridership-san-francisco": (OK, "Browser: article loads"),
    "https://www.vibrantnotvacant.com/": (SERVER, "Browser: 400 “DisallowedHost” server configuration error"),
    "https://www.tripadvisor.com/Restaurant_Review-g35805-d429089-Reviews-Margie_s_Candies-Chicago_Illinois.html": (BLOCK, "Browser: 403 bot protection"),
    "https://www.sightline.org/2021/01/28/more-parking-isnt-harmless-it-actually-makes-us-drive-more/": (BLOCK, "Browser: Cloudflare challenge"),
    "https://www.washingtonpost.com/news/dr-gridlock/wp/2016/04/06/heres-what-metro-could-learn-from-chicagos-experience-in-shutting-down-part-of-its-subway/": (BLOCK, "Browser: Akamai “Access Denied”"),
    "https://www.pjstar.com/story/news/politics/county/2015/07/16/peoria-city-council-reviews-waiver/33867791007/": (BLOCK, "Browser: 402 with an empty page"),
    "http://www.sj-r.com/opinion/20160507/letter-state-shouldnt-raid-transportation-funds": (BLOCK, "Browser: 402 with an empty page"),
    "https://roadtorock.org/upcoming-events/": (BLOCK, "Browser: Cloudflare challenge"),
    "https://www.axs.com/venues/127743/radius-chicago-tickets?skin=radius": (BLOCK, "Browser: Cloudflare challenge"),
}

# Per-host results for URLs not listed above.
HOST = {
    "www.pacebus.com": (DENIED, "Pace “Access denied” page (403) for this page; pacebus.com/fares and /paratransit load"),
    "ilga.gov": (OK, "Opens (browser and same-origin request)"),
    "www.ilga.gov": (OK, "Opens (browser and same-origin request)"),
    "metrarail.com": (SERVER, "CloudFront 504: the former Metra domain no longer reaches a server"),
    "www.metrarail.com": (SERVER, "CloudFront 504: the former Metra domain no longer reaches a server"),
    "ridertools.metrarail.com": (SERVER, "CloudFront 504: the former Metra domain no longer reaches a server"),
    "www.rtams.com": (NORESP, "Timed out by script; the browser could not open the site"),
    "savetransitnow.org": (NORESP, "Timed out by script; the browser could not open the site"),
    "www.savetransitnow.org": (NORESP, "Timed out by script; the browser could not open the site"),
    "pulse.pacebus.com": (NORESP, "Network unreachable by script; the browser could not open the site"),
    "www.trb.org": (NOTCHK, "Redirect loop by script; the browser could not open the site"),
    "activetrans.org": (BLOCK, "Browser: Cloudflare challenge"),
    "www.activetrans.org": (BLOCK, "Browser: Cloudflare challenge"),
    "www.artic.edu": (BLOCK, "Browser: Cloudflare “Attention Required”"),
    "www.lcfpd.org": (BLOCK, "Browser: Cloudflare challenge"),
    "www.bloomberg.com": (BLOCK, "Browser: “Are you a robot?” check"),
    "www.linkedin.com": (LOGIN, "Browser: LinkedIn sign-in wall"),
    "www.nytimes.com": (NOTCHK, "Site not opened in the audit browser"),
    "www.transit.dot.gov": (OK, "PDF returns 200 (same-origin request)"),
    "www.transportation.gov": (OK, "PDF returns 200 (same-origin request)"),
}


def main():
    review = [r for r in csv.DictReader(open("../../2026-11-20/nita-external-links-browser-check.csv"))
              if r["browser_result"].startswith("review-")]
    script = {r["url"]: r for r in csv.DictReader(open("us-script-status.csv"))}
    results = {}
    with open("us-check-results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "domain", "links", "linking_pages", "first_found_on", "result_2026_11_20",
                    "us_script_status", "us_final_url", "us_result", "us_note"])
        for r in review:
            u = r["url"]
            s = script[u]
            if u in URL:
                res, note = URL[u]
            elif s["status"] == "200":
                res, note = OK, "200" + (f" after redirect to {s['final_url']}" if s["final_url"] else "")
            elif s["status"] == "404":
                res, note = NF, "404" + (f" at {s['final_url']}" if s["final_url"] else "")
            else:
                res, note = HOST.get(urlsplit(u).hostname, (NOTCHK, "No result recorded"))
            results[u] = res
            w.writerow([u, r["domain"], r["links"], r["linking_pages"], r["first_found_on"], r["browser_result"],
                        s["status"], s["final_url"], res, note])
    rows = list(csv.DictReader(open("../../2026-11-20/nita-external-links-browser-check.csv")))
    with open("nita-external-links-browser-check-merged.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            if r["url"] in results:
                r["browser_result"] = results[r["url"]]
                r["browser_note"] = "US check 2026-11-24 (see us-check-results.csv)"
            w.writerow(r)


if __name__ == "__main__":
    main()
