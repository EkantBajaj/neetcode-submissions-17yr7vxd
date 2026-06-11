class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        used = [False]*len(nums)

        def generate_v2():
            if len(sub)==len(nums):
                res.append(sub.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                sub.append(nums[i])
                used[i]=True
                generate_v2()
                sub.pop()
                used[i]=False
        

        def generate(choices):
            if len(sub)==len(nums):
                res.append(sub.copy())
                return
            if not choices:
                return
            
            for i,choice in enumerate(choices):
                sub.append(choice)
                generate(choices[0:i]+choices[i+1:])
                sub.pop()
        
        generate_v2()

        return res
