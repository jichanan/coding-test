# 나의 풀이 (time limit exceed)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        import re

        while '#' in s:
            s = re.sub('.#', '', s)

        while '#' in t:
            t = re.sub('.#', '', t)

        return s == t

# 솔루션
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for char in s:
            if char == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)

        for char in t:
            if char == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)

        return stack_s == stack_t