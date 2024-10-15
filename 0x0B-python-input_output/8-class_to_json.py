#!/usr/bin/python3
"""class_to_json module.

A script to convert a Python class instance to a JSON-compatible dictionary.
"""


def class_to_json(obj) -> dict:
    """
    Convert a Python class instance to a JSON-compatible dictionary.

    Args:
        obj: The Python class instance to be converted to a dictionary.
    """
    return obj.__dict__
