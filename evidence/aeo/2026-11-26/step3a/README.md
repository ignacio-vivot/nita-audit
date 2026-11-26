# AEO Step 3 part A — direct answers and answer clarity (2026-11-26)

Evidence for Step 3 part A of the [AEO work plan](../../../../docs/audit/03-aeo/aeo-audit-plan.md): an assessment of the 20 priority answers for directness, completeness, currency, and consistency, and the checks behind findings `AEO-NITA-001` to `003` and `AEO-MTB-001` and `002`.

## Method

1. **Priority answer assessment.** [`assess_priority_answers.py`](assess_priority_answers.py) joins the answer map (Step 2 part A), the structure inventory (Step 2 part B), and the answer-feature summary (Step 2 part C) with the reviewer's judgment for each priority question and writes [`priority-answer-assessment.csv`](priority-answer-assessment.csv). A passage counts as direct when the first one or two sentences of a section whose heading matches the question answer it. It is marked “in hidden section” when that passage sits in a closed accordion or an inactive tab, and “no” when the answer is only in a table, a tool, a link, or several sections.

   `python3 -I assess_priority_answers.py`

2. **Rider PDFs.** The five PDFs linked from Discounted Fare and Ride Free Programs that were not reviewed in Step 2 (the permit replacement application and four brochures) were fetched on 2026-11-26 with curl's default settings into [`rider-pdfs/`](rider-pdfs/) and converted with `pdftotext -layout`. [`pdf_branding.py`](pdf_branding.py) counts agency names, former RTA addresses, and the RTA mailing address in these five and in the two applications from Step 2 ([`pdf-branding.csv`](pdf-branding.csv)).

   `python3 -I pdf_branding.py`

3. **Former RTA addresses.** The web addresses printed in the PDFs were requested with curl and opened in the built-in browser on 2026-11-26 ([`rta-domains-check.txt`](rta-domains-check.txt)). `rtachicago.org` redirects to the NITA homepage, and `fares.rtachicago.org` and `getaccess.org` redirect to the NITA Fare Programs portal (`fares.nita.illinois.gov`, which returns 403 to curl but opens in a browser). The eight portal links on Discounted Fare and Ride Free Programs point to `getaccess.org` and therefore reach the same portal.
4. **Board meeting details.** Days of the week for the listed meetings were computed from their dates; the Meeting Materials `mailto` link and Add to Calendar entries were checked live on 2026-11-26 (Step 2 part D).

## Results

| Direct passage | NITA (14) | My Transit Benefit (6) |
| --- | --- | --- |
| Yes | 6 | 3 |
| Yes, but in a closed accordion or tab | 4 | 0 |
| Partial | 1 | 2 |
| No | 3 | 1 |
| Not fully current or consistent (“no” or “partial”) | 6 | 4 |

Questions without a direct passage that belong to Step 3 part B (missing or scattered answers): `Q-NITA-13` (seniors), `Q-NITA-24` (trip planning), and `Q-MTB-06` (employee enrollment). Currency problems already recorded in SEO are referenced, not repeated: `SEO-NITA-027` (budget hearing, paratransit call hours) and `SEO-MTB-008` (employer law).

| PDF | RTA | Regional Transportation Authority | rtachicago.org | NITA | RTA mailing address |
| --- | --- | --- | --- | --- | --- |
| Reduced Fare Application | 7 | 1 | 5 | 0 | Yes |
| Ride Free Application | 5 | 1 | 4 | 0 | Yes |
| Permit Replacement Application | 3 | 1 | 0 | 0 | Yes |
| Reduced Fare Brochure (English, Spanish) | 4, 3 | 0, 0 | 4, 4 | 0, 0 | No |
| Ride Free Brochure (English, Spanish) | 5, 5 | 0, 0 | 4, 4 | 0, 0 | No |

## Correction to Step 2 part A

While checking fares for `AEO-NITA-001`, the answer-map row for `Q-NITA-04` (Regional Day Pass) was found to be wrong: the Regional Passes table on Paying for your ride does list zones 1-3 ($13.50/$8) and 1-4 ($16/$9), at the prices Metra gives. The row was changed from “conflicting” to “direct” in [`build_answer_map.py`](../../2026-11-25/answer-map/build_answer_map.py) and [`answer-map.csv`](../../2026-11-25/answer-map/answer-map.csv), and the counts in the Step 2 README, the matrix, and the work plan were updated (NITA: 24 direct, 3 conflicting).

## Files

`assess_priority_answers.py`, `priority-answer-assessment.csv`, `rider-pdfs/` (five PDFs and their text), `pdf_branding.py`, `pdf-branding.csv`, `rta-domains-check.txt`.
