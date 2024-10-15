#!/usr/bin/python3
"""append_write module - A script to append text to a file."""


def append_write(filename="", text="") -> int:
    """
    Append text to a specified text file.

    Args:
        filename (str): The name of the text file where\
            the text will be appended.
        text (str): The text to be appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
