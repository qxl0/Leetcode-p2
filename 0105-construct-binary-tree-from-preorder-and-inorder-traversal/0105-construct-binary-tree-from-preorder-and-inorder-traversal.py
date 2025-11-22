# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if n==0:
            return None
        Map = {v:i for i,v in enumerate((inorder))}
        val = preorder[0]
        idx = Map[val]
        llen=idx
        rlen=n-1-idx
        root = TreeNode(val)
        root.left = self.buildTree(preorder[1:1+llen], inorder[:llen])
        root.right = self.buildTree(preorder[1+llen:], inorder[llen+1:])
        return root