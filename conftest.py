#
#  Import LIBRARIES
import pytest

#  Import FILES

#
# #


"""Pytest EP5 - Fixtures and Conftest"""


@pytest.fixture
def numbers() -> list[int]:
    return [1, 2, 3, 4, 5]


@pytest.fixture(name="some_numbers")
def my_numbers() -> list[int]:
    return [1, 2, 3, 4, 5]
