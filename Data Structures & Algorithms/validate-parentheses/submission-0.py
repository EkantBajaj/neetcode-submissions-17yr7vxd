class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{",")":"(","]":"["}
        openSet = {"{","(","["}
        stack = []
        for char in s:
            if char in openSet:
                stack.append(char)
            elif stack and stack.pop()==closeToOpen[char]:
                continue
            else:
                return False
        return True if not stack else False
        