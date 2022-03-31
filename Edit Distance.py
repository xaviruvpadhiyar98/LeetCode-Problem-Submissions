# Edit Distance

"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize the matrix
        m = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        # Fill the first row and column
        for i in range(len(word1) + 1):
            m[i][0] = i
        for j in range(len(word2) + 1):
            m[0][j] = j
        # Fill the rest of the matrix
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    m[i][j] = m[i - 1][j - 1]
                else:
                    m[i][j] = min(m[i - 1][j - 1] + 1, m[i - 1][j] + 1, m[i][j - 1] + 1)
        # Return the value in the bottom right corner
        return m[-1][-1]
