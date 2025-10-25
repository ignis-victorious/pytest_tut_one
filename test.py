"""This file contains tests for main."""

# #
#  Import LIBRARIES
#  Import FILES
from main import add_some_numbers

#

# 1. Have some code to test (ideally in clean functions or classes!)
# 2. Install pytest
# 3. Import your function, make up an expected output, and then check for it.
#


def test_add_some_numbers() -> None:
    assert add_some_numbers(x=10, y=10) == 20
    assert add_some_numbers(x=1, y=1) == 2
    assert add_some_numbers(x=10, y=100) == 110
