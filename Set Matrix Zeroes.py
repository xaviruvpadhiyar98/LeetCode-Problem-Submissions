# Set Matrix Zeroes

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


from typing import List


class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Initialize the row and column indices
        row = len(matrix)
        col = len(matrix[0])
        # Initialize the row and column indices
        row_index = [False for i in range(row)]
        col_index = [False for i in range(col)]
        # Iterate through the matrix
        for i in range(row):
            for j in range(col):
                # If the element is 0, set the row and column indices
                if matrix[i][j] == 0:
                    row_index[i] = True
                    col_index[j] = True
        # Iterate through the matrix again
        for i in range(row):
            for j in range(col):
                # If the row or column index is True, set the element to 0
                if row_index[i] or col_index[j]:
                    matrix[i][j] = 0
        return matrix
