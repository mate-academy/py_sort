"""list sort module"""
from typing import List


def sort(nums: List[int]):
    """
    sorting by inserts algorithm function
    :param nums: list for sorting
    :return: sorted list
    """
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        past_i = i - 1
        while past_i >= 0 and nums[past_i] > item_to_insert:
            nums[past_i + 1] = nums[past_i]
            past_i -= 1
        # Вставляем элемент
        nums[past_i + 1] = item_to_insert
    return nums
