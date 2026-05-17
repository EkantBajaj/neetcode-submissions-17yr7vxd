class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0]*len(obstacleGrid[0])
        dp[0]=1
        row,col = len(obstacleGrid),len(obstacleGrid[0])
        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c]==1:
                    dp[c]=0
                elif c-1 >= 0:
                    dp[c] = dp[c]+dp[c-1]
        return dp[-1]