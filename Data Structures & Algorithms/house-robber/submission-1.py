class Solution:
    def rob(self, nums: List[int]) -> int:
        # d[i] is the maximum amount i have on till index i
        # choice is that i can skip this house or rob this house
        # transition max(dp[i-1], num[i]+dp[i-2])
        n = len(nums)
        dp = [0]*(n+2)
        for i in range(n-1,-1,-1):
            dp[i]=max(dp[i+1],nums[i]+dp[i+2])
        return dp[0]
