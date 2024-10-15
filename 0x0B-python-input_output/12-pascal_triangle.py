#!/usr/bin/python3
"""pascal_triangle module - A script to generate Pascal's Triangle."""


def pascal_triangle(n: int) -> list:
    """
    Generate Pascal's Triangle up to a specified number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.
    """
    if n <= 0:
        return []
    rows = [[1]]
    while len(rows) != n:
        last_row = rows[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        rows.append(new_row)
    return rows
