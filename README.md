# Practice Competitions

Three self-scored machine-learning practice problems. Each folder has a `README.md`
with the task, a `data/` folder (test answers included in `test_labels.csv` so you
can score yourself), and a `starter.ipynb` with a baseline to beat.

| Folder | Task | Metric |
|---|---|---|
| [`starcraft-matchup/`](starcraft-matchup/) | Classify the race matchup of StarCraft II games | macro-F1 |
| [`weather-rain/`](weather-rain/) | Predict daily rainfall in 10 cities | RMSE |
| [`tuition-bracket/`](tuition-bracket/) | Predict a university student's tuition bracket from a messy, hand-typed family form | macro-F1 |

Requirements: Python 3 with `pandas`, `numpy`, `scikit-learn`, `xgboost`,
`matplotlib`, `seaborn`, `jupyter`. On macOS, XGBoost also needs `brew install libomp`.
