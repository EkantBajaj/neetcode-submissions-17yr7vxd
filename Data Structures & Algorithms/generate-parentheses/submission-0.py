class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        sub = []

        def generate(o,c):
            if o==0 and c==0:
                result.append("".join(sub.copy()))
                return
            
            if o>0:
                sub.append("(")
                generate(o-1,c)
                sub.pop()
            
            if c>0:
                if o<c:
                    sub.append(")")
                    generate(o,c-1)
                    sub.pop()
        generate(n,n)
        return result