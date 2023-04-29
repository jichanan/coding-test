class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        new = []
        for i in nums:
            if i % 2 == 0:
                new.insert(0, i)
            else:
                new.append(i)
        return new