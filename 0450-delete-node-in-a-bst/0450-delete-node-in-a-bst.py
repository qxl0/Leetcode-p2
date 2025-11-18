# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def suc(node):            
            node = node.right
            while node.left:
                node = node.left
            return node.val
        def pre(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.right:
                root.val = suc(root)
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = pre(root)
                root.left = self.deleteNode(root.left, root.val)
        return root