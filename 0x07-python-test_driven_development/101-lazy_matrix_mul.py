#!/usr/bin/python3
"""
lazy_matrix_mul module.

This module defines a function for multiplying two matrices using NumPy.

The `lazy_matrix_mul` function performs matrix multiplication\
     using NumPy's matmul operation.
"""

import numpy


def lazy_matrix_mul(m_a, m_b) -> list:
    """
    Multiply two matrices using NumPy's matmul.

    Args:
        m_a (numpy.ndarray): The first matrix represented as a NumPy array.
        m_b (numpy.ndarray): The second matrix represented as a NumPy array.

    Returns:
        numpy.ndarray: The result of multiplying m_a and m_b.
    """
    return numpy.matmul(m_a, m_b)
