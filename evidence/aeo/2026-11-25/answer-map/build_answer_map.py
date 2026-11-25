"""Write the AEO answer map (Step 2, part A) from the reviewer's notes.

Each row records, for one inventory question, where the answer was found after reading
the structured page text in page-text/ (and the two application PDFs): status, page,
location, the heading above the answer, its position (words from the H1, from the
{w=N} markers), a short excerpt, and notes on currency and consistency. The excerpts
are quoted from the pages fetched on 2026-11-25.

Status values: direct (answered in one or two sentences on the expected page), partial
(answer incomplete or indirect), scattered (parts on different sections or pages),
conflicting (the website gives different answers, or the answer differs from the
operator's source), outdated (answer contains past dates presented as current),
link-only (answer only in a linked tool or PDF), missing (no answer found).

Usage: python3 -I build_answer_map.py  (reads ../question-inventory.csv, writes answer-map.csv)
"""
import csv

P = "https://nita.illinois.gov"
M = "https://www.mytransitbenefit.com"
pay = P + "/riders/paying-for-your-ride"
rf = P + "/riders/free-and-reduced-fare-programs"
acc = P + "/riders/access"
at = P + "/riders/accessible-transit"

# question_id, status, page, location, heading above, words from H1, excerpt, notes
R = [
    ("Q-NITA-01", "direct", pay, "accordion (table)", "CTA and Pace (accordion under “How much will my ride cost?”)", 226,
     "CTA 'L' train fare | $2.50* | $1.25* | $2.50* | $1.25*; CTA Bus fare | $2.25 | $1.10 | $2.50 | $1.25",
     "Columns: Ventra full, Ventra reduced, cash, cash reduced. Matches CTA on 2026-11-24 (SEO fare check). Values are in a table inside a closed accordion; no sentence states the fare in words."),
    ("Q-NITA-02", "direct", pay, "section + accordion (table)", "How to pay to ride transit; Metra (accordion)", 65,
     "Metra calculates fares based on distance, using a zone system.",
     "Zone explanation in the open section; prices in tables inside the Metra accordion. Matches Metra."),
    ("Q-NITA-03", "direct", pay, "section", "How to pay to ride transit", 65,
     "You can pay for transit with a credit card, debit card, or your smart phone. Ventra is the region’s fare payment system",
     "Cash on buses is stated in the CTA and Pace accordion."),
    ("Q-NITA-04", "conflicting", pay, "opening text + accordion (table)", "Paying for your ride (opening); Regional Passes (accordion)", 0,
     "The Regional Day Pass (RDP) can be purchased only in the Ventra app.",
     "The price table lists $10 (reduced $6) for “1-1, 1-2, 2-3-4” and $9.50 on weekends but omits trips between zone 1 and zones 3 or 4. "
     "Metra (metra.com/rdp, 2026-11-25) prices the RDP as the Metra Day Pass plus $2.50, so those trips cost $13.50 and $16 ($8 and $9 reduced)."),
    ("Q-NITA-05", "partial", pay, "accordion (table footnote)", "CTA and Pace (accordion)", None,
     "A special $5 fare applies when boarding the CTA Blue Line at O’Hare paying transit value or buying a Single-Ride Ticket",
     "The answer is a footnote under the fare table inside a closed accordion; no heading or sentence frames it as the answer to the $5 question."),
    ("Q-NITA-06", "direct", pay, "accordion (table)", "Children; Students (accordions)", None,
     "On CTA, children under 7 ride free with a fare-paying customer.",
     "“The Metra Family Fares program … is valid through Labor Day” gives no year."),
    ("Q-NITA-07", "direct", rf, "accordion", "Reduced Fare Permits > Senior Reduced Fare / Persons with Disabilities Reduced Fare / Medicare card holders (accordions)", 643,
     "All individuals 65 years old and over who are ineligible for the NITA Ride Free Program are eligible to receive a reduced fare permit.",
     "Eligibility is split across three closed accordions; the section intro names the groups."),
    ("Q-NITA-08", "direct", rf, "opening text + section", "Discounted Fare and Ride Free Programs (opening); Apply online for NITA Fare Programs", 0,
     "Apply online using the Fare Portal below or for in person assistance with Ride Free and Reduced Fare cards, you can find your nearest registration site",
     "Paper applications (PDF) and a phone option under Reduced Fare Permits."),
    ("Q-NITA-09", "direct", rf, "accordion", "Renewing Reduced Fare Permits (accordion)", None,
     "Reduced Fare Permits do not auto-renew. Apply via the NITA Fare Programs Portal",
     "Searchers ask with “RTA” in the query; the page does not mention the RTA (SEO-NITA-028)."),
    ("Q-NITA-10", "direct", rf, "tab panel + accordion", "How to replace your Ride Free Permit (tab); Replace Lost, Stolen or Damaged Reduced Fare Cards (accordion)", 596,
     "you can apply for a new one on the NITA Fare Programs Portal or download a replacement application, or call (312) 913-3110",
     "The Ride Free replacement text says “If your reduced fare permit is lost”."),
    ("Q-NITA-11", "direct", rf, "section", "Ride Free Permits", 334,
     "Older adults and people with disabilities who are enrolled in the Illinois Department on Aging’s Benefit Access program are eligible to ride free",
     "Clear eligibility rule."),
    ("Q-NITA-12", "direct", rf, "tab panels", "How to apply for a Ride Free Permit; How to renew Ride Free Permits (tabs)", 418,
     "Once you are found eligible for BAP, then complete NITA's Ride Free application in our new online portal.",
     "Answers sit in tab panels that show one at a time; the text is in the HTML."),
    ("Q-NITA-13", "scattered", rf, "section + accordion", "Ride Free Permits; Senior Reduced Fare (accordion)", 334, "(no single statement)",
     "No passage says how seniors ride: free if enrolled in the Benefit Access Program, otherwise at a reduced fare from age 65 with a permit. "
     "The reader has to combine two sections; “senior” appears only in an accordion label."),
    ("Q-NITA-14", "link-only", P + "/riders/free-and-reduced-fare-programs/registration-sites", "external tool",
     "Discounted Fare and Ride Free Programs (opening link “Registration Site Locator”)", 0,
     "you can find your nearest registration site using our Registration Site Locator",
     "The locator is an ArcGIS map on another domain; the page lists only the four City of Chicago sites, in the alerts accordion. The Access page says there are 62 registration sites."),
    ("Q-NITA-15", "direct", rf, "section + accordions", "Military Service Fare Program", 1027,
     "Free or reduced fare rides are available for qualifying military personnel",
     "Rules vary by operator and are explained in CTA, Metra, and Pace accordions."),
    ("Q-NITA-16", "direct", acc, "opening text + section", "Access Program (opening); Who is eligible?", 0,
     "allows residents of the NITA region who qualify for the Supplemental Nutrition Assistance Program (SNAP) or Illinois Department of Human Services' FRESH Program to take CTA, Metra, or Pace at a reduced price",
     "Clear and current (expanded to CTA and Pace on 2026-10-01)."),
    ("Q-NITA-17", "direct", acc, "section", "How do I get Access?", 181,
     "The fastest way to get a permit is to apply online at GetAccess.org.",
     "Includes phone, paper, and in-person options and the 7 to 10 business days to receive the permit."),
    ("Q-NITA-18", "direct", acc, "accordion (FAQ)", "Frequently Asked Questions > Is the program available on CTA and Pace?", 290,
     "the Access Pilot Program expanded regionwide to CTA and Pace on October 1, 2026",
     "The page calls the credential “Access Permit”; Paying for your ride says “Access card”."),
    ("Q-NITA-19", "direct", at, "accordion", "Paratransit Certification (accordion)", 1100,
     "To apply for ADA Paratransit, call NITA's ADA Paratransit Certification program at 312-663-HELP (4357)",
     "About 1,100 words down the page inside a closed accordion, with no heading such as “How to apply”. The steps for first-time applicants are clear."),
    ("Q-NITA-20", "partial", at, "section + accordion", "ADA Paratransit; Types of Eligibility (accordion)", 491,
     "for individuals who, because of their disability, are unable to use CTA or Pace fixed route transit service for some or all of their trip",
     "The eligibility rule is part of the service description and the eligibility types are in an accordion; there is no direct “Who qualifies?” answer."),
    ("Q-NITA-21", "conflicting", at, "accordion", "Paratransit Certification (accordion)", 1100,
     "between 8:00 a.m. and 5:00 p.m., Monday through Friday",
     "The Riders page says 8:30 a.m.; Google's AI Overview and Pace say 8:30 (SEO-NITA-027)."),
    ("Q-NITA-22", "missing", at, "—", "—", None, "(no answer)",
     "The page describes an origin-to-destination service but never says it can be used for any trip purpose, which is what the “People also ask” question asks."),
    ("Q-NITA-23", "conflicting", at, "tab panels", "How accessible is our region’s transit system? (CTA and Pace Buses / CTA Trains / Metra tabs)", 74,
     "More than 70 percent of CTA 'L' stations are accessible",
     "The Riders page says 75 percent of CTA stations (SEO-NITA-027). The CTA Trains text sends readers to “the RTA's trip planner”."),
    ("Q-NITA-24", "partial", P + "/riders/how-to-ride", "section (embedded tool)", "Plan your ride; Trip Planner", 100,
     "Use the trip planner to find the best transit route for your trip.",
     "The answer is a tool, not text, and the page has empty H2 headings around it. Mode-by-mode riding tips follow in tab panels."),
    ("Q-NITA-25", "scattered", P + "/contact", "table", "Contact > We're Here to Help", 0, "NITA Travel Information | 312-836-7000",
     "Not on How to ride or Riders; only in the Contact table, with no hours (CTA's trip planning page gives Monday to Friday 6 a.m. to 8 p.m.)."),
    ("Q-NITA-26", "direct", P + "/safety/app", "opening + section + FAQ text", "What is NITA Ride Safe?; How it works; Frequently Asked Questions", 16,
     "NITA Ride Safe lets you report safety concerns on any train, bus, or platform in the region, without making a phone call.",
     "Strong answer page: short definition, numbered steps, a 911 versus Ride Safe comparison, and nine question-and-answer pairs written as plain text (no FAQ markup)."),
    ("Q-NITA-27", "direct", P + "/riders/how-to-ride/getting-to-the-obama-presidential-center", "sections",
     "Ride Metra / Ride CTA / Ride Pace to the Obama Presidential Center", 81,
     "Metra’s Electric Line provides a direct connection to the new center from downtown",
     "Contains Outlook Safe Links URLs (SEO-NITA-026) and an empty H2."),
    ("Q-NITA-28", "direct", P + "/about-nita", "opening text", "About NITA", 0,
     "The Northern Illinois Transit Authority (NITA), formerly the Regional Transportation Authority, was created by the Illinois General Assembly and Governor JB Pritzker",
     "Good definition; the homepage itself has no such text (SEO-NITA-010)."),
    ("Q-NITA-29", "scattered", P + "/about-nita", "opening text; Funding page; blog", "About NITA", 0, "(no single statement)",
     "About NITA does not name the NITA Act, Public Act 104-457, or the 2026-09-01 transition date; the Funding page and blog posts mention the act's passage and funding in separate places."),
    ("Q-NITA-30", "missing", "—", "—", "—", None, "(no answer)",
     "No NITA page explains the taxes or revenue sources created by the NITA Act, although “What is the NITA tax in Illinois?” appears in “People also ask” and “nita transit tax” in autocomplete."),
    ("Q-NITA-31", "outdated", P + "/transit-funding/2027-regional-transit-budget", "numbered list", "Three ways to get involved today", 109,
     "Submit comment using the comment box below by December 4, or email communications@nita.illinois.gov.",
     "Correct deadline, but the same list still invites readers to a November 12 hearing (SEO-NITA-027)."),
    ("Q-NITA-32", "conflicting", P + "/about-nita/boards-and-committees/meeting-materials", "opening text", "Meeting Materials", 0,
     "All NITA Board meetings take place at 9:00 a.m. in the Board Room, 16th Floor, 175 W. Jackson Blvd., Chicago, IL 60604",
     "Board of Directors says the board meets on the third Thursday of each month, but the upcoming meeting is Thursday, December 10, 2026 (the second Thursday) and November 12 was also a second Thursday; "
     "the 2027 budget page says the November 12 meeting began at 1 p.m. The public comment rule (email by noon the day before) is clear."),
    ("Q-NITA-33", "direct", P + "/about-nita/boards-and-committees/board-of-directors", "opening + list", "Members", 40,
     "NITA is governed by a 20-member Board of Directors", "Lists members with bios and explains the appointing authorities."),
    ("Q-NITA-34", "direct", P + "/contact", "table", "We're Here to Help", 0, "NITA Administrative Offices … 312-913-3200",
     "Table of six phone lines; office hours 8:30 a.m. to 5 p.m."),
    ("Q-NITA-35", "outdated", P + "/nita-rider-advisory-council", "opening text", "NITA Riders Advisory Council", 0,
     "Applications are open from September 24 through October 31, 2026.",
     "The period has ended; the “Apply now” heading has no text or link in the HTML (SEO-NITA-027)."),
    ("Q-NITA-36", "direct", P + "/about-nita/transparency/foia", "section", "How to submit a request", 116,
     "please submit your request in writing to: Freedom of Information Officer",
     "The page names the agency “Northern Illinois Transportation Authority” twice."),
    ("Q-NITA-37", "partial", P + "/transit-funding", "sections", "What is operating funding?; What is capital funding?", 87,
     "The regional transit operating budget refers to the expected revenues and expenses related to running the region’s transit system",
     "Explains the two budget types; the fiscal cliff and the NITA Act are told as a narrative without dates or a summary of new revenue sources."),
    ("Q-NITA-38", "direct", P + "/communities/people-over-parking-act", "opening text", "People Over Parking Act", 0,
     "a new Illinois law effective June 1, 2026. The new law no longer allows municipalities to impose minimum parking requirements for new developments located near",
     "Also a map tool and an FAQ written as plain text."),
    ("Q-NITA-39", "direct", P + "/communities/people-over-parking-act", "section + FAQ text", "How to obtain assistance; Frequently Asked Questions", 264,
     "Complete the interest form.", "Eligibility, timing, and evaluation are answered in the FAQ."),
    ("Q-NITA-40", "missing", P + "/communities/access-to-transit-program", "—", "—", None, "(no answer)",
     "Describes the program and lists the 2026 awards and examples, but gives no eligibility, call-for-projects timing, or application steps."),
    ("Q-NITA-41", "partial", P + "/communities/community-planning", "opening text", "Community Planning", 0,
     "provides funding and technical assistance to local governments to help foster the growth of sustainable, equitable, walkable, and transit-friendly communities",
     "Defines the program; no application steps or call-for-projects timing on the page (only in a related blog excerpt)."),
    ("Q-NITA-42", "partial", P + "/region/section-5310", "opening text", "Section 5310", 0,
     "a federal program that aims to improve mobility for seniors and individuals with disabilities",
     "Defines the program and lists funded projects; who can apply and when is not stated in the page text."),
    ("Q-MTB-01", "partial", M + "/", "section", "How the Program Works", 0,
     "Section 132(f) of federal tax law allows employees to pay for transit and parking costs using pre-tax dollars.",
     "No sentence says what the program is or that NITA runs it; only the H1 slogan carries the name."),
    ("Q-MTB-02", "direct", M + "/behind-the-benefits", "section", "About Transit Benefits", 0,
     "Section 132(f) of federal tax law allows employees to pay for transit and parking costs using pre-tax dollars.",
     "The same paragraph is repeated on the homepage."),
    ("Q-MTB-03", "direct", M + "/behind-the-benefits", "section", "About Transit Benefits", 0,
     "for 2026, the monthly amount is $340 for transit and $340 for parking.",
     "The homepage and Employers say “up to $340 each month” for transit and parking together, which reads as one combined limit."),
    ("Q-MTB-04", "direct", M + "/employees", "section", "How you save", 74,
     "You can set aside up to $340 for transit and $340 for parking, per month", "Clear yes."),
    ("Q-MTB-05", "partial", M + "/employees", "section + calculator", "How you save; Employee Savings Calculator", 74,
     "Employees can save up to 40 percent through reduced taxes", "“Up to 40 percent” with no worked example; the calculator needs JavaScript."),
    ("Q-MTB-06", "missing", M + "/employees", "—", "—", None, "(no answer)",
     "No enrollment steps for employees; the page only says to encourage an employer to enroll and links to the employee login."),
    ("Q-MTB-07", "direct", M + "/employees", "heading + link", "Login", 52,
     "Log into your Transit Fare Benefit account to check your balance, order a new card, add more money, and more.",
     "The login box heading is an H1 (SEO-MTB-003)."),
    ("Q-MTB-08", "partial", M + "/behind-the-benefits", "empty headings",
     "The RTA/NITA Transit Benefit Prepaid Mastercard®; Ventra® Direct Loads; Pace Vanpool", 177, "(headings only)",
     "The three product headings have no text; Employers mentions CTA, Metra, and Pace only."),
    ("Q-MTB-09", "missing", "—", "—", "—", None, "(no answer)", "No page says whether unused funds roll over or expire."),
    ("Q-MTB-10", "missing", M + "/behind-the-benefits", "empty heading", "The RTA/NITA Transit Benefit Prepaid Mastercard®", 177, "(heading only)",
     "No explanation of the card or how it works with Ventra; the card name still says RTA."),
    ("Q-MTB-11", "outdated", M + "/employers", "section", "New law requires employers to offer transit benefits", 204,
     "the new Transit Benefits Program Act, which goes into effect on January 1, 2024",
     "The law is misnamed and its 2024 start is written as upcoming (SEO-MTB-008)."),
    ("Q-MTB-12", "partial", M + "/employers", "section", "New law requires employers to offer transit benefits", 204,
     "The new Illinois law requires employers with more than 50 full-time or part-time employees, located within a mile of fixed-route transit service",
     "Legal summaries say 50 or more; to confirm with NITA's legal team (SEO-MTB-008)."),
    ("Q-MTB-13", "link-only", M + "/employers", "links", "Employers (opening)", 0, "Employer Login; Account Set Up Guide",
     "Sign-up steps are only in the PDF set-up guide; the page text has none."),
    ("Q-MTB-14", "partial", M + "/employers", "section + calculator", "How you save; Employer Savings Calculator", 148,
     "Your company can offer the NITA Transit Benefit Fare Program in the form of a pre-tax, employee-paid payroll deduction.",
     "The homepage says “Up to 7.65% in savings”; the Employers calculator uses an 8.45% rate; no sentence explains the difference."),
    ("Q-MTB-15", "missing", "—", "—", "—", None, "(no answer)", "No page says whether the program has fees for employers or employees."),
]


def main():
    inv = {r["question_id"]: r for r in csv.DictReader(open("../question-inventory.csv"))}
    assert set(inv) == {r[0] for r in R}, set(inv) ^ {r[0] for r in R}
    with open("answer-map.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["question_id", "website", "audience", "topic", "question", "priority_answer_feature_sample",
                    "answer_status", "answer_page", "location", "heading_above", "words_from_h1", "answer_excerpt", "notes"])
        for q, st, pg, loc, h, wd, ex, nt in R:
            i = inv[q]
            w.writerow([q, i["website"], i["audience"], i["topic"], i["question"], i["priority_answer_feature_sample"],
                        st, pg, loc, h, "" if wd is None else wd, ex, nt])


if __name__ == "__main__":
    main()
