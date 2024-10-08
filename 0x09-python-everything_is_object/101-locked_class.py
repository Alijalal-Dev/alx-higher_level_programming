#!/usr/bin/python3
"""Defines a locked class with restricted attribute creation."""


class LockedClass:
    """
    A class that allows the creation of only one instance attribute,\
    ``first_name``.

    Attributes:
        __slots__ (list): A list containing only ``first_name`` to restrict\
            attribute creation.
    """

    __slots__ = ["first_name"]
