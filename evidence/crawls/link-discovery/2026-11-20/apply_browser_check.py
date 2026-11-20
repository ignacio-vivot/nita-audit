"""Apply the 2026-11-20 browser check to the pending external links (SEO Step 2, part F).

The 459 URLs in nita-external-links-pending-validation.csv were inconclusive by
script. One sample URL per domain was opened in the Claude desktop app's built-in
browser (Chromium) from Argentina on 2026-11-20; on domains that loaded normally,
every pending URL was opened. Results are recorded below as observed (page title,
HTTP status, or browser error). Team rule (2026-11-20): a link that opens normally
in a browser is treated as working; links that fail definitively in the browser
(not found, certificate error, removed account, parked domain, unrelated generic
redirect) are treated as broken; everything else stays for review from the US.

Output: nita-external-links-browser-check.csv (one row per pending URL).
Usage: python3 -I apply_browser_check.py
"""
import csv

OK, DL = "ok", "ok-download"
NF, GEN, CERT, GONE, PARK, NITA403 = ("broken-not-found", "broken-generic-redirect", "broken-certificate",
                                     "broken-account-removed", "broken-domain-parked", "broken-nita-403")
BLOCK, NOLOAD, NOTCHK = "review-blocked", "review-did-not-load", "review-not-checked"

