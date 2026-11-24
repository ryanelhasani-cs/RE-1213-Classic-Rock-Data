"""Compare a song with decade averages using scaled Euclidean distance."""
from data import FEATURES


def compare_song_decades(songs, song):
    # Calculate each feature's mean and standard deviation across all songs.
    # Features with no variation or too little data cannot be standardized.
    means = songs[FEATURES].mean()
    stds = songs[FEATURES].std()
    usable = stds[stds.notna() & (stds > 0)].index.tolist()
    if not usable:
        raise ValueError("No usable features with a nonzero standard deviation.")
    missing = [name for name in usable if song[name] != song[name]]
    if missing:
        raise ValueError("This song is missing features: " + ", ".join(missing))

    standardized = (songs[usable] - means[usable]) / stds[usable]
    decade_averages = standardized.groupby(songs["Decade"]).mean().dropna()
    if decade_averages.empty:
        raise ValueError("There are no complete decade averages to compare.")
    selected = (song[usable].astype(float) - means[usable]) / stds[usable]
    distances = ((decade_averages - selected) ** 2).sum(axis=1) ** 0.5
    return distances.sort_values()
