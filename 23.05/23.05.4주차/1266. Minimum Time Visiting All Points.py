class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        ans = 0

        for i in range(len(points)-1):
            test = abs(points[i][0] - points[i+1][0])
            test2 = abs(points[i][1] - points[i+1][1])
            ans += max(test, test2)
        return ans