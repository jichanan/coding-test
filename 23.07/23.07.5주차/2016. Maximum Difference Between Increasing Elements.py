class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        n = len(nums)
        tem = []

        for i in range(n-1):
            for k in range(i+1,n):
                tem.append(nums[k]-nums[i])

        ans = max(tem)
        
        if ans <= 0:
            return -1

        return ans
