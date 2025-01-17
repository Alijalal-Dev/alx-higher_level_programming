#!/usr/bin/python3
"""Send a POST request to a URL with the letter as a parameter."""

import sys
from requests import post


if __name__ == "__main__":
    payload = {"q": ""}
    if len(sys.argv) > 1:
        payload["q"] = sys.argv[1]
    response = post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_rsp = response.json()
        if json_rsp == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_rsp.get("id"), json_rsp.get("name")))
    except ValueError:
        print("Not a valid JSON")
