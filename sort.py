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
    return sorted(songs, key=lambda song: song[category])



songs = load_songs()
sample_songs = songs[:100]  # Take the first 100 songs for sampling

sorted_sample = slow_insertion_sort(sample_songs, "Danceability")

for index in range(1, len(sorted_sample)):
    if sorted_sample[index - 1]["Danceability"] > sorted_sample[index]["Danceability"]:
        print(f"Songs are sorted wrong at index {index}")
        break
print("Songs are sorted correctly")

for song in sorted_sample[:10]:
    print(song["Track"], song["Danceability"])


'''
Tradeoff Justification:

My insertion sort is super slow, its in o(n^2) time, and is just not a great alogrithm in general. my CSV is over 14k entries long, that would take eons. Thats why im only testingit wiht 100 songs.
Pythons build in sorted is much faster and accurate, so i trust it with all 14k. 
'''

