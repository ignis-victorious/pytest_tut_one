# #
#  Import LIBRARIES
import pytest

#  Import FILES
from main import multiply

#


"""Pytest EP4 - Parametrizing Your Tests"""
"""Parameterize"""


@pytest.mark.parametrize(argnames="a,b, expected", argvalues=[(10, 5, 50), (10, 10, 100), (1, 1, 1)])
# @pytest.mark.parametrize(argnames="a,b, expected", argvalues=[(10, 5, 50)])
def test_multiply(a: int, b: int, expected: int) -> None:
    result: int = multiply(a=a, b=b)
    assert result == expected


# def test_multiply() -> None:
#     result: int = multiply(a=10, b=5)
#     assert result == 50
