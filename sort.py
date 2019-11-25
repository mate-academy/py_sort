"""
module selection sort
"""
from typing import List


def selection_sort(lst: List[int]):
    """
    Selection Sort algorithm segments the list into two parts: sorted and unsorted.
    We continuously remove the smallest element of the unsorted segment of
    the list and append it to the sorted segment.
    :param lst: List[int]
    """
    for i, _ in enumerate(lst):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        lst[i], lst[lowest_value_index] = lst[lowest_value_index], lst[i]
