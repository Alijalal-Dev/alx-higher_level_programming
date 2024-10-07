#!/usr/bin/python3
"""
add_integer module.

This module provides a function for adding two intgers or floats.
"""


def add_integer(a, b=98) -> int:
    """
    Return the integer addition of two numbers.

    Args:
        a (int or float): The first numeric value.
        b (int or float): The second numeric value.

    Raises:
        TypeError: if `a` or `b` is not a numeric value (int or float).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
