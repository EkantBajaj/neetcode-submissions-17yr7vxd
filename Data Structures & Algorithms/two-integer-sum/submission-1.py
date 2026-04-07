class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        n=len(nums)
        for i in range(0,n):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target-nums[i]]=i

            

