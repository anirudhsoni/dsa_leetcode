# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        cache={None:0}

        def getD(node):
            if node in cache:
                return cache[node]
            cache[node] =  max(node.val+getD(node.left),node.val+getD(node.right),node.val)
            return cache[node]

        def maxPath(node):
            if not node:
                return float('-infinity')
            ld=getD(node.left)
            rd=getD(node.right)
            print(node.val,ld,rd)
            return max(ld+rd+node.val,maxPath(node.left),maxPath(node.right),ld+node.val,rd+node.val,node.val)
        
        return maxPath(root)
        