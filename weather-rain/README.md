# How Much Did It Rain?

Daily weather for **10 cities** (codes `b, le, lh, p, q, sa, si, su, t, u`).
For every day we know temperature, wind, sunshine, and a full hour-by-hour log
of humidity, cloud cover, pressure, soil moisture and more — but for the test
period the **rain amount is missing**.

**Your task:** predict `rain_sum (mm)` — total rain that day — for every row of
`test.csv`.

The test period comes **after** the training period, like a real future:

| Split | Dates |
|---|---|
| train | 2018-01-01 → 2020-02-29 |
| test  | 2020-03-01 → 2021-07-31 (17 months) |

## Files

| File | Rows | What it is |
|---|---|---|
| `data/train.csv` | 7,900 | daily weather **with** `rain_sum (mm)` |
| `data/train_hourly.csv` | 189,600 | hourly weather for the train days |
| `data/test.csv` | 5,180 | daily weather, `rain_sum (mm)` removed, plus `id` |
| `data/test_hourly.csv` | 124,320 | hourly weather for the test days |
| `data/test_labels.csv` | 5,180 | `id, rain_sum (mm)` — the answers, **for scoring only** |
| `starter.ipynb` | | loads data, trains a baseline, scores it |

## Columns

Daily (`train.csv`, `test.csv`): `time` (date), `city`, `elevation` (m),
max/min temperature and "feels-like" temperature (°C), `sunrise`, `sunset`,
`shortwave_radiation_sum` (sunshine energy, MJ/m²), `snowfall_sum`,
max wind speed and gusts (km/h), dominant wind direction (°),
`et0_fao_evapotranspiration` (water evaporated, mm), and the target `rain_sum (mm)`.

Hourly (`*_hourly.csv`): `time` (hour), `city`, temperature, relative humidity,
dew point, feels-like temperature, sea-level and surface pressure, snowfall,
cloud cover (total / low / mid / high), radiation (shortwave / direct / diffuse /
direct-normal), wind at 10 m and 100 m, gusts, evapotranspiration, vapour
pressure deficit, soil temperature and soil moisture at 4 depths.

A few training days have missing values; the test files have none.

## Metric

**RMSE** of `rain_sum (mm)` (lower is better). Negative predictions make no
sense — clip them to 0.

## Notes

- Rain is unknown for the **whole** test period, so features like "yesterday's
  rain" cannot exist for test rows. Lags of *other* columns are fine.
- `test_labels.csv` is for scoring at the very end. For choosing features and
  settings, hold out the **last months of train** as validation (a random
  split would leak neighbouring days).
