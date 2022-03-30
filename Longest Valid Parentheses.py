# Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:
# Input: s = "(()"
# Output: 2
# Example 2:
# Input: s = ")()())"
# Output: 4
# Example 3:
# Input: s = ""
# Output: 0
# Example 4:
# Input: s = ")()())"
# Output: 4


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
