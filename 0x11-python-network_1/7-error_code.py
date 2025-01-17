#!/usr/bin/python3
"""Display the URL request response."""

import sys
from requests import get


if __name__ == "__main__":
    response = get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
