# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def dfs(node,res):
        #     if node.left:
        #         dfs(node.left,res)
        #     res.append(node.val)
        #     if node.right:
        #         dfs(node.right,res)
        #     return res
        
        # if not root:
        #     return None
        # return dfs(root,[])[k-1]
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            dfs(node.left)
            if cnt == 0:
                return
            cnt -=1
            if cnt==0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res