#!/usr/bin/python3
"""load_from_json_file module.

A script to load a Python object from a JSON file.
"""
from json import load


def load_from_json_file(filename) -> any:
    """
    Load a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to be loaded.
    """
    with open(filename) as fp:
        return load(fp)
