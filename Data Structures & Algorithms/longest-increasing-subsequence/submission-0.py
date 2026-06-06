class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def lis(n): # lenght of longest increasing subsequense ending on n
            if dp[n]!=-1:
                return dp[n]
            ans=1
            for i in range(n):
                if nums[i]<nums[n]:
                    ans = max(ans,lis(i)+1)
            dp[n]=ans
            return ans
        l = len(nums)
        dp = [-1]*(l)
        for i in range(l):
            lis(i)

        print(dp)

        return max(dp)        