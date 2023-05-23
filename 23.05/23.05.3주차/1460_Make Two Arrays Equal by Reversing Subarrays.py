class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        target.sort()
        arr.sort()
        if target == arr:
            return True
        else:
            return False