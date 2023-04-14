class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and 0 <= i and j < len(arr):
                    if arr[i] == 2 * arr[j]:
                        return 'ture'