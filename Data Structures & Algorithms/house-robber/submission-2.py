from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def func(n): #max money i will have on after n houses
            if n<=0:
                return 0
            
            return max(func(n-1),nums[n-1]+func(n-2))
        return func(len(nums))

            