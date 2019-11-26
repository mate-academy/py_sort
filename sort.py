"""Classic Bubble sort"""

from typing import List


def sort(arr: List[int]):
    """General function"""
    index = 0
    swap_count = 0
    while index < len(arr):
        if index + 1 != len(arr) and arr[index] > arr[index + 1]:
            arr[index], arr[index+1] = arr[index+1], arr[index]
            swap_count = 1
        index += 1
        if index == len(arr) and swap_count == 1:
            swap_count = 0
            index = 0
    return arr
