"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        valToNode = {}

        dummy = Node(0,None,None)
        current = head
        prev = dummy

        while current:
            if id(current) in valToNode:
                new = valToNode[id(current)]
            else:
                new = Node(current.val,None,None)
                valToNode[id(current)]=new
            prev.next = new
            if id(current.random) in valToNode:
                random = valToNode[id(current.random)]
            else:
                random = Node(current.random.val,None,None) if current.random else None
                valToNode[id(current.random)]=random
            new.random = random
            current = current.next
            prev = new
        
        return dummy.next
