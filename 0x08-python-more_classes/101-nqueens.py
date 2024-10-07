#!/usr/bin/python3
"""N-Queens Puzzle Solver.

This script solves the N-Queens puzzle, which aims to place N
non-attacking queens on an NxN chessboard. It determines all
possible solutions for the puzzle.

Usage:
    ./101-nqueens.py N

    Where `N` is an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Each solution is represented as a list of queen positions,
where each position is represented as [row, column].

The script provides functions for initializing the chessboard,
finding solutions, and displaying the results.
"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[" " for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board):
    """Return a deep copy of a chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Return the queen positions on a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return (solution)


def xout(board, row, col):
    """Mark non-attacking positions on the chessboard as 'x'.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """
    Recursively solve the N-Queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The number of placed queens.
        solutions (list): A list of solutions.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
