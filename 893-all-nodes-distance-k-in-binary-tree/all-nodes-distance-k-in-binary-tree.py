# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res=[]
        parent={}

        def detNodes(n,d,un=None):
            if not n or n==un:
                return
            if n and d==0:
                res.append(n.val)
                return
            detNodes(n.left,d-1,un)
            detNodes(n.right,d-1,un)
        
        def getPar(n,p):
            if not n:
                return
            parent[n]=p
            getPar(n.left,n)
            getPar(n.right,n)
        
        getPar(root,None)
        cur=target
        prev=None
        d=k
        while d>0 and cur:
            detNodes(cur,d,prev)
            # print(cur.val,d,prev)
            # print(res)
            prev=cur
            cur=parent[cur]
            d-=1
        if cur and d==0:
            res.append(cur.val)
        return res


        