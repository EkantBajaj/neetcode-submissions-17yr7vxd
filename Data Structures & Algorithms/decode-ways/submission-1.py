from functools import cache
class Solution:
    
    def numDecodings(self, s: str) -> int:
        @cache
        def func(i):

            if i<0:
                return 1
            
            ans = 0
            if s[i]!='0':
                ans += func(i-1)
            
            if i>0 and 10 <= int(s[i-1:i+1]) <= 26:
                ans += func(i-2)
            
            return ans
        
        return func(len(s)-1)

        