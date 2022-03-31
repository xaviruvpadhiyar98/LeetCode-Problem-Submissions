# Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).


from itertools import combinations, chain, product
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(
            chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))
        )


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
