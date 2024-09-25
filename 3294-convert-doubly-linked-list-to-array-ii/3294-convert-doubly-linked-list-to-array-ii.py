"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        ret = []
        head = node        
        while node!=None:
            ret.insert(0,node.val)
            node = node.prev
        node = head.next
        while node!=None:
            ret.append(node.val)
            node = node.next
        
        
        return ret