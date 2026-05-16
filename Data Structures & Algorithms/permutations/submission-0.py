class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def permutation(perm,nums):
            nonlocal res
            if not nums:
                return res.append(perm.copy())
            for i in range(len(nums)):
                perm.append(nums[i])
                permutation(perm,nums[:i]+nums[i+1:])
                perm.pop()
        
        permutation([],nums)
        return res
