class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = [[[-2]*N for _ in range(N)] for _ in range(N)]
        def f(x1,y1,x2): # both A and B -> (N-1,N-1) max cherries picked up
            y2 = x1+y1-x2
            if x1==N or y1==N or x2==N or y2==N or grid[x1][y1]==-1 or grid[x2][y2]==-1:
                return -1
            if x1==N-1 and y1==N-1:
                return grid[x1][y1]
            if dp[x1][y1][x2]!=-2:
                return dp[x1][y1][x2]
            get = grid[x1][y1] if x1==x2 and y1==y2 else grid[x1][y1]+grid[x2][y2]
            nxt = f(x1+1,y1,x2+1)
            nxt = max(nxt, f(x1+1,y1,x2))
            nxt = max(nxt, f(x1,y1+1,x2+1))
            nxt = max(nxt, f(x1,y1+1,x2))
            ans = -1
            if nxt!=-1:
                ans = get+nxt
            dp[x1][y1][x2]=ans
            return ans

        ans = f(0,0,0)
        return ans if ans!=-1 else 0