#!/usr/bin/python3
"""MyList Class."""


class MyList(list):
    """
    MyList is a subclass of the built-in list class with added functionality.

    Attributes:
        Inherits attributes of the built-in list class.

    Methods:
        Inherits methods of the built-in list class.
    """

    def print_sorted(self) -> list:
        """Print elements of the list in sorted order."""
        print(sorted(self))
