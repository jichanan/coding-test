# 나의 풀이
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        current_rich = 0

        for account in accounts:
            for i in account:
                current_rich += i
            if current_rich > richest:
                richest = current_rich
                current_rich = 0
            else:
                current_rich = 0
        
        return richest

# 솔루션 (가독성높이기)
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0

        for account in accounts:
            current_rich = 0
            current_rich = sum(account)
            richest = max(richest, current_rich)

        return richest

