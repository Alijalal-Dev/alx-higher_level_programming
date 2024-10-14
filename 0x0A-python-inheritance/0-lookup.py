#!/usr/bin/python3
"""A module to look up attributes and methods of objects."""


def lookup(obj) -> list:
    """
    Return a list of attributes and methods of the given object.

    Args:
        obj (object): The object to look up attributes and methods for.
    """
    return dir(obj)
