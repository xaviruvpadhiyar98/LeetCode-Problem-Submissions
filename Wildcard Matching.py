# Wildcard Matching
# Example 1:
# Input: s = "aa", p = "*"
# Output: true
# Example 2:
# Input: s = "aa", p = "a"
# Output: false
# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
# Example 4:
# Input: s = "adceb", p = "*a*b"
# Output: true


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p) == 1:
            return s == p or p == "?"
        if p[1] != "*":
            return s[0] == p[0] and self.isMatch(s[1:], p[1:])
        while s and p[0] != "?" and p[0] != s[0]:
            s = s[1:]
        return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
