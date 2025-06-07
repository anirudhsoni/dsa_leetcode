# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=True

        def dfs(n):
            nonlocal balanced
            if not balanced or not n:
                return 0
            l=1+dfs(n.left)
            r=1+dfs(n.right)
            if abs(l-r)>1:
                balanced=False
            return max(l,r)
        dfs(root)
        return balanced
            