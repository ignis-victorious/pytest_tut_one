# #
#  Import LIBRARIES
from typing import Any

from requests.exceptions import RequestException  # <--- THE FIX

#  Import FILES
from main import make_get_request

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
