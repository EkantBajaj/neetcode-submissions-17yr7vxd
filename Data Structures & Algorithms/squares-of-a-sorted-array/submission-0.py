class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        n = len(nums)
        res = [0]*n
        l =0
        r=n-1
        n = n-1
        while n >=0 and l<=r:
            if abs(nums[l]) >= abs(nums[r]):
                res[n]=(nums[l]**2)
                l+=1
            else:
                res[n]=(nums[r]**2)
                r-=1
            n-=1
        return res