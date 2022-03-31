# Add Binary
# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))
    print(Solution().addBinary("1010", "1011"))
