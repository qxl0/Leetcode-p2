# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if node1 and not node2 or node2 and not node1:
                return False
            if not node1 and not node2:
                return True
            left = same(node1.left, node2.left)
            right = same(node1.right, node2.right)
            if left and right and node1.val == node2.val:
                return True
            return False
        if not root: return False
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        