#!/usr/bin/python3
"""Module with a Square class derived from the Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
            y (int, optional): The y-coordinate of the square.
            id (int, optional): The identifier for the instance.
                If None, a unique identifier will be assigned.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value) -> None:
        """Set the size of the square.

        Args:
            value (int): The size value to set.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args and len(args) != 0:
            idx = 0
            for arg in args:
                if idx == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif idx == 1:
                    self.size = arg
                elif idx == 2:
                    self.x = arg
                elif idx == 3:
                    self.y = arg
                idx += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key in ("size", "x", "y"):
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """Return a dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
