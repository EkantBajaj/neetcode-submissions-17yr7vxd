class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check=set(nums)
        if len(check)==len(nums):
            return False
        else:
            return True