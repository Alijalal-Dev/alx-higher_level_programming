#!/usr/bin/python3
"""Authenticate to Github API."""

import sys
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
