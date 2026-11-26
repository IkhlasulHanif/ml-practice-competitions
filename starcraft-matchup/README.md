# StarCraft II — Guess the Matchup

Each row is one professional StarCraft II game (tournaments: DH Masters Winter,
DH Masters Last Chance, IEM Katowice; Sep 2021 – Feb 2022). We know how both
players played (economy, speed, losses), but **not which race each player used**.

**Your task:** predict the `matchup` of every game in `test.csv`.

StarCraft II has three races: **T**erran, **P**rotoss, **Z**erg. A matchup is the
pair of races in a game, ignoring order, so there are 6 classes:
`TvT, TvP, TvZ, PvP, PvZ, ZvZ`.

## Files

| File | Rows | What it is |
|---|---|---|
| `data/train.csv` | 496 | games with `matchup`, `p1_race`, `p2_race` |
| `data/test.csv` | 333 | games to predict (`matchup`, `p1_race`, `p2_race` removed) |
| `data/test_labels.csv` | 333 | `id, matchup` — the answers, **for scoring only** |
| `starter.ipynb` | | loads data, trains a baseline, scores it |

## Columns

- `id` — game id; `played_at` — UTC timestamp; `tournament`; `map` (different
  tournaments use different versions/prefixes of the same map, e.g. `[ESL] Hardwire`)
- `game_length` — seconds; `winner` — `1` or `2`
- Per player (`p1_…` / `p2_…`):
  - `apm` actions per minute; `spm` screens per minute
  - `sq` spending quotient (how well a player spends resources, higher = better)
  - `avg_pac_per_min`, `avg_pac_action_latency`, `avg_pac_actions`, `avg_pac_gap` —
    "perception–action cycle" stats: how often the player shifts screen focus and
    acts, and how fast
  - `max_collection_rate`, `avg_collection_rate_minerals/gas`, `minerals/gas_collected`,
    `avg_unspent_minerals/gas`, `minerals/gas_lost` — economy
  - `workers_produced`, `workers_killed`, `workers_lost`
  - `supply_block` — seconds spent unable to build because of supply cap
- Train only: `p1_race`, `p2_race`, `matchup`

## Metric

**Macro-F1** over the 6 classes (classes are unbalanced: TvP is 3× as common as
ZvZ, so every class counts equally). Accuracy is reported alongside.

## Notes

- `test_labels.csv` is for scoring at the very end. Never train, tune or select
  features on it — use cross-validation on `train.csv` for that.
