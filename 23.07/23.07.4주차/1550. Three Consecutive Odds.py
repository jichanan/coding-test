class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        max_odd = 0
        tem = 0

        for i in arr:
            if i % 2 == 1:
                tem += 1
                max_odd = max(tem, max_odd)
            else:
                tem = 0

        if max_odd >= 3:
            return True
        else:
            return False