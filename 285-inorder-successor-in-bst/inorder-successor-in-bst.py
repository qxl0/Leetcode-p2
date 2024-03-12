# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        succ = None 
        def dfs(node):
            nonlocal succ 
            if not node: return 
            if (node.val<=p.val): # node's v <= p 
                dfs(node.right)
            else:
                succ = node 
                dfs(node.left)
        dfs(root)
        return succ 
