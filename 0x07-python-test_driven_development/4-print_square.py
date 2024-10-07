#!/usr/bin/python3
"""
print_square module.

This module provides a function to print a square made of '#'\
characters of given size.
"""


def print_square(size) -> None:
    """
    Print a square of '#' characters of the specified size.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If the 'size' argument is not an integer.
        ValueError: If the 'size' argument is a negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
