#!/usr/bin/python3
"""Square Class."""


class Square:
    """
    The class represent a square.

    Attributes:
        __size (int): The size of square.
    """

    def __init__(self, size) -> None:
        """
        Initialize a new Square instance with the given size.

        Args:
            size (int): size of square.
        """
        self.__size = size
