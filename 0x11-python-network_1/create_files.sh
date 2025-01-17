echo -n '#!/usr/bin/python3
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
' > 2-post_email.py

echo -n '#!/usr/bin/python3
"""Display the URL request response."""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
' > 3-error_code.py

echo -n '#!/usr/bin/python3
"""Python script that fetches `https://alx-intranet.hbtn.io/status`."""

from requests import get


if __name__ == "__main__":
    response = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
' > 4-hbtn_status.py

echo -n '#!/usr/bin/python3
"""Send a request, and displays the value of the X-Request-Id variable."""

import sys
from requests import get


if __name__ == "__main__":
    response = get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
' > 5-hbtn_header.py

echo -n '#!/usr/bin/python3
"""Send a POST request to URL."""

import sys
from requests import post


if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    response = post(sys.argv[1], data=payload)
    print(response.text)
' > 6-post_email.py

echo -n '#!/usr/bin/python3
"""Display the URL request response."""

import sys
from requests import get


if __name__ == "__main__":
    response = get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
' > 7-error_code.py

echo -n '#!/usr/bin/python3
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
' > 8-json_api.py

echo -n '#!/usr/bin/python3
"""Authenticate to Github API."""

import sys
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
' > 10-my_github.py

echo -n '#!/usr/bin/python3
"""Display the 10 commits from the `rails` repo."""

import sys
from requests import get


if __name__ == "__main__":
    response = get(
        "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1]
        )
    )

    commits = response.json()
    try:
        for idx in range(10):
            print(
                "{}: {}".format(
                    commits[idx].get("sha"),
                    commits[idx].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
' > 100-github_commits.py
