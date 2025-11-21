"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        presum = [[0]*n for _ in range(n)]
        presum[0][0] = grid[0][0]
        for j in range(1,n):
            presum[0][j] = presum[0][j-1] + grid[0][j]
        for i in range(1,n):
            presum[i][0] = presum[i-1][0] + grid[i][0]
        for i in range(1,n):
            for j in range(1,n):
                presum[i][j] = grid[i][j] + presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1]
        def getSum(a,b,c,d):
            return presum[c][d]-(presum[c][b-1] if b>0 else 0)-(presum[a-1][d] if a>0 else 0)+(presum[a-1][b-1] if a >0 and b>0 else 0)
        def dfs(i1,j1,i2,j2):
            if i1==i2 and j1==j2:
                return Node(grid[i1][j1], True, None, None, None, None)
            sm = getSum(i1,j1,i2,j2)
            isLeaf = (sm == 0 or sm ==(i2-i1+1)*(j2-j1+1))
            
            me = Node(grid[i1][j1], isLeaf, None,None,None,None)
            if isLeaf:
                return me            
            # not isLeaf
            i3 = i1 + (i2-i1)//2
            j3 = j1 + (j2-j1)//2
            me.topLeft = dfs(i1,j1,i3,j3)
            me.topRight = dfs(i1,j3+1, i3, j2)
            me.bottomLeft = dfs(i3+1,j1,i2,j3)
            me.bottomRight = dfs(i3+1,j3+1,i2,j2)
            return me

            
        return dfs(0,0,n-1,n-1)