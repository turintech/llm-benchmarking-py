from typing import List

import pytest

from llm_benchmark.control.double import DoubleForLoop


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 5), (10, 285)])
def test_sum_square(n: int, S: int) -> None:
    assert DoubleForLoop.sum_square(n) == S


@pytest.mark.parametrize("n, S", [(1, 0), (2, 1), (3, 4), (10, 165)])
def test_sum_triangle(n: int, S: int) -> None:
    assert DoubleForLoop.sum_triangle(n) == S


@pytest.mark.parametrize(
    "arr, count",
    [
        ([0], 0),
        ([1, 2, 3], 0),
        ([1, 1, 1], 0),
        ([1, 1, 2], 1),
        ([1, 1, 2, 2], 2),
    ],
)
def test_count_pairs(arr: List[int], count: int) -> None:
    assert DoubleForLoop.count_pairs(arr) == count


@pytest.mark.parametrize(
    "arr0, arr1, count",
    [
        ([0], [0], 1),
        ([1, 2, 3], [2, 3, 1], 0),
        ([1, 1, 1], [1, 2, 3], 1),
        ([1, 1, 2], [1, 2, 2], 2),
        ([1, 1, 2, 2], [1, 1, 2, 2], 4),
    ],
)
def test_count_duplicates(arr0: List[int], arr1: List[int], count: int) -> None:
    assert DoubleForLoop.count_duplicates(arr0, arr1) == count
