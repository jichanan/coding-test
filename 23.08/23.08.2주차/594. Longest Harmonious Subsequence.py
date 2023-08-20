# 나의 풀이 (시간초과)
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        result = 0

        nums.sort()

        for num in nums:
            if num+1 in nums:
                result = max(result,nums.count(num) + nums.count(num+1))

        return result

# 솔루션
from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        result = 0
        num_count = Counter(nums)  # 각 숫자의 등장 횟수를 카운트

        for num in num_count:
            if num + 1 in num_count:
                result = max(result, num_count[num] + num_count[num + 1])

        return result