# Per-URL results (pages opened individually).
URL = {
 "https://www.facebook.com/NITAchicago/": (OK, "NITA Facebook page loads"),
 "https://www.facebook.com/ChicagoRTA": (GONE, "Facebook: \"This content isn't available right now\""),
 "https://www.facebook.com/ChicagoRTA/": (GONE, "Same page as /ChicagoRTA"),
 "http://www.facebook.com/ChicagoRTA": (GONE, "Same page as /ChicagoRTA"),
 "https://www.facebook.com/ChicagoRTA?v=wall": (GONE, "Same page as /ChicagoRTA"),
 "https://www.facebook.com/thecta": (OK, "Chicago Transit Authority page"),
 "https://www.facebook.com/thecta/": (OK, "Chicago Transit Authority page"),
 "https://www.facebook.com/pages/Chicago-Transit-Authority/134339103322388": (OK, "Redirects to facebook.com/thecta/"),
 "https://www.facebook.com/PaceBus": (OK, "Pace Suburban Bus page"),
 "https://www.facebook.com/AIHChicago/posts/save-the-date-our-pre-kwanzaa-celebration-marketplace-is-backjoin-africa-interna/1571434345014553/": (OK, "Post loads"),
 "https://www.facebook.com/hashtag/ihearttransit": (OK, "Hashtag page loads"),
 "https://www.apta.com/Pages/default.aspx": (OK, "Redirects to APTA homepage"),
 "https://www.apta.com/news-publications/public-transportation-facts/": (OK, "Redirects to Public Transportation Facts"),
 "http://www.apta.com/mediacenter/pressreleases/2016/Pages/160315_Shared-Use-Mobility.aspx": (GEN, "Redirects to unrelated \"Contact Congress\" page"),
 "http://www.apta.com/mediacenter/pressreleases/2017/Pages/September-Transit-Savings-Report-.aspx": (GEN, "Redirects to unrelated \"Contact Congress\" page"),
 "http://www.apta.com/mediacenter/pressreleases/2017/Pages/Transit-Savings.aspx": (GEN, "Redirects to unrelated \"Contact Congress\" page"),
 "http://www.apta.com/members/memberprogramsandservices/leadershipapta/Pages/default.aspx": (NF, "APTA \"Page not found\" (404)"),
 "http://www.apta.com/resources/reportsandpublications/Documents/APTA-Hidden-Traffic-Safety-Solution-Public-Transportation.pdf": (GEN, "Redirects to generic \"News & Research\" page"),
 "http://www.apta.com/resources/reportsandpublications/Documents/APTA-Shared-Mobility.pdf": (GEN, "Redirects to generic \"News & Research\" page"),
 "http://www.apta.com/resources/reportsandpublications/Documents/APTA_Health_Benefits_Litman.pdf": (GEN, "Redirects to generic \"News & Research\" page"),
 "https://www.apta.com/DocumentsNonMember/APTA_Calendar_2018_MedRes_Final.pdf": (NF, "APTA \"Page not found\" (404)"),
 "https://www.apta.com/news-publications/press-releases/releases/transit-workforce-shortage-root-causes-potential-solutions-and-the-road-ahead/": (GEN, "Redirects to generic \"Newsroom\" page"),
 "https://www.apta.com/research-technical-resources/research-reports/who-rides-public-transportation/": (GEN, "Redirects to generic \"News & Research\" page"),
 "https://www.apta.com/research-technical-resources/research-reports/transit-workforce-shortage/": (GEN, "Redirects to generic \"News & Research\" page"),
 "https://www.apta.com/wp-content/uploads/APTA-Bus-Manufacturing-Task-Force-Recommendations.pdf": (DL, "PDF offered as a download"),
 "https://www.transit.dot.gov/ASAP": (OK, "All Stations Accessibility Program page"),
 "https://www.transit.dot.gov/CIG": (OK, "Capital Investment Grants page"),
 "https://www.transit.dot.gov/about/news/us-department-transportation-announces-81-million-grant-award-purple-line-bus-rapid": (OK, "News release loads"),
 "https://www.transit.dot.gov/funding/grant-programs/capital-investments/about-program": (OK, "About the Program page"),
 "https://www.transit.dot.gov/funding/grants/fiscal-year-2016-low-or-no-emission-low-no-bus-program-projects": (OK, "Page loads"),
 "https://www.transit.dot.gov/funding/grants/grant-programs/all-stations-accessibility-program-fy22-23-projects": (OK, "Page loads"),
 "https://www.transit.dot.gov/funding/grants/low-or-no-emission-vehicle-program-5339c": (NF, "FTA \"Page not found\" (404)"),
 "https://www.transit.dot.gov/grant-programs/areas-persistent-poverty-program": (OK, "Page loads"),
 "https://www.transit.dot.gov/grant-programs/community-project-fundingcongressionally-directed-spending": (OK, "Page loads"),
 "https://www.transit.dot.gov/grant-programs/rail-vehicle-replacement-grants": (OK, "Page loads"),
 "https://www.transit.dot.gov/ntd/transit-agency-profiles": (OK, "Page loads"),
 "https://www.transit.dot.gov/regulations-and-programs/ccam/about/coordinating-council-access-and-mobility-ccam-federal-fund": (OK, "Redirects to CCAM Program Inventory"),
 "https://www.transit.dot.gov/sites/fta.dot.gov/files/2025-01/Third-Party-Contracting-Guidance-%28Circular-4220.1G%29.pdf": (NOTCHK, "PDF; not opened to avoid a download; curl blocked (403)"),
 "https://www.transit.dot.gov/sites/fta.dot.gov/files/docs/funding/procurement/8286/fta-best-practices-procurement-and-lessons-learned-manual-2016.pdf": (NOTCHK, "PDF; not opened to avoid a download; curl blocked (403)"),
 "https://www.transportation.gov/RAISEgrants": (OK, "Redirects to BUILD Grant Program page"),
 "https://www.transportation.gov/equity-Justice40": (GEN, "Redirects to the DOT homepage"),
 "https://www.transportation.gov/grants/mega-grant-program": (OK, "Page loads"),
 "https://www.transportation.gov/sustainability/climate/federal-programs-directory-congestion-mitigation-and-air-quality-cmaq": (NF, "DOT \"Page not found\" (404)"),
 "https://www.transportation.gov/sites/dot.gov/files/docs/BeyondTraffic_tagged_508_final.pdf": (NOTCHK, "PDF; not opened to avoid a download; curl blocked (403)"),
 "https://www.transportation.gov/sites/dot.gov/files/docs/Draft_Beyond_Traffic_Framework.pdf": (NOTCHK, "PDF; not opened to avoid a download; curl blocked (403)"),
 "http://www.chicagobusiness.com/article/20150806/BLOGS02/150809898/report-gets-it-half-right-on-emanuels-transportation-moves": (NF, "Crain's \"Page not found\" (404)"),
 "http://www.chicagobusiness.com/article/20150905/ISSUE07/309059998/letters-to-the-editor": (OK, "Article loads"),
 "http://www.chicagobusiness.com/article/20151012/BLOGS02/151019990/cubs-cardinals-cta-metra-divvy-boost-service-to-wrigley": (OK, "Article loads"),
 "http://www.chicagobusiness.com/article/20160419/BLOGS02/160419805/cta-in-line-for-100-million-for-red-line-north?utm_source=BLOGS02&utm_medium=rss&utm_campaign=chicagobusiness": (OK, "Article loads"),
 "http://www.chicagobusiness.com/article/20160922/BLOGS02/160929963/chicagoans-crush-on-cars-is-cooling": (NF, "Crain's \"Page not found\" (404)"),
 "http://www.chicagobusiness.com/article/20161130/BLOGS02/161139982/biggest-tif-in-city-history-gets-council-ok": (NF, "Crain's \"Page not found\" (404)"),
 "http://www.chicagobusiness.com/article/20170108/BLOGS02/170109892/cta-lands-1-1-billion-goodbye-grant-from-obama": (NF, "Crain's \"Page not found\" (404)"),
 "http://www.chicagobusiness.com/article/20171002/BLOGS02/171009976": (NF, "Crain's \"Page not found\" (404)"),
 "http://www.chicagobusiness.com/article/20180102/BLOGS02/180109988/whats-behind-chicagos-downtown-jobs-boom": (NF, "Crain's \"Page not found\" (404)"),
 "http://www.chicagobusiness.com/article/20180112/ISSUE07/180119943/guess-what-else-is-key-to-the-jobs-boom-public-transit": (NF, "Crain's \"Page not found\" (404)"),
 "http://www.chicagobusiness.com/article/20180316/ISSUE01/180319945/whats-making-traffic-worse-in-chicago-signs-point-to-uber-lyft": (NF, "Crain's \"Page not found\" (404)"),
 "https://www.chicagobusiness.com/greg-hinz-politics/how-covid-will-permanently-change-transit-ridership-chicago": (OK, "Article loads"),
 "https://bigmarsh.org/bike-programs/?doing_wp_cron=1750797308.9703860282897949218750": (NF, "Big Marsh \"Page not found\" (404)"),
 "https://bigmarsh.org/eco-recreation/": (OK, "Redirects to Eco-Recreation Programs"),
 "https://bigmarsh.org/faq/": (OK, "Redirects to FAQ"),
 "https://www.cdc.gov/": (OK, "CDC homepage"),
 "https://www.cdc.gov/policy/hst/hi5/index.html": (NF, "CDC \"Page Not Found\" (404)"),
 "https://www.cdc.gov/policy/hst/hi5/publictransportation/index.html": (NF, "CDC \"Page Not Found\" (404)"),
 "https://www.sheddaquarium.org/": (OK, "Homepage"),
 "https://www.sheddaquarium.org/programs-and-events/jazzin-at-the-shedd": (OK, "Page loads"),
 "https://www.sheddaquarium.org/shedd-pride-night": (OK, "Page loads"),
 "http://www.luriegarden.org/": (OK, "Homepage"),
 "https://www.luriegarden.org/": (OK, "Homepage"),
 "https://www.mta.info/budget/dedicated-taxes": (OK, "Redirects to MTA budget page"),
 "https://www.mta.info/document/176416": (NOTCHK, "Document link; not opened"),
 "https://www.smartcitiesdive.com/news/new-york-transit-agency-MTA-state-budget-deal-Hochul/649483/": (OK, "Article loads"),
 "https://www.smartcitiesdive.com/news/parking-under-pressure-why-3-cities-price-spots-based-on-demand/699726/": (OK, "Article loads"),
 "https://www.unitedcenter.com/": (OK, "Homepage"),
 "https://www.unitedcenter.com/events/": (OK, "Events page"),
 "http://www.twitter.com/RTA_Chicago": (GONE, "x.com/RTA_Chicago: \"This account doesn't exist\""),
 "https://rideonrtachicago.wpcomstaging.com/wp-content/uploads/2021/03/March-9-RTA-Webinar-Transcript.docx": (GONE, "WordPress.com: \"Active domain connection for this domain not found\" (403)"),
 "https://www.rtachicago.com/plans-programs/grants-projects/community-planning": (CERT, "https://www.rtachicago.com certificate expired (ERR_CERT_DATE_INVALID)"),
 "https://www.rtachicago.com/plans-programs/regional-transit-strategic-plan": (CERT, "https://www.rtachicago.com certificate expired (ERR_CERT_DATE_INVALID)"),
}

