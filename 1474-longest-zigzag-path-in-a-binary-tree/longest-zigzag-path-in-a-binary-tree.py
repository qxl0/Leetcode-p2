# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLen = 0
        def dfs(node):
            nonlocal maxLen
            if not node: return -1,-1
            _,r = dfs(node.left)
            l,_ = dfs(node.right)
            left = r+1
            right = l+1
            maxLen = max(maxLen, left,right)
            return (left,right)
        dfs(root)
        return maxLen