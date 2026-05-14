class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i-1] if i>0 else 0
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
        
        return -1
