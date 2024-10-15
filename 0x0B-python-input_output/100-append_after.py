#!/usr/bin/python3
"""append_after module.

A script to insert a line of text after each line containing\
    a specific string in a file.
"""


def append_after(filename="", search_string="", new_string="") -> None:
    """
    Insert a line of text after each line containing a specific string\
         in a file.

    Args:
        filename (str): The name of the file to be processed.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to insert after each matching line.
    """
    with open(filename) as fp:
        lines = fp.readlines()
    with open(filename, "w") as fp:
        for line in lines:
            fp.write(line)
            if search_string in line:
                fp.write(new_string)
