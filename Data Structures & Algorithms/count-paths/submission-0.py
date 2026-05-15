class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row,col = m,n
        dp = [0]*n
        dp[0]=1
        for r in range(row):
            for c in range(col):
                if c-1>=0:
                    dp[c]+=dp[c-1]
        return dp[-1]