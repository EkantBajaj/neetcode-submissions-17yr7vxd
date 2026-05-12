# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        r = (-float("inf"),float("inf"))
        def dfs(root,r):
            if not root:
                return True

            if r[0]<root.val<r[1]:
                bst = True
            else:
                bst = False

            return bst and dfs(root.left,(r[0],root.val)) and dfs(root.right,(root.val,r[1]))
        
        return dfs(root,r)