"""import"""
from typing import List


def merge(first_list: List[int], second_list: List[int]) -> List[int]:
    """merges two sorted lists"""
    merged = []
    i, j = 0, 0
    len_first, len_second = len(first_list), len(second_list)

    while i < len_first and j < len_second:
        if first_list[i] < second_list[j]:
            merged.append(first_list[i])
            i += 1
        else:
            merged.append(second_list[j])
            j += 1
    if len_first - i > 0:
        merged.extend(first_list[i:])
    else:
        merged.extend(second_list[j:])
    return merged


def sort(lst: List[int]):
    """sort list"""
    list_len = len(lst)
    #  base case
    if list_len <= 1:
        return lst

    midpoint = int(list_len / 2)
    left = sort(lst[:midpoint])
    right = sort(lst[midpoint:])
    #  return merged(left, right) do not pass tests
    merged = merge(left, right)
    i = 0
    while i < len(merged):
        lst[i] = merged[i]
        i += 1
    return lst
