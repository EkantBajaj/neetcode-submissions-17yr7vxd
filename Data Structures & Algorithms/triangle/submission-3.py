class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0]*len(row) for row in triangle]
        dp[-1] = triangle[-1][:]
        n = len(triangle)

        for r in range(n-2,-1,-1):
            for c in range(len(triangle[r])):
                dp[r][c]= triangle[r][c]+min(dp[r+1][c],dp[r+1][c+1])
        
        return dp[0][0]