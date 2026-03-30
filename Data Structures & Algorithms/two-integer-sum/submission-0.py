class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_map = {}
        for i,val in enumerate(nums):
            if val not in index_map:
                index_map[target-val]=i
            else:
                return [index_map[val],i]