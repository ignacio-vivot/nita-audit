"""Assess the questions with missing, scattered, partial, or link-only answers (AEO Step 3, part B).

Joins the answer map (../../2026-11-25/answer-map/answer-map.csv), the answer-feature
captures of Step 2 part C (../answer-features/google-answer-features-2026-11-26.jsonl) and of
this part (google-gap-questions-2026-11-26.jsonl, queries in gap-queries.tsv), and the
reviewer's assessment of each gap question (G below), and writes question-gaps.csv with,
per question:
- the answer-map status and the page that should answer it;
- where the answer is found today, on the website or elsewhere on the same domain;
- the recommended location for a direct answer (an existing section, a short question
  block on the program page, or a new section), without proposing new pages where a
  section would do;
- the Google query captured for it, the ranks of NITA or My Transit Benefit pages in the
  first organic results (matched on the displayed URL), whether the AI Overview lists them
  as a source (matched on the source labels), and the first three other sources;
- the related finding.

Usage: python3 -I question_gaps.py
"""
import csv
import json
import re

OWN = {"nita.illinois.gov": re.compile(r"nita\.illinois\.gov"),
       "mytransitbenefit.com": re.compile(r"mytransitbenefit\.com")}
# A source label names the website itself ("Northern Illinois Transit Authority (.gov)",
# "NITA Community Planning") or one of its pages ("… | Northern Illinois Transit Authority",
# "Northern Illinois Transit Authority | …").
# Labels that only mention the agency or the act ("FACT SHEET: Northern Illinois Transit
# Authority Act", "Illinois Department of Revenue NITA Tax Bulletin") do not count.
OWN_LABEL = {"nita.illinois.gov": re.compile(r"^Northern Illinois Transit Authority( \(\.gov\))?$|^Northern Illinois Transit Authority \||\| Northern Illinois Transit\b|^NITA (?!Transit Benefit)[^|]*$"),
             "mytransitbenefit.com": re.compile(r"mytransitbenefit|NITA Transit Benefit")}

# question_id: (where the answer is today, recommended location, related finding)
G = {
    "Q-NITA-13": ("Ride Free Permits section (Benefit Access enrollment, no age stated) and the closed “Senior Reduced Fare” accordion (65 and over); the only senior FAQ on the domain is the 2011 RTA press release “Senior Ride Free FAQs”, which describes the former Circuit Breaker program.",
                  "Two or three sentences at the top of Discounted Fare and Ride Free Programs that answer the senior question in one place; archive note on the 2011 press release.", "AEO-NITA-004"),
    "Q-NITA-14": ("The Registration Sites menu link redirects to an ArcGIS locator; the page text names only the four City of Chicago sites, in the alerts accordion.",
                  "One sentence near the locator link saying how many sites there are and what can be done there.", "Not a finding (link to a working locator)"),
    "Q-NITA-20": ("The service definition (“unable to use CTA or Pace fixed route transit service for some or all of their trip”) and the closed “Types of Eligibility” accordion.",
                  "A “Who qualifies for ADA Paratransit?” passage after the ADA Paratransit description, before the application steps (with AEO-NITA-001).", "AEO-NITA-004"),
    "Q-NITA-22": ("Not stated; the page describes an origin-to-destination service without saying that trips may be for any purpose.",
                  "One sentence in the ADA Paratransit section: rides can be for any purpose (49 CFR 37.131(d)).", "AEO-NITA-004"),
    "Q-NITA-24": ("“Use the trip planner to find the best transit route for your trip.” and the embedded tool (UX-NITA-008).",
                  "Keep the tool; add one sentence with the phone option (Travel Information Center) under “Plan your ride”.", "AEO-NITA-004"),
    "Q-NITA-25": ("Contact table only (“NITA Travel Information | 312-836-7000”), without hours.",
                  "Number and hours under “Plan your ride” on How to ride and on Riders.", "AEO-NITA-004"),
    "Q-NITA-29": ("About NITA links the Public Act 104-0457 PDF; Moving the system says the Governor signed the act in December 2025; the Funding page says the act passed “in the early morning hours of October 31” (no year); the board summary PDF gives June 1, 2026 as the effective date and September 1, 2026 as the end of RTA Board terms.",
                  "A short “The NITA Act” section on About NITA: what the act does, when it was signed, when it took effect, and when NITA replaced the RTA.", "AEO-NITA-005"),
    "Q-NITA-30": ("Closed “Sales tax” and “State 5.0% Sales Tax on Gasoline” accordions on Moving the system; the rates there (1.25% Cook, .50% collar counties, plus a “New 2026 0.25%”) do not match the Illinois Department of Revenue bulletin FY 2026-34 (1.25%/1.50% Cook, 1.00% collar counties since August 1, 2026).",
                  "A visible “Where does the new funding come from?” passage on Moving the system with the current rates and their effective date, linked from About NITA and the Funding page.", "AEO-NITA-005"),
    "Q-NITA-37": ("Funding page tabs (“What is operating funding?”, “What is capital funding?”) and the November 2025 blog post; no dated summary of the fiscal cliff or of the new revenue sources.",
                  "Same as Q-NITA-30: one dated passage on the new funding, linked from the Funding page.", "AEO-NITA-005"),
    "Q-NITA-40": ("Program description and 2026 awards; no eligibility, timing, or application steps; Google lists a NITA PDF titled “ACCESS TO TRANSIT PROGRAM” (…/general/ProgramGuide) that the page does not link.",
                  "A short “Who can apply and when” section on the program page, linking the program guide.", "AEO-NITA-006"),
    "Q-NITA-41": ("Program description and 2026 projects; the application window (through April 17, 2026) and the online form are only in the April 1, 2026 blog post, which the program page does not link.",
                  "A short “Who can apply and when” section on the program page, updated for each call for projects.", "AEO-NITA-006"),
    "Q-NITA-42": ("Program definition, funded projects, and the local match rules; who can apply and when are only in the linked Program Management Plan PDF.",
                  "Two sentences on eligible applicants and the call schedule above the Program of Projects.", "AEO-NITA-006"),
    "Q-MTB-01": ("No passage; see AEO-MTB-002.", "Opening passage under the H1 (AEO-MTB-002).", "AEO-MTB-002"),
    "Q-MTB-06": ("Employees says to ask the employer to enroll and links the Employee Login; enrollment depends on the employer's ordering model, described only in the employer Account Setup Guide PDF.",
                  "A short “How to enroll” passage on Employees: check whether your employer participates, then order through the employer or the Employee Login.", "AEO-MTB-003"),
    "Q-MTB-08": ("Behind the Benefits has three product headings (“The RTA/NITA Transit Benefit Prepaid Mastercard®”, “Ventra® Direct Loads”, “Pace Vanpool”) with empty panels; the employer guide PDF describes the three products.",
                  "Fill the three product sections with the guide's descriptions.", "AEO-MTB-003"),
    "Q-MTB-09": ("Not stated on the website; the employer guide lists credit-adjustment options, including funds “Returned only upon employee termination”.",
                  "One question-and-answer on Employees about unused funds and leaving a job, confirmed with the program team.", "AEO-MTB-003"),
    "Q-MTB-10": ("Empty “Prepaid Mastercard” and “Ventra® Direct Loads” panels; the employer guide explains both; Google also uses a 2013 RTA press release on nita.illinois.gov.",
                  "Fill the product sections; one question-and-answer on Employees about using the card or Ventra.", "AEO-MTB-003"),
    "Q-MTB-13": ("Steps only in the Account Setup Guide PDF linked from Employers.",
                  "A three- or four-step summary on Employers with the PDF as detail.", "AEO-MTB-003"),
    "Q-MTB-15": ("Not stated on the website; the employer guide gives a $0.00 monthly fee for ACH debit and 4% of the total order for credit cards.",
                  "One sentence on Employers stating the fees.", "AEO-MTB-003"),
}


