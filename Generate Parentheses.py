# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n, n, "", result)
        return result

    def dfs(self, left, right, path, result):
        if left == 0 and right == 0:
            result.append(path)
            return
        if left > 0:
            self.dfs(left - 1, right, path + "(", result)
        if right > left:
            self.dfs(left, right - 1, path + ")", result)
