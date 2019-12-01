import pytest

import sort


def test_sort():
    list_for_sort = [2, 1, 3, -5, 3, 4]
    sort.sort(list_for_sort)
    assert list_for_sort == [-5, 1, 2, 3, 3, 4]