def load_captures():
    caps = {}
    for path in ("../answer-features/google-answer-features-2026-11-26.jsonl", "google-gap-questions-2026-11-26.jsonl"):
        for line in open(path, encoding="utf-8"):
            o = json.loads(line)
            caps[o["query"]] = o
    return caps


def queries():
    q = {}
    for path in ("../answer-features/queries.tsv", "gap-queries.tsv"):
        for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"):
            q[r["question_id"]] = r["query"]
    return q


def main():
    amap = {r["question_id"]: r for r in csv.DictReader(open("../../2026-11-25/answer-map/answer-map.csv", encoding="utf-8"))}
    caps, qs = load_captures(), queries()
    with open("question-gaps.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["question_id", "website", "question", "answer_map_status", "answer_page", "where_the_answer_is_today",
                    "recommended_location", "google_query_2026_11_26", "captured_utc", "own_site_ranks_in_first_results",
                    "own_site_listed_as_ai_overview_source", "other_ai_overview_sources", "related"])
        for qid, (now, rec, rel) in G.items():
            m = amap[qid]
            site = m["website"]
            query = qs.get(qid, "")
            c = caps.get(query)
            ranks = cited = others = when = ""
            if c:
                when = c["captured_utc"]
                ranks = "; ".join(f'{r["rank"]} ({r["title"]})' for r in c["top_results"] if OWN[site].search(r["cite"])) or "none"
                labels = (c.get("ai_overview") or {}).get("source_labels", [])
                cited = "yes" if any(OWN_LABEL[site].search(s) for s in labels) else "no"
                own_titles = [r["title"].rstrip(". …") for r in c["top_results"] if OWN[site].search(r["cite"])]
                seen = []
                for s in labels:
                    if OWN_LABEL[site].search(s) or any(t and s.startswith(t) for t in own_titles):
                        continue
                    key = s.split(" · ")[0].split(" | ")[0].replace(" (.gov)", "")
                    key = key[4:] if key.startswith("The ") else key
                    if key not in seen:
                        seen.append(key)
                others = "; ".join(seen[:3])
            w.writerow([qid, site, m["question"], m["answer_status"], m["answer_page"], now, rec, query, when, ranks, cited, others, rel])


if __name__ == "__main__":
    main()
