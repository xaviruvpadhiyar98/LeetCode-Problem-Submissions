# Sudoku Solver
# A sudoku solution must satisfy all of the following rules:
#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in range(1, 10):
                            if isValid(board, i, j, str(k)):
                                board[i][j] = str(k)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        def isValid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        solve(board)
