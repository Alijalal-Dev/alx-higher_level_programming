#!/usr/bin/python3
"""This module defines a function for adding attributes to objects."""


def add_attribute(obj, __name, __value) -> None:
    """
    Add a new attribute to the given object.

    Args:
        obj (object): The object to which the attribute is added.
        __name (str): The name of the new attribute.
        __value (any): The value of the new attribute.

    Raises:
        TypeError: If the object is not user-defined and lacks `__dict__`.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, __name, __value)
