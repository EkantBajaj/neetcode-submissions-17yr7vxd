# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        
        # res = []
        # q = deque([root])
        # while q:
        #     found = False
        #     for _ in range(len(q)):
        #         if not found:
        #             res.append(q[-1].val)
        #             found = True
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return res
        res = []
        def dfs(node,depth):
            if not node:
                return None
            if len(res)==depth:
                res.append(node.val)
            
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return res

        