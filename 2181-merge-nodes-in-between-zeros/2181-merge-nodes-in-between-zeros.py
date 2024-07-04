# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        dummy = ListNode()
        ret = dummy
        cur = head
        while cur:
            sm = 0
            nxt = cur.next
            while nxt and nxt.val!=0:
                sm+=nxt.val
                nxt = nxt.next 
            # stop
            if sm==0:
                return dummy.next 
            ret.next = ListNode(sm)
            ret = ret.next 
            cur = nxt
        
        return dummy.next
