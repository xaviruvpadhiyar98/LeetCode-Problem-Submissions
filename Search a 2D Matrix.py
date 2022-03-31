# Search a 2D Matrix
"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # If the matrix is empty, return False
        if not matrix:
            return False
        # Initialize the row and column indices
        row = len(matrix)
        col = len(matrix[0])
        # Initialize the row and column indices
        row_index = 0
        col_index = col - 1
        # Iterate through the matrix
        while row_index < row and col_index >= 0:
            # If the element is equal to the target, return True
            if matrix[row_index][col_index] == target:
                return True
            # If the element is greater than the target, decrement the column index
            elif matrix[row_index][col_index] > target:
                col_index -= 1
            # If the element is less than the target, increment the row index
            else:
                row_index += 1
        # Return False
        return False
