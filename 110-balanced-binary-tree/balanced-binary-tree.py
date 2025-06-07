# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            return 1+max(dfs(node.left),dfs(node.right))


        def chk(node):
            if not node:
                return True
            l=chk(node.left)
            if abs(dfs(node.left)-dfs(node.right))>1:
                return False
            r=chk(node.right)
            return l and r
        return chk(root)

        