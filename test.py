# #
#  Import LIBRARIES
from typing import Any

import pytest
from requests.exceptions import RequestException  # <--- THE FIX

#  Import FILES
from main import Person, add_some_numbers, make_get_request

#


"""Pytest EP3 - Mocking & Patching the Requests Module"""
"""Tests for the get-request code."""
# Why mock? - We dont want to have to rely on dependencies, plus we can test offline!
# pip install pytest-mock


def test_valid_response(mocker) -> None:
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"headers": {"tst": 123}}
    mocker.patch("main.rq.get", return_value=mock_response)

    result: Any | dict[str, str] = make_get_request(url="validurl")
    assert result == {"tst": 123}
    # assert result == {}


def test_invalid_response(mocker) -> None:
    mocker.patch("main.rq.get", side_effect=RequestException)
    result: Any | dict[str, str] = make_get_request(url="invalidurt")
    assert result == {"Error": "oh no!"}


# def test_valid_response(mocker) -> None:
#     assert 1


"""Pytest EP2 - Writing Tests for a Basic Custom Class + Properties & Methods"""


# Asses INSTANCE of Person
def test_person_creation() -> None:
    test_instance: Person = Person(fname="John", lname="Smith", age=55)
    expected: list[str] = ["fname", "lname", "age"]
    assert list(vars(test_instance).keys()) == expected
    # assert test_instance.fname == "Johns"
    assert test_instance.fname == "John"
    assert test_instance.lname == "Smith"
    assert test_instance.age == 55


def test_full_namef() -> None:
    test_instance_a = Person(fname="John", lname="Smith", age=55)
    assert test_instance_a.full_name == "John Smith", "This is the text that will appear if the test fails!"

    test_instance_b = Person(fname="James", lname="Smith", age=55)
    assert test_instance_b.full_name == "James Smith", "This is the text that will appear if the test fails!"

    test_instance_c = Person(fname="abc", lname="def", age=55)
    assert test_instance_c.full_name == "abc def", "This is the text that will appear if the test fails!"


def test_setting_age() -> None:
    test_instance = Person(fname="John", lname="Smith", age=55)
    test_instance.update_age(new_age=100)
    assert test_instance.age == 100


def test_setting_age_with_invalid_input() -> None:
    test_instance = Person(fname="John", lname="Smith", age=55)

    with pytest.raises(expected_exception=ValueError):
        test_instance.update_age(new_age=-5)


# def test_full_name() -> None:
#     test_instance = Person(fname="John", lname="Smith", age=55)
#     # assert test_instance.full_name == "John Smith"
#     assert test_instance.full_name == "JohnSmith", "This is the text that will appear if the test fails!"
#     # assert test_instance.full_name == "JohnSmith"


""" Pytest EP1 - The Absolute Basics of Writing Tests """
"""This file contains tests for main."""
# 1. Have some code to test (ideally in clean functions or classes!)
# 2. Install pytest
# 3. Import your function, make up an expected output, and then check for it.
#


def test_add_some_numbers() -> None:
    assert add_some_numbers(x=10, y=10) == 20
    assert add_some_numbers(x=1, y=1) == 2
    assert add_some_numbers(x=10, y=100) == 110
