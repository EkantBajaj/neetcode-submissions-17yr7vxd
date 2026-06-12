from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def func(n):
         # minimum cost to reach at n
            if n==0:
                return 0
            if n==1:
                return 0

            return min(func(n-1)+cost[n-1],func(n-2)+cost[n-2])
        return func(len(cost))
    