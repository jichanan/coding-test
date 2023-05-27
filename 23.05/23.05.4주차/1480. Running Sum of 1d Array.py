class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        sum = 0

        for num in nums:
            sum += num
            ans.append(sum)
        
        return ans