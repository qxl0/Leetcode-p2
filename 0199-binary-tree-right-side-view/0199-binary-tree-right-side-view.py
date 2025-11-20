# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def bfs(node,level):
            if not node:
                return
            if len(ret)==level:
                ret.append(node.val)
            if node.right:
                bfs(node.right,level+1)
            if node.left:
                bfs(node.left,level+1)
            
        bfs(root, 0)
        return ret
