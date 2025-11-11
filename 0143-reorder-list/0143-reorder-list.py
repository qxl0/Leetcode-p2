# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get length of list
        l = 0
        cur = head
        while cur:
            l += 1            
            cur = cur.next
        
        # go to the meddle
        l = (l+1)//2
        end = None
        cur = head
        if l==1:
            end = cur
        while l:
            l -= 1
            cur = cur.next             
            if l==1:
                end = cur
        if end:
            end.next = None
        middle = cur
        # reverse second half
        # ln->ln-1->...->l2->l1->l0
        # l0->l1->l2...->...
        prev,cur = None,middle
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # prev: head of reversed list        
        # now, merge (head, rev)
        dummy = ListNode()
        cur = dummy
        l1,l2 = head,prev
        while l1 and l2:
            cur.next = l1
            l1 = l1.next
            cur.next.next = l2            
            l2 = l2.next  
            cur = cur.next.next
        if l1:
            cur.next = l1
        return dummy.next 