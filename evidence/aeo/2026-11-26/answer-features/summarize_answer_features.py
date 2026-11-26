"""Summarize the answer-feature capture for the 20 priority questions (AEO Step 2, part C).

Joins queries.tsv, google-answer-features-2026-11-26.jsonl (browser capture), and the
answer map (../../2026-11-25/answer-map/answer-map.csv), and writes
answer-features-summary.csv with, per question:
- whether an AI Overview and a featured snippet were shown;
- the ranks of NITA or My Transit Benefit pages among the first organic results
  (matched on the displayed URL only);
- whether the AI Overview lists NITA or My Transit Benefit among its sources (matched on
  the source labels Google shows);
- the first three other sources named by the AI Overview;
- the answer-map status of the question on the website;
- the reviewer's note comparing the AI Overview with the website's answer (NOTES below,
  written after reading each capture).

Usage: python3 -I summarize_answer_features.py
"""
import csv
import json
import re

OWN = {"nita.illinois.gov": re.compile(r"nita\.illinois\.gov"),
       "mytransitbenefit.com": re.compile(r"mytransitbenefit\.com")}
OWN_LABEL = {"nita.illinois.gov": re.compile(r"Northern Illinois Transit|\bNITA\b(?! Transit Benefit)"),
             "mytransitbenefit.com": re.compile(r"mytransitbenefit|NITA Transit Benefit")}

NOTES = {
    "Q-NITA-01": "CTA pages lead; the AI Overview answers from CTA and lists Paying for your ride as one source. The fares it gives match the website.",
    "Q-NITA-02": "Metra pages hold the first six results and all AI Overview sources; no NITA page in the first results. Expected for an operator fare question.",
    "Q-NITA-08": "NITA ranks first and is the main AI Overview source. The overview calls the credential the “Regional Transportation Authority (RTA/NITA) Reduced Fare Permit”, gives the mailing address “Regional Transportation Authority, PO Box 301150” from the RTA-branded application PDF, and asks whether the user meant another agency's RTA (Greater Dayton or Riverside); results 6 and 7 are Riverside agencies.",
    "Q-NITA-09": "NITA ranks first and is cited, but the overview also cites a 2018 CHI 311 page, and the results include the RTA-era press release and the 2022 RTA blog post on the online portal.",
    "Q-NITA-12": "NITA ranks first and is cited; the overview's processing time (“about 3 to 4 weeks”) is attributed to the Village of Schaumburg, while NITA's Ride Free application PDF says online applications are processed within 3 days. Results include the RTA-era press release and the 2022 blog post.",
    "Q-NITA-13": "CTA ranks first and NITA second; the overview combines CTA, NITA, the 44th Ward, and CHI 311 to explain both programs, which NITA's own page answers only in separate sections (answer map: scattered).",
    "Q-NITA-16": "NITA's Access page ranks second and is cited; the overview gives NITA Customer Service hours as 8:30 AM to 5:00 PM and 62 registration sites.",
    "Q-NITA-19": "Pace ranks first and NITA second. The overview gives 312-663-HELP with hours Monday to Friday 8:30 AM to 5:00 PM, attributed to Pace; NITA's Accessible transit page says 8:00 a.m. to 5:00 p.m. (`SEO-NITA-027`).",
    "Q-NITA-21": "Pace holds the first three results; NITA is fifth. The overview gives the certification line as 8:00 AM to 5:00 PM, so two overviews captured in the same session give different hours for the same line.",
    "Q-NITA-24": "CTA holds five of the first eight results and all sources; NITA's How to ride is sixth and not cited. The overview gives the NITA Travel Information Center number and hours from CTA; NITA's pages give the number only on Contact, without hours.",
    "Q-NITA-26": "NITA's Ride Safe page ranks first and supplies every NITA statement in the overview (definition, features, what to report, 911).",
    "Q-NITA-28": "The NITA homepage ranks first; the overview cites NITA, the State newsroom, DuPage County, a law firm, and Wikipedia. “People also ask” shows “What is the Nita tax in Illinois?” and “What is the Nita Act?”, which the website answers only in separate places (answer map: scattered; the tax question was corrected from missing to conflicting in Step 3 part B).",
    "Q-NITA-31": "The 2027 budget page and the budget PDF rank first and second and are cited. The overview gives the December 4 comment deadline and the December 10 board vote; it does not repeat the past November 12 hearing.",
    "Q-NITA-38": "ilga.gov and Chicago Cityscape rank above NITA (third); the overview cites NITA first and links its map and technical assistance page.",
    "Q-MTB-02": "National sources only (Reddit, Jawnt, MTA, City of Chicago, MetLife); no My Transit Benefit page in the first results or sources.",
    "Q-MTB-03": "Federal and HR sources (DOT, SHRM, Edenred); no My Transit Benefit page.",
    "Q-MTB-04": "National benefit administrators and NYC sources; no My Transit Benefit page.",
    "Q-MTB-06": "CTA's Transit Benefit Fare Program page ranks first; the My Transit Benefit homepage is fifth. The overview cites it as “NITA Transit Benefit Program” and also names a “CTA Transit Benefit Fare Program”; it explains enrollment from employer and university sources (answer map: missing).",
    "Q-MTB-11": "Law firms and ilga.gov answer; My Transit Benefit Employers is sixth and not cited. The overview names the law “Transportation Benefits Program Act”, says it took effect January 1, 2024, and applies to “50 or more covered employees”; the website says “Transit Benefits Program Act”, “goes into effect on January 1, 2024”, and “more than 50” (`SEO-MTB-008`).",
    "Q-MTB-12": "ilga.gov and law firms lead; My Transit Benefit Employers is eighth and listed among the overview's sources. The overview says “at least 50 covered employees”.",
}


def main():
    queries = {r["query"]: r for r in csv.DictReader(open("queries.tsv"), delimiter="\t")}
    amap = {r["question_id"]: r for r in csv.DictReader(open("../../2026-11-25/answer-map/answer-map.csv"))}
    rows = []
    for line in open("google-answer-features-2026-11-26.jsonl"):
        d = json.loads(line)
        q = queries[d["query"]]
        qid = q["question_id"]
        site = amap[qid]["website"]
        own = [f'{r["rank"]} ({r["title"]})' for r in d["top_results"] if OWN[site].search(r["cite"])]
        labels = d["ai_overview"]["source_labels"] if d["ai_overview"] else []
        cited = any(OWN_LABEL[site].search(x) for x in labels)
        others = [x for x in labels if not OWN_LABEL[site].search(x)][:3]
        rows.append({
            "question_id": qid, "website": site, "query": d["query"], "captured_utc": d["captured_utc"],
            "ai_overview": "yes" if d["ai_overview_shown"] else "no",
            "featured_snippet": "yes" if d["featured_snippet"] else "no",
            "people_also_ask": len(d["people_also_ask"]),
            "own_site_ranks_in_first_results": "; ".join(own) or "none",
            "own_site_listed_as_ai_overview_source": "yes" if cited else "no",
            "other_ai_overview_sources": "; ".join(others),
            "answer_map_status": amap[qid]["answer_status"],
            "note": NOTES[qid],
        })
    with open("answer-features-summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
