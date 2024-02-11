# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        dummy = ListNode(0,head)                        
        cur,nxt = head,head.next

        dummy2 = head.next
        # 1->2->3->4->5
        #    ^     ^
        while nxt and nxt.next:
            nxtodd = nxt.next

            # change links
            cur.next = nxtodd
            nxt.next = nxtodd.next
            
            # move
            cur = cur.next
            nxt = nxtodd.next
        cur.next = dummy2
        return dummy.next
        
