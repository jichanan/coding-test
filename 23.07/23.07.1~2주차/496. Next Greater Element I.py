class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        tem = []
        ans = []
        found = True

        for num1 in nums1:
            test = nums2.index(num1) + 1
            a = nums2[test:]
            for i in a:
                if found and i > num1:
                    tem.append(i)
                    found = False
            if tem == []:
                ans.append(-1)
            else:
                k = tem[0]
                ans.append(k)
            found = True
            tem = []
        
        return ans