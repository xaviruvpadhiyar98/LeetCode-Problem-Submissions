# First Missing Positive
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


def main():
    sol = Solution()
    nums = [1, 2, 0]
    print(sol.firstMissingPositive(nums))
    nums = [3, 4, -1, 1]
    print(sol.firstMissingPositive(nums))
    nums = [7, 8, 9, 11, 12]
    print(sol.firstMissingPositive(nums))


if __name__ == "__main__":
    main()
