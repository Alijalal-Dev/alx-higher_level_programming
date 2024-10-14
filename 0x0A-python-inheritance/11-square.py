#!/usr/bin/python3
"""This module defines a Square class that inherits Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, a subclass of Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initialize a Square instance with the given size.
    """

    def __init__(self, size) -> None:
        """
        Initialize a Square instance with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than zero.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
