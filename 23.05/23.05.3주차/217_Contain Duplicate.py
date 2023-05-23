class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set_nums = set(nums)
        if len(nums) == len(set_nums):
            return False
        else: 
            return True