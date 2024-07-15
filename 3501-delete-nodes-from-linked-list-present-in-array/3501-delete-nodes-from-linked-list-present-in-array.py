# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        Set = set(nums)

        dummy = ListNode(0,head)
        cur = dummy
        while cur.next:
            if cur.next.val in Set:
                # delete cur.next 
                cur.next = cur.next.next                
            else:
                cur = cur.next 
        return dummy.next