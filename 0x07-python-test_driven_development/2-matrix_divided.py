#!/usr/bin/python3
"""
matrix_divided module.

This module provides a function for dividing all elements\
    of matrix by a specified divisor.

Functions:
    matrix_divided(matrix, div) -> list: Divided all elements of a matrix by\
        `div`, rounding to 2 decimal places.
"""


def matrix_divided(matrix, div) -> list:
    """
    Divide all elements of a matrix by the specified divisor.

    Args:
        matrix (list of lists): The matrix to be divided.\
            Each element must be an integer or float.
        div (int or float): The divisor by which all matrix\
            elements will be divided.

    Returns:
        list: A new matrix with elements rounded\
            to 2 decimal places afther division.

    Raises:
        TypeError: If matrix is not matrix (list of lists) or integers/floats,
                    if each row of the matrix doesn't have the same size.
                    or if `div` is not a number.
        ZeroDivisionError: If `div` equal to zero.
    """
    if not (isinstance(matrix, list) and matrix and all(
        isinstance(row, list) and row and
        all(isinstance(val, (int, float)) for val in row)
            for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(val / div, 2) for val in row] for row in matrix]
