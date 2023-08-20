class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 == 0:
            l = len(nums1) / 2 - 1
            l = int(l)
            ans = (nums1[l] + nums1[l+1]) / 2
        else:
            l = (len(nums1) // 2) 
            ans = nums1[l]

        return ans