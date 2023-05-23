# 솔루션 (동적 프로그래밍)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Coin Change Dynamic Programming
def coin_change(coins, amount):
    # dp 테이블 초기화
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # 동전 종류 반복
    for coin in coins:
        # 거스름돈 계산
        for i in range(coin, amount + 1):
            # 경우의 수 갱신
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # 결과 반환
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([10,50,100], 350))