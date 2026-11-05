import csv
from pathlib import Path

from analysis import find_decade_average, compare_song_decade  # analysis.py file with functions
from user import get_user_input  # gets user input for the song

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

    print(f"The best guess for the decade of the song is: {best_guess_decade}")

if __name__ == "__main__":
    main()