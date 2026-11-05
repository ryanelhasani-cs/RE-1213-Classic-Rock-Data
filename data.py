import csv
from pathlib import Path

csv_folder_path = Path(__file__).parent # "UltimateClassicRock.csv" I shared the path so that all version files would have access,  csv is in a higher folder
csv_path = csv_folder_path / "UltimateClassicRock.csv"

# def clean_csv():
#     ''' Cleans CSV Data
    
#     Im gonna be honest, I dont know why this exists, the data is already clean?
    
#     '''

# def sort_csv():
#     ''' CSV sorter
    
#     All my other functions so far have all be focused on the single task of guessing when a song was written, but I think there should be other functuons as well.
#     This function will take in a user category, like song title, year created, dancability, etc, and return a new file ordered by their want

#     '''

def transform_song_data(row: dict[str]):
    ''' Convert CSV row into useable data

    args:
        row dict[str]: This is a row from the csv, with all its categories and scores 

    returns:
        song dict[str, dict[str, int|float]]: This is the song with all its categories and scores, but with the data types converted to int or float as needed
    '''
    song = row.copy()
    minutes, seconds = song["Duration"].split(":")
    song["Duration"] = int(minutes) * 60 + int(seconds)

    for category in ("Year", "Key", "Mode", "Time_Signature"):
        song[category] = int(song[category])

    for category in ("Danceability", "Energy", "Loudness", "Speechiness", "Acousticness", "Instrumentalness", "Liveness", "Valence", "Tempo"):
        song[category] = float(song[category])

    return song


def load_songs():
    ''' Loads the csv

    This function reads the csv and puts it all into dictionaries. Im unsure if this will exist at all, the find_decade_average() function may be enough?
    
    Args:
        None

    Returns:
        list[dict[str, dict[str, int|float]]]: This function returns a list of dictionaries, each dictionary is a song with its categories and scores
    '''
    with open(csv_path, 'r') as fh:
        return [transform_song_data(row) for row in csv.DictReader(fh)]

