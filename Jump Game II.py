# Jump Game II
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Input: nums = [2,3,1,1,4]
# Output: 2
# Input: nums = [2,3,0,1,4]
# Output: 2


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 0
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]
