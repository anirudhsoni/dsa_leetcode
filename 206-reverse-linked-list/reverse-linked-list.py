# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Head=None
        def dfs(node,prev=None):
            nonlocal Head
            if not node:
                return
            elif node and not node.next:
                Head=node
                Head.next=prev
                return 
            tmp=node
            dfs(node.next,tmp)
            node.next=prev
            return 
        dfs(head)
        return Head

        