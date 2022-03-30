# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if (
                    i == ")"
                    and stack[-1] != "("
                    or i == "]"
                    and stack[-1] != "["
                    or i == "}"
                    and stack[-1] != "{"
                ):
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
