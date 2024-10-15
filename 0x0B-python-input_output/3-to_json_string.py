#!/usr/bin/python3
"""
to_json_string module.

A script to convert a Python object to a JSON-formatted string.
"""
from json import dumps


def to_json_string(my_obj) -> str:
    """
    Convert a Python object to a JSON-formatted string.

    Args:
        my_obj (object): The Python object to be converted to JSON.
    """
    return dumps(my_obj)
