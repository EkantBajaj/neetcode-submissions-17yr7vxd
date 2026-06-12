class Solution:
    def climbStairs(self, n: int) -> int:
        
        dpArray = [-1]*(n+1)
        def dp(n): # number of ways to reach n
            if dpArray[n]!=-1:
                return dpArray[n]
            if n==0 or n==1:
                return 1
            ans = dp(n-1)+dp(n-2)
            dpArray[n]=ans
            return ans
        
        return dp(n)

