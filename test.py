#
#  Import LIBRARIES
# import pytest

#  Import FILES
from main import find_average, find_biggest, find_smallest

#
# #


"""Pytest EP5 - Fixtures and Conftest"""


# @pytest.fixture
# def numbers() -> list[int]:
#     return [1, 2, 3, 4, 5]


# @pytest.fixture(name="some_numbers")
# def my_numbers() -> list[int]:
#     return [1, 2, 3, 4, 5]


def test_find_average(numbers: list[int]) -> None:
    assert find_average(nums=numbers) == 3.0


def test_find_biggest(numbers: list[int]) -> None:
    assert find_biggest(nums=numbers) == 5


def test_find_smallest(some_numbers: list[int]) -> None:
    assert find_smallest(nums=some_numbers) == 1


# # Original code
# def test_find_average() -> None:
#     numbers: list[int] = [1, 2, 3, 4, 5]
#     assert find_average(nums=numbers) == 3.0


# def test_find_biggest() -> None:
#     numbers: list[int] = [1, 2, 3, 4, 5]
#     assert find_biggest(nums=numbers) == 5


# def test_find_smallest() -> None:
#     numbers: list[int] = [1, 2, 3, 4, 5]
#     assert find_smallest(nums=numbers) == 1
