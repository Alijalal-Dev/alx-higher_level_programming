#!/usr/bin/python3
"""Square Class."""


class Square:
    """
    The class represent a square.

    Attributes:
        __size (int): Teh size of the squre.
    """

    def __init__(self, size=0) -> None:
        """
        Initialize a new Square instance with the given size.

        Args:
            size (int): The size of the square.
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

    def __eq__(self, other: 'Square') -> bool:
        """
        Compare two Square instances for equality based on their ereas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other: 'Square') -> bool:
        """
        Compare two Square instances for inequality based on their ereas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other: 'Square') -> bool:
        """
        Compare two Square instances for greater than based on their ereas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is greater than the other,\
                False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other: 'Square') -> bool:
        """
        Compare two Square instances for greater than or\
            equal based on their ereas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is greater than or\
                equal to the other, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other: 'Square') -> bool:
        """
        Compare two Square instances for less than based on their ereas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is less than the other,\
                False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other: 'Square') -> bool:
        """
        Compare two Square instances for less than or\
            equal based on their ereas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is less than or\
                equal to the other, False otherwise.
        """
        return self.area() <= other.area()
