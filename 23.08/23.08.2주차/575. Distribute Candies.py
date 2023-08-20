class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        tem = {}

        for candy in candyType:
            if candy not in tem:
                tem[candy] = 1
            else:
                tem[candy] += 1

        test = list(tem.keys())
        leng = int(len(candyType) / 2)

        if len(test) >= leng:
            return leng
        else:
            return len(test)