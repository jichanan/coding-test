# 나의 풀이 (시간초과)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        sum = 1

        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            for r in nums_copy:
                sum = r * sum
            ans.append(sum)
            sum = 1
        
        return ans

# 솔루션 - 왼쪽요소들의 곱과 오른쪽요소들의 곱을 곱한다.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1] * length

        # 왼쪽 요소들의 곱 계산
        left_product = 1
        for i in range(length):
            result[i] *= left_product
            left_product *= nums[i]

        # 오른쪽 요소들의 곱 계산 및 결과에 곱셈
        right_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result