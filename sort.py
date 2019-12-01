""" module"""
from typing import List


def sort(list_item: List[int]):
    """bubble sort"""
    length_list = len(list_item)
    for i in range(length_list):
        for j in range(length_list - i - 1):
            if list_item[j] > list_item[j + 1]:
                k = list_item[j]
                list_item[j] = list_item[j + 1]
                list_item[j + 1] = k
    return list_item
