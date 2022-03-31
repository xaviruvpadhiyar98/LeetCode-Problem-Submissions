# Search in Rotated Sorted Array II

"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
"""

# Example 1:
# Input: nums = [1,0,1,1,1], target = 0
# Output: true
# Example 2:
# Input: nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2
# Output: true

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        if nums[0] == target:
            return True
        if nums[-1] == target:
            return True
        for i in range(1, len(nums) - 1):
            if nums[i] == target:
                return True
        return False


if __name__ == "__main__":
    print(Solution().search([1, 0, 1, 1, 1], 0))  # True
    print(
        Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2)
    )  # True
