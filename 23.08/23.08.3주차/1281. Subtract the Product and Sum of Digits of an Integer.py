class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))

        s = 0
        m = 1

        for i in n:
            s += int(i)

        for i in n:
            m *= int(i)

        ans = m-s

        return ans