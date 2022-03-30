# Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = sorted(nums[i + 1 :])
        return
