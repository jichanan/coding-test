class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        k = 0
        expected = heights.copy()
        expected.sort()
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                k += 1
        return k 