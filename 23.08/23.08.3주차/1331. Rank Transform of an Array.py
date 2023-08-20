class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ans = arr.copy()
        tem = {}

        arr = set(arr)
        arr = list(arr)
        arr.sort()

        for i in range(1, len(arr)+1):
            tem[arr[i-1]] = i

        for i in range(len(ans)):
            ans[i] = tem[ans[i]]

        return ans