#나의 풀이(time limit exceed)
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        test = []

        for i in range(1, 100000):
            if i not in nums:
                test.append(i)

        ans = min(test)

        return ans

# 솔루션
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # 1부터 n까지의 숫자 중 양수인 경우만 저장
        positive_nums = set([num for num in nums if num > 0])
        
        # 1부터 n까지의 숫자 중 가장 작은 양수를 찾아서 반환
        for i in range(1, n+2):
            if i not in positive_nums:
                return i