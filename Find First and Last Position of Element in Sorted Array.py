# Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,2,3,3,3,3,4,5,9], target = 3
# Output: [2,5]


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
                while left >= 0 and nums[left] == target:
                    left -= 1
                right = mid
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]
