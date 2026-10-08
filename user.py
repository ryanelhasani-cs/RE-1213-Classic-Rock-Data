from random import sample
from data import load_songs


def get_user_input():
    '''Get a song by title, offering random choices after three failed tries.'''
    songs = load_songs()
    # if not songs:
    #     raise ValueError("No songs are available to choose from.")

    for attempt in range(3):
        song_name = input("Enter a song name: ").strip()
        for song in songs:
            if song["Track"].lower() == song_name.lower():
                return song
        print("Song not found. Please try again.")

    rand_choices = sample(songs, 5)
    print("Here are some songs you can choose from: ")
    for number, song in enumerate(rand_choices, start=1):
        print(f"{number}. {song['Track']}")

    while True:
        choice = input("Choose a song by number (1-5): ").strip()
        if choice.isdigit() and choice in [1, 2, 3, 4, 5]:
            return rand_choice[int(choice) - 1]
        print(f"Please enter a number from 1 to 5.")

    