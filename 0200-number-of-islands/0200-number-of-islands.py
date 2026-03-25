class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n  = len(grid),len(grid[0])
        def dfs(i,j):
            grid[i][j]='#'
            for di,dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                ni,nj = i+di,j+dj
                if ni<0 or ni>=m or nj<0 or nj>=n or grid[ni][nj]!='1':
                    continue
                dfs(ni,nj)
        ret = 0        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ret += 1
                    dfs(i,j)
        return ret