class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        test = int(num ** (1/2))

        if test*test == num:
            return True