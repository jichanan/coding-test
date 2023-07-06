# 나의 풀이 (memory limit exceed)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = [[]]  
        ans = []

        for num in nums:
            result += [curr + [num] for curr in result]

        for sum3 in result:
            if len(sum3) == 3 and sum(sum3) == 0:
                sum3.sort()
                ans.append(tuple(sum3))

        b = set(ans)
        return b

# 솔루션
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # 입력 숫자 배열을 오름차순으로 정렬
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 중복된 숫자는 건너뜀

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 중복된 숫자 건너뜀
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result