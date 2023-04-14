class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        # 3개 이하면 mountain array 성립 불가능
        if len(arr) < 3:
            return False
        i = 0
        while i < (len(arr) - 1) and arr[i] < arr[i+1]:
            i += 1
        if i == 0 or i == len(arr) - 1:
            return False
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1
        if i == len(arr) - 1:
            return True