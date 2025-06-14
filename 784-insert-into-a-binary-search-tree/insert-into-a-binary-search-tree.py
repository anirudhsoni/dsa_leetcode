# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        cur=root
        prev=None
        while cur:
            prev=cur
            if cur.val<val:
                cur=cur.right
            elif cur.val>val:
                cur=cur.left
        if not prev:
            return TreeNode(val)
        if prev.val>val:
            prev.left=TreeNode(val)
        else:
            prev.right=TreeNode(val)
        return root