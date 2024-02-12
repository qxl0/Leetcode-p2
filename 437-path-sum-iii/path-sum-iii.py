# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        Map = defaultdict(int)
        Map[0] = 1
        ret = 0
        def dfs(node, sm):
            nonlocal ret
            if not node: return
            newsm = sm+node.val
            if newsm-targetSum in Map:
                ret += Map[newsm-targetSum]
            Map[newsm]+=1
            dfs(node.left,newsm)
            dfs(node.right,newsm)
            Map[newsm]-=1
            if Map[newsm]==0: del Map[newsm]
        dfs(root,0)
        return ret

        