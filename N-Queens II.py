# N-Queens II
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.


class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    dfs(queens + [q], xy_diff + [p - q], xy_sum + [p + q])

        result = []
        dfs([], [], [])
        return len(result)
