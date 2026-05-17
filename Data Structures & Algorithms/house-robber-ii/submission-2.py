class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp=[0]*(n+2)

        for i in range(n-1,0,-1):
            dp[i]=max(dp[i+1],nums[i]+dp[i+2])
        
        case1 = dp[1]

        dp = [0]*(n+1)
        for i in range(n-2,-1,-1):
            dp[i]=max(dp[i+1],nums[i]+dp[i+2])
        case2 = dp[0]

        return max(case1,case2)