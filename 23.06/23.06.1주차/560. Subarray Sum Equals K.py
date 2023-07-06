# 나의 풀이 (memory limit exceeded)
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0

        def get_subarrays(nums):
            result = []

            for i in range(len(nums)):
                for j in range(i+1, len(nums)+1):
                    result.append(nums[i:j])

            return result

        subarrays = get_subarrays(nums)

        for x in subarrays:
            if sum(x) == k:
                count += 1

        return count

# 솔루션
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        sum_counts = {0: 1}  # 초기값으로 0의 누적 합이 한 번 등장한 것으로 설정합니다.

        for num in nums:
            cumulative_sum += num

            # 누적 합에서 k를 뺀 값이 이전에 등장한 적이 있는지 확인합니다.
            if cumulative_sum - k in sum_counts:
                count += sum_counts[cumulative_sum - k]

            # 현재 누적 합의 빈도를 증가시킵니다.
            if cumulative_sum in sum_counts:
                sum_counts[cumulative_sum] += 1
            else:
                sum_counts[cumulative_sum] = 1

        return count