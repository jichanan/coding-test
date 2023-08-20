class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        tem = list(set(arr))
        ans = []
        for i in tem:
            ans.append(arr.count(i))

        if len(ans) == len(set(ans)):
            return True
        else:
            return False