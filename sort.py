"""Sort a list in-place without using built-in functions (sort(), sorted(), etc)"""
from typing import List


def sort(array: List[int]):
    """Realization of bubble sort"""
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
