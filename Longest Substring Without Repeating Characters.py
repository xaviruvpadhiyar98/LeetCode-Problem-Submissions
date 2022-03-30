# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        start = 0
        end = 0
        char_dict = {}
        while end < len(s):
            if s[end] in char_dict:
                start = max(start, char_dict[s[end]] + 1)
            char_dict[s[end]] = end
            end += 1
            max_len = max(max_len, end - start)
        return max_len
