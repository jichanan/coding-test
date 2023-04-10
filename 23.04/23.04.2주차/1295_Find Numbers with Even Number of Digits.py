class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = []
        for num in nums:
            if len(str(num)) % 2 == 0:
                even += [num]
        return len(even)