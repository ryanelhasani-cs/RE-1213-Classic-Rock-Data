

def binary_search(songs, category, target):
    '''Performs a binary search on the sorted list of songs to find the target value in the specified category'''

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