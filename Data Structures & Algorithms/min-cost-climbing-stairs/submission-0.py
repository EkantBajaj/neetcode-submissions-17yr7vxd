class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d=[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            d[i] = min(cost[i-1]+d[i-1],cost[i-2]+d[i-2])
        return d[-1]
