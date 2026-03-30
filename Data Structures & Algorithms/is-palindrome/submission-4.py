class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0 
        last = len(s)-1
        s=s.lower()
        while start<last:
            if not s[start].isalnum():
                start +=1
                continue
            if not s[last].isalnum():
                last -=1
                continue
            if s[start]!= s[last]:
                return False
            start +=1
            last -=1
        return True
            
            

        