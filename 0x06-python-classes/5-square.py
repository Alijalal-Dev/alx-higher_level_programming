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
        """
        self.size = size

    @property
    def size(self) -> int:
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value) -> None:
        """
        Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (side length squared).
        """
        return self.__size ** 2

    def my_print(self) -> None:
        """Print a square pattern of '#' characters."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
