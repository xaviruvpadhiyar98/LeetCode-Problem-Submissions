# Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# IndexError: string index out of range
# if p[1] == "*":
# Fix the below testcase also
# Input
#   "mississippi"
#   "mis*is*p*."
# Output
#   true
# Expected
#   false
# Input
#   "ab"
#   ".*"
# Output
#   false
# Expected
#   true


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == ".")
        if p[1] != "*":
            if len(s) == 0 or (s[0] != p[0] and p[0] != "."):
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            if self.isMatch(s, p[2:]):
                return True
            i = 0
            while i < len(s) and (s[i] == p[0] or p[0] == "."):
                if self.isMatch(s[i + 1 :], p[2:]):
                    return True
                i += 1
            return False
