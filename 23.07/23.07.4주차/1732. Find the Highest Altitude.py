class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        tem = [0]

        for i in gain:
            tem.append(tem[-1] + i)

        ans = max(tem)

        return ans