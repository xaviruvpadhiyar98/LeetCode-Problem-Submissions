# Sort Colors
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize the indices
        red = 0
        white = 0
        blue = len(nums) - 1
        # Iterate through the array
        while white <= blue:
            # If the element is 0, swap it with the element at the index of red
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                # Increment red
                red += 1
                # Increment white
                white += 1
            # If the element is 1, increment white
            elif nums[white] == 1:
                white += 1
            # If the element is 2, swap it with the element at the index of blue
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                # Decrement blue
                blue -= 1
        return nums
