# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(0,head)
        prev,cur = dummy,dummy.next
        while cur and cur.next:
            prev = prev.next
            cur = cur.next.next
        # when stop
        prev.next = prev.next.next
        return dummy.next
