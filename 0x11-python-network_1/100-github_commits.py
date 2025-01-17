#!/usr/bin/python3
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
