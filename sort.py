"""
sort
"""
from typing import List


def sort(numbers: List[int]):
    """

    :param numbers: unsorted list
    :return: sorted list
    """
    temp = True
    while temp:
        temp = False
        for i in range(1, len(numbers) - 1):
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
                temp = True

    return numbers
