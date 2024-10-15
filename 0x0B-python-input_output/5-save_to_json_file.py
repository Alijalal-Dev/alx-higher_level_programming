#!/usr/bin/python3
"""
save_to_json_file module.

A script to save a Python object as a JSON file.
"""
from json import dump


def save_to_json_file(my_obj, filename) -> None:
    """
    Save a Python object as a JSON file.

    Args:
        my_obj (object): The Python object to be saved as a JSON file.
        filename (str): The name of the JSON file\
            to be created or overwritten.
    """
    with open(filename, "w") as fp:
        dump(my_obj, fp)
