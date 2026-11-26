"""Rebuild both practice competitions from the original Kaggle files in raw/.

Run from anywhere:  python3 scripts/make_splits.py
"""
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
SEED = 42

# Non-English map names -> English. Prefixes/suffixes ("[ESL]", "LE", "- Ladder")
# are kept on purpose: cleaning them is part of the students' work.
MAP_TRANSLATIONS = {
    "2000 атмосфер РВ": "2000 Atmospheres LE",
    "2000 애트모스피어 - 래더": "2000 Atmospheres - Ladder",
    "Atmosphère 2 000 EC": "2000 Atmospheres LE",
    "Berlingrad EC": "Berlingrad LE",
    "Blackburn EE": "Blackburn LE",
    "Mentes curiosas EE": "Curious Minds LE",
    "Берлинград РВ": "Berlingrad LE",
    "世界主宰-天梯版": "Jagannatha - Ladder",
    "光影交错-天梯版": "Lightshade - Ladder",
    "大气2000-天梯版": "2000 Atmospheres - Ladder",
    "新奇之地-天梯版": "Curious Minds - Ladder",
    "柏林加德-天梯版": "Berlingrad - Ladder",
    "硬线-天梯版": "Hardwire - Ladder",
    "紫晶浪漫-天梯版": "Romanticide - Ladder",
    "贝克特工业-天梯版": "Beckett Industries - Ladder",
    "锈化山巅-天梯版": "Oxide - Ladder",
    "闪烬平原-天梯版": "Glittering Ashes - Ladder",
    "黑色燃烧-天梯版": "Blackburn - Ladder",
    "글리터링 애쉬즈 - 래더": "Glittering Ashes - Ladder",
    "베를린그라드 - 래더": "Berlingrad - Ladder",
    "블랙번 - 래더": "Blackburn - Ladder",
    "큐리어스 마인즈 - 래더": "Curious Minds - Ladder",
    "프라이드 오브 알타리스 - 래더": "Pride of Altaris - Ladder",
    "하드와이어 - 래더": "Hardwire - Ladder",
}


def make_starcraft() -> None:
    out = ROOT / "starcraft-matchup" / "data"
    out.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(RAW / "oprec-ristek-ds-2022" / "train.csv")
    df["map"] = df["map"].str.replace("\xa0", " ").replace(MAP_TRANSLATIONS)
    assert df["map"].map(lambda s: s.isascii()).all(), "untranslated map name"

    # Same train:test ratio as the original competition (829:554).
    train, test = train_test_split(
        df, test_size=554 / (829 + 554), stratify=df["matchup"], random_state=SEED
    )
    hidden = ["matchup", "p1_race", "p2_race"]
    test_labels = test[["id", "matchup"]]
    test = test.drop(columns=hidden)

    assert not set(train["id"]) & set(test["id"])
    assert not set(hidden) & set(test.columns)
    assert test_labels["matchup"].notna().all()

    train.to_csv(out / "train.csv", index=False)
    test.to_csv(out / "test.csv", index=False)
    test_labels.to_csv(out / "test_labels.csv", index=False)
    print(f"starcraft: train {train.shape}, test {test.shape}")
    print(train["matchup"].value_counts().to_dict())


TRAIN_END = "2020-02-29"
TEST_START, TEST_END = "2020-03-01", "2021-07-31"
TARGET = "rain_sum (mm)"


def make_weather() -> None:
    src = RAW / "weather-forecasting-datavidia"
    out = ROOT / "weather-rain" / "data"
    out.mkdir(parents=True, exist_ok=True)

    daily = pd.read_csv(src / "train.csv")
    hourly = pd.read_csv(src / "train_hourly.csv")
    day = pd.to_datetime(daily["time"])
    hday = pd.to_datetime(hourly["time"]).dt.normalize()

    train = daily[day <= TRAIN_END]
    test = daily[(day >= TEST_START) & (day <= TEST_END)]
    test = test[test[TARGET].notna()].sort_values(["city", "time"]).reset_index(drop=True)
    test.insert(0, "id", range(len(test)))
    test_labels = test[["id", TARGET]]
    test = test.drop(columns=[TARGET])

    train_hourly = hourly[hday <= TRAIN_END]
    test_hourly = hourly[(hday >= TEST_START) & (hday <= TEST_END)]

    assert pd.to_datetime(train["time"]).max() < pd.to_datetime(test["time"]).min()
    assert TARGET not in test.columns
    assert test_labels[TARGET].notna().all()
    assert pd.to_datetime(test_hourly["time"]).min() >= pd.Timestamp(TEST_START)

    train.to_csv(out / "train.csv", index=False)
    train_hourly.to_csv(out / "train_hourly.csv", index=False)
    test.to_csv(out / "test.csv", index=False)
    test_hourly.to_csv(out / "test_hourly.csv", index=False)
    test_labels.to_csv(out / "test_labels.csv", index=False)
    print(f"weather: train {train.shape}, test {test.shape}, "
          f"train_hourly {train_hourly.shape}, test_hourly {test_hourly.shape}")


if __name__ == "__main__":
    make_starcraft()
    make_weather()
