# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: 
                return 0,0
            lr,lnr = dfs(node.left)
            rr,rnr = dfs(node.right)

            rob = node.val+lnr+rnr
            norob = max(lr,lnr)+max(rr,rnr)
            return rob,norob

        r,nr = dfs(root)
        return max(r,nr)
