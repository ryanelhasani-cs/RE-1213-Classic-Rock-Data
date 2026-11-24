"""Load the song data and prepare the numeric features used by the model."""
from pathlib import Path
import pandas as pd

CSV_PATH = Path(__file__).parent / "UltimateClassicRock.csv"
FEATURES = [
    "Danceability", "Energy", "Loudness", "Speechiness", "Acousticness",
    "Instrumentalness", "Liveness", "Valence", "Tempo",
]


def load_songs():
    songs = pd.read_csv(CSV_PATH)
    for column in ["Year", *FEATURES]:
        songs[column] = pd.to_numeric(songs[column], errors="coerce")
    songs["Decade"] = (songs["Year"] // 10 * 10).astype("Int64")
    return songs
