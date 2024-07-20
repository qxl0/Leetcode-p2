# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ret = 0
        def dfs(node): # return # of good leaf nodes pair
            nonlocal ret
            if node and not node.left and not node.right:
                return [(1,0)]
            left,right = None,None
            if node.left:
                left = dfs(node.left)  # [(lc, height), ....]
            if node.right:
                right = dfs(node.right)
            
            # update ret 
            if left and right:
                for l,lh in left:
                    for r,rh in right:
                        if lh+rh+2<=distance:
                            ret += l*r
                ans = [(l,h+1) for l,h in left]+[(r,h+1) for r,h in right]            
            elif left:
                ans = [(l,h+1) for l,h in left]
            elif right:
                ans = [(r,h+1) for r,h in right]
            return ans

        dfs(root)
        return ret