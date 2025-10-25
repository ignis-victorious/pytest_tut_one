# #
#  Import LIBRARIES

#  Import FILES
#


"""Pytest EP4 - Parametrizing Your Tests"""

"""Some basic code."""


# Suppose we want to run a function with a range of inputs to test it?
# Rather than writing multiple tests, we can use parameterize!
def multiply(a: int, b: int) -> int:
    """Multiply some numbers"""
    return a * b
