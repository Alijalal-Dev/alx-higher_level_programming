#!/usr/bin/python3
"""Rectangle Class."""


class Rectangle:
    """
    A Class to represent a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances \
            currently in existence.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0) -> None:
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self) -> int:
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Calculate and return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self) -> str:
        """Return a string representation of the Rectangle \
            using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectagnle_str = ""
        for _ in range(self.__height):
            rectagnle_str += "#" * self.__width + "\n"
        return rectagnle_str[:-1]

    def __repr__(self) -> str:
        """Return a string representation of the Rectangle object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self) -> None:
        """Print a message when an instance of Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
