import pytest

import sort


def test_selection_sort():
    l = [2, 1, 3, -5, 3, 4]
    sort.selection_sort(l)
    assert l == [-5, 1, 2, 3, 3, 4]