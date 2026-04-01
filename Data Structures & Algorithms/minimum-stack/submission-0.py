class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [float("infinity")]
        

    def push(self, val: int) -> None:
        if val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
