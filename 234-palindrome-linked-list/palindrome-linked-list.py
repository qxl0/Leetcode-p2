# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def findMiddle(node):
            slow=fast=node 
            while fast and fast.next:
                slow=slow.next 
                fast=fast.next.next 
            return slow 
        def findReverse(node):
            prev,cur = None,node 
            while cur:
                tmp = cur.next 
                cur.next = prev
                prev = cur 
                cur = tmp 
            return prev 
        middle = findMiddle(head)
        head2 = findReverse(middle) 
        # compare 
        while head2:
            if head2.val!=head.val: 
                return False 
            head2 = head2.next 
            head = head.next 
        return True 


