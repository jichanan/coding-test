class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, num in enumerate(nums):
            if (target - num in nums) and (index != nums.index(target-num)):
                return index, nums.index(target-num)