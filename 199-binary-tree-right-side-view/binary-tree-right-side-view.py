# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append(root)
        ret = []
        while q:
            qlen = len(q)
            first = True
            for _ in range(qlen):                
                cur = q.popleft()
                if first:
                    ret.append(cur.val)
                    first = False
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return ret 
            
