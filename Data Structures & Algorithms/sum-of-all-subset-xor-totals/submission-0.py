class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def generate(i,cur_xor):
            nonlocal res
            if i==len(nums):
                res+=cur_xor
                return
            
            generate(i+1,cur_xor)
            generate(i+1,cur_xor^nums[i])
        generate(0,0)
        return res