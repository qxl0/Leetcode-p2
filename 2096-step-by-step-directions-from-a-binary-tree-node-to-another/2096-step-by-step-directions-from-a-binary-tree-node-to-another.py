# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        '''
        1. from root node, do dfs find target node, record path, and dirs
        '''
        def findtarget(node, path, dirs, target):   
            if not node: return False         
            if node.val==target:
                return True
            if node.left:
                path.append(node.left.val)
                dirs.append('L')
                if findtarget(node.left, path, dirs, target):
                    return True
                dirs.pop()
                path.pop()
            if node.right:
                path.append(node.right.val)
                dirs.append('R')
                if findtarget(node.right, path, dirs, target):
                    return True
                dirs.pop()
                path.pop()
            return False
        path, dirs = [], []
        findtarget(root, path, dirs, startValue)
        # print(path,dirs)
        path2, dirs2 = [], []
        findtarget(root, path2, dirs2, destValue)
        # print(path2, dirs2)
        k = 0
        while k<len(path) and k<len(path2) and path[k] == path2[k]:
            k += 1
        ret = ''
        for j in range(k, len(path)):
            ret += 'U'
        ret += ''.join(dirs2[k:])
        return ret

