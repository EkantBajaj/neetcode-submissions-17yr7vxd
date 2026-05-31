class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub = []
        def generate(i):
            if i >= len(nums):
                result.append(sub.copy())
                return
            generate(i+1)

            sub.append(nums[i])
            generate(i+1)
            sub.pop()
        generate(0)
        return result