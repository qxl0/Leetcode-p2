# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def isleaf(node):
            return node and not node.left and not node.right
        def dfs(node):
            if not node: return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if isleaf(node) and node.val == target:
                return None
            return node
        dfs(root)
        if isleaf(root) and root.val == target:
            return None
        return root