class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res  = 0
        def generate(i,curr_xor):
            nonlocal res
            if i==len(nums):
                res += curr_xor
                return
            
            generate(i+1,curr_xor^nums[i])
            generate(i+1,curr_xor)

        generate(0,0)

        return res