class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cons = 0
        cons_max = 0
        for num in nums:
            if num == 1:
                cons += 1
            else:
                if cons > cons_max:
                    cons_max = cons
                cons = 0
            cons_max = max(cons, cons_max)
        return cons_max