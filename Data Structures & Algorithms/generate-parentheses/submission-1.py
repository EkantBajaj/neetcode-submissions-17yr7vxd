class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        sub = []

        def generate(o,c):
            if o==n and c==n:
                result.append("".join(sub.copy()))
            
            if o<n:
                sub.append("(")
                generate(o+1,c)
                sub.pop()
            
            if c<n:
                if c<o:
                    sub.append(")")
                    generate(o,c+1)
                    sub.pop()
        
        generate(0,0)

        return result