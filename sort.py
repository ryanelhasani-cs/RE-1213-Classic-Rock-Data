from data import load_songs



def slow_insertion_sort(songs, category):
    '''Sorts the list of songs by title using slow insertion sort'''
    for i in range(1, len(songs)):
        current_song = songs[i]
        current_val = current_song[category]

        position = i - 1

        while position >= 0 and songs[position][category] > current_val:
            songs[position + 1] = songs[position]
            position -= 1

        songs[position + 1] = current_song

    return songs

def better_sort_by_title(songs, category):
    '''Sorts the list of songs by title using python faster sorted'''
    return sorted(songs, key=lambda song: song[category], reverse=True)



songs = load_songs()
sample_songs = songs[:100]  # Take the first 100 songs for sampling

sorted_sample = slow_insertion_sort(sample_songs, "Danceability")

for index in range(1, len(sorted_sample)):
    if sorted_sample[index - 1]["Danceability"] < sorted_sample[index]["Danceability"]:
        print(f"Songs are sorted wrong at index {index}")
        break
    print("Songs are sorted correctly")

for song in sorted_sample[:10]:
    print(song["Track"], song["Danceability"])

