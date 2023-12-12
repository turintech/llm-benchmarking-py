from typing import List

import pytest

from llm_benchmark.control.single import SingleForLoop


@pytest.mark.parametrize("n, S", [(0, 0), (1, 0), (2, 1), (10, 45), (100, 4950)])
def test_sum_range(n: int, S: int) -> None:
    assert SingleForLoop.sum_range(n) == S


@pytest.mark.parametrize(
    "v, M",
    [([0], 0), ([1, 2, 3], 3), ([3, 2, 1], 3), ([3, 3, -1], 3), ([-1, -1, -3], -1)],
)
def test_max_list(v: List[int], M: int) -> None:
    assert SingleForLoop.max_list(v) == M


@pytest.mark.parametrize(
    "n, m, S",
    [
        (1, 1, 0),
        (10, 1, 45),
        (10, 2, 20),
        (10, 3, 18),
        (10, 12, 0),
        (100, 3, 1683),
        (100, 12, 432),
        (101, 100, 100),
    ],
)
def test_sum_modulus(n: int, m: int, S: int) -> None:
    assert SingleForLoop.sum_modulus(n, m) == S
