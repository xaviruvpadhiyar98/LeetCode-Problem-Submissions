# Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return list(d.values())
