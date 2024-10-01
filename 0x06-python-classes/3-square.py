#!/usr/bin/python3
"""Square Class."""


class Square:
    """
    The class represent a square.

    Attributes:
        __size (int): The size of square.
    """

    def __init__(self, size=0) -> None:
        """
        Initialize a new Square instance with the given size.

        Args:
            size (int): size of square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (side length squared).
        """
        return self.__size ** 2
