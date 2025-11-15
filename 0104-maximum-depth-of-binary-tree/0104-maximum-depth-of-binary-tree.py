# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        stack = []
        if root is not None:
            stack = [(root,1)]
        while stack:
            cur, cur_depth = stack.pop()
            depth = max(depth, cur_depth)
            if cur.left:
                stack.append((cur.left, cur_depth+1))
            if cur.right:
                stack.append((cur.right, cur_depth+1))
        return depth