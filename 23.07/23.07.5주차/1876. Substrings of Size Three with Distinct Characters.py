class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        tem = []
        ans = 0
        n = len(s)

        for i in range(n-2):
            tem.append(s[i:i+3])

        for i in tem:
            if len(set(i)) == 3:
                ans += 1

        return ans