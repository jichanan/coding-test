class Solution:
    def thousandSeparator(self, n: int) -> str:
        b = len(str(n))
        nums = []

        while b > 0:
            nums.append(b-3)
            b = b - 3

        tem = [num for num in nums if num > 0]

        n = list(str(n))

        for i in tem:
            n.insert(i,'.')

        n = ''.join(n)
        return n
