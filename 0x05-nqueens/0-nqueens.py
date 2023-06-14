#!/usr/bin/python3
"""
N-Queens puzzle solver
"""

import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the same diagonal (left to right)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check if there is a queen in the same diagonal (right to left)
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens(board, row):
    """
    Recursively solve the N-Queens puzzle
    """
    if row == len(board):
        solutions.append(board.copy())
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(board, 0)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])
