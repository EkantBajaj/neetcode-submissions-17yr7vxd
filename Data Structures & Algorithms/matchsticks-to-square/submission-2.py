class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_match = sum(matchsticks)
        length = sum_match//4
        sides = [0]*4
        matchsticks.sort(reverse=True)
        if sum_match%4 !=0:
            return False
        def generate(i):
            if i==len(matchsticks):
                return True
            
            for side in range(4):
                if sides[side]+matchsticks[i] <= length:
                    sides[side]+= matchsticks[i]
                    if generate(i+1):
                        return True
                    sides[side]-= matchsticks[i]
            
            return False
        
        return generate(0)
