#!/usr/bin/python3
"""This module defines a custom MyInt class that inherits ``int``."""


class MyInt(int):
    """
    MyInt class, a subclass of int.

    Attributes:
        None

    Methods:
        __eq__(self, value): Check if the value is not equal to self.
        __ne__(self, value): Check if the value is equal to self.
    """

    def __eq__(self, value) -> bool:
        """
        Check if the value is not equal to self.

        Args:
            value: The value to compare against.
        """
        return self.real != value

    def __ne__(self, value) -> bool:
        """
        Check if the value is equal to self.

        Args:
            value: The value to compare against.
        """
        return self.real == value
