#!/usr/bin/python3
"""write_file module - A script to write text to a file."""


def write_file(filename="", text="") -> int:
    """
    Write text to a specified text file.

    Args:
        filename (str): The name of the text file where\
            the text will be written.
        text (str): The text to be written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
