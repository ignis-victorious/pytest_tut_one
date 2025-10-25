# #
#  Import LIBRARIES
from typing import Any

import requests as rq

# Import the specific exception directly
from requests.exceptions import RequestException  # <--- THE FIX

#  Import FILES
#


"""Pytest EP3 - Mocking & Patching the Requests Module"""
"""Requests code."""


def make_get_request(url: str) -> Any | dict[str, str]:
    try:
        response: rq.Response = rq.get(url=url)
    except RequestException:
        return {"Error": "oh no!"}
    return response.json()["headers"]


print("START")
works: Any | dict[str, str] = make_get_request(url="https://httpbin.org/get")
print(works, "\n\n")
fails: Any | dict[str, str] = make_get_request(url="https://notasite.abc")
print(fails)
print("END")


"""Pytest EP2 - Writing Tests for a Basic Custom Class + Properties & Methods"""
"""Person class."""
# Person class:
# first name: str, last name: str, age: int
# property: full_name
# method: update_age


class Person:
    def __init__(self, fname: str, lname: str, age: int) -> None:
        self.fname: str = fname
        self.lname: str = lname
        self.age: int = age

    @property
    def full_name(self) -> str:
        return f"{self.fname} {self.lname}"

    def update_age(self, new_age: int) -> None:
        if new_age > 0:
            self.age = new_age
            # self.age = new_age + 1
            return
        raise ValueError


john: Person = Person(fname="John", lname="Smith", age=55)
print(vars(john).keys())
# Person(fname="John", lname="Smith", age=55)


"""Pytest EP1 - The Absolute Basics of Writing Tests"""
"""This file contains some code I want to run tests for"""


def add_some_numbers(x: int, y: int) -> int:
    """Well, add some numbers.."""
    return x + y


#
#  Import LIBRARIES
#  Import FILES
#
# #
