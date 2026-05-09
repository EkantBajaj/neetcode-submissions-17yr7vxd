class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"*": lambda a,b : a*b , "+": lambda a,b :a+b, "-": lambda a,b: a-b, "/": lambda a,b: a/b}
        for char in tokens:
            if char not in operations:
                stack.append(char)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operations[char](a,b))
        return int(stack[-1])