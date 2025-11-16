# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(node1, node2):
            if node1 and node2:
                return (
                node1.val == node2.val
                and isSametree(node1.left, node2.left)
                and isSametree(node1.right, node2.right)
                )
            return node1 is node2

        if not root: return False

        return (
            isSametree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
                    