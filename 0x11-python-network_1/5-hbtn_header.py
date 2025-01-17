#!/usr/bin/python3
"""Send a request, and displays the value of the X-Request-Id variable."""

import sys
from requests import get


if __name__ == "__main__":
    response = get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
