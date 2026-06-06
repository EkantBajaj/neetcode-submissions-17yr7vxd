class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def coinNeeded(am):
            #state: minimum coin need for amount am
            if dp[am]!=-1:
                return dp[am]
            if am==0:
                return 0
            ans = float("inf")
            for coin in coins:
                if am-coin >= 0:
                    ans = min(ans,coinNeeded(am-coin)+1)
            dp[am]=ans
            return ans
        dp=[-1]*(amount+1)
        ans=coinNeeded(amount)
        print(dp)
        return ans if ans!=float("inf") else -1 