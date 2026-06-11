class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

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
        
        generate(nums)

        return res
