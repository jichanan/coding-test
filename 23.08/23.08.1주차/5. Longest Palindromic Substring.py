class Solution:
    def longestPalindrome(self, s: str) -> str:
        tem = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                test = s[i:j+1]
                if test == test[::-1]:
                    tem.append(test)

        ans = max(tem, key=len)

        return ans