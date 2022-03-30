# Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if not self.isValid(row):
                return False
        # check columns
        for i in range(9):
            column = [row[i] for row in board]
            if not self.isValid(column):
                return False
        # check 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [
                    board[i][j],
                    board[i][j + 1],
                    board[i][j + 2],
                    board[i + 1][j],
                    board[i + 1][j + 1],
                    board[i + 1][j + 2],
                    board[i + 2][j],
                    board[i + 2][j + 1],
                    board[i + 2][j + 2],
                ]
                if not self.isValid(square):
                    return False
        return True

    def isValid(self, row):
        row = [i for i in row if i != "."]
        if len(row) != len(set(row)):
            return False
        return True
