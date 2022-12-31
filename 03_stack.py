from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        20. Valid Parentheses
        """
        stack = []
        par = {"{": "}", "(": ")", "[": "]"}

        for sym in s:
            if sym in par:
                stack.append(sym)
            elif len(stack) == 0 or par[stack[-1]] != sym:
                return False
            else:
                stack.pop(-1)

        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()

    # print(s.isValid("()"))
    # print(s.isValid("()[]{}"))
    # print(s.isValid("(]"))
    # print(s.isValid("["))
