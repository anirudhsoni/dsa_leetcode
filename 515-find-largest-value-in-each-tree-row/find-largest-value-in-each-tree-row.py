# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        q=deque()
        q.append(root)
        while q:
            mx=float('-inf')
            for i in range(len(q)):
                popped=q.popleft()
                if popped:
                    mx=max(mx,popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
            if mx!=float('-inf'):
                ans.append(mx)

        return ans

        