#!/usr/bin/python3
"""inherits_from module."""


def inherits_from(obj, a_class) -> bool:
    """
    Check if the object is an instance of a class that inherits
    (directly or indirectly) from the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare inheritance against.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
