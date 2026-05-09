class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        bestBuy = prices[0]

        for price in prices:
            if price < bestBuy:
                bestBuy = price
            profit = max(profit, price-bestBuy)

        return profit    