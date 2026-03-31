class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0 
        i=1
        buy_price = prices[0]
        while i < len(prices):
            if prices[i]< buy_price:
                buy_price = prices[i]
            profit = max(profit,prices[i]-buy_price)
            i+=1
        
        return profit