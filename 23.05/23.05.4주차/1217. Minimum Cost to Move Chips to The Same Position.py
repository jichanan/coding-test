class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        odd = []
        even = []

        for i in position:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        if len(odd) < len(even):
            return len(odd)
        else:
            return len(even)