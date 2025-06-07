# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        cache={None:0}

        def getD(node):
            if node in cache:
                return cache[node]
            cache[node] = 1 + max(getD(node.left),getD(node.right))
            return cache[node]

        def dia(node):
            if not node:
                return 0
            ld=getD(node.left)
            rd=getD(node.right)
            return max(ld+rd,dia(node.left),dia(node.right))
        
        return dia(root)