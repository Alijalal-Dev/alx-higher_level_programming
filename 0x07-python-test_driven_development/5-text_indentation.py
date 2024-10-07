#!/usr/bin/python3
"""
text_indentation module.

This module provides a function to format and print text with indentation.\
The text is split at '.', '?' and ':', and two newlines\
are added after each of these characters.
"""


def text_indentation(text) -> None:
    """
    Format and print text with indentation.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If the 'text' argument is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip(" ")
    if not text:
        return
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)]
        )
    [print(line.strip(" "), end="") for line in text.splitlines(True)]
