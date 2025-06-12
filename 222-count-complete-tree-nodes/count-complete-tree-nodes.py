# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def dfs(n):
            if not n:
                return 0
            return 1+dfs(n.left)+dfs(n.right)
        
        return dfs(root)