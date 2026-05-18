class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf")]*(amount+1)
        dp[0]=0

        for coin in coins:
            for amnt in range(coin,amount+1):
                dp[amnt]= min(dp[amnt],dp[amnt-coin]+1)
        
        if dp[amount]==float("inf"):
            return -1
        return dp[amount]