# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lv={}
        def dfs(n,r,c):
            if not n:
                return
            if r not in lv:
                lv[r]=[c,n.val]
            if lv[r][0]<c:
                lv[r]=[c,n.val]
            dfs(n.left,r+1,c*2)
            dfs(n.right,r+1,c*2+1)
        dfs(root,0,0)
        # print(lv)
        res=[]
        for i in range(len(lv)):
            res.append(lv[i][1])
        return res
        