# Word Search
"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time: O(m*n*4^(m*n))
        # Space: O(m*n)
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, 0, visited):
                    return True
        return False

    def dfs(self, board, word, i, j, idx, visited):
        if idx == len(word):
            return True
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or visited[i][j]
            or board[i][j] != word[idx]
        ):
            return False
        visited[i][j] = True
        res = (
            self.dfs(board, word, i + 1, j, idx + 1, visited)
            or self.dfs(board, word, i - 1, j, idx + 1, visited)
            or self.dfs(board, word, i, j + 1, idx + 1, visited)
            or self.dfs(board, word, i, j - 1, idx + 1, visited)
        )
        visited[i][j] = False
        return res
