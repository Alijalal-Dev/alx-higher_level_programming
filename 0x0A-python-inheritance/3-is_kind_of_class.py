#!/usr/bin/python3
"""is_kind_of_class module."""


def is_kind_of_class(obj, a_class) -> bool:
    """
    Check if the object is an instance of the specified class or its subclass.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare the object against.
    """
    return isinstance(obj, a_class)
