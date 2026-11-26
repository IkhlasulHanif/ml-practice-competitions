# Who Pays What? — Predicting a Student's Tuition Bracket

## The story

At Indonesian public universities, tuition is not the same for everyone.
Each new student is placed in a **UKT bracket** (*Uang Kuliah Tunggal*, "single
tuition fee"), and the bracket decides how much they pay every semester. The
idea is fairness: a farmer's child and a doctor's child study the same programme
but pay very different amounts.

| Bracket | Meaning |
|---|---|
| 0 | Fee fully waived — the student holds a government tuition scholarship (KIP-K) |
| 1 | Lowest fee |
| 2 … 6 | Increasing fees |
| 7 | Highest fee |

To decide the bracket, every admitted student fills in an online form about their
family: income, jobs, house, vehicles, debts, electricity, and so on. A committee
then reviews the form and assigns the bracket.

The university wants a model that reads the form and **predicts the bracket the
committee would give**, so staff can spot unusual cases and review faster.

One warning: the form was typed **by hand** by thousands of families. Free-text
answers (such as "what is your roof made of?") come in hundreds of spellings,
capitalisations and typos. Numbers were typed by hand too.

## Your task

Predict `ukt_bracket` (0–7) for every row in `test.csv`.

## Files

| File | Rows | What it is |
|---|---|---|
| `data/train.csv` | 24,304 | forms **with** `ukt_bracket` |
| `data/test.csv` | 6,076 | forms to predict |
| `data/test_labels.csv` | 6,076 | `id, ukt_bracket` — the answers, **for scoring only** |
| `starter.ipynb` | | loads data, trains a baseline, scores it |

## Columns

Money is in Indonesian rupiah (IDR). For scale: about IDR 15,000–16,000 = 1 USD,
and a typical monthly minimum wage is IDR 2–3 million.

| Column | Meaning |
|---|---|
| `id` | form id |
| `family_income` | monthly family income, as a range |
| `num_dependents` | number of people the parents support |
| `parent_occupation` | main job of the parent / guardian |
| `parent_education` | highest education of the parent / guardian (codes below) |
| `asset_ownership`, `home_ownership` | does the family own its home, rent it, or live with relatives |
| `home_location`, `city` | home regency ("Regency"/"Reg." = rural district) or city |
| `family_monthly_spending` | family spending per month (IDR) |
| `gov_aid_program` | `KIS/JKS/BPJS` = registered in a government health-insurance programme, empty = not |
| `scholarship_history` | previous scholarship or tuition aid (`KIPK` = the KIP-K government scholarship) |
| `father_alive`, `mother_alive` | Alive / Deceased |
| `vehicles_value` | estimated market value of all the family's vehicles (IDR) |
| `electricity_watt` | capacity of the home electricity connection (W). Small connections (450 W, 900 W) are typical of low-income homes |
| `land_area_m2`, `building_area_m2` | size of the plot and of the house |
| `njop_per_m2` | government-assessed land value per m² (IDR), used for property tax |
| `roof_material`, `wall_material`, `floor_material` | free text: what the house is built from |
| `utilities_monthly_spending` | electricity + water bill per month (IDR) |
| `total_debt`, `monthly_debt_installment` | family debt and monthly repayment (IDR) |
| `study_program` | the programme the student was admitted to |
| `admission_route` | `SNBT` = national entrance test, `SNBP` = admitted on school grades |
| `ukt_bracket` | **target** (train only) |

**Education codes** (written in many styles, e.g. `S1`, `S-1/D4`, `S- 2`):

| Code | Level |
|---|---|
| SD, MI | primary school (MI = Islamic primary) |
| SMP, SLTP, MTs | junior high school (MTs = Islamic) |
| SMA, SLTA, MA | senior high school (MA = Islamic) |
| D1 … D4 | vocational diploma, 1–4 years |
| S1 | bachelor's degree |
| S2 | master's degree |
| S3 | doctorate |

"or equivalent" means "or a school of the same level".

## Metric

**Macro-F1** over the 8 brackets: every bracket counts equally, including the
rare ones. Accuracy is shown alongside.

## Notes

- `test_labels.csv` is for scoring at the very end. Never train, tune or choose
  features on it — use cross-validation on `train.csv` for that.
