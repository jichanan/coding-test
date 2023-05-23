# 나의 풀이 -> O(n^2)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = []
        for i in nums:
            if nums.count(i) == 1:
                return i

# 솔루션
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            if freq == 1:
                return num