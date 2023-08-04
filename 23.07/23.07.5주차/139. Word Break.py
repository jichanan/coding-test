# 나의 풀이 (오답)
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        for word in wordDict:
            if word in s:
                s = s.replace(word, "")

        if s != "":
            return False
        else:
            return True

# 솔루션
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[n]