"""Search for a song and compare it with the average of each decade."""
import pandas as pd
from analysis import compare_song_decades
from data import load_songs
from user import get_user_input


def main():
    songs = load_songs()
    song = get_user_input(songs)
    if song is None:
        return
    try:
        distances = compare_song_decades(songs, song)
    except ValueError as error:
        print(f"Cannot compare this song: {error}")
        return

    print(f"\nSong: {song['Track']} — {song['Artist']}")
    print(f"Closest match: {int(distances.index[0])}s")
    print("\nClosest decades:")
    for decade, distance in distances.head(3).items():
        print(f"  {int(decade)}s: {distance:.2f}")
    if pd.isna(song["Decade"]):
        print("\nActual decade: unknown")
    else:
        actual = int(song["Decade"])
        if actual in distances.index:
            print(f"\nDistance from actual decade: {distances.loc[actual]:.2f}")
        else:
            print("\nDistance from actual decade: unavailable")
        print(f"Actual decade: {actual}s")


if __name__ == "__main__":
    main()
