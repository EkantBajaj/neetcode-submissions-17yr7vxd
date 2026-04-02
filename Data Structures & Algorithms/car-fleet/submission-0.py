class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        
        cars = sorted(cars)
        
        stack = []
        for i in range(len(cars)-1,-1,-1):
            time = float(target-cars[i][0])/cars[i][1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
