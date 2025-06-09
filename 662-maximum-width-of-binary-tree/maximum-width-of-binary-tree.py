# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d={}

        def dfs(n,r,c):
            if not n:
                return
            if r not in d:
                d[r]=[float('infinity'),float('-infinity')]
            d[r][0]=min(d[r][0],c)
            d[r][1]=max(d[r][1],c)
            dfs(n.left,r+1,c*2)
            dfs(n.right,r+1,c*2+1)
        dfs(root,0,0)
        w=1
        for i in d:
            w=max(w,d[i][1]-d[i][0]+1)
        return w
        
        
