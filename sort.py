"""docstring"""
from typing import List


def merge(list_1: List[int], list_2: List[int]) -> List[int]:
    """
    Takes 2 sorted lists and returns merged list
    containing elements of both given lists in sorted order.
    :param list_1: List[int]
    :param list_2: List[int]
    :return: List[int]
    """
    combined = []
    len_1 = len(list_1)
    len_2 = len(list_2)
    idx_1 = idx_2 = 0

    while idx_1 < len_1 and idx_2 < len_2:
        if list_1[idx_1] <= list_2[idx_2]:
            combined.append(list_1[idx_1])
            idx_1 += 1
        else:
            combined.append(list_2[idx_2])
            idx_2 += 1

    if idx_1 < len_1:
        combined += list_1[idx_1:]
    if idx_2 < len_2:
        combined += list_2[idx_2:]
    return combined


def sort(list_to_sort: List[int]):
    """
    Sort given list by merge-sort algorithm.
    :param list_to_sort: List[int]
    """
    if len(list_to_sort) < 2:
        return list_to_sort

    middle = len(list_to_sort) // 2
    left = list_to_sort[:middle]
    right = list_to_sort[middle:]

    sort(left)
    sort(right)

    sorted_list = merge(left, right)
    for idx, item in enumerate(sorted_list):
        list_to_sort[idx] = item
    return sorted_list
    # The last line added only to satisfy "pylint" test
