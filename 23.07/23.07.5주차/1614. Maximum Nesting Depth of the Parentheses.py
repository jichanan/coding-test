class Solution:
    def maxDepth(self, s: str) -> int:
        s = list(s)
        tem = 0
        depth = []

        for i in s:
            if i == '(':
                tem += 1
                depth.append(tem)
            elif i == ')':
                tem = tem - 1
                depth.append(tem)

        if depth == []:
            return 0

        ans = max(depth)
        return ans
