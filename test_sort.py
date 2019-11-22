import pytest

import sort


def test_sort():
    l = [2, 1, 3, -5, 3, 4]
    sort.sort(l)
    assert l == [-5, 1, 2, 3, 3, 4]