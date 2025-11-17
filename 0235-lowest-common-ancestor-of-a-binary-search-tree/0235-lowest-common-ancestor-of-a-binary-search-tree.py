# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node:
                return None
            if p.val<=node.val<=q.val:
                return node
            if node.val<=p.val:
                return dfs(node.right, p, q)
            if node.val>=q.val:
                return dfs(node.left, p, q)
        if p.val>q.val:
            p,q = q,p
        
        return dfs(root, p, q)