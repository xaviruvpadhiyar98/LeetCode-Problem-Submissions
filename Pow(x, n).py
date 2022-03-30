# Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        return (
            self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)
        )
