class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        ans = []
        if target not in nums:
            return [-1, -1]

        a = nums.index(target)
        ans.append(a)

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                ans.append(i)
                break

        return ans