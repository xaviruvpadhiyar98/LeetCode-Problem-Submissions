# Substring with Concatenation of All Words
# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Example 3:
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# Example 4:
# Input: s = "mississippi", words = ["is"]
# Output: []


from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_num = len(words)
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        res = []
        for i in range(len(s) - word_num * word_len + 1):
            word_dict_tmp = word_dict.copy()
            for j in range(word_num):
                word = s[i + j * word_len : i + (j + 1) * word_len]
                if word in word_dict_tmp:
                    word_dict_tmp[word] -= 1
                    if word_dict_tmp[word] == 0:
                        del word_dict_tmp[word]
                else:
                    break
            if not word_dict_tmp:
                res.append(i)
        return res
