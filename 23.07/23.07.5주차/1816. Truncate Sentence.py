class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split()

        tem = a[:k]

        ans = ' '.join(tem)
        return ans