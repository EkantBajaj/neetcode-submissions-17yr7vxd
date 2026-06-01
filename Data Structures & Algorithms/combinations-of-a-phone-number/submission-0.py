class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res=[]
        sub=[]
        if digits=="":
            return []
        
        def generate(i):

            if i==len(digits):
                res.append("".join(sub))
                return
            
            for ch in phone[digits[i]]:
                sub.append(ch)
                generate(i+1)
                sub.pop()

        generate(0)

        return res   
        