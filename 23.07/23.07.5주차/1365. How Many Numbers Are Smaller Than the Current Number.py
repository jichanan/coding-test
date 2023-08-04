class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        count = 0

        for num in nums:
            for num2 in nums:
                if num > num2:
                    count += 1
            ans.append(count)
            count = 0

        return ans