class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res = []
        sub = []
        candidates.sort()
       

        def generate(i,total):
            if total == target:
                res.append(sub.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            sub.append(candidates[i])
            generate(i+1,total+candidates[i])
            sub.pop()
            j=i
            while j+1<len(candidates) and candidates[j]==candidates[j+1]:
                j+=1
            
            generate(j+1,total)
            
        
        generate(0,0)
        return res