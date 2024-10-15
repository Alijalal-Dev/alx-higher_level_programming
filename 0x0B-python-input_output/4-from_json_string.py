#!/usr/bin/python3
"""
from_json_string module.

A script to parse a JSON-formatted string and convert it to a Python object.
"""
from json import loads


def from_json_string(my_str) -> any:
    """
    Parse a JSON-formatted string and convert it to a Python object.

    Args:
        my_str (str): The JSON-formatted string\
            to be converted to a Python object.
    """
    return loads(my_str)
