"""Count agency names and addresses in the rider PDFs linked from Discounted Fare and Ride Free Programs.

Reads the text of the seven PDFs linked from
https://nita.illinois.gov/riders/free-and-reduced-fare-programs (fetched with curl's default
settings; text extracted with `pdftotext -layout`): the two applications in
../../2026-11-25/answer-map/ (fetched 2026-11-25) and the other five in rider-pdfs/
(fetched 2026-11-26). Writes pdf-branding.csv.

Usage: python3 -I pdf_branding.py
"""
import csv
import glob
import os
import re

PATS = {
    "RTA": r"\bRTA\b",
    "Regional Transportation Authority": r"Regional Transportation Authority",
    "rtachicago.org": r"rtachicago\.org",
    "NITA": r"\bNITA\b",
    "Northern Illinois Transit Authority": r"Northern Illinois Transit Authority",
    "PO Box 301150": r"P\.?O\.? Box 301150",
}
FILES = sorted(glob.glob("../../2026-11-25/answer-map/*-Application-*.txt") + glob.glob("rider-pdfs/*.txt"))


def main():
    with open("pdf-branding.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pdf", "url"] + list(PATS))
        for p in FILES:
            name = os.path.basename(p).replace(".txt", ".pdf")
            t = open(p, errors="replace").read()
            w.writerow([name, "https://nita.illinois.gov/uploads/files/general/Riders/" + name]
                       + [len(re.findall(x, t)) for x in PATS.values()])


if __name__ == "__main__":
    main()
