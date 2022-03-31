# Combinations
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].


from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))
