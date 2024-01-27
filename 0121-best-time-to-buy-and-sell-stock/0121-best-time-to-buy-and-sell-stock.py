class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > max_price:
                max_profit = max(prices[i] - max_price, max_profit)
            else:
                max_price = prices[i]
        return max_profit