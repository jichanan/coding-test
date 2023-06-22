class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        count = []
        test = nums.copy()
        test.sort()

        if nums == test:
            return 0

        for i in range(len(nums)):
            if nums[i] != test[i]:
                count.append(i)
        end = len(count)
        ans = int(count[end-1]) - int(count[0]) + 1

        return ans