#!/usr/bin/python3
"""Send a POST request to URL."""

import sys
from requests import post


if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    response = post(sys.argv[1], data=payload)
    print(response.text)
