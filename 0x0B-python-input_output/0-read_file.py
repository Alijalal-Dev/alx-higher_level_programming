#!/usr/bin/python3
"""
read_file module.

A script to read and print the content of a file.
"""


def read_file(filename="") -> None:
    """
    Read the content of a specified file and print it to the standard output.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
