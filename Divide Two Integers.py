# Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Constraints:
# -231 <= dividend, divisor <= 231 - 1
# divisor != 0
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Example 3:
# Input: dividend = -2147483648, divisor = 2
# Output: -1073741824
# Example 4:
# Input: dividend = -2147483648, divisor = -3
# Output: 715827882


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0:
            return self.divide_positive(abs(dividend), abs(divisor))
        else:
            return -self.divide_positive(abs(dividend), abs(divisor))

    def divide_positive(self, dividend: int, divisor: int) -> int:
        res = 0
        while dividend >= divisor:
            tmp = divisor
            cnt = 1
            while tmp <= (dividend >> 1):
                tmp <<= 1
                cnt <<= 1
            res += cnt
            dividend -= tmp
        return res
