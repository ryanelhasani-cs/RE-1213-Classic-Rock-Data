import csv
from pathlib import Path

csv_folder_path = Path(__file__).parent.parent # "UltimateClassicRock.csv" I shared the path so that all version files would have access,  csv is in a higher folder
csv_path = csv_folder_path / "UltimateClassicRock.csv"

def clean_csv():
    ''' Cleans CSV Data
    
    Im gonna be honest, I dont know why this exists, the data is already clean?
    
    '''

def load_csv():
    ''' Loads the csv

    This function reads the csv and puts it all into dictionaries. Im unsure if this will exist at all, the find_decade_average() function may be enough?
    
    '''

def sort_csv():
    ''' CSV sorter
    
    All my other functions so far have all be focused on the single task of guessing when a song was written, but I think there should be other functuons as well.
    This function will take in a user category, like song title, year created, dancability, etc, and return a new file ordered by their want

    '''