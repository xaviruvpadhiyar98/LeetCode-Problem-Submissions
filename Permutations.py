# Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
