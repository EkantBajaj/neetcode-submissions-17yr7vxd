class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)

        stack = []
        for i,temprature in enumerate(temperatures):
            while stack and temprature > stack[-1][1]:
                index,_ = stack.pop()
                result[index]= i-index
            stack.append((i,temprature))
        return result