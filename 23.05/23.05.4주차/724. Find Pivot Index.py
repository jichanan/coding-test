class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            right = sum(nums[i+1:])
            left = sum(nums[:i])
            if left == right:
                return i
        return -1