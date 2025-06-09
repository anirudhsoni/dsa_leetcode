# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath=[]
        qPath=[]

        def getPathP(n):
            if not n:
                return
            pPath.append(n)
            if pPath[-1]!=p:
                getPathP(n.left)
                getPathP(n.right)
                if pPath[-1]!=p:
                    pPath.pop()
        def getPathQ(n):
            if not n:
                return
            qPath.append(n)
            # print(qPath) 
            if qPath[-1]!=q:
                getPathQ(n.left)
                getPathQ(n.right)
                if qPath[-1]!=q:
                    qPath.pop()
        getPathP(root)
        getPathQ(root)
        # for i in pPath:
        #     print(i.val)
        # # print('xXx')
        # for i in qPath:
        #     print(i.val)
        lca=pPath[0]
        i=0
        while i<len(pPath) and i<len(qPath) and pPath[i]==qPath[i]:
            i+=1
            lca=pPath[i-1]
        return lca

        