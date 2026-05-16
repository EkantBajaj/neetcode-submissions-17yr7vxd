class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1c,s2c = [0]*26,[0]*26
        matches = 0
        for i in range(len(s1)):
            idx1 = ord(s1[i])-ord("a")
            idx2 = ord(s2[i])-ord("a")
            s1c[idx1]+=1
            s2c[idx2]+=1
        
        matches = 0
        for i in range(len(s1c)):
            if s1c[i]==s2c[i]:
                matches+=1
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            idx = ord(s2[r])-ord("a")
            s2c[idx]+=1

            if s1c[idx]==s2c[idx]:
                matches+=1
            elif s1c[idx]==s2c[idx]-1:
                matches-=1
            
            idx = ord(s2[l])-ord("a")
            s2c[idx]-=1
            if s1c[idx] == s2c[idx]+1:
                matches-=1
            elif s1c[idx]==s2c[idx]:
                matches+=1
            
            l+=1
        
        return matches==26