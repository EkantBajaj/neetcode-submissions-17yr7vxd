class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        # def generate(i,total):
        #     if total == target:
        #         res.append(sub.copy())
        #         return
            
        #     if i>=len(nums) or total>target:
        #         return
        #     generate(i+1,total)
        #     sub.append(nums[i])
        #     generate(i,total+nums[i])
        #     sub.pop()
        
        # generate(0,0)
        # return res

        # res = []
        # sub = []

        def generate(i,total):
            if total == target:
                res.append(sub.copy())
                return
            if i>=len(nums) or total>target:
                return

            generate(i+1,total)
            sub.append(nums[i])
            generate(i,total+nums[i])
            sub.pop()

        generate(0,0)
        return res