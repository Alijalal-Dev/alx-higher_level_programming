#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """
    Represent a node in a singly-linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): the next Node in the linked list.
    """

    def __init__(self, data, next_node=None) -> None:
        """
        Initialize a Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): the next Node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        """Get the data stored in the Node."""
        return self.__data

    @data.setter
    def data(self, value) -> None:
        """
        Set the data stored in the Node.

        Args:
            value (int): The new data value.

        Reises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self) -> 'Node':
        """Get the next Node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value) -> None:
        """
        Set the next Node in the linked list.

        Args:
            value (Node): The new next Node.

        Raises:
            TypeError: If value is not a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represent a singly-linked list.

    Attributes:
        __head (Node): The first Node in the linked list.
    """

    def __init__(self) -> None:
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value) -> None:
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node and value > current.next_node.data:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self) -> str:
        """Return a string representation of the linked list."""
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
