class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []

        for num in nums1:
            if num in nums2:
                ans.append(num)

        ans = set(ans)

        ans = list(ans)

        return ans