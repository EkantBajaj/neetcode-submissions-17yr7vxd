class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub = []
        nums = [i for i in range(1,n+1)]

        def generate(i):
            if len(sub)==k:
                res.append(sub.copy())
                return
            if i==len(nums):
                return
            
            generate(i+1)
            sub.append(nums[i])
            generate(i+1)
            sub.pop()
        
        generate(0)
        return res