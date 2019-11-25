"""module docstring"""

def sort(unsorted):
    """docstring"""
    iterations = 0
    while iterations < len(unsorted):
        for seq, value in enumerate(unsorted):
            if seq == len(unsorted) - 1:
                break
            if value > unsorted[seq + 1]:
                shuffle = value
                unsorted[seq] = unsorted[seq + 1]
                unsorted[seq + 1] = shuffle
        iterations += 1

    return unsorted
