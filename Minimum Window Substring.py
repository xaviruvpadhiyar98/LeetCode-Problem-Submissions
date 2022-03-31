# Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Create a hashmap of all the characters in t
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        left, right = 0, 0
        min_len = len(s) + 1
        min_str = ""
        count = len(t)
        while right < len(s):
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
                if t_dict[s[right]] >= 0:
                    count -= 1
            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_str = s[left : right + 1]
                if s[left] in t_dict:
                    t_dict[s[left]] += 1
                    if t_dict[s[left]] > 0:
                        count += 1
                left += 1
            right += 1
        return min_str


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
