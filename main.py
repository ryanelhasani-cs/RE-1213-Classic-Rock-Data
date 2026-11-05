import csv
from pathlib import Path

from analysis import find_decade_average, compare_song_decade  # analysis.py file with functions
from user import get_user_input  # gets user input for the song
from data import load_songs  # loads the csv file into a list of dictionaries
from sort import better_sort_by_title # this uses pythons fast search algo
from search import binary_search  # gets the binary search

csv_folder_path = Path(__file__).parent # "UltimateClassicRock.csv" I shared the path so that all version files would have access,  csv is in a higher folder
csv_path = csv_folder_path / "UltimateClassicRock.csv"

def main():
    ''' Main processing

    The goal of this code is to find compare a given songs information (time signature, dancability, acousitcness, etc), weighs all the similarities, 
    and tried to guess what decade a song is from. This takes in a song from a user

    '''

    user_song = get_user_input()
    decade_averages = find_decade_average()

    best_guess_decade = compare_song_decade(user_song, decade_averages)

    print(f"The best guess for the decade of the {user_song['Track']} is: {best_guess_decade}")

    # MOVING ONTO PHASE 3

    songs = load_songs()

    songs_by_year = better_sort_by_title(songs, "Year")
    year = int(input("Enter a year to search for songs: "))
    song = binary_search(songs_by_year, "Year", year)

    if song is None:
        print("No song found for year")
    else:
        print(f"Found song: {songs_by_year[song]['Track']} by {songs_by_year[song]['Artist']} from year {year}")

    song = binary_search(songs_by_year, "Year", 1980)

    if song is None:
        print("No song found for year")
    else:
        print(f"Found song: {songs_by_year[song]['Track']} by {songs_by_year[song]['Artist']} from year {year}")

    song = binary_search(songs_by_year, "Year", 2222)

    if song is None:
        print("No song found for year")
    else:
        print(f"Found song: {songs_by_year[song]['Track']} by {songs_by_year[song]['Artist']} from year {year}")

if __name__ == "__main__":
    main()
