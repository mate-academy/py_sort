"""Sort module."""
from typing import List


def sort(input_list: List[int]):
    """sort a list using bubble sort."""
    for i in range((len(input_list)) - 1):
        for j in range((len(input_list)) - i - 1):
            if input_list[j] > input_list[j + 1]:
                buff = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = buff
    return input_list
