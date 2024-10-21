#!/usr/bin/python3
"""Module with a Rectangle class derived from the Base class."""
from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): The identifier for the instance.
                If None, a unique identifier will be assigned.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self) -> int:
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value) -> None:
        """Set the x-coordinate of the rectangle.

        Args:
            value (int): The x-coordinate value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self) -> int:
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value) -> None:
        """Set the y-coordinate of the rectangle.

        Args:
            value (int): The y-coordinate value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self) -> int:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self) -> None:
        """Display the rectangle using '#' characters."""
        if self.width == 0 and self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        string = "[{}] ({}) {}/{} - {}".format(
            str(self.__class__.__name__),
            self.id,
            self.x,
            self.y,
            self.width,
        )
        if type(self) == Rectangle:
            string += "/{}".format(self.height)
        return string

    def update(self, *args, **kwargs) -> None:
        """Update the attributes of the rectangle.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args and len(args) != 0:
            idx = 0
            for arg in args:
                if idx == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
                elif idx == 4:
                    self.y = arg
                idx += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key in ("width", "height", "x", "y"):
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """Return a dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
