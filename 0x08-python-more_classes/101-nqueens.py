#!/usr/bin/python3
"""
N-Queens problem module
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, solutions):
    """
    Solve the N-Queens problem using backtracking
    """
    n = len(board)

    # Base case: All queens are placed
    if row == n:
        solutions.append(board[:])
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1


def print_solution(board):
    """
    Print the N-Queens solution in the required format
    """
    n = len(board)
    solution = []

    for row in range(n):
        queen_pos = [row, board[row]]
        solution.append(queen_pos)

    print(solution)


if __name__ == '__main__':
    # Parse the command-line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [-1] * n

    # Solve the N-Queens problem
    solutions = []
    solve_nqueens(board, 0, solutions)

    # Print the solutions
    for solution in solutions:
        print_solution(solution)
