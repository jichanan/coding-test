# 나의 풀이 (Time Limit Exceeded)
class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        move = 0

        for i in range(len(nums)):
            while nums.count(nums[i]) != 1:
                nums[i] += 1
                move += 1

        return move

# 솔루션
class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        level, res = -1, 0
        for num in sorted(nums):
            if level < num:
                level = num
            else:
                level += 1
                res += (level - num)
        return res