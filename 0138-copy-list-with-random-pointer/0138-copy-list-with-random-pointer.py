"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Map = {}
        cur = head
        while cur:
            newnode = Node(cur.val)            
            newnode.next = cur.next
            newnode.random = cur.random
            Map[cur] = newnode
            cur = cur.next
        # replace random
        cur = head
        while cur:
            newnode = Map[cur]
            newnode.random = Map[cur.random] if cur.random else None
            newnode.next = Map[cur.next] if cur.next else None
            cur = cur.next
        return Map[head] if head else None


