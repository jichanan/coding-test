class Solution:
    def addBinary(self, a: str, b: str) -> str:
        test = bin(int(a,2) + int(b,2))[2:]

        return test