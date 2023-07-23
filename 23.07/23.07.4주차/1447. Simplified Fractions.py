def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        fractions = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if gcd(numerator, denominator) == 1:
                    fractions.append(f"{numerator}/{denominator}")
        return fractions