"""
Sort a list in-place without using built-in functions (sort(), sorted(), etc)
"""

from typing import List


def sort(lst: List[int]):
    """Sort func"""
    len_lst = len(lst)
    for i in range(len_lst):
        lowest_index = i
        len_lst = len(lst)
        for j in range(i+1, len_lst):
            if lst[j] < lst[lowest_index]:
                lowest_index = j
        lst[i], lst[lowest_index] = lst[lowest_index], lst[i]
