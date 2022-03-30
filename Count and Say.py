# # Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#     countAndSay(1) = "1"
#     countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n - 1)
            curr = ""
            count = 1
            for i in range(len(prev)):
                if i == len(prev) - 1 or prev[i] != prev[i + 1]:
                    curr += str(count) + prev[i]
                    count = 1
                else:
                    count += 1
            return curr
