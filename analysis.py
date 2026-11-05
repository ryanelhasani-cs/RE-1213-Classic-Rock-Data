import csv
from pathlib import Path
from data import load_songs

csv_folder_path = Path(__file__).parent # "UltimateClassicRock.csv" I shared the path so that all version files would have access,  csv is in a higher folder
csv_path = csv_folder_path / "UltimateClassicRock.csv"

def find_decade_average() -> dict[int, dict[str, float|int]]:
    ''' Find's decade average

    This function goes through every song in a decade, averages each of their categories, and returns it as a dictionary

    Average needs to be relative to score, so like absolute value of (song_score - average) / average?

    Args:
        None

    Returns:
        dict[int, dict[str, float|int]]: This function returns a dictionary with the decade, and then the "average song" of that decade, with scores for each category

    '''
    decade_average_dict = {}
    songs_per_decade = {}
    
    songs = load_songs()

    for song in songs:
        year = song["Year"]
        decade = (year // 10) * 10
        decade_average_dict.setdefault(decade, {})
        songs_per_decade.setdefault(decade, 0)
        songs_per_decade[decade] += 1

        for category in ("Danceability", "Energy", "Loudness", "Speechiness", "Acousticness", "Instrumentalness", "Liveness", "Valence", "Tempo"):
            decade_average_dict[decade][category] = decade_average_dict[decade].get(category, 0) + song[category]

        for category in ("Key", "Mode", "Time_Signature"): # might need to make this different, average might not work.
            decade_average_dict[decade][category] = decade_average_dict[decade].get(category, 0) + song[category]

    for decade in decade_average_dict:
        for category in decade_average_dict[decade]:
            decade_average_dict[decade][category] /= songs_per_decade[decade]

    return decade_average_dict


        
    

def compare_song_decade(user_song: dict, decade_averages: dict) -> int:
    ''' Compares the song to the decade
    
    This function will take the averages from find_decade_average() and weigh the categories of the user song against it. It is not just a counter,
    like its not just 4 categories go to 80's so we guess 80's, it weighs them. If a song is near identical to the 70's, but the 80's vageley gets 
    more categories, it takes that into consideration. Essentially its a sum of magnitutes of similarity, not just tallys, and summary:
    The lowest magnitude of difference is the closest decade, and best guess

    I mean obviously we have the year the song is from.... but thats no fun. This is an interesting test to see if a song fits its decade, maybe we can
    prove that musically, a song had influence on the future

    Args:
        user_song dict[str, dict[str, int|float]]: This is the user song and its categories and scores
        decade_averages dict[int, dict[str, float|int]]: This is the decade averages and their categories and scores

    Returns:
        int: returns the decade that is the best guess for the song, based on its categories and scores

    '''

    categories = ("Danceability", "Energy", "Loudness", "Speechiness", "Acousticness", "Instrumentalness", "Liveness", "Valence", "Tempo", "Key", "Mode", "Time_Signature")
    scores = {}

    # makes sure each decade starts at a score of 0
    for decade in decade_averages:
        scores[decade] = 0

    for category in categories:
        similar_decade = None
        smallest_diff = None

        for decade in decade_averages:
            average = decade_averages[decade][category]
            difference = abs(user_song[category] - average)

            if smallest_diff is None or difference < smallest_diff:
                smallest_diff = difference
                similar_decade = decade

        scores[similar_decade] += 1

    # best match
    best_decade_match = None
    highest_score = 0

    for decade in scores:
        if scores[decade] > highest_score:
            highest_score = scores[decade]
            best_decade_match = decade

    return best_decade_match