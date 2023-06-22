class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dic = {}
        ans = []
        for num in nums:
            if num in dic:
                dic[num] += 1
            else: 
                dic[num] = 1

        for key, val in dic.items():
            if val == 2:
                ans.append(key)

        ans.sort()
        return ans