#!/usr/bin/python3
"""Send a POST request to URL."""

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    data = urlencode(payload).encode("ascii")

    req = Request(sys.argv[1], data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
