class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result  = []
        sub_set = []
        def generate(i,current_sub_set):
            if i==len(nums):
                result.append(current_sub_set.copy())
                return
            
            current_sub_set.append(nums[i])
            generate(i+1,current_sub_set)
            current_sub_set.pop()
            generate(i+1,current_sub_set)
        
        generate(0,sub_set)
        return result