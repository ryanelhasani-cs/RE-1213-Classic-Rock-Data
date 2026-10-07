import csv
from pathlib import Path
from data import load_songs

csv_folder_path = Path(__file__).parent # "UltimateClassicRock.csv" I shared the path so that all version files would have access,  csv is in a higher folder
csv_path = csv_folder_path / "UltimateClassicRock.csv"

def find_decade_average():
    ''' Find's decade average

    This function goes through every song in a decade, averages each of their categories, and returns it as a dictionary

    Average needs to be relative to score, so like absolute value of (song_score - average) / average?

    '''
    songs = load_songs()

    for song in songs:
        year = int(song["Year"])
        decade = (year // 10) * 10
        
    

def compare_song_decade():
    ''' Compares the song to the decade
    
    This function will take the averages from find_decade_average() and weigh the categories of the user song against it. It is not just a counter,
    like its not just 4 categories go to 80's so we guess 80's, it weighs them. If a song is near identical to the 70's, but the 80's vageley gets 
    more categories, it takes that into consideration. Essentially its a sum of magnitutes of similarity, not just tallys, and summary:
    The lowest magnitude of difference is the closest decade, and best guess

    I mean obviously we have the year the song is from.... but thats no fun. This is an interesting test to see if a song fits its decade, maybe we can
    prove that musically, a song had influence on the future

    
    '''