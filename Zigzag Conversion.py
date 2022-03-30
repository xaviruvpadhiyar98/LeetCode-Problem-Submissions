# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                for j in range(i, len(s), 2 * numRows - 2):
                    res += s[j]
            else:
                for j in range(i, len(s), 2 * numRows - 2):
                    res += s[j]
                    if j + 2 * numRows - 2 - 2 * i < len(s):
                        res += s[j + 2 * numRows - 2 - 2 * i]
        return res
