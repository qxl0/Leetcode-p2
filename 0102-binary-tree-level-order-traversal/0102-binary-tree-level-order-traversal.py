# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        ret = []
        def bfs(node, level):
            if len(ret)==level:
                ret.append([])
            ret[level].append(node.val)
            if node.left:
                bfs(node.left,level+1)
            if node.right:
                bfs(node.right,level+1)
        if not root:
            return []
        bfs(root,0)
        return ret