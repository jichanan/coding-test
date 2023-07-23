class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        ans = 0
        col = list(zip(*grid))
        for i,row in enumerate(grid):
            s = sum(row)
            if s > 1:
                ans += s
            elif s == 1:
                j = row.index(1)
                if sum(col[j]) > 1:
                    ans += 1
        return ans