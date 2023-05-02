class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        for i in nums:
            while nums.count(i) > 1:
                nums.remove(i)
        nums.sort()
        try:
            ans = nums[-3]
        except:
            ans = max(nums)
        return ans