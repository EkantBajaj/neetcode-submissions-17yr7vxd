class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []
        def generate(i):
            if i>=len(nums):
                res.append(sub.copy())
                return

            j=i
            while j+1 < len(nums) and nums[j]==nums[j+1]:
                j+=1
            
            generate(j+1)

            sub.append(nums[i])
            generate(i+1)
            sub.pop()
        
        generate(0)
        return res