class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       count = defaultdict(int)
       l =0
       r = 0
       res=0
       count[s[r]]+=1
       while r <len(s):
        if r-l+1 - max(count.values()) <= k:
            print(r,l,count)
            res=max(res,r-l+1)
            r+=1
            if r<len(s):
                count[s[r]]+=1
        else:
            count[s[l]]-=1
            l+=1
       return res
