# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        def dfs(node,mx):
            nonlocal ret
            if not node: return -inf
            if node.val>=mx:
                ret += 1
            dfs(node.left, max(mx, node.val))
            dfs(node.right, max(mx, node.val))
        dfs(root, -inf)
        return ret

        