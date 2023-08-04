# 나의 풀이 (memory exceeded)
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        digit = ['0','1','2','3','4','5','6','7','8','9']
        ans = ""

        for i in s:
            if i in digit:
                ans = ans * int(i)
            else:
                ans += i

        return ans

# 솔루션
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0

        for i in s:
            if i.isdigit():
                total_length *= int(i)
            else:
                total_length += 1

        for i in reversed(s):
            k %= total_length
            if k == 0 and i.isalpha():
                return i

            if i.isdigit():
                total_length /= int(i)
            else:
                total_length -= 1