# Maximal Rectangle
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # DP to store the max area of rectangle ending at each position
        dp = [[0] * n for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i - 1][j] + 1 if i > 0 else 1
                else:
                    dp[i][j] = 0
            max_area = max(max_area, self.largestRectangleArea(dp[i]))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # Stack to store the indices of the bars
        stack = []
        # The maximum area
        max_area = 0
        # The index of the bar
        i = 0
        # Loop through the heights array
        while i < len(heights):
            # If the stack is empty or the current bar is higher than the bar at the top of the stack
            if not stack or heights[i] >= heights[stack[-1]]:
                # Push the current index to the stack
                stack.append(i)
                # Increment the index
                i += 1
            # If the current bar is lower than the bar at the top of the stack
            else:
                # Pop the index from the stack
                j = stack.pop()
                # Calculate the area with the popped index and the current index
                max_area = max(
                    max_area, heights[j] * (i if not stack else i - stack[-1] - 1)
                )
        # Calculate the area with the remaining bars
        while stack:
            j = stack.pop()
            max_area = max(
                max_area, heights[j] * (i if not stack else i - stack[-1] - 1)
            )
        return max_area
