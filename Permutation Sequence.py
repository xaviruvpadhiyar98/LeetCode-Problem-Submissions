# Permutation Sequence
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
# Given n and k, return the kth permutation sequence.


from collections import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(map(str, list(permutations(range(1, n + 1), n))[k - 1]))
