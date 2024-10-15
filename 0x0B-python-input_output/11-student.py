#!/usr/bin/python3
"""A Python class representing a Student."""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age) -> None:
        """
        Initialize a 'Student' object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """
        Convert a 'Student' object to a JSON-compatible dictionary.

        Args:
            attrs (list): A list of attribute names to include in the output.
        """
        if (isinstance(attrs, list) and
                all(isinstance(elem, str) for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json) -> None:
        """
        Update a 'Student' object's attributes from a JSON dictionary.

        Args:
            json (dict): A JSON dictionary containing\
                attribute-value pairs to update.
        """
        for k, v in json.items():
            setattr(self, k, v)
