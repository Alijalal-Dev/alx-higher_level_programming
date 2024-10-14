#!/usr/bin/python3
"""This module defines a Rectangle class that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class, a subclass of BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initialize a Rectangle instance\
            with width and height.
        area(self): Calculate the area of the rectangle.
        __str__(self): Return a string representation of the rectangle.
    """

    def __init__(self, width, height) -> None:
        """
        Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than zero.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        return "[{}] {}/{}".format(
            str(self.__class__.__name__),
            self.__width,
            self.__height)
