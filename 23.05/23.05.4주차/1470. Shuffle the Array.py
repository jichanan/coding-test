class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []
        half = int(len(nums) / 2)

        left = nums[0:half]
        right = nums[half:]
        for i in range(half):
            ans.append(left[i])
            ans.append(right[i])
            
        return ans