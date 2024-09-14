class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m,n =len(grid),len(grid[0])
        vis = [[0]*n for _ in range(m)]
        @cache
        def dfs(i,j,h):
            if h<=0: return False
            if [i,j]==[m-1,n-1] and h>0:
                return True
            for ii,jj in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if ii<0 or ii>=m or jj<0 or jj>=n or vis[ii][jj]==1:
                    continue
                vis[ii][jj]=1
                if grid[ii][jj]==1:
                    if dfs(ii,jj,h-1):
                        return True
                else: # 0
                    if dfs(ii,jj,h):
                        return True
                vis[ii][jj]=0
            return False 
        vis[0][0]=1
        return dfs(0,0,(health-1 if grid[0][0]==1 else health))
                

            