class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False]*len(nums)
        
        def permutation(perm):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                perm.append(nums[i])
                used[i]=True
                permutation(perm)
                perm.pop()
                used[i]=False
        
        permutation([])
        return res
