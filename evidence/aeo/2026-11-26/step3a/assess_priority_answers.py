"""Assess the 20 priority answers for directness, completeness, currency, and consistency (AEO Step 3, part A).

Joins the answer map (Step 2 part A), the text-visibility measure (Step 2 part B), and the
answer-feature summary (Step 2 part C) with the reviewer's judgment for each priority
question (J below), and writes priority-answer-assessment.csv.

Criteria:
- direct_passage: "yes" when the first one or two sentences of a section whose heading
  matches the question answer it; "in hidden section" when that passage exists but sits in
  a closed accordion or inactive tab; "no" when no such passage exists (answer only in a
  table, a tool, a link, or spread over sections).
- complete / current_and_consistent: judged against the question and against the
  website's other pages and partner sources checked in Steps 2A and 2C.

Usage: python3 -I assess_priority_answers.py
"""
import csv

# question_id: (direct_passage, complete, current_and_consistent, assessment, related finding)
J = {
    "Q-NITA-01": ("no", "yes", "yes", "Fares are only in a table inside the closed “CTA and Pace” accordion; no sentence states them. CTA ranks first; NITA third and cited.", "AEO-NITA-001"),
    "Q-NITA-02": ("partial", "yes", "yes", "The zone system is explained in visible text; prices are only in accordion tables. Metra answers this question in Google.", "AEO-NITA-001"),
    "Q-NITA-08": ("yes", "partial", "no", "The opening text answers how to apply; the linked application PDFs are RTA-branded and give an RTA mailing address, which Google's AI Overview repeats.", "AEO-NITA-002"),
    "Q-NITA-09": ("in hidden section", "yes", "partial", "“Reduced Fare Permits do not auto-renew” opens a closed accordion. The page does not use the RTA name people search with (SEO-NITA-028).", "AEO-NITA-001"),
    "Q-NITA-12": ("in hidden section", "yes", "partial", "Question-style headings with direct answers, but in tab panels; the renewal form and replacement text use RTA branding or the wrong permit name.", "AEO-NITA-002"),
    "Q-NITA-13": ("no", "partial", "yes", "No passage for seniors; the answer is split between Ride Free and Reduced Fare sections (Step 3 part B).", "Step 3B"),
    "Q-NITA-16": ("yes", "yes", "yes", "The opening text defines the program and eligibility; question-style headings follow.", "Positive"),
    "Q-NITA-19": ("in hidden section", "yes", "no", "The first sentence of the Paratransit Certification accordion answers it, about 1,100 words below the H1 and without a “How to apply” heading; call hours conflict with the Riders page (SEO-NITA-027).", "AEO-NITA-001"),
    "Q-NITA-21": ("in hidden section", "yes", "no", "Same accordion; two AI Overviews on 2026-11-26 gave different hours (8:30 and 8:00) for the same line.", "AEO-NITA-001; SEO-NITA-027"),
    "Q-NITA-24": ("no", "partial", "yes", "The answer is an embedded tool; the NITA Travel Information Center number is only on Contact (Step 3 part B).", "Step 3B"),
    "Q-NITA-26": ("yes", "yes", "yes", "A short definition, numbered steps, and a plain-text FAQ; ranks first and supplies the AI Overview.", "Positive"),
    "Q-NITA-28": ("yes", "yes", "yes", "About NITA opens with a clear definition; the homepage has none (SEO-NITA-010).", "Positive"),
    "Q-NITA-31": ("yes", "yes", "no", "“Three ways to get involved today” gives the December 4 deadline; the same list still invites readers to the November 12 hearing (SEO-NITA-027).", "SEO-NITA-027"),
    "Q-NITA-38": ("yes", "yes", "yes", "The opening text states the law and its effective date; an FAQ follows.", "Positive"),
    "Q-MTB-02": ("partial", "yes", "yes", "“How the Program Works” explains Section 132(f), not the program; no sentence says what the NITA Transit Benefit Fare Program is or who runs it.", "AEO-MTB-002"),
    "Q-MTB-03": ("yes", "yes", "no", "Behind the Benefits gives $340 for transit and $340 for parking; the homepage and Employers say “up to $340 each month” for both together.", "AEO-MTB-001"),
    "Q-MTB-04": ("yes", "yes", "partial", "Employees answers it directly; other pages state the limit differently.", "AEO-MTB-001"),
    "Q-MTB-06": ("no", "no", "n/a", "No enrollment steps for employees (Step 3 part B).", "Step 3B"),
    "Q-MTB-11": ("yes", "yes", "no", "Answered, but the law is misnamed and its 2024 start is written as upcoming (SEO-MTB-008).", "SEO-MTB-008"),
    "Q-MTB-12": ("partial", "partial", "no", "“More than 50” employees, where the law and legal summaries say 50 or more (SEO-MTB-008).", "SEO-MTB-008"),
}


def main():
    amap = {r["question_id"]: r for r in csv.DictReader(open("../../2026-11-25/answer-map/answer-map.csv"))}
    feat = {r["question_id"]: r for r in csv.DictReader(open("../answer-features/answer-features-summary.csv"))}
    assert set(J) == set(feat), set(J) ^ set(feat)
    with open("priority-answer-assessment.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["question_id", "website", "question", "answer_page", "answer_map_status", "direct_passage", "complete",
                    "current_and_consistent", "own_site_ranks_2026_11_26", "own_site_cited_in_ai_overview", "assessment", "related"])
        for q, (d, c, cc, a, rel) in J.items():
            m, g = amap[q], feat[q]
            w.writerow([q, m["website"], m["question"], m["answer_page"], m["answer_status"], d, c, cc,
                        g["own_site_ranks_in_first_results"], g["own_site_listed_as_ai_overview_source"], a, rel])


if __name__ == "__main__":
    main()
