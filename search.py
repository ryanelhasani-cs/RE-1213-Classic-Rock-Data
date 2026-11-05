

def linear_search_by_title(songs: list[dict[str, str|int|float]], song_name: str) -> dict[str, str|int|float]|None:
    ''' Does a linear search for a song by title in the list of songs
    
    Args:
        songs (list[dict[str, str|int|float]]): A list of song dictionaries
        song_name (str): The name of the song to search for
    
    Returns:
        dict[str, str|int|float]|None: The song dictionary if found, otherwise None
    
    '''
    for song in songs:
        if song["Track"].lower() == song_name.lower():
            return song
    return None

def binary_search(songs: list[dict[str, str|int|float]], category: str, target: str|int|float) -> int|None:
    '''Performs a binary search on the sorted list of songs to find the target value in the specified category
    
    Args:
        songs (list[dict[str, str|int|float]]): A list of song

    Returns:
        int|None: The index of the song if found, otherwise None
    
    '''

    # makes sure its sorted
    for i in range(1, len(songs)):
        if songs[i - 1][category] > songs[i][category]:
            print("Songs are sorted wrong, binary search will not work")
            return None

    low = 0
    high = len(songs) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = songs[mid][category]

        if mid_val == target:
            return mid  # Target found
        elif mid_val < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return None


