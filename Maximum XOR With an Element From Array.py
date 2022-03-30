# Maximum XOR With an Element From Array
# You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].
# The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.
# Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.
# Example 1:
# Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# Output: [3,3,7]
# Example 2:
# Input: nums =  [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# Output: [15,-1,5]


from typing import List
import bisect


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        max_xor = 0
        for query in queries:
            xi, mi = query
            if xi > mi:
                max_xor = -1
                break
            elif xi == mi:
                max_xor = xi
                break
            else:
                index = bisect.bisect_left(nums, mi)
                if index == len(nums):
                    max_xor = -1
                else:
                    max_xor = max(max_xor, nums[index] ^ xi)
        return [max_xor] * len(queries)


def main():
    nums = [0, 1, 2, 3, 4]
    queries = [[3, 1], [1, 3], [5, 6]]
    print(Solution().maximizeXor(nums, queries))


if __name__ == "__main__":
    main()
