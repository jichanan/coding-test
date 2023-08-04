import re
class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            test = re.findall("\([^()]*\)", s)
            a = test[-1][1:-1][::-1]
            s = s.replace(test[-1], a, 1)
        return s
