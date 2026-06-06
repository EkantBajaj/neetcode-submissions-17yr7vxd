class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def func(i,amount):
            if amount==0:
                return 1
            if i<0:
                return 0
            if dp[i][amount]!=-1:
                return dp[i][amount]
            ways=0
            for coin in range(0,amount+1,coins[i]):
                ways += func(i-1,amount-coin)
            dp[i][amount]=ways
            return ways
        
        return func(len(coins)-1,amount)