# Domain-level results from the sample URL (apply to every pending URL on the domain).
DOM = {
 # loaded normally (single pending URL, or all URLs on the domain share the sample result)
 "www.goodmantheatre.org": (OK, "Redirects to current A Christmas Carol page"),
 "www.grantparkmusicfestival.com": (OK, "Homepage"), "www.ssa.gov": (OK, "Homepage"),
 "www.womenandchildrenfirst.com": (OK, "Homepage"), "highways.dot.gov": (OK, "Article loads"),
 "napersettlement.org": (OK, "Page loads"), "www.napersettlement.org": (OK, "Page loads"),
 "northdusablelsd.org": (OK, "Page loads"), "wgnradio.com": (OK, "Redirects to the same article"),
 "www.aurora-il.org": (OK, "Redirects to City of Aurora homepage"), "www.bnd.com": (OK, "Article loads"),
 "www.centerforjewishlife.com": (OK, "Homepage"), "www.cfo.com": (OK, "Redirects to the same article"),
 "www.enterprisecarshare.com": (OK, "Redirects to homepage"), "www.fhwa.dot.gov": (OK, "Redirects to Carbon Reduction Program page"),
 "www.manta.com": (OK, "Page loads"), "www.orland-park.il.us": (OK, "Redirects to Village of Orland Park homepage"),
 "www.politico.com": (OK, "Article loads"), "www.village.homewood.il.us": (OK, "Homepage"),
 "seatgeek.com": (OK, "Page loads"), "thehill.com": (OK, "Article loads"),
 # definitive failures
 "access.umn.edu": (NF, "\"Page not found\" (404)"), "www.amtrak.com": (NF, "Amtrak 404"),
 "www.chicagoautoshow.com": (NF, "\"Page not found\" (404)"), "www.equiticity.org": (NF, "404"),
 "www.mchenrycountyil.gov": (NF, "404"),
 "www.cnt.org": (CERT, "ERR_CERT_COMMON_NAME_INVALID"), "betterstreetsforbuses.com": (CERT, "ERR_CERT_COMMON_NAME_INVALID"),
 "rsgresearch.com": (CERT, "ERR_CERT_COMMON_NAME_INVALID"), "www.czs.org": (CERT, "ERR_CERT_COMMON_NAME_INVALID"),
 "www.hullhousemuseum.org": (CERT, "ERR_CERT_COMMON_NAME_INVALID"), "voterguide.sfelections.org": (CERT, "ERR_CERT_COMMON_NAME_INVALID"),
 "www.heremagazine.com": (CERT, "ERR_CERT_DATE_INVALID (expired)"), "cmapbicycleusage.metroquest.com": (CERT, "ERR_CERT_DATE_INVALID (expired)"),
 "willconnects2040.metroquest.com": (CERT, "ERR_CERT_DATE_INVALID (expired)"),
 "rideonrtachicago.wpcomstaging.com": (GONE, "WordPress.com: \"Active domain connection for this domain not found\" (403)"),
 "www.chicagofashionfest.com": (PARK, "Redirects to a \"domain for sale\" page"),
 "www.westmontbbq.com": (PARK, "Redirects to a parked-domain page (ww16.westmontbbq.com)"),
 "www.rtachicago.org": (NITA403, "Redirects to a nita.illinois.gov /files/documents/ path that returns 403 Forbidden"),
 "www.rtachicago.com": (NITA403, "Redirects to a nita.illinois.gov /files/documents/ path that returns 403 Forbidden"),
 "rtachicago.org": (NITA403, "Redirects to a nita.illinois.gov /files/documents/ path that returns 403 Forbidden"),
 "rtachicago.com": (NITA403, "Redirects to a nita.illinois.gov /files/documents/ path that returns 403 Forbidden"),
 # blocked or challenged in the browser
 "www.rtams.org": (BLOCK, "Redirects to datahub.nita.illinois.gov; CloudFront 403 \"Request blocked\""),
 "rtams.org": (BLOCK, "Redirects to datahub.nita.illinois.gov; CloudFront 403 \"Request blocked\""),
 "uat.rtams.org": (BLOCK, "Redirects to uat-datahub.nita.illinois.gov; CloudFront error"),
 "datahub.nita.illinois.gov": (BLOCK, "CloudFront 403 \"Request blocked\""),
 "metrarail.com": (BLOCK, "CloudFront 504"), "www.metrarail.com": (BLOCK, "CloudFront 504"),
 "ridertools.metrarail.com": (BLOCK, "CloudFront 504"),
 "www.pacebus.com": (BLOCK, "Pace \"Access denied\" (403)"), "www.chicagoparkdistrict.com": (BLOCK, "\"Access denied\" (403)"),
 "www.ventrachicago.com": (BLOCK, "403, empty page"), "garfieldconservatory.org": (BLOCK, "Cloudflare challenge (403)"),
 "fpdcc.com": (BLOCK, "Cloudflare challenge (403)"), "activetrans.org": (BLOCK, "Cloudflare challenge (403)"),
 "www.activetrans.org": (BLOCK, "Cloudflare challenge (403)"), "www.bart.gov": (BLOCK, "Cloudflare challenge (403)"),
 "bikecommuterchallenge.org": (BLOCK, "Redirects to biketoworkchallenge.org; Cloudflare challenge"),
 "gispro2017.sched.com": (BLOCK, "Cloudflare challenge (403)"), "www.artic.edu": (BLOCK, "Cloudflare \"Attention Required\" (403)"),
 "www.bloomberg.com": (BLOCK, "Bloomberg \"Are you a robot?\""), "www.lcfpd.org": (BLOCK, "Cloudflare challenge (403)"),
 "blockclubchicago.org": (BLOCK, "\"Checking your browser\" (403)"), "chicagoreader.com": (BLOCK, "\"Checking your browser\" (403)"),
 "brookfieldil.gov": (BLOCK, "403 Forbidden"), "forgeparks.com": (BLOCK, "403 Forbidden"), "getairsports.com": (BLOCK, "403 Forbidden"),
 "journals.sagepub.com": (BLOCK, "Cloudflare challenge (403)"), "maywood-il.org": (BLOCK, "Redirects to maywood-il.gov; 403 Forbidden"),
 "mlb.mlb.com": (BLOCK, "403"), "mysouthshoreline.com": (BLOCK, "Sucuri firewall \"Access Denied\" (403)"),
 "www.mysouthshoreline.com": (BLOCK, "Sucuri firewall \"Access Denied\" (403)"), "roadtorock.org": (BLOCK, "Cloudflare challenge (403)"),
 "rules.house.gov": (BLOCK, "403"), "www.christkindlmarket.com": (BLOCK, "403 Forbidden"),
 "www.ahpd.org": (BLOCK, "403 Forbidden"), "www.axs.com": (BLOCK, "Cloudflare challenge (403)"),
 "www.clippercard.com": (BLOCK, "403"), "www.desplaines.org": (BLOCK, "Redirects to desplainesil.gov \"Error!\" page"),
 "www.dpparks.org": (BLOCK, "403 Forbidden"), "www.dupagecounty.gov": (BLOCK, "403 Forbidden"),
 "www.gfoa.org": (BLOCK, "Cloudflare challenge (403)"), "www.greencarreports.com": (BLOCK, "Cloudflare challenge (403)"),
 "www.kohlchildrensmuseum.org": (BLOCK, "403"), "www.lakecountyil.gov": (BLOCK, "Cloudflare \"Attention Required\" (403)"),
 "www.newpf.org": (BLOCK, "403"), "www.pjstar.com": (BLOCK, "402 (likely regional block)"), "www.sj-r.com": (BLOCK, "402 (likely regional block)"),
 "www.planetizen.com": (BLOCK, "Cloudflare \"Attention Required\" (403)"), "www.publicsource.org": (BLOCK, "\"Checking your browser\" (403)"),
 "www.qconline.com": (BLOCK, "Captcha \"Security Check\""), "www.sightline.org": (BLOCK, "Cloudflare challenge (403)"),
 "www.tripadvisor.com": (BLOCK, "403"), "www.urban.org": (BLOCK, "Cloudflare challenge (403)"), "www.vah.com": (BLOCK, "403 Forbidden"),
 "www.vibrantnotvacant.com": (BLOCK, "400 \"DisallowedHost\" server error"), "www.washingtonpost.com": (BLOCK, "\"Access Denied\" (403)"),
 "www.willcountyillinois.com": (BLOCK, "Redirects to willcounty.gov; Cloudflare \"Attention Required\""),
 "www.linkedin.com": (BLOCK, "LinkedIn sign-in wall"), "illinoisepi.files.wordpress.com": (BLOCK, "Redirects to illinoisupdate.com; file requires login (403)"),
 "chicago.metromix.com": (BLOCK, "503 Service Temporarily Unavailable"),
 # did not load in the browser
 "www.rtams.com": (NOLOAD, "Navigation failed"), "tinyurl.com": (NOLOAD, "Navigation failed"),
 "pulse.pacebus.com": (NOLOAD, "Navigation failed"), "rosemont.com": (NOLOAD, "Navigation failed"),
 "www.savetransitnow.org": (NOLOAD, "Navigation failed"), "savetransitnow.org": (NOLOAD, "Not opened; www host failed"),
 "www.trb.org": (NOLOAD, "Navigation failed"), "ebidexchange.com": (NOLOAD, "Navigation failed"),
 "www.ebidexchange.com": (NOLOAD, "Not opened; apex host failed"), "hpbrewfest.com": (NOLOAD, "Navigation failed"),
 "metratracker.com": (NOLOAD, "Navigation failed"), "aprpullmanportermuseum.org": (NOLOAD, "Navigation failed"),
 "hauntedtrailsburbank.com": (NOLOAD, "Navigation failed"), "take.lyft.com": (NOLOAD, "Navigation failed"),
 "tmweb.pacebus.com": (NOLOAD, "Navigation failed"), "www.chicagoclimateaction.org": (NOLOAD, "Navigation failed"),
 "www.dhbusinessledger.com": (NOLOAD, "Navigation failed"), "www.projectaction.org": (NOLOAD, "Navigation failed"),
 "www.sheffieldgardenwalk.com": (NOLOAD, "Navigation failed"),
 # not checked
 "ilga.gov": (NOTCHK, "Navigation not permitted in the audit browser"), "www.ilga.gov": (NOTCHK, "Navigation not permitted in the audit browser"),
 "www.nytimes.com": (NOTCHK, "Site not allowed in the audit browser"),
 "gcc02.safelinks.protection.outlook.com": (NOTCHK, "Outlook Safe Links wrapper; not opened"),
}


def main():
    rows = list(csv.DictReader(open("nita-external-links-pending-validation.csv")))
    missing = set()
    with open("nita-external-links-browser-check.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "domain", "script_status", "links", "linking_pages", "first_found_on", "browser_result", "browser_note"])
        for r in rows:
            u, h = r["url"], r["url"].split("/")[2].lower()
            res = URL.get(u) or DOM.get(h)
            if res is None:
                missing.add(h)
                res = (NOTCHK, "")
            w.writerow([u, h, r["script_status"], r["links"], r["linking_pages"], r["first_found_on"], res[0], res[1]])
    if missing:
        print("unmapped domains:", sorted(missing))


if __name__ == "__main__":
    main()
