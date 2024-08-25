"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        ans = []
        dummy = Node(-1,None,root)
        while dummy.next:
            dummy = dummy.next
            ans.append(dummy.val)
        return ans