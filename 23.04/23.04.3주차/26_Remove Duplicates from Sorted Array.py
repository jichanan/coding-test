# 내가 푼 답안 (오답)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        test = []
        for num in nums:
            if num not in test:
                test.append(num)
            else:
                nums.remove(num)

# 솔루션
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for num in nums:
            while nums.count(num) > 1:
                nums.remove(num)