class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        for i in range(len(prices)):
            test = prices[i+1:]
            for k in test:
                if prices[i] >= k:
                    prices[i] = prices[i] - k
                    break
                    
        return prices

