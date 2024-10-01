#!/usr/bin/python3
"""Square Class."""


class Square:
    """
    The class represent a square.

    Attributes:
        __size (int): The size of square.
        __position (tuple): The position of the square in a coordinate system.
    """

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        Initialize a new Square instance with the given size and position.

        Args:
            size (int): size of square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self) -> tuple:
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square as a tuple of two integers.
        """
        return self.__position

    @position.setter
    def position(self, value) -> None:
        """
        Set The position of the square.

        Args:
            value (tuple): the position to set, a tuple of 2 positive integers.

        Raises:
            TypeError: if the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")
