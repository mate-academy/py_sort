"""
docstring
"""
from typing import List


def sort(lst: List[int]):
    """

    :param lst:
    :return:
    """
    for i in range(len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst
