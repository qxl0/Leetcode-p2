# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isleaf(node):
            return node and not node.left and not node.right
        def getleaf(node):
            if not node: return []
            if isleaf(node): return [node.val]
            left = getleaf(node.left)
            right = getleaf(node.right)
            return left+right
        s1 = getleaf(root1)
        s2 = getleaf(root2)
        return len(s1)==len(s2) and all(a==b for a,b in zip(s1,s2))
            