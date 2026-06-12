from functools import cache
class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def func(start,n):
            if n<=start:
                return 0
            
            return max(func(start,n-1),nums[n-1]+func(start,n-2))
        n=len(nums)
        return max(func(0,n-1),func(1,n))


