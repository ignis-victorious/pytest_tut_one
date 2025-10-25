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
