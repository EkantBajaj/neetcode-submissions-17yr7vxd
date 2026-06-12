from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

    
        @cache
        def func(i,amount):
            if amount==0:
                return 0
            if i<0:
                return float("inf")
            take = float("inf")
            if coins[i]<= amount:
                take = 1+func(i,amount-coins[i])   
            not_take = func(i-1,amount)

            return min(take,not_take)
        
        ans= func(len(coins)-1,amount)
        return ans if ans!=float("inf") else -1