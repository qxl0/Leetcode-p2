# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            # print(f'->{node.val if node else "null"}')
            if not node:
                return None
            if node in [p,q]: 
                # print(f'<- 1. {node.val}')
                return node
            l = dfs(node.left)
            r = dfs(node.right)

            if l and r: 
                # print(f'<- 2. {node.val}')
                return node
            # print(f'<- 3. {l.val if l else r.val if r else "null"}')
            return l if l else r
        return dfs(root)
