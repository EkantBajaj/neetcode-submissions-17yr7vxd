class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        bestBuy = prices[0]
        maxProfit = 0

        for price in prices:
            bestBuy = min(bestBuy,price)
            maxProfit = max(maxProfit,price-bestBuy)
        return maxProfit 