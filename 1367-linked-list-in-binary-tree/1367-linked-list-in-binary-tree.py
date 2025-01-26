# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        n = 0
        s2 = []
        while head:
            n += 1
            s2.append(head.val)
            head = head.next
        def findNext(s):
            next = [0]*n
            next[0] = -1
            cv,i = 0, 2
            while i<n:
                if s[i-1]==s[cv]:
                    next[i] = cv+1
                    i += 1
                    cv += 1
                elif cv > 0:
                    cv = next[cv]
                else:
                    next[i] = 0
                    i += 1
            return next
        next = findNext(s2)
        def helper(cur, i):
            if i == n:
                return True
            if cur == None:
                return False
            while i>=0 and s2[i]!=cur.val:
                i = next[i]
            return helper(cur.left, i+1) or helper(cur.right, i+1)
        return helper(root, 0)