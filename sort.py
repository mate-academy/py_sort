'''
Module
'''
from typing import List


def sort(lst: List[int]):
    '''
    sort list
    :param lst:
    :return:
    '''
    lnght = len(lst)
    for _ in range(lnght - 1):
        for j in range(lnght - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
