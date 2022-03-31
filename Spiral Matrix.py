# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,7,8,9,6,3,2,5]


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][i])
            if left < right:
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res
