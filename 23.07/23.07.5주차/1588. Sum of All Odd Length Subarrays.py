class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total_sum = 0

        for i in range(n):
            for j in range(i, n, 2):
                total_sum += sum(arr[i:j+1])

        return total_sum
