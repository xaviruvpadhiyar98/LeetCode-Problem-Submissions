# Largest Rectangle in Histogram

from typing import List


class Solution:
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
