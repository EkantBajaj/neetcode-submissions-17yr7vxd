class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False]*len(nums)
        
        def permutation(perm):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if (
                    i > 0 and
                    nums[i] == nums[i - 1] and
                    not used[i - 1]
                ):  # skip duplicate branch
                    continue
                perm.append(nums[i])
                used[i]=True
                permutation(perm)
                perm.pop()
                used[i]=False
        
        permutation([])
        return res