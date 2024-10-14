#!/usr/bin/python3
"""is_same_class module."""


def is_same_class(obj, a_class) -> bool:
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        abj (object): The object to check.
        a_class (type): The class to compare the object against.
    """
    return type(obj) is a_